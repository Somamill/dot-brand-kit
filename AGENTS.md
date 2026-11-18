<!-- required-agent-tools:start -->
## Required design and video tools

Read `.agent-tools/policy.md` for UI or video work. Use **Impeccable** and **Hallmark** for UI design and review, and **Hyperframes** for video creation. If missing, run `python3 .agent-tools/setup.py` (add `--browser` for rendered Hallmark checks). Tools install globally for Codex; app runtime dependencies stay separate. Invoke checks through `.agent-tools/run.py`. Respect existing project design rules; dot. apps use the shared brand kit. Report checks actually run and any limitations.
<!-- required-agent-tools:end -->

## Shared standards and agent changes

Read `docs/MULTI_REPO.md` before changes spanning dot. apps. Keep app versions, repositories and Store/community targets independent. Validate kit changes with `python3 scripts/build.py` and `python3 kit/check.py`; review generated diffs. Use exact reviewed source commits, linked consumer PRs and honest local test evidence. GitHub Actions and automatic distribution remain disabled under owner instruction; do not reactivate without renewed explicit approval. No credentials, personal media or invented CI results.

For App Store presentation, metadata or release work, read `docs/APP_STORE_PLAYBOOK.md`. Keep Apple requirements distinct from our creative targets, require real Store-build evidence, and verify current platform eligibility. Changes to this policy need linked consumer adoption PRs; no Actions, paid campaigns or Apple publication is implied.
