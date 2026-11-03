# Emoji Picker

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `inline`, `overlay`, `reaktion` |
| **States** | `open`, `no-results` |
| **Gestures** | `tap`, `swipe`, `long-press` |
| **Animations** | `pop-in`, `stagger` |
| **Related** | `mention-input`, `rich-text-editor`, `icon`, `text-input` |
| **Status** | documented |

## Description
An emoji picker is an emoji selection for chat/comments.

## Purpose

- Chat
- Comments
- Messages

## Variants

| Variant | Description |
|---------|-------------|
| **inline** | the selection stays shown permanently below the field (compose mode) |
| **overlay** | flap at the cursor, closes after the selection |
| **reaktion** | minimal grid with a few emojis above a message |

## Features

- Categories
- Search
- Recent

## Distinction

- **Do not confuse with** [mention-input](../../../primitives/fields/mention-input/): a mention selects a person
  from a data record and creates a link, an emoji is only a character.
- **Do not confuse with** [icon](../../../primitives/media/icon/): emojis belong to the content, icons to
  the user interface. Always use `icon` for buttons and menus.
- The picker makes a selection, it does not produce content of its own.

## Best Practices

- Keep the most-used emojis at the top; categories through tabs, not endless scrolling.
- Always insert at the cursor position, not at the end of the text.
- Only offer skin and gender variants when the user explicitly chooses them.
- Limit reactions on a message (max. one per person and emoji), otherwise the
  evaluation becomes unreadable.

## See also

- [fields – overview](../index.md)
- [Mention Input](../../../primitives/fields/mention-input/) — people instead of characters
- [Rich Text Editor](../../../workbenches/fields/rich-text-editor/) — chat and comment input
- [Base component](../../../primitives/basics/base.md)
