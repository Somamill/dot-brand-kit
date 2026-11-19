"""Open a reviewable snapshot update for one registered product."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('member')
parser.add_argument('revision', help='Full commit SHA of a reviewed foundation release')
args = parser.parse_args()


def git(*argv, cwd=root):
    return subprocess.check_output(['git', *argv], cwd=cwd, text=True).strip()


if not re.fullmatch(r'[0-9a-f]{40}', args.revision):
    parser.error('Provide a full SHA')
registry = json.loads(git('show', f'{args.revision}:products/index.json'))
profile = registry.get(args.member)
if not profile:
    parser.error('Register the product before proposing adoption')
repo = profile['repository']
scope = profile['scope']
if (not re.fullmatch(r'[a-z0-9-]+', args.member) or not re.fullmatch(r'Somamill/[\w.-]+', repo)
        or not re.fullmatch(r'\.|[\w-]+(?:/[\w-]+)*', scope)):
    parser.error('Invalid registry entry')

branch = f'design/foundation-{args.member}-{args.revision[:12]}'
with tempfile.TemporaryDirectory(prefix='dot-adoption-') as directory:
    work = Path(directory) / 'product'
    subprocess.run(['gh', 'repo', 'clone', repo, str(work), '--', '--depth=1'], check=True)
    if not (work / scope).is_dir() or not (work / scope).resolve().is_relative_to(work.resolve()):
        parser.error('Product scope is missing or outside the checkout')
    base = git('branch', '--show-current', cwd=work)
    output = work / scope / 'branding/foundation'
    staged = Path(directory) / 'foundation'
    subprocess.run([sys.executable, str(root / 'scripts/adopt-foundation.py'),
                    args.member, args.revision, str(staged)], check=True)
    for name, data in ((p.name, p.read_bytes()) for p in staged.iterdir()):
        target = output / name
        if target.is_symlink() or not target.resolve().is_relative_to((work / scope).resolve()):
            parser.error('Unsafe destination path')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    git('add', '--', str(output.relative_to(work)), cwd=work)
    if not git('diff', '--cached', '--name-only', cwd=work):
        print('The product is already on this revision.')
        raise SystemExit(0)
    git('diff', '--cached', '--check', cwd=work)
    git('switch', '-c', branch, cwd=work)
    git('commit', '-m', f'Adopt reviewed dot. foundation for {args.member}', cwd=work)
    git('push', 'origin', branch, cwd=work)
    subprocess.run(['gh', 'pr', 'create', '--repo', repo, '--base', base, '--head', branch,
                    '--title', f'Adopt dot. foundation for {profile["name"]}',
                    '--body', f'Vendor the generated foundation and selected profile from {args.revision}. '
                    'The snapshot records hashes and exact provenance. Run affected product checks before '
                    'wiring it into app runtime. This proposal only adds design-system inputs.'], check=True)
