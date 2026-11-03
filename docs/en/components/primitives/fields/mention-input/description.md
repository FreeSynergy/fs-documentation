# Mention Input

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `text-input` |
| **Variants** | `feld`, `inline`, `mehrzeilig` |
| **States** | `open`, `loading` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `fade-in`, `pop-in` |
| **Related** | `tags-input`, `combobox`, `emoji-picker`, `text-input` |
| **Status** | documented |

## Description
A mention input is a text field with user/contact mentions.

## Purpose

- Chat
- Comments
- Messages

## Variants

| Variant | Description |
|---------|-------------|
| **feld** | an own field only for mentions (e.g. recipients) |
| **inline** | a mention in the middle of the running text of a comment |
| **mehrzeilig** | chat editor with several lines and mentions |

## Features

- @-mention
- Auto-complete
- Selected users

## Distinction

- **Do not confuse with** [tags-input](../tags-input/): tags are free terms,
  a mention points at a contact and triggers a notification.
- **Do not confuse with** [combobox](../combobox/): the combobox writes a value into the
  field, the mention embeds the person in running text.
- Typed text like "@john" without a selection is **not** a mention and creates no notification.

## Best Practices

- Only open the suggestion list after `@` and one further character, sort hits by closeness.
- Delete an inserted mention with a single backspace (treat it as atomic).
- Always show the display name, store the contact ID internally – never store the name.
- On `long-press`, open the contact card ([hover-card](../../../widgets/overlays/hover-card/) on the desktop).

## See also

- [fields – overview](../index.md)
- [Tags Input](../tags-input/) — free terms instead of contacts
- [Emoji Picker](../../../widgets/fields/emoji-picker/) — inserting characters
- [Base component](../../basics/base.md)
