# Credits

Every registered dot. app includes Credits in its native About or Settings
screen. A registered product with a web interface can place Credits in About
or the site footer. Read the shared credit details from
[`foundation/credits.json`](../foundation/credits.json) at the app's
reviewed kit revision. Keep product-specific credits and license notices
with the product.

## What appears

- **Made by Max** and **Part of dot.** as concise credits. Localize the
  surrounding words and preserve names and URLs.
- **Send feedback** opens a new email to `max@miller-max.com`, the main
  public contact from the shared credit details. Make the address easy to copy.
  Welcome questions, ideas, and bug reports. Suggested copy: “Got an idea or
  spotted something odd? I’d love to hear from you.”
- **Support on Ko-fi** links to Max's approved Ko-fi page on surfaces where
  an external tip link is permitted. Use a native link with a clear label
  and open the person's browser. Support is voluntary and provides no
  app features, content or privileges.
- **Social links** appear only when Max supplies and approves public
  account URLs. Add each approved account to the shared `socials` array
  with a `name` and an HTTPS `url`. Give each link a visible name and an
  accessible label. Hide the section while the list is empty.

Publish the same email on the product website, repository README, and the public support page used in App Store Connect. Keep App Review contact details in their separate fields. Invite users to email freely and let them decide what to send. Do not attach logs, files, or personal data automatically. App Store editions must check the applicable App Review
rules for the release and storefront before enabling a direct Ko-fi link or
other in-app tipping prompt. Where no permitted route is established, show
the creator and suite credits in the app and keep Ko-fi on the website and
README. See [Apple's payment rules and gift exception](https://developer.apple.com/app-store/review/guidelines/#business).

For repository and portfolio social icons, use the [README presentation standard](README_PRESENTATION.md). The suite’s Reddit profile is an additional place to share feedback. Keep the direct email option available.

## Adoption checks

Open Credits in the app's normal entry point. Verify the approved URL,
keyboard and screen-reader access, localized names, and the absence of a
social heading when there are no links. For Store builds, verify the
support row in every applicable storefront configuration. Keep the
pinned credit details and rendered UI in sync when the owner adds socials
or changes the support destination.
