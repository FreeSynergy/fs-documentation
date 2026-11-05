# Reaction Bar

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `inline`, `compact` |
| **States** | `own-active`, `empty` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `pop-in` (count change) |
| **Related** | `badge`, `emoji-picker`, `message-bubble`, `tooltip` |
| **Status** | skeleton |

## Description

A reaction bar shows reactions to a message as emoji with a count and lets the person toggle their own reaction.

## Purpose

- Reactions below a chat message
- Quick react via an [emoji-picker](../../fields/emoji-picker/) (variant `reaction`)
- Aggregated view of who reacted (tooltip)

## Variants

| Variant | Description |
|---|---|
| **inline** | row of emoji chips under a message |
| **compact** | one summary chip with the total |

## Features

- Emoji plus count per chip
- Own reaction highlighted; click toggles
- "+" chip opens the emoji picker
- Tooltip lists who reacted

## Data binding

Binds aggregated reactions: ActivityStreams `Like` / `EmojiReact` with `Undo`, MIMI reaction, Matrix `m.annotation`. Register (ADR 0023): `Reaction → reaction-bar | text`. ⚠️ Not in our frontend files; known from the products (messenger requirement `message.react`).

## Distinction

- **Do not confuse with** [badge](../../../primitives/feedback/badge/): a badge is not operable.
- **Do not confuse with** [emoji-picker](../../fields/emoji-picker/): that selects an emoji; the bar shows and toggles existing reactions.

## Best Practices

- Cap the chips and group the rest in an overflow chip.
- Each chip needs a text name for screen readers.
- Do not expose who reacted if the conversation hides it.

## Blinc note

Partly in Blinc (`badge`, `toggle_group`). Built in our layer because of the reaction data model. Backlog id: none ⚠️.

## Open points

- ⚠️ Custom emoji (images) – supported?

## See also

- [data – overview](../index.md)
- [Message Bubble](../message-bubble/)
- [Emoji Picker](../../fields/emoji-picker/)
- [Badge](../../../primitives/feedback/badge/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)
