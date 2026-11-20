# Background tool map

Host inventory checked 20 November 2026. Availability and MCP connections vary by session; check relevant tools/configuration instead of assuming them. Use installed stable compatible tools, and install missing appropriate tools from official distributions. Do not install or run unrelated tools merely to fill this list. Global setup details: `~/.agents/tool-policy/background-control.md` and `~/.agents/tool-policy/setup.py` when available. Repo design bootstrap: `.agent-tools/setup.py`.

| Work | Preferred tools | Limits / useful probe |
| --- | --- | --- |
| GitHub/repo administration | Connected GitHub tools; `gh`, Git | API/CLI before browser; no force-push, fabricated statuses or Actions reactivation |
| Chrome flows/forms | `playwright-cli`, isolated named headless session | Load its skill; inspect targeted DOM; close only owned session; personal tabs require a task need |
| Browser errors/performance | Chrome DevTools MCP | Inspect console/network/performance; browser checks do not validate native apps |
| App Store Connect | `asc`, existing authorized release scripts | Load `asc-cli-usage` and the matching `asc-*` skill; validate existing credentials without dialogs; no implied submission or publication |
| Xcode project generation/release orchestration | XcodeGen, fastlane where already adopted | Reuse repo specifications, lanes and lockfiles; do not migrate projects merely because a tool is installed |
| Native iPhone/iPad/macOS build/test | `mobilebuildmcp`, `xcodebuild`, XCTest/XCUIAutomation; Xcode MCP where useful | Load Apple/native CLI skills, consult help and project scheme; preserve signing and SDK compatibility |
| Simulator creation/boot/install/launch | MobileBuildMCP simulator-management; `xcrun simctl` when smaller | Select one owned suitable simulator; boot is not a physical-device test; never erase unrelated devices |
| Connected physical iPhone/iPad | MobileBuildMCP device tools, `xcrun devicectl`, native XCTest | Device trust, developer mode/unlock and hardware can require the owner; do not route around OS security or take over a personal phone casually |
| Native screenshot/video/audio evidence | Existing approved recorder, `ffmpeg`/`ffprobe`, `idevicescreenshot` where compatible | Check real device support and permissions; preserve raw captures and distinguish physical from simulated sources; iPhone Mirroring is a narrow fallback, not routine automation |
| Mac/native UI | Xcode/XCTest/accessibility APIs and purpose-built app CLIs; built-in Computer Use or Peekaboo for a specific UI gap | Background APIs first; rendered/native checks where appearance or input requires them; no global clicks or unrelated app control |
| UI/marketing design | Impeccable, Hallmark, existing design system; supported image-generation tools | Run required skill setup/context and rendered checks for actual design work; no invented native screenshots |
| Video/motion | Hyperframes, FFmpeg/ffprobe | Use editable sources and render/inspect; public App Store previews need captured app operation |
| Local 3D, lighting, rigging, rendered art | Blender background, Metal GPU when supported | Preserve project architecture, run supported validation and inspect rendered output; no global preference changes just for a job |
| Godot | Compatible `godot --headless`, project test runner, native export tools | Match the project version; headless checks complement motion/playability review |
| Image processing/export | Installed ImageMagick (`magick`), native project tools; vector/code-native assets where suitable | Verify dimensions, alpha, color/profile and actual image quality; use the image skill/tool for AI image creation/editing |
| Local secret checks | Gitleaks through the existing Mac validator | Scan the clean checkout before project commands; fully redact values; review findings without blanket exclusions |
| Targeted Python correctness | Ruff through the existing Mac validator | Check changed Python files with error-only rules; no auto-fixes or unrelated formatting; preserve project configuration |
| Swift formatting/build logs/profiling | SwiftFormat (`swiftformat`), bundled `swift-format`, SwiftLint, xcbeautify; xctrace with its skill | Target changed files, preserve pipeline exit status; measure performance claims with native tools |
| Dependencies/docs/search | `uv`, Node/npm, `ctx7`, `rg`, RTK; indexed code tools when useful | Respect lockfiles and use version-specific primary documentation; no private code/secrets in public doc queries |
| Trend/ASO evidence | Apple public charts/Connect, licensed accessible research sources | Record dates, platform/storefront, metric, scope and estimate status; see TREND_RESEARCH.md |

These CLI tools were on PATH in this host audit: rtk, ctx7, playwright-cli, mobilebuildmcp, xcodebuild, xcrun, swiftformat, swiftlint, peekaboo, asc, xcodegen, fastlane, xcbeautify, ffmpeg, ffprobe, magick, blender, godot, hyperframes, impeccable, uv, gh, brew, node, python3, idevicescreenshot and idevice_id. pymobiledevice3 was not on PATH; do not claim it is installed. MCP/skill availability must be discovered in the active chat rather than inferred from this file.

For a task, record only the tools actually needed, version/configuration checks and resulting evidence in the repo context/PR. Do not dump private device inventories. A successful install/help command establishes availability, not app correctness or successful physical-device control.


## Fast task routing

Run `python3 ~/Developer/Tools/mac-development-tools/preflight.py web|macos|simulator|device`
with one route on Max’s Mac. If the script is unavailable, run the applicable
tool below directly. Then run a project-specific check before escalating.

