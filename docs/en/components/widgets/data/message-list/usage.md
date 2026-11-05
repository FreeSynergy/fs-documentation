# Message List - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Shows one conversation. The hosting program decides which actions and gestures belong to the rows.

## Examples

```jsx
<MessageList
  context={conversation.id}
  messages={messages}
  onLoadOlder={loadOlder}
  onVisible={markRead}
/>
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Messenger chat | `chat`, full area |
| Helpdesk ticket | `chat`, `small`, with a reply field below |
| Thread | `thread` in a [drawer](../../overlays/drawer/) |

## Embedding in other programs (ADR 0037)

The message list in a ticket or contact view shows one folder/group only. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Up/Down moves between messages, Home/End jumps to first/last, a shortcut jumps to the next unread.
- Screen readers announce new incoming messages politely; own messages are not announced.
- Separators are read as headings ("Yesterday").
