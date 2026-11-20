# Voice and copy

Use calm, direct language and sentence case. Name an action with a verb
such as “Save article” or “Open book.” Describe supported features and
platforms accurately. The dot. signature signals membership.

## Decide how much text the control needs

Start with the task. The screen's title, placement and native controls
should communicate what a person can do. Remove a line if the same
information is already clear in the interface.

| Use | When | Example |
| --- | --- | --- |
| Familiar symbol | The action is familiar in this context and people can predict the result. | Back in a navigation bar, Play in a player. |
| Symbol and short label | The object, scope or outcome needs a name. | “Import subtitles,” “Save to vocabulary.” |
| Setting name and native switch | A persistent setting has two states. | “Autoplay” plus a switch. Its position shows on or off. |
| Setting name and current value | The setting has several values. | “Playback speed” with “1.25×” and a native picker. |
| Visible action verb and essential detail | The decision affects files, privacy, money or other consequential state. | “Delete 3 downloads.” Explain where the files are removed if the scope matters. |

Give icon-only controls a localized accessibility name and Mac tooltip
or menu label as appropriate. Use consistent symbols for the same action.
Keep visible input labels, important state and recovery instructions.
When a control needs its label for discovery, make that label available
on touch as well as with a pointer. Pair color with position, shape, text,
or another perceptible cue. Use the [dot. controls](../../docs/CONTROLS.md).

## Remove the copy that has no job

- **Headings and summaries.** A settings title and working controls can
  carry a screen. Cut subtitles, filler badges, and sentences that repeat
  the heading or describe what the user can already see.
- **Feedback.** Let a saved item appear in its destination or update the
  control state. Use brief feedback when the result is otherwise hard to
  notice. For an error, say what happened and how to recover.
- **Help.** Keep essential instructions beside the decision. Put optional
  details in an inline disclosure or Help. Show a hint at the point of need
  when revealing a new gesture or interaction.
- **Playfulness.** Use a product accent, a responsive control state,
  a brief motion cue or a restrained illustration where it helps orient the
  user. Respect Reduce Motion and retain useful cues without animation.
  Keep terms stable across languages and avoid jokes in errors or warnings.

| Before | After |
| --- | --- |
| “Playback settings” and “Configure your playback preferences below.” | “Playback” above the controls. |
| “Toggle automatic playback on or off.” | “Autoplay” with the native switch. |
| “Use this feature to bring your own subtitle files into Immersed.” | “Import subtitles.” Show supported formats near the picker if needed. |
| “Your operation could not be completed at this time.” | “Couldn’t connect. Check the address and try again.” |
| A trash icon acting on several selected downloads. | “Delete 3 downloads” in the confirmation. |

## Check the actual screen

Use a task scenario and open the interface in a second language. Check
whether the main next action is apparent, what each exposed switch changes,
and whether the outcome is visible after acting. Check the native
accessibility name, role and state, keyboard access, and RTL where applicable.
If a symbol depends on a tooltip or a guess, add a short visible label.
Check first use and failure states alongside repeat use. Report usability
observations based on actual sessions.

## Research

- Apple prioritizes concise wording, clear hierarchy and recognizable
  platform controls. [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles)
  · [Icons](https://developer.apple.com/design/human-interface-guidelines/icons)
  · [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles)
- Icon research treats familiarity, complexity and closeness to the meaning
  as distinct properties. Check a symbol in its task context.
  [McDougall et al., symbol norms](https://pubmed.ncbi.nlm.nih.gov/10502873/)
  · [McDougall et al., user performance](https://pubmed.ncbi.nlm.nih.gov/11218339/)
- For web input controls, give users enough visible context to know what to
  enter or choose. Write action labels that tell users what will happen.
  [W3C labels and instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions)
  · [GOV.UK button guidance](https://design-system.service.gov.uk/components/button/)
