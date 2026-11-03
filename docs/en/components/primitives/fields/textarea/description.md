# Textarea

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `fix`, `mitwachsend`, `chat` |
| **States** | `filled`, `error` |
| **Gestures** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animations** | `expand`, `highlight` |
| **Related** | `text-input`, `rich-text-editor`, `field`, `scroll-area` |
| **Status** | documented |

## Description
A textarea is a multi-line input field for text.

## Purpose

- Messages
- Comments
- Descriptions

## Variants

| Variant | Description |
|---------|-------------|
| **fix** | given height, longer input scrolls inside the field |
| **mitwachsend** | the height grows with the text up to a ceiling |
| **chat** | grows up to three lines, Enter sends, `Shift+Enter` wraps |

## Features

- Auto-resize
- Placeholder
- Validation

## Distinction

- **Do not confuse with** [text-input](../text-input/): here stand paragraphs and long
  sentences, there exactly one line.
- **Do not confuse with** [rich-text-editor](../../../workbenches/fields/rich-text-editor/): this field stores
  plain text without formatting.
- **Do not confuse with** [code-editor](../../../workbenches/special/code-editor/): running text needs no
  line numbers and no syntax highlighting.

## Best Practices

- Set the starting height by the expected length (comment three lines, description eight lines).
- Always give `mitwachsend` a ceiling, otherwise the field pushes the whole view away.
- Only show a character counter when there is a limit.
- `Tab` leaves the field; only offer a tab jump when code is being entered.
- Sending with `Enter` only in chat mode, otherwise `Ctrl+Enter` – sending by accident is expensive.

## See also

- [fields – overview](../index.md)
- [Text Input](../text-input/) — single line
- [Rich Text Editor](../../../workbenches/fields/rich-text-editor/) — formatted text
- [Base component](../../basics/base.md)