- **Web** — Reuse the project’s browser tests first. For a new check, use a unique `playwright-cli -s=<task>` headless session. Assert against locators or query only the states needed. Use Chrome DevTools MCP for scoped console, network, or profiling evidence. Close the task’s session.
- **Mac / Simulator** — Run the repo's native test entry point or discover schemes through MobileBuildMCP. Start with the relevant test target or test case. Save the result bundle and use `xcresulttool get test-results summary --path <bundle>` or the installed CLI’s structured summary. Keep raw logs on disk. Use accessibility identifiers to drive native UI tests.
- **Physical iPhone / iPad** — Probe CoreDevice reachability, then use MobileBuildMCP device build/test/install/launch or `xcrun devicectl` for the supported operation. Use an authorized test target and known device. A paired connection doesn't establish install, unlock, signing, or test readiness. Use an approved app-scoped capture path when physical footage is required.
- **Large searches and logs** — Discover MCP tools on demand, batch independent read-only checks, filter structured output locally, and return counts, failures, and artifact paths. Use `rg`/RTK for scoped output and keep the original output for diagnosis. Preserve command exit codes. Capture a narrow rendered artifact for visual review.

Primary references checked 2026-11-20:

- Deferred tool discovery and selective context loading. [OpenAI tool search](https://developers.openai.com/api/docs/guides/tools-tool-search), [Anthropic code execution with MCP](https://www.anthropic.com/research/code-execution-with-mcp).
- CLI and headless browser workflows for coding agents. [Playwright coding agents](https://playwright.dev/docs/getting-started-cli).
- Native test destinations, command-line tools and result bundles. [Apple Xcode command-line tools](https://developer.apple.com/documentation/xcode/xcode-command-line-tool-reference), [Apple test results](https://developer.apple.com/documentation/xcode/running-tests-and-interpreting-results), [MobileBuildMCP upstream changelog](https://github.com/getsentry/MobileBuildMCP/blob/main/CHANGELOG.md).

## Installed development workflows

Load the installed `gh` skill for GitHub CLI work, `build-run-debug` alongside the
Apple/native skill for macOS build/run/debug, and `test-triage`,
`signing-entitlements` or `packaging-notarization` for the matching task.
Reuse the existing project entry point before creating another build wrapper.
The OpenAI macOS skills are available from [OpenAI Plugins](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/skills);
GitHub CLI provides [its own skill](https://github.com/cli/cli/tree/trunk/skills/gh).
Check skill availability in the active agent session; installed files alone do
not establish that a running chat has loaded them.

Install missing tools from their official package distributions when needed:
`brew install swiftformat asc xcodegen fastlane`, and
`brew install openclaw/tap/peekaboo` for the vendor's Peekaboo formula.
Preserve project version pins and inspect additional taps before trusting them.
The ASC vendor's `asc install-skills` installs its reviewed workflow pack;
review its source pin before updating skills. Tool installation adds no app
runtime dependency and does not authorize new credentials or broader access.

On the configured Mac, use `~/.agents/tool-policy/gh-background` and
`~/.agents/tool-policy/asc-background` for credential-dependent CLI operations.
These wrappers enter the existing non-graphical runner and privately load the
authorized credential configuration; never put keys in source, shell history,
launcher arguments or logs. They do not rewrite stock CLI credentials.
Use authenticated connectors where supported, preserve scope restrictions, and
keep private-repository validation paused if only public-repository access works.
If the wrapper is unavailable on another host, configure an equivalent approved
background credential path; never copy Max's credentials into a consumer repo.

Xcode MCP uses `xcrun mcpbridge`. Register it only if missing, enable external
agents in Xcode's Intelligence settings with appropriate owner approval, and
verify a live MCP handshake/tool response. Registration is not live verification.
Use MobileBuildMCP or native CLI builds when editor tools are unavailable.

For Peekaboo, check `peekaboo permissions status --all-sources --json` before UI
work. macOS privacy grants require the owner's approval; never edit TCC or
bypass protections. In Peekaboo 4, use `peekaboo window list` (the older
`peekaboo list` command was removed). Keep native observations scoped to the
authorized app and leave external vision-provider uploads unconfigured unless
explicitly authorized. A native window query demonstrates access, not UI
correctness, visual quality or physical-device readiness.


## Growing public tool journal

[dot-agent-toolsuite](https://github.com/Somamill/dot-agent-toolsuite) is the public
field guide for reviewed findings, safe tool receipts and approved kit provenance.
Where installed, route supported CLI calls through its `scripts/run-tool.mjs`
wrapper. Native connector/MCP outcomes can be recorded explicitly after observing
the result. Never record raw arguments, output, source, private project names,
personal paths, keys or precise timestamps. A passed command is not automatic
proof of app correctness or production quality.

At the end of a participating agent task, sync the kit and publish accumulated
allowlisted data using the journal's documented scripts and existing approved
background credential route. After an approved update to this kit's requirements
or tool map, run that sync/publication path as part of finishing the kit task.
Publication batches safe events; it does not create one remote commit per tool
call. Failed authentication or publication leaves local records pending and must
be reported rather than bypassed. Other working-tree files are not auto-uploaded.

Coverage is limited to instrumented workflows and participating agents. This is
not a universal interceptor or an instant webhook. Changes made outside these
paths appear on the next agent/task sync. Keep GitHub Actions and the existing
paused poller disabled; no new scheduler or service is required.
