# Background tool map

Host inventory checked 18 November 2026. Availability and MCP connections vary by session; check relevant tools/configuration instead of assuming them. Use installed stable compatible tools, and install missing appropriate tools from official distributions. Do not install or run unrelated tools merely to fill this list. Global setup details: `/Users/max/.agents/tool-policy/background-control.md` and `/Users/max/.agents/tool-policy/setup.py` when available. Repo design bootstrap: `.agent-tools/setup.py`.

| Work | Preferred tools | Limits / useful probe |
| --- | --- | --- |
| GitHub/repo administration | Connected GitHub tools; `gh`, Git | API/CLI before browser; no force-push, fabricated statuses or Actions reactivation |
| Chrome flows/forms | `playwright-cli`, isolated named headless session | Load its skill; inspect targeted DOM; close only owned session; personal tabs require a task need |
| Browser errors/performance | Chrome DevTools MCP | Inspect console/network/performance; browser checks do not validate native apps |
| Native iPhone/iPad/macOS build/test | `mobilebuildmcp`, `xcodebuild`, XCTest/XCUIAutomation; Xcode MCP where useful | Load Apple/native CLI skills, consult help and project scheme; preserve signing and SDK compatibility |
| Simulator creation/boot/install/launch | MobileBuildMCP simulator-management; `xcrun simctl` when smaller | Select one owned suitable simulator; boot is not a physical-device test; never erase unrelated devices |
| Connected physical iPhone/iPad | MobileBuildMCP device tools, `xcrun devicectl`, native XCTest | Device trust, developer mode/unlock and hardware can require the owner; do not route around OS security or take over a personal phone casually |
| Native screenshot/video/audio evidence | Existing approved recorder, `ffmpeg`/`ffprobe`, `idevicescreenshot` where compatible | Check real device support and permissions; preserve raw captures and distinguish physical from simulated sources; iPhone Mirroring is a narrow fallback, not routine automation |
| Mac/native UI | Xcode/XCTest/accessibility APIs and purpose-built app CLIs; computer-control fallback | Background APIs first; rendered/native checks where appearance or input requires them; no global clicks or unrelated app control |
| UI/marketing design | Impeccable, Hallmark, existing design system; supported image-generation tools | Run required skill setup/context and rendered checks for actual design work; no invented native screenshots |
| Video/motion | Hyperframes, FFmpeg/ffprobe | Use editable sources and render/inspect; public App Store previews need captured app operation |
| Local 3D, lighting, rigging, rendered art | Blender background, Metal GPU when supported | Preserve project architecture, run supported validation and inspect rendered output; no global preference changes just for a job |
| Godot | Compatible `godot --headless`, project test runner, native export tools | Match the project version; headless checks complement motion/playability review |
| Image processing/export | Installed ImageMagick (`magick`), native project tools; vector/code-native assets where suitable | Verify dimensions, alpha, color/profile and actual image quality; use the image skill/tool for AI image creation/editing |
| Swift formatting/build logs/profiling | swift-format, SwiftLint, xcbeautify; xctrace with its skill | Target changed files, preserve pipeline exit status; measure performance claims with native tools |
| Dependencies/docs/search | `uv`, Node/npm, `ctx7`, `rg`, RTK; indexed code tools when useful | Respect lockfiles and use version-specific primary documentation; no private code/secrets in public doc queries |
| Trend/ASO evidence | Apple public charts/Connect, licensed accessible research sources | Record dates, platform/storefront, metric, scope and estimate status; see TREND_RESEARCH.md |

These CLI tools were on PATH in this host audit: rtk, ctx7, playwright-cli, mobilebuildmcp, xcodebuild, xcrun, swiftlint, xcbeautify, ffmpeg, ffprobe, magick, blender, godot, hyperframes, impeccable, uv, gh, brew, node, python3, idevicescreenshot and idevice_id. pymobiledevice3 was not on PATH; do not claim it is installed. MCP/skill availability must be discovered in the active chat rather than inferred from this file.

For a task, record only the tools actually needed, version/configuration checks and resulting evidence in the repo context/PR. Do not dump private device inventories. A successful install/help command establishes availability, not app correctness or successful physical-device control.
