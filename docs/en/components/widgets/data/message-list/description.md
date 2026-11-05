# Message List

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `chat`, `thread`, `mail` |
| **States** | `loading-older`, `anchored-bottom`, `scrolled-up`, `leer` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `slide-in` (new message), `fade-in` |
| **Related** | `timeline`, `list-view`, `message-bubble`, `mail-view`, `separator` |
| **Status** | skeleton |

## Description

A message list shows the messages of one conversation in time order, anchored at the bottom, loading older ones on demand, with day and unread separators.

## Purpose

- Chat view of a conversation
- Reply thread area (side column)
- Compact message window embedded in other programs (ADR 0037)

## Variants

| Variant | Description |
|---|---|
| **chat** | flat, chronological, anchored at the bottom |
| **thread** | reply thread in a side area |
| **mail** | one row per mail, expandable ⚠️ |

## Features

- Anchored at the bottom: new messages keep the end in view
- Loads older messages while scrolling up (virtualised rows)
- Day separators and an "unread from here" separator
- Typing indicator ("is typing") as last element
- Jump to the next unread message

## Data binding

Binds a sequence of messages in one context: ActivityStreams `Note` series in a `context`, Matrix room timeline, MIMI conversation. Register (ADR 0023): `Message → bubble | mail | list-entry | text`; the list picks the representation per entry (default `bubble`, or `mail` in mail conversations). Rows are [message-bubble](../message-bubble/) or [mail-view](../mail-view/) (compact).

## Distinction

- **Do not confuse with** [timeline](../timeline/): a timeline lays events along a time axis. ⚠️ Open whether `message-list` becomes a variant of `timeline`.
- **Do not confuse with** [list-view](../list-view/): a list-view is a generic list without reverse scroll or anchoring.
- **Do not confuse with** [message-bubble](../message-bubble/): that is one message.

## Best Practices

- Keep the position when older messages load.
- Mark the unread boundary; do not jump to the end if the person scrolled up.
- Rows must be virtual; conversations have thousands of entries.

## Blinc note

Partly in Blinc: `virtual_list` exists, but reverse scrolling and bottom anchoring are missing. Built in our layer on top; a reverse-scroll option could be proposed upstream ⚠️. Backlog id: none ⚠️.

## Open points

- ⚠️ Variant of `timeline` or own component
- ⚠️ Typing indicator: part of this component (decomposition) or separate

## See also

- [data – overview](../index.md)
- [Message Bubble](../message-bubble/)
- [Mail View](../mail-view/)
- [Timeline](../timeline/)
- [List View](../list-view/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)
