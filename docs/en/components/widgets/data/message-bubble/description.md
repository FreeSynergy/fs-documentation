# Message Bubble

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `incoming`, `own`, `compact` |
| **States** | `own`, `incoming`, `selected`, `edited`, `deleted`, `failed` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `slide-in`, `pop-in` (reaction) |
| **Related** | `message-list`, `message-status`, `encryption-state`, `reaction-bar`, `link-preview`, `avatar` |
| **Status** | skeleton |

## Description

A message bubble shows one chat message with sender, content, reply reference, reactions, delivery state and encryption.

## Purpose

- One message inside a [message-list](../message-list/)
- Search hits and previews (compact)
- Quoted/forwarded message

## Variants

| Variant | Description |
|---|---|
| **incoming** | left, with sender name and avatar |
| **own** | right, with delivery status |
| **compact** | one line, for search results and previews |

## Features

- Sender, time and edit mark
- Reply reference with a jump to the original
- Attachments and [link-preview](../link-preview/)
- [reaction-bar](../reaction-bar/) below the content
- [message-status](../../../primitives/feedback/message-status/) and [encryption-state](../../../primitives/feedback/encryption-state/)
- Tombstone for deleted messages

## Data binding

Binds one message: ActivityStreams `Note` plus MIMI content / Matrix event. Register (ADR 0023): `Message → bubble`. The same data type is shown by [mail-view](../mail-view/) (`mail`), list rows (`list-entry`) and as plain `text`.

## Distinction

- **Do not confuse with** [mail-view](../mail-view/): a mail has header fields, body and attachments; a bubble is a chat line.
- **Do not confuse with** [card](../../containers/card/): a card is generic; the bubble binds the message model.
- **Do not confuse with** [message-list](../message-list/): that one lays out many bubbles.

## Best Practices

- The sender is visible without hover.
- Group consecutive messages of one sender; show the avatar once.
- Actions (reply, react, edit) are offered by the host, e.g. as a hover bar or via a swipe gesture from the frontend (ADR 0037).

## Blinc note

No Blinc equivalent. Built in our layer on `cn::card`-like primitives. Backlog id: none ⚠️.

## Open points

- ⚠️ Rendering of rich text (rich-text-editor read-only mode, planned change)
- ⚠️ Thread indicator inside the bubble

## See also

- [data – overview](../index.md)
- [Message List](../message-list/)
- [Reaction Bar](../reaction-bar/)
- [Link Preview](../link-preview/)
- [Mail View](../mail-view/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)
