# dot. controls

Use the [dot. copy guide](../kit/guidelines/copy.md) to choose between symbols,
short labels and supporting text.

Use Apple’s standard symbols and controls across macOS, iPhone, and iPad.
Use system navigation and toolbar items where the platform provides them.
The inline icon button uses a 21-point SF Symbol that scales with text
settings inside a minimum 44-point target. The borderless style lets groups
of secondary actions sit together, while native controls handle interaction
states. Use the app’s accent for selection or an active setting where useful.

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
[Apple toggles](https://developer.apple.com/design/human-interface-guidelines/toggles) ·
[SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)

## Shared action meanings

| Intent | Native symbol or control | In a React Native surface |
| --- | --- | --- |
| Bring existing files or media into the app | `square.and.arrow.down`. A native folder picker that selects a scan scope can use `folder`. | Use an arrow entering a tray, such as Ionicons `download-outline`, for a local file import. Pair it with a clear Import label when space allows. |
| Find content | `magnifyingglass` or the platform search field. | `search-outline` with a localized accessible name. |
| Dismiss an overlay | `xmark` for an icon-only close. Keep native Back, Cancel, and Done where they express navigation, cancellation, or completion. | `close-outline`. Name the object being dismissed, such as Close lookup. |
| Show the current choice | Native selection when available. For custom controls, add a checkmark, a filled symbol, or a distinct shape with the app accent and announce the selected state. | Use `accessibilityState.selected` with a perceptible visual indicator and the app accent. |

Keep the icon and its hit area separate. An icon-only action needs a localized name and at least a 44-point touch target. A plain plus creates something new. Selection describes the current choice and stays distinct from transient press feedback. Preserve each product’s accent, layout, feature entry points and native focus behavior.

## Render the specimen on a Mac

From the kit checkout, compile and render the fixture without opening a window.

```sh
swiftc Sources/DotFoundation/*.swift fixtures/render-controls.swift -o /tmp/dot-controls-preview
/tmp/dot-controls-preview /tmp/dot-controls.png
```
