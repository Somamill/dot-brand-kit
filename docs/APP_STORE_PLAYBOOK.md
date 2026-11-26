# App Store release and growth playbook

Policy v2 — researched 18 November 2026. Applies to registered dot. Store products. Independent projects maintain their own presentation policy. App Store optimization (ASO) means relevant discovery plus an honest, convincing product page; rankings or downloads are never guaranteed. Recheck Apple's linked requirements and the target app's live App Store Connect controls before each release: platform eligibility and upload specifications change.

## 1. Release brief before assets or metadata

Identify the App Store ID, bundle ID, platform, storefront/localization, selected build and source commit. Read the app's local marketing brief, Store-scope document, current listing and review messages. A repository version, archived metadata file or successful upload is not proof of what is live. Keep Store and community capabilities separate.

Write one audience, one primary problem, one main outcome and a short feature-to-evidence matrix. Every advertised feature must have an implemented flow and verification in the selected Store build/platform. Cover the meaningful shipped features across the screenshot story, description and optional preview; do not cram every setting into one image. Map secondary features to copy or explain why omitted. Pending PRs and planned features are not marketing evidence.

Follow the [app version and Git naming rules](AGENT_DEVELOPMENT.md#app-version-and-git-naming) before assigning the marketing version, upload build number or release tag.

Keep app versions and release timing independent. Align suite typography, spacing, semantic colors, tone and release terminology through the adopted dot. kit; retain read.'s reading identity, sovo.'s listening identity and Immersed.'s learning identity. Do not rename bundle IDs, URL schemes or data locations. Never delay a necessary safety/bug fix solely to synchronize campaigns.

## 2. Three different public asset types

| Asset | Purpose | Required evidence |
| --- | --- | --- |
| Screenshot feature card | Explain a benefit around the real app interface | Current native capture, matching platform/build, truthful populated state |
| App preview | Demonstrate the actual flow in motion | Device-captured app footage; current Apple video specifications |
| Creative asset | Express the brand or broader value in eligible header/search/event placements | Original/licensed artwork, truthful claims, correct placement and eligibility |

A polished advertisement is welcome; an invented interface is not a screenshot. Apple's 2.3.3 guidance allows framing and overlays while requiring a majority of each device's screenshot set to show the app in use. Our stronger default is real app UI on **every** screenshot feature card. Dedicated creative assets are separate, optional placements, not a replacement for required screenshots. Current creative-asset support covers iOS/iPadOS 27+; do not promise the same placement on Mac or older OS versions. Check the current controls and specifications before production.

A physical-device demonstration requested by App Review is a **fourth, private review deliverable**. Record launch and the requested normal flows on the required real device/OS. Do not substitute a simulator, animated advertisement, stock footage or edited marketing preview for that evidence.

## 3. Screenshot storytelling and design standard

Default plan: 5–7 useful feature cards per supported platform/localization, within Apple's current limit of 10. This is a project target, not Apple's minimum; fewer strong truthful cards beat filler. The first three explain the main outcome, the primary action and a distinctive verified benefit. Later cards cover other major features, comfort/accessibility or cross-device use only where supported and tested.

Each card has one short benefit headline, optional brief supporting copy, and a large legible view of the actual app. Use consistent margins, type scale and app accent from the adopted brand kit. Device frames, original backgrounds and restrained annotations may add craft; they must not hide the feature being explained. Read the headline and UI at App Store thumbnail/phone size, not only at full export resolution. Keep essential text clear of crops; localize the composition, not just the string.

Capture the actual iPhone, iPad and Mac experience separately. Never stretch an iPhone capture into an iPad/Mac listing or combine incompatible interface states. Mac cards must clearly show real Mac app use. Check light/dark appearance, current icon, typography and the selected release's actual UI. Do not present a browser fixture as native evidence.

Use original, licensed or demonstrably redistributable sample media. Avoid personal libraries, credentials, user messages and copyrighted covers/video clips without permission. No invented awards, press logos, ratings, testimonials, performance figures or Apple endorsement. A competitor's screenshots show presentation techniques, not permission to reuse their assets or claims.

Retain the raw captures, editable composition sources, export instructions and an asset manifest in the app's established marketing/release layout. Record build/source, device/OS, locale, feature, capture method, sample-content rights and export dimensions/hash. Keep private review media and credentials out of public Git. Use existing large-asset storage conventions rather than committing duplicate rendered videos.

## 4. Video and visual tooling

Load Impeccable and Hallmark for screenshot/marketing design and copy review; preserve the established app identity. For video production load Hyperframes and its required render workflow. Native capture comes first; use the owner's approved background capture tools. If a necessary tool is unavailable, report it instead of inventing a capture or silently switching to a personal screen session. Keep these tools outside app runtime dependencies.

For an App Store preview, use recorded app operation with simple explanatory edits, no fabricated UI or unrelated cinematic introduction. Make the opening useful with sound muted, choose a representative poster frame, and localize readable overlays. Current preview length is 15–30 seconds, up to three per eligible device/language; verify accepted resolution, codec, orientation and size on Apple's current specification page. Screenshot dimensions and video dimensions are different. A separate creative-asset video can be more expressive within that placement's own rules.

Inspect the final rendered exports and native source captures. Automated dimension/format checks supplement, not replace, visual review. Use current screenshot formats/resolutions and opaque images; record a successful Asset Library upload/processing result before claiming acceptance. Creating an editable template or rendering HTML is not native UI validation.

## 5. Metadata, localization and discovery

Preserve the approved public name and exact dot punctuation. A proposed descriptive name/subtitle is a draft until its identity, availability and target build are checked. Current field limits: name 30 characters, subtitle 30, keywords 100, promotional text 170, description 4,000. Validate each locale against Apple's current field rules and App Store Connect; do not assume all fields are editable in every release state.

Choose search intent from the target users' actual problem and verified features. Record the candidate terms, language/storefront, relevance and available evidence; label volume/difficulty as unknown without a real data source. Prefer a focused specific query over unsupported claims about dominating a competitive generic term. Use the right primary category for each app rather than making every suite app identical.

Keep keyword terms relevant and comma-separated; avoid duplicates already covered by name/subtitle/category, filler and unauthorized competitor/trademark terms. Promotional text is for timely value, not keyword stuffing; Apple says it does not affect search ranking. Write a clear opening description, scannable feature benefits, requirements and honest limitations. Do not promise free supplied books/videos, universal sync, AI, DRM access or offline behavior without verification. Keep monetization, privacy, support and What's New consistent with the actual release.

Select supported locales based on the product's real audience and ability to support them; en-US, de-DE and ja-JP are candidates, not an automatic promise of translated app UI. Check localized search phrasing, cultural fit, line breaks and screenshot readability. AI translations and internal agent checks are accepted. External language review is optional. Clearly disclose interface-language limits. Do not mechanically translate a comma list or claim one locale's search results prove another's demand.

### What’s New for every app update

Every dot. App Store update must have version-specific **What’s New** notes for each submitted platform and locale where Apple provides the field. Start with the changes actually included in the selected build. Save the final copy with the repository’s release metadata and carry the same copy into App Store Connect.

- Start each nonblank line with a literal `• `. Use plain text, one bullet per line, and no introductory or closing paragraphs, standalone headings, or Markdown formatting.
- Use one short sentence per bullet. Aim for one to five bullets and put the most useful change first. A patch can have one bullet when that is all that changed.
- Name the feature, action, or fix and what the user will notice. Replace generic filler with a specific, verified change. Keep internal commit details out unless they explain a user-visible result.
- Match each platform’s actual changes. Localize the wording naturally for each submitted locale while preserving the bullet format, and respect Apple’s current field limit.
- Before submission, compare the saved text with the selected build and the repo copy. Check the App Store Connect display or read the field back through the API and confirm the bullets and line breaks survived. Correct missing notes and paragraph blocks before proceeding.

Example format for a hypothetical update:

```text
• Jump to a saved highlight from search.
• Fixed a crash when opening some EPUB files.
```

[Things 3](https://apps.apple.com/us/app/things-3/id904237743) uses short bullets that name the affected part of the app. [Obsidian](https://apps.apple.com/us/app/obsidian-connected-notes/id1557175442) calls out platform-specific changes clearly. [BookPlayer](https://apps.apple.com/us/app/bookplayer/id1138219998) names concrete bugs, such as a Watch launch crash. Use these examples for specificity and prioritization. Keep the dot. notes in the flat bullet format above.

## 6. App Store Connect capability plan

Before changing anything, record each feature as **use now / test later / not applicable**, with reason, target platform/localization and required permission. Use an existing connector/API or CLI where sufficient; otherwise use an authorized isolated background browser. Read the current state before each write, keep receipts/IDs and verify the result after saving. Do not submit twice after a timeout. Never commit sessions or secrets, change an unrelated app, or withdraw an in-review submission merely to polish graphics.

- **Asset Library:** organize screenshots, previews and approved creative assets by version/platform/locale. Inspect Header and Search Results eligibility and preview the actual placements. Keep old approved assets until replacements are verified so a failure has a rollback path.
- **Product page optimization:** for an eligible released iOS/iPadOS page, define a hypothesis, one main creative variable, baseline/control, target audience and decision rule before starting. Do not claim a Mac PPO test or apply PPO to a custom product page. Check active tests before changing release assets; updates can confound results.
- **Custom product pages:** use only for real distinct acquisition intents with appropriate screenshots/copy, supported keywords and a measurable unique URL. Current availability is iPhone/iPad; deep links require implemented, tested destinations and supported OS versions. Verify eligibility rather than creating empty pages for every feature. CPP metadata requires review.
- **Analytics and attribution:** record baseline impressions, product-page views, downloads and Apple's defined conversion metric, separated by storefront, source, device/platform and date range. Preserve the denominator/definition; also track retention and crash signals when available. Use campaign links for external promotion. Respect privacy thresholds and mark missing data unavailable, not zero. Start with useful 7/28-day windows, but do not declare a winner from low counts or overlapping releases.
- **Reviews:** monitor feedback and respond under the owner's communication authorization. Any in-app request uses Apple's supported mechanism after a meaningful completed action, without interrupting reading/playback, rewards or review gating. Do not reset ratings as routine housekeeping.
- **Events and featuring:** assess genuine timely in-app experiences and legitimate featuring nominations where available; routine updates do not automatically justify an event. Confirm dates, supported content and rights. Paid Apple Ads campaigns and budgets require explicit spending authorization; this playbook does not start one.

An extra preview or fancier treatment is a hypothesis, not guaranteed improvement. Apple's own PPO examples include a preview treatment losing to the original. Keep a known-good control and adopt changes on credible results, not competitor appearance alone.

## 7. Release packet and completion gate

### Complete App Store Connect

For each App Store setup, version, or release task, inspect the actual App Store Connect record for every in-scope platform, locale, and storefront. Complete every required or applicable field and resolve submission warnings against the selected build. Agents own routine fixes: generate and verify missing assets, update the asset catalog, repair broken links, prepare or update the app’s published support and privacy pages from verified facts, and save corrected metadata and declarations within the task’s authorization. Continue the rest of the work if one field needs an owner-only answer.

| Area | Complete and check against the release |
| --- | --- |
| Build and artwork | Select the intended build. Check the compiled app icon and any required listing artwork, including platform variants. Correct the asset catalog and rebuild if the icon itself is wrong. Populate the required screenshot sets and applicable previews. |
| Product page | Complete the name, subtitle, category, description, keywords, support URL, and applicable marketing, copyright and version fields. Check localized metadata and media for each intended storefront. |
| What’s New | For each update, verify localized, build-specific notes in the [bullet format](#whats-new-for-every-app-update) and check that the saved field matches the repository’s release metadata. |
| Age and accessibility | Answer the age-rating questionnaire from actual content and capabilities, including web access, user content and communication where present. Complete applicable accessibility declarations from features the app actually supports. |
| Privacy and compliance | Check that the privacy policy and labels match the build, including third-party SDKs and enabled services. Complete applicable content rights, encryption/export, license, trader and region-specific declarations using documented facts and authorized decisions. |
| Review and distribution | Complete reviewer contact, notes, demo access, sample files, requested evidence, and applicable availability, pricing and release settings. Use the owner’s approved commercial and distribution choices. |

Use the authorized background App Store Connect API or CLI first. For fields the API does not expose, use the authorized App Store Connect browser workflow. Reopen or re-read saved values and check processing before calling the record complete. Escalate only when a material fact is unavailable, an owner-only legal declaration or agreement is required, or access or authorization is missing. Never guess compliance answers, publish unsupported claims, or bypass an Apple requirement. Preparing or saving a record does not authorize submission or release.

Use the current Apple references for [app and compliance information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-compliance-information), [age ratings](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions), [screenshot requirements](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) and [review information](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/).

Use a public support page with the email from the [Credits standard](CREDITS.md). Invite questions, bug reports, and ideas. App Store Connect’s Support URL points to the page, and the App Review contact email is set separately.

### Record the release evidence

For every Store listing/release task, include the following in the app's release record or PR. Use "not applicable" with a reason rather than silently skipping a platform or field:

```text
App ID / bundle ID / platform / current ASC version and state:
Selected build / source commit / native verification / review messages:
Audience / core outcome / feature-to-evidence coverage and limitations:
Locales / name / subtitle / keywords / category / description / promo / What's New:
Screenshot story (order, benefit, real capture, build/device/OS, locale, rights):
Previews and creative assets (separate types, editable source, eligibility):
Export dimensions/format/hash / rendered review / upload IDs and processing:
App Store Connect fields and assets complete / declarations and URLs checked:
Private physical-device review demo and reviewer steps, if requested:
PPO / CPP / analytics / reviews / events / featuring: choice and reason:
Baseline / hypothesis / measurement window / rollback assets:
Saved metadata vs submitted items vs approved/live items, with receipts:
Local commands/results / checks not run / unresolved issues / authorization:
```

Check field limits, spelling, exact product names, links, required device sets, current icon and all platform/localization variants. Reconcile privacy/age/accessibility declarations and review contact/notes with the actual binary and account practices. Include reviewer-accessible sample files and reproduce the core flow. Do not claim 100% compliance or guaranteed approval; Apple makes the decision.

Publishing follows the owner's existing authorization: prepare and verify concrete changes, then complete authorized actions without repeatedly asking about routine steps. This task's rules do not themselves authorize new uploads, agreements, advertising spend or publication. Report "saved", "submitted", "approved" and "live" separately and verify each claimed state. All GitHub Actions and automatic Store delivery remain off; use local background checks and keep the remaining branch protections.

## 8. Mandatory current research, panoramic design and languages

Before each release, follow [TREND_RESEARCH.md](TREND_RESEARCH.md): check current Apple rules and storefront trends, include adjacent and cross-category references, distinguish revenue estimates from popularity and record a fresh research note. Continuous multi-card curves/scenes are encouraged with an editable master, exact slices and standalone readable cards; inspect seams, real UI, crops and localized/RTL presentation. Local rendering/3D tools may create original supporting art, never fabricated app screenshots.

[LOCALIZATION.md](LOCALIZATION.md) and [LANGUAGES.json](LANGUAGES.json) define the future 12-language UI/Store baseline and system-language default. Dictionary/learning-content languages stay separate. Agents must audit real implementation before the next user-facing release, report missing translations/default selection/layout review as blockers and never count this policy as completed localization. The owner explicitly deferred current-app implementation.

For general Mac-based development and tool installation/automation, follow [AGENT_DEVELOPMENT.md](AGENT_DEVELOPMENT.md) and [TOOL_CATALOG.md](TOOL_CATALOG.md), not only this release guide. Working agents maintain the repo-specific design/context and update managed requirements through the local sync. Actions remain off.

## 9. Observed references and primary sources

On 18 November 2026 the first public US screenshot for [Readwise Reader](https://apps.apple.com/us/app/readwise-reader/id1567599761), [BookPlayer](https://apps.apple.com/us/app/bookplayer/id1138219998), [LingQ](https://apps.apple.com/us/app/lingq-learn-languages/id379385811) and [Matter](https://apps.apple.com/us/app/matter-reading-app/id1501592184) was visually inspected from Apple's listing assets. Reader pairs a reading benefit with a large library view; BookPlayer foregrounds playback; LingQ frames its immersion flow; Matter uses editorial recognition around the interface. These observations support benefit-led sequencing and clear UI, not conversion or revenue claims. Do not imitate recognition that our apps have not earned. Competitor media are research references and are not included as reusable project assets.

Apple rules and capability references (recheck for every release):

- [Screenshot presentation: guideline 2.3.3](https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots/)
- [Current App Review Guidelines, including accurate metadata and creative assets](https://developer.apple.com/app-store/review/guidelines/)
- [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/)
- [Manage App Store assets and creative placements](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-your-app-store-assets)
- [Creative-asset specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications)
- [App preview specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/)
- [Product page and metadata](https://developer.apple.com/app-store/product-page/)
- [App Store search](https://developer.apple.com/app-store/search/)
- [PPO eligibility](https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization/)
- [PPO developer examples](https://developer.apple.com/app-store/product-page-optimization/)
- [Custom product pages](https://developer.apple.com/app-store/custom-product-pages/)
- [Submit custom product pages](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-a-custom-product-page/)
- [Analytics](https://developer.apple.com/app-store-connect/analytics/)
- [Ratings and reviews](https://developer.apple.com/app-store/ratings-and-reviews/)
- [In-app events](https://developer.apple.com/app-store/in-app-events/)
