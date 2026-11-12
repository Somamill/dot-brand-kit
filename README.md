# dot.

A quieter way to read, listen, and learn.

Shared identity for [read.](https://github.com/Somamill/read), [listen.](https://github.com/Somamill/listen), and [Immersed](https://github.com/Somamill/immersed).

## Edit once, adopt separately

Edit `kit/tokens.json`, guidelines, or vector marks. Run `python3 scripts/build.py` and `python3 kit/check.py`, then commit generated exports together. Increase the kit version for published kit changes; use independent app versions. Review changes through pull requests.

Each app checks this public repository hourly through GitHub Actions (and on manual dispatch), copies `kit/` into `branding/dot/`, records the source commit, validates it, and opens a PR. GitHub may delay scheduled runs or disable schedules in inactive public repositories after 60 days; manually dispatch to resume. There is no cross-repository secret or shared personal access token. Nothing auto-merges. Multiple upstream revisions may produce separate PRs; close older proposals when adopting the newest one.

The first setup installs this infrastructure and an initial snapshot directly into the apps. Subsequent updates arrive as PRs. Updating this kit changes vendored assets and guidance; product screens adopt the tokens in separate feature changes.

## Contents

- `kit/tokens.json`: canonical semantic tokens, with generated CSS and TypeScript exports.
- `kit/logos/`: initial suite/app vector marks, not platform app-icon packages.
- `kit/guidelines/`: identity, icon rules, copy, versioning and changelog conventions.
- `kit/check.py`: dependency-free shared validation used by all apps.
- `scripts/build.py`: deterministic export generation.

## CI and release boundaries

Each app adds a `dot. brand check` alongside its existing platform checks. App tests, packaging, signing, notarization, and iPhone workflows stay in those apps. Existing changelog history is preserved; use the common format for new entries through the app's own release tooling.

PRs opened with GITHUB_TOKEN do not automatically trigger other GitHub workflows. The sync run validates the kit before opening its PR. Before merging a bot PR, use the app's normal validation process or push a human-authored commit to trigger its PR checks. A future dedicated GitHub App token can enable automatic PR-triggered checks without sharing a personal token.

Brand names and artwork are starting proposals; no trademark or domain availability search has been performed.
