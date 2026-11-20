"""Export a validated, committed design-system revision to a new snapshot directory."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

from palette import product_css

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('member', help='Product key from the registry')
parser.add_argument('revision', help='Full reviewed commit SHA')
parser.add_argument('destination', type=Path, help='New snapshot directory inside the product scope')
args = parser.parse_args()
if not re.fullmatch(r'[a-z0-9-]+', args.member) or not re.fullmatch(r'[0-9a-f]{40}', args.revision):
    parser.error('Provide a registry key and a full commit SHA')
if args.destination.exists() or args.destination.is_symlink():
    parser.error('Use a new directory and review the diff before replacing an existing snapshot')


def read(path):
    return subprocess.check_output(['git', '-C', str(root), 'show', f'{args.revision}:{path}'])


registry = json.loads(read('products/index.json'))
if args.member not in registry:
    parser.error('Register the product before adoption')
profile = registry[args.member]
files = {name: read('foundation/' + name) for name in ('tokens.json', 'tokens.css', 'components.css')}
tokens = json.loads(files['tokens.json'])
if tokens['schemaVersion'] != 1 or not re.fullmatch(r'2\.\d+\.\d+', tokens['version']):
    parser.error('Expected a compatible 2.x foundation')
if tuple(map(int, tokens['version'].split('.'))) >= (2, 1, 0) and 'accent' in profile:
    files['tokens.css'] += product_css(profile, tokens['colors']).encode()
files['product.json'] = json.dumps(profile, indent=2).encode() + b'\n'
if 'mark' in profile:
    path = f'products/{args.member}.svg'
    if profile['mark'] != path:
        parser.error('Invalid product mark path')
    files['mark.svg'] = read(path)
manifest = {'repository': 'Somamill/dot-brand-kit', 'commit': args.revision,
            'version': tokens['version'], 'member': args.member,
            'files': {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}}
with tempfile.TemporaryDirectory(dir=args.destination.parent) as temporary:
    stage = Path(temporary) / 'snapshot'
    stage.mkdir()
    for name, data in files.items():
        (stage / name).write_bytes(data)
    (stage / 'source.json').write_text(json.dumps(manifest, indent=2) + '\n')
    stage.rename(args.destination)
print(f"Adopted {args.member} foundation {tokens['version']} at {args.revision}")
