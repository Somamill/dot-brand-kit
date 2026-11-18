<!-- required-agent-tools:start -->
## Required design and video tools

Read `.agent-tools/policy.md` for UI or video work. Use **Impeccable** and **Hallmark** for UI design and review, and **Hyperframes** for video creation. If missing, run `python3 .agent-tools/setup.py` (add `--browser` for rendered Hallmark checks). Tools install globally for Codex; app runtime dependencies stay separate. Invoke checks through `.agent-tools/run.py`. Respect existing project design rules; dot. apps use the shared brand kit. Report checks actually run and any limitations.
<!-- required-agent-tools:end -->

## Shared standards and agent changes

Read `docs/MULTI_REPO.md` before changes spanning dot. apps. Keep app versions, repositories and Store/community targets independent. Validate kit changes with `python3 scripts/build.py` and `python3 kit/check.py`; review generated diffs. Use exact reviewed source commits, linked consumer PRs and honest local test evidence. GitHub Actions and automatic distribution remain disabled under owner instruction; do not reactivate without renewed explicit approval. No credentials, personal media or invented CI results.

For App Store presentation, metadata or release work, read `docs/APP_STORE_PLAYBOOK.md`. Keep Apple requirements distinct from our creative targets, require real Store-build evidence, and verify current platform eligibility. Changes to this policy need linked consumer adoption PRs; no Actions, paid campaigns or Apple publication is implied.

<!-- connected-requirements:start -->
## Connected agent requirements and project design ownership

Before work, run `python3 .agent-tools/run.py requirements`; if approved shared requirements changed, run it with `--update`, review and commit the managed diff. Read `.agent-tools/requirements/AGENT_DEVELOPMENT.md`, `TOOL_CATALOG.md` and `.agent-tools/PROJECT_CONTEXT.md`, then the applicable local design/native/Store instructions. The updater downloads documentation/data only and must preserve local edits; no Actions or permanent service is introduced.

Agents working on this repo maintain PROJECT_CONTEXT.md and the actual design sources in the same PR when behavior, UI, tools, localization or acceptance constraints change. Use the strongest relevant compatible background tools, install/configure missing official tools when needed, exploit local hardware where useful, and verify actual output/quality. Do not run every tool unnecessarily or replace native/visual validation with a browser/compile check.

UI/release work must read `LOCALIZATION.md` and `LANGUAGES.json`: future system/per-app language defaults and twelve-language coverage are release requirements, not proof of implementation. Dictionary/media/learning content is separate. Store work also reads `APP_STORE_PLAYBOOK.md` and `TREND_RESEARCH.md`: refresh current cross-category/financial-vs-popularity evidence and keywords, and inspect continuous feature-card seams/standalone readability where used. Missing required coverage/evidence must be reported, not silently waived. Preserve existing owner authorization, privacy, project identity and Actions-off policy.
<!-- connected-requirements:end -->
