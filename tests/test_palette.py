import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from palette import product_css, validate_palette


class PaletteTests(unittest.TestCase):
    def setUp(self):
        self.colors = json.loads((ROOT / 'foundation/tokens.json').read_text())['colors']
        self.immersed = json.loads((ROOT / 'products/immersed.json').read_text())

    def test_rejects_missing_duplicate_and_low_contrast_accents(self):
        cases = (
            (dict(self.immersed, accent={}), {}, 'requires valid'),
            (self.immersed, {'immersed': self.immersed}, 'overlapping'),
            (dict(self.immersed, accent={'light': '#FFFFFF', 'dark': '#FFFFFF'}), {}, 'contrast'),
        )
        for product, previous, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                validate_palette('new-app', product, self.colors, previous)

    def test_export_applies_product_roles_in_both_appearances(self):
        css = product_css(self.immersed, self.colors)
        self.assertIn('--dot-accent: #42684B;', css)
        self.assertIn('--dot-accent: #B6E3C4;', css)
        self.assertIn('--dot-onAccent: #11281B;', css)
        self.assertNotIn(self.colors['accent']['light'], css)


if __name__ == '__main__':
    unittest.main()
