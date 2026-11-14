"""Validate a saved UGC job; never query or change external services."""
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def validate(job):
    schema = json.loads((ROOT / 'schemas/job.schema.json').read_text(encoding='utf-8'))
    errors = [e.message for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(job)]
    attempts = job.get('generationAttempts', [])
    numbers = [a.get('attempt') for a in attempts if isinstance(a, dict)]
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        errors.append('generationAttempts must retain contiguous ordered attempts starting at 1')
    if numbers and all(isinstance(n, int) for n in numbers):
        if job.get('retryCount') != max(numbers) - 1:
            errors.append('retryCount must equal the number of retries actually started')
    if job.get('stage') == 'Generation Failed' and job.get('retryCount') != 3:
        errors.append('Generation Failed requires three exhausted retries; use Blocked for other blockers')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('job', type=Path)
    args = parser.parse_args()
    job = json.loads(args.job.read_text(encoding='utf-8-sig'))
    errors = validate(job)
    if errors:
        for error in errors:
            print('FAIL:', error)
        raise SystemExit(1)
    print('PASS:', args.job)
