"""Validate and export app-owned appearance roles."""
from colorsys import rgb_to_hls
import re

THEMES = ('light', 'dark')
HEX = re.compile(r'#[0-9A-Fa-f]{6}')


def rgb(color):
    return [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]


def luminance(color):
    return sum(weight * (value / 12.92 if value <= .04045 else ((value + .055) / 1.055) ** 2.4)
               for value, weight in zip(rgb(color), (.2126, .7152, .0722)))


def contrast(first, second):
    dark, light = sorted(map(luminance, (first, second)))
    return (light + .05) / (dark + .05)


def roles(product, colors, theme):
    return product['accent'][theme], product.get('onAccent', colors['onAccent'])[theme]


def validate_palette(name, product, colors, previous):
    if product['kind'] != 'app' and 'accent' not in product:
        return
    for field in ('accent', 'onAccent'):
        if field == 'onAccent' and field not in product:
            continue
        values = product.get(field)
        if (not isinstance(values, dict) or set(values) != set(THEMES)
                or any(not isinstance(value, str) or not HEX.fullmatch(value) for value in values.values())):
            raise ValueError(f'{name} requires valid light and dark {field} colors')
    for theme in THEMES:
        accent, ink = roles(product, colors, theme)
        backgrounds = [colors[theme][role] for role in ('surface', 'background')]
        if any(contrast(accent, background) < 4.5 for background in [ink, *backgrounds]):
            raise ValueError(f'{name} {theme} accent fails 4.5:1 contrast')
        hue, _, saturation = rgb_to_hls(*rgb(accent))
        for other_name, other in previous.items():
            if other.get('kind') != 'app' or product['kind'] != 'app':
                continue
            other_accent = other['accent'][theme]
            other_hue, _, other_saturation = rgb_to_hls(*rgb(other_accent))
            distance = abs(hue - other_hue)
            if accent.lower() == other_accent.lower() or (
                    min(saturation, other_saturation) >= .15
                    and min(distance, 1 - distance) < 15 / 360):
                raise ValueError(f'{name} and {other_name} have overlapping {theme} accents')


def product_css(product, colors):
    blocks = []
    for theme in THEMES:
        accent, ink = roles(product, colors, theme)
        selector = ':root, [data-dot-theme="light"]' if theme == 'light' else '[data-dot-theme="dark"]'
        blocks.append(f'{selector} {{\n  --dot-accent: {accent};\n  --dot-onAccent: {ink};\n}}\n')
    return '\n' + ''.join(blocks)
