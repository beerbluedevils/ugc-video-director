"""Apply a top-level patch, validate, then atomically replace one existing job."""
import argparse
import json
import os
import tempfile
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from validate_job import validate


def update(path, patch):
    path = path.resolve(strict=True)
    if path.name != 'job.json':
        raise ValueError('Expected an existing job.json')
    old = json.loads(path.read_text(encoding='utf-8-sig'))
    if not isinstance(patch, dict):
        raise ValueError('Patch must be a JSON object')
    if patch.get('productId', old['productId']) != old['productId']:
        raise ValueError('ProductId cannot change')
    if patch.get('retryCount', old['retryCount']) < old['retryCount']:
        raise ValueError('Cannot reset retry count')
    for key in ('generationAttempts', 'errors'):
        if key in patch:
            prior = old.get(key, [])
            # An in-progress attempt may have its result completed; its identity/history must remain.
            if not isinstance(patch[key], list) or len(patch[key]) < len(prior):
                raise ValueError('Cannot discard history: ' + key)
            if key == 'errors' and patch[key][:len(prior)] != prior:
                raise ValueError('Cannot replace prior errors')
            if key == 'generationAttempts':
                for before, after in zip(prior, patch[key]):
                    if before.get('attempt') != after.get('attempt'):
                        raise ValueError('Cannot replace attempt identities')
                    for field, value in before.items():
                        if before.get('result') not in ('Pending', 'Generating') and after.get(field) != value:
                            raise ValueError('Cannot rewrite completed attempt history')
    new = {**old, **patch, 'updatedAt': datetime.now(ZoneInfo('Asia/Bangkok')).isoformat(timespec='seconds')}
    errors = validate(new)
    if errors:
        raise ValueError('; '.join(errors))
    fd, name = tempfile.mkstemp(prefix='.job-', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(new, f, ensure_ascii=False, indent=2)
            f.write('\n')
            f.flush()
            os.fsync(f.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('job', type=Path)
    parser.add_argument('--patch-file', type=Path, required=True)
    args = parser.parse_args()
    update(args.job, json.loads(args.patch_file.read_text(encoding='utf-8-sig')))
    print('Updated:', args.job)
