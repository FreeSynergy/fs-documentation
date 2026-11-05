# Message Bubble - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Shows one chat message; always used through a list or as a quoted element.

## Examples

```jsx
<MessageBubble message={m} variant={m.own ? "own" : "incoming"} onReply={reply} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Chat | inside [message-list](../message-list/) |
| Search hit | `compact` |
| Forwarded message | `compact` inside another bubble |

## Embedding in other programs (ADR 0037)

A single bubble can sit in a contact or ticket view as the "last message". Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Focusable as part of the list; Enter opens actions provided by the host.
- Reading order: sender, time, content, attachments, reactions, state.
- Reactions are announced as "Thumbs up, 2".
