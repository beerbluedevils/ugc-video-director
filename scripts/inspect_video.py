"""Read video metadata locally. Does not verify imagery or narration."""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inspect(path):
    path = path.resolve(strict=True)
    probe = shutil.which('ffprobe')
    if probe:
        result = subprocess.run([probe, '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(path)], capture_output=True, text=True, check=True)
        return {'method': 'ffprobe', 'path': str(path), 'sizeBytes': path.stat().st_size, 'metadata': json.loads(result.stdout), 'visualReview': 'not checked', 'narrationReview': 'not checked'}
    sys.path.insert(0, str(ROOT / 'tools/python'))
    try:
        import imageio_ffmpeg
    except ImportError as exc:
        raise RuntimeError('Install ffprobe or imageio_ffmpeg before metadata inspection') from exc
    frames = imageio_ffmpeg.read_frames(str(path))
    try:
        metadata = next(frames)
    finally:
        frames.close()
    return {'method': 'imageio_ffmpeg', 'path': str(path), 'sizeBytes': path.stat().st_size, 'metadata': metadata, 'visualReview': 'not checked', 'narrationReview': 'not checked'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.video), ensure_ascii=False, indent=2))
