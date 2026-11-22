"""Build and validate independent dot foundations and product profiles."""
import json
import re
import sys
from pathlib import Path

from palette import validate_palette

root = Path(__file__).resolve().parents[1]
tokens = json.loads((root / 'foundation/tokens.json').read_text())
registry = {}
seen = set()
for path in sorted((root / 'products').glob('*.json')):
    if path.name == "index.json":
        continue

    product = json.loads(path.read_text())
    identity = (product['repository'], product['scope'])
    if (not re.fullmatch(r'[a-z0-9-]+', path.stem) or identity in seen
            or not re.fullmatch(r'Somamill/[\w.-]+', identity[0])
            or not re.fullmatch(r'\.|[\w-]+(?:/[\w-]+)*', identity[1])):
        raise ValueError(f'Invalid or duplicate member in {path.name}')
    seen.add(identity)
    validate_palette(path.stem, product, tokens['colors'], registry)
    if 'mark' in product and (product['mark'] != f'products/{path.stem}.svg'
                              or not (root / product['mark']).is_file()):
        raise ValueError(f'Invalid mark in {path.name}')
    registry[path.stem] = product

css = ['/* Generated from foundation/tokens.json. */']
for theme in ('light', 'dark'):
    selector = ':root, [data-dot-theme="light"]' if theme == 'light' else '[data-dot-theme="dark"]'
    css.append(selector + ' {')
    colors = tokens['colors'][theme] | {k: tokens['colors'][k][theme] for k in ('accent', 'onAccent')}
    for key, value in colors.items():
        css.append(f'  --dot-{key}: {value};')
    css.append('}')
css.append(':root {')
for group in ('spacing', 'radius'):
    for key, value in tokens[group].items():
        css.append(f'  --dot-{group}-{key}: {value}px;')
for key, value in tokens['typography'].items():
    unit = 'px' if key.endswith('Size') else ''
    css.append(f'  --dot-{key}: {value}{unit};')
css.append('}')
swift = ['// Generated from foundation/tokens.json.', 'public enum DotMetrics {']
for key, value in tokens['spacing'].items():
    swift.append(f'    public static let space{key.title()}: Double = {value}')
for key, value in tokens['radius'].items():
    swift.append(f'    public static let radius{key.title()}: Double = {value}')
swift += [f"    public static let minimumTarget: Double = {tokens['interaction']['minTarget']}", '}']
catalogue = ['# dot. catalogue', '', 'A quieter way to read, listen, and learn.', '']
for product in registry.values():
    if 'publicLinks' in product:
        links = ' · '.join(f'[{label}]({url})' for label, url in product['publicLinks'].items())
        catalogue.append(f"- {product['name']} · {links}")
        continue

    suffix = ' · Dictionary data' if product['kind'] == 'data' else ''
    url = 'https://github.com/' + product['repository']
    if product['scope'] != '.':
        url += '/tree/main/' + product['scope']
    mark = product.get('mark')
    icon = f'<img src="{mark}" width="24" height="24" alt=""> ' if mark else ''
    catalogue.append(f"- {icon}[{product['name']}]({url}){suffix}")
catalogue += ['', '[App support and privacy policies](https://github.com/Somamill/Somamill/tree/main/support)']
outputs = {
    'foundation/tokens.css': '\n'.join(css) + '\n',
    'Sources/DotFoundation/DotMetrics.swift': '\n'.join(swift) + '\n',
    'products/index.json': json.dumps(registry, indent=2) + '\n',
    'CATALOGUE.md': '\n'.join(catalogue) + '\n',
}
for name, content in outputs.items():
    path = root / name
    if '--check' in sys.argv:
        if not path.exists() or path.read_text() != content:
            raise SystemExit(f'Stale generated asset: {name}')
    else:
        path.write_text(content)
