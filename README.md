# dot.

A quieter way to read, listen, and learn.

Shared identity for [read.](https://github.com/Somamill/read), [sovo. / listen.](https://github.com/Somamill/listen), [Immersed.](https://github.com/Somamill/immersed), and [Kotoba Atlas](https://github.com/Somamill/kotoba-atlas).

## Edit once, adopt separately

Edit `kit/tokens.json`, guidelines, or vector marks. Run `python3 scripts/build.py` and `python3 kit/check.py`, then commit generated exports together. Increase the kit version for published kit changes; use independent app versions. Review changes through pull requests.

**GitHub Actions are disabled by owner instruction (17 November 2026).** There is no active hourly distribution or automatic Store delivery. Do not resume either without renewed explicit approval. The workflow files retained in app repositories describe an optional hosted route, not a running service.

For local adoption, review a full commit in an isolated checkout of this public repository. In each app, run its existing `sync-dot-brand.py` against that checkout, then validate `branding/dot/check.py` and the affected app checks. The sync rejects modified, staged, untracked or ignored files inside `kit/` and records the exact source commit and file hashes. Review each resulting PR separately; no cross-repository personal access token or automatic merge is needed.

The initial setup installed snapshots in the apps. Subsequent updates are proposed through PRs. Updating this kit changes vendored assets and guidance; product screens adopt the tokens in separate feature changes.

## Contents

- `kit/tokens.json`: canonical semantic tokens, with generated CSS and TypeScript exports.
- `kit/logos/`: initial suite/app vector marks, not platform app-icon packages.
- `kit/guidelines/`: identity, icon rules, copy, versioning and changelog conventions.
- `kit/check.py`: dependency-free shared validation used by all apps.
- `scripts/build.py`: deterministic export generation.

## CI and release boundaries

Each app has a local `dot. brand check` alongside its existing platform checks. App tests, packaging, signing, notarization, and iPhone workflows stay in those apps. Existing changelog history is preserved; use the common format for new entries through the app's own release tooling.

Checks run locally while Actions are disabled. Required hosted checks may therefore leave app PRs blocked; do not fake results or weaken branch protection to merge them. A kit update changes the shared snapshot, not proof that every native screen has adopted it.

See [multi-repository and agent workflow](docs/MULTI_REPO.md) for change scope, compatibility, test evidence and release boundaries.

Brand names and artwork are starting proposals; no trademark or domain availability search has been performed.

## App Store presentation and growth

Use the [App Store playbook](docs/APP_STORE_PLAYBOOK.md) before Store metadata, screenshot, preview or release work. It defines benefit-led feature cards using real app captures, separate creative assets, ASO/localization, App Store Connect experiments and release evidence. Each app keeps a local marketing brief and pins its adopted playbook revision in AGENTS.md.
