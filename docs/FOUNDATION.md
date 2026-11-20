# Adopt dot.

The versioned foundation owns the dot. identity, tokens, interaction patterns and presentation standards. Add one file under `products/` with a stable product key, display name, repository, directory scope, product kind and supported platforms. Set optional light/dark accents and a product-owned mark. Run `python3 scripts/foundation.py` and review the generated catalogue. Repository ownership never grants membership. In the mixed `sovo` repository, only native sovo. under `ios/` is a member. Shinkoiwa and its public support project have their own identity. Kotoba Atlas is a member data product.

Pin the Swift package to a reviewed SemVer release. Import `DotFoundation` and use `DotCard`, `DotActionStyle` and `DotMetrics` with native app colors and controls. For web, vendor `foundation/` from the same release and import `components.css`. Product CSS sets `--dot-accent` and `--dot-onAccent` for its light and dark appearances. Check contrast with the actual foreground. Keep app icons and feature-specific views in each app.

For native interaction, prefer system menus, search, alerts, progress and sheets. On web use labeled search fields, native buttons and dialogs, accessible status/error text and visible keyboard focus. Move focus into dialogs, close with the expected keyboard action and restore focus to the trigger. Read [localization](LOCALIZATION.md) and keep learning/data languages separate. Use system type and text scaling for native controls. For custom-engine fonts, track the OFL notice and select the appropriate Noto Sans, Noto Sans Arabic and regional JP/SC/TC CJK fonts. Never redistribute Apple system font files. Preserve reader font preferences. Use semantic headings, readable line height, at least AA contrast, appropriately sized hit targets and reduced-motion equivalents.

The [script fixture](../fixtures/scripts.html) exercises mixed direction, ruby, regional glyphs, Cyrillic and enlarged German text. Test the real rendering stack before declaring script support. Use the [Store playbook and release packet](APP_STORE_PLAYBOOK.md) for presentation. Shared design changes must pass generation and validation before adoption. The initial 1.x layout stays available for existing importers, with new generic components developed in the versioned foundation.

For common actions and binary settings, start with the [dot. controls](CONTROLS.md).

Add the shared [Credits](CREDITS.md) to each registered product interface.

## Desktop update experience

For directly distributed macOS apps, use a compatible signed updater such as [Sparkle](https://sparkle-project.org/documentation/). Provide automatic availability checks, a visible Check for Updates command, release notes and Later/Skip choices. Require HTTPS, verified update signatures, a signed and notarized app, and channel/version compatibility. Preserve update preferences and document how to recover a prior compatible release. Mac App Store executable updates go through the Store under [Apple’s review guidelines](https://developer.apple.com/app-store/review/guidelines/). Dictionary data has its own version and integrity checks. The tooling repository owns reusable technical orchestration; product-specific signing and delivery configuration stays with the product.

For reproducible web adoption, run `python3 scripts/adopt-foundation.py PRODUCT FULL_COMMIT path/to/new-snapshot` from the reviewed kit checkout. This exports the shared assets and selected product profile only, with a version/commit/hash manifest. Test the product with that snapshot and review the resulting PR before replacing its previous revision. An existing destination is refused, so an update can be staged without disturbing the current release.

To prepare a consumer PR, run `python3 scripts/propose-adoption.py PRODUCT FULL_COMMIT` with authenticated GitHub CLI access. It uses a disposable checkout, validates the registered scope, and commits only the generated foundation snapshot. The PR remains available for product validation before runtime migration. Use only reviewed kit releases.


## Product color

Give each app one recognizable hue family. Choose it for the product and nearby
suite apps, then select light and dark role values independently. Keep reading
and media areas neutral or user-configurable. Use accent for primary actions,
selection and focus, and reserve semantic success, warning and error roles for
their meanings. Pair status and selection with a label, shape or icon. Use the
same palette for the app’s chrome, icon art direction and marketing accents
where appropriate.

The registry requires app accents to meet 4.5:1 with their action foreground,
surface and background in both appearances. Exact duplicates and chromatic hue
pairs within 15° are rejected as a suite differentiation check. Visually compare
adjacent product palettes as well. In the app itself, check normal text at 4.5:1,
large text at 3:1 and essential controls and indicators at 3:1 against adjacent
colors. Inspect focus, selection, pressed and disabled states, overlays on
actual content, increased contrast and color-vision simulations. Check both
appearances in rendered app screens. A palette check covers token pairs only.

Design for inviting, comfortable repeat use through a clear hierarchy,
predictable controls and task completion. Evaluate actual task performance and
user preference. Color effects depend on context, and research gives no basis
for promising engagement from a hue alone.

Research checked 2026-11-20:

- Accessibility and adaptive appearance. [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Apple HIG Color](https://developer.apple.com/design/human-interface-guidelines/color).
- Contrast and reading performance, plus limits of broad color-psychology claims. [Hall and Hanna](https://doi.org/10.1080/01449290410001669932), [Elliot and Maier](https://doi.org/10.1146/annurev-psych-010213-115035).
- Product references for a recognizable brand accent and neutral, high-contrast working surfaces. [Spotify design history](https://newsroom.spotify.com/2026-04-23/spotify-design-history/), [Linear UI redesign](https://linear.app/now/how-we-redesigned-the-linear-ui).
