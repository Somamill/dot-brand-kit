# dot.

[![Catalogue: Open](https://img.shields.io/badge/Catalogue-Open-26374D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Somamill/dot-brand-kit/blob/main/CATALOGUE.md) [![Reddit: dot. apps](https://img.shields.io/badge/Reddit-dot.%20apps-AD3000?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/user/dot-app/)

[Catalogue](https://github.com/Somamill/dot-brand-kit/blob/main/CATALOGUE.md) | [Reddit](https://www.reddit.com/user/dot-app/) | [Contact](#contact)

A quieter way to read, listen, and learn.

dot. is an enduring product family and design system. Its [catalogue](CATALOGUE.md) is generated from explicit product profiles. The repository hosting a product is independent of its membership.

Use [the adoption guide](docs/FOUNDATION.md) for new projects. Existing applications can migrate on their own release schedules. The 1.x snapshot under `kit/` supports existing consumers while the 2.x foundation carries generic semantics and platform components.

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

## Shared Mac tooling

Build and release tooling is owned by [Mac Development Tools](https://github.com/Somamill/mac-development-tools). Each project configures its own jobs. Membership and brand validation are configured at the product level.

## Contact

Questions, ideas, or something that feels off? [Email Max](mailto:max@miller-max.com). Feedback is always welcome.
