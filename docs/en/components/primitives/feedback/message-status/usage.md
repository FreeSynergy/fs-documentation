# Message Status - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Shows the delivery state of one sent message. Used inside [message-bubble](../../../widgets/data/message-bubble/) and as an entry in list rows.

## Examples

```jsx
<MessageStatus status={message.state} at={message.stateAt} />
```

```jsx
<MessageStatus variant="icon-text" status="failed" reason="No encrypted path" />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Chat bubble | `icon`, `small`, next to the time |
| Sent-mail list | `icon` in a column |
| Failure | `failed` plus retry action offered by the host |

## Embedding in other programs (ADR 0037)

Message state is shown wherever a message appears. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Not focusable on its own; the tooltip text is part of the parent's accessible name.
- Screen readers read the state word ("Read"), not the glyph.
- State changes are announced politely only for the newest message of a conversation.
