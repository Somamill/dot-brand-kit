# dot. controls

Use familiar symbols for repeat actions. Keep the controls mostly monochrome
and give the app's registered accent to active states. Rounded buttons and a
quiet background take a cue from [Nothing OS](https://nothing.community/en/d/61774).
The icon set pairs a rounded stroke with small dots inside selected glyphs.
The dots are part of the artwork. Use separate native indicators for status.
The default glyph is 26 points and scales with text settings. Keep icons
monochrome so product accents and state affordances remain clear.

| Intent | Control | How to use it |
| --- | --- | --- |
| Go back | Native navigation, or `DotIconButton(.back, …)` | Use the system Back control when available. In custom chrome, put the semantic backward chevron on the leading edge and return to the previous screen. |
| Dismiss | `DotIconButton(.close, …)` | Use the × for closing a sheet or dismissing a view. |
| Find or configure | `DotIconButton(.search, …)` or `.settings` | A magnifier opens search. A gear opens settings. Place the control near its scope. |
| Play or pause | `DotIconButton(.play, …)` or `.pause` | Show the symbol and spoken name for the next action. |
| Enable or disable a setting | `DotSwitch` | Use a native settings row and name the setting. The thumb position communicates state alongside tint. |
| Confirm, delete, or perform an unfamiliar action | Visible localized label | Use a short verb and add a familiar icon when it adds clarity. |

Supply localized action names for VoiceOver and Mac tooltips, including for
icon-only controls. Keep native keyboard behavior and visible focus. Check
the backward chevron and leading placement in RTL, both switch positions
with color removed, and the disabled state in light and dark modes. Dot icon
buttons provide a 44-point minimum target. On the web, use a real button with
an accessible name and a labeled native checkbox for binary settings.

```swift
DotIconButton(.back, title: "Back", action: goBack)
DotSwitch("Notifications", isOn: $notificationsEnabled)
```

[Apple buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) ·
[Apple toggles](https://developer.apple.com/design/human-interface-guidelines/toggles)

## Render the specimen on a Mac

From the kit checkout, compile and render the fixture without opening a window.

```sh
swiftc Sources/DotFoundation/*.swift fixtures/render-controls.swift -o /tmp/dot-controls-preview
/tmp/dot-controls-preview /tmp/dot-controls.png
```
