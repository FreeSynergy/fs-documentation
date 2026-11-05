# Message Status

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `icon`, `icon-text` |
| **States** | `sending`, `sent`, `delivered`, `read`, `failed` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `pop-in` (state change) |
| **Related** | `badge`, `encryption-state`, `progress`, `tooltip`, `message-bubble` |
| **Status** | skeleton |

## Description

A message status shows how far a sent message has come: being sent, sent, delivered, read or failed. It is a small display element and is not operable.

## Purpose

- State of a sent message in a bubble or list row
- Delivery and read receipts (read receipts are the person's choice)
- Error marker with the reason as tooltip, e.g. no encrypted path

## Variants

| Variant | Description |
|---|---|
| **icon** | state icon only, for bubbles and list rows |
| **icon-text** | icon with a short word, for details and tables |

## Features

- Five states, each distinguishable without colour (icon shape and tooltip text)
- Tooltip with the time of the state change (see [tooltip](../../../widgets/overlays/tooltip/))
- Hidden for incoming messages

## Data binding

Binds the **message state**: MIMI message-status draft `-02`, ActivityStreams `Read`, Matrix `m.receipt`, mail DSN/MDN. In the representation register (ADR 0023): `MessageState → message-status | text`. The state is stored **locally** in `fs-store` (ADR 0037), so previews work without a Matrix or mail server behind them. ⚠️ Whether `sending` is a stored state or only a UI state is open.

## Distinction

- **Do not confuse with** [badge](../badge/): a badge is a free-form marker, this component has a fixed state set bound to the message model.
- **Do not confuse with** [progress](../progress/): there is no percentage, only discrete states.
- **Do not confuse with** [encryption-state](../encryption-state/): that one says *how* a message is protected and is operable.

## Best Practices

- Never rely on colour alone; the icon shape differs per state.
- Show `failed` permanently, the other states can fade after a while.
- Offer a retry through the host (bubble menu), not inside this component.

## Blinc note

Not in Blinc (`cn::badge` is the closest, no direct equivalent). Built in our layer because it binds the message state. Backlog id: none ⚠️ (decomposition has no Blinc issue for it).

## Open points

- ⚠️ Group chats: aggregated state (delivered to 3 of 5) or per recipient?
- ⚠️ Mail: is a DSN `delivered` the same as chat `delivered`?

## See also

- [feedback – overview](../index.md)
- [Badge](../badge/)
- [Encryption State](../encryption-state/)
- [Message Bubble](../../../widgets/data/message-bubble/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../basics/base.md)
