# Interface and Store localization — future release requirement

Owner clarification, 18 November 2026: establish this as a requirement for future updates; do not translate or change current app behavior as part of the policy task. The owner will adjust existing apps. Agents must check the actual implementation next time rather than assume the policy means translations exist.

## Coverage baseline

LANGUAGES.json defines a 12-language initial UI baseline: English, Simplified Chinese, Hindi, Spanish, French, Arabic, Bangla/Bengali, Portuguese (Brazil), Russian, Indonesian, German and Japanese. The required language families include English, Chinese, Spanish, Arabic, Indonesian, Portuguese, French, Japanese, Russian and German. Retain Hindi and Bangla from the existing baseline. Add Traditional Chinese and European Portuguese variants when audience, storefront and script/region needs warrant them. This is a practical coverage choice, not a claim of a definitive current top-ten ranking. Speaker totals vary by L1/L2 definition, date and dataset; do not copy restricted Ethnologue data into the public repo. Revisit coverage with real app/storefront usage and properly licensed public data.

New or changed user-facing UI must use the app's established localization system and include the baseline languages. Before the next user-facing Store release, audit the whole shipped UI and metadata against this baseline. Missing translations, broken default selection or unreviewed layouts are explicit release blockers; report them with a plan. Only an explicit owner exception can waive the gate, including an urgent hotfix. Do not silently claim that resource placeholders or English fallbacks count as translated support.

## Device default and language boundaries

The first-run default is the user's supported system/per-app preferred language, using Apple's normal language negotiation and native resources or the project's compatible framework equivalent. Respect the ordered preference list, supported language/script/region matching and English fallback. Honor an existing explicit user override; offer System as the default where an in-app selector exists. Do not infer language from IP, country, timezone, a dictionary choice or the first entry of an unordered object. Test language changes and any documented restart behavior.

Keep interface locale separate from reading text, subtitles, dictionary meanings, vocabulary, names, audio and the language being learned. Do not translate user media or expand a Japanese dictionary dataset to twelve definition languages to satisfy UI localization. Dictionary-only/data repositories are exempt from changing lexical content; their actual website/tool UI can still need localization. Preserve existing supported languages and localized saves/settings.

## Translation completeness and quality

Inventory screens, menus, onboarding, errors, empty/loading states, settings, accessibility labels, notifications/widgets/extensions, permission descriptions, help and release copy. Use stable semantic keys/context or native string catalogs; no blanket search-and-replace of source literals and no duplicate ad-hoc translation engine. Declare supported bundle locales only when corresponding resources are real and usable. Preserve placeholders, formatting types, plural rules, units, dates/numbers, links and product names.

Use native/layout-leading concepts and test Arabic RTL, mixed-script text, long German/Russian strings, Hindi/Bangla shaping, CJK line breaking, Dynamic Type, VoiceOver and font glyph coverage. AI and machine translations are accepted for app UI, accessibility text, permission prompts, support material and Store listings. Internal checks may be performed by an agent. External language review and native-speaker sign-off are optional and do not gate release. Fix known meaning errors, misleading claims and broken rendering before shipping. Tests verify missing keys, placeholders/plurals, default/override/fallback behavior and representative localized native flows; screenshots of translated text alone do not prove functional correctness.

Render the localized text directly. Keep translation source and completed checks in internal
release evidence. Do not ship translator notes, AI attribution, draft badges, “unverified
text” labels or their localized equivalents in app UI, accessibility text, Store copy,
screenshots, or support material. Check changed locales and published assets for these
labels and their equivalents before release. Resolve failures found by internal checks through
the existing release process.

## App Store and release evidence

Localize relevant name/subtitle/keywords/description/promo/What's New, feature-card text, previews and support text for each target supported by Apple. Re-research intent per language instead of translating the keyword comma list. UI BCP-47 tags and App Store Connect locale identifiers are not interchangeable: resolve Apple's current labels/shortcodes before upload. Apple added Bangla and Urdu among new metadata languages in March 2026; old supported-language lists are stale. Verify current platform/locale availability and the live record.

Storefront listing language can differ from runtime UI language. Test actual product-page previews and the runtime preferred-language behavior separately. If a locale is unavailable for a placement, document its supported fallback; do not create an invented locale identifier or advertise full UI support based only on a translated listing. Privacy/support claims and content-language restrictions must remain understandable.

Add a release coverage table: target language; app/extension/permission-string completion; metadata/assets completion; default/override/fallback tests; native layout/accessibility evidence; translation source and internal checks; unresolved gaps/owner exception. Use complete/partial/missing/untested honestly. Policy targets do not count as completed translations.

## Sources

- [Apple localization and per-app language preferences](https://developer.apple.com/localization/)
- [Apple language negotiation background](https://developer.apple.com/library/archive/qa/qa1828/_index.html)
- [Preparing app text for translation](https://developer.apple.com/documentation/xcode/preparing-your-apps-text-for-translation)
- [Current App Store metadata languages](https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-localizations/)
- [March 2026 metadata language expansion](https://developer.apple.com/news/?id=97t4mt64)
- [Ethnologue 2026 dataset scope and license](https://shop.ethnologue.com/products/2026-ethnologue-200)
