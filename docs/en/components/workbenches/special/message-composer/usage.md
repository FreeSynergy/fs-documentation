# Message Composer - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Writing surface for chat and mail.

## Examples

```jsx
<MessageComposer variant="mail" draft={draft} onChange={save} onSend={send} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Messenger chat | `chat` |
| Mail | `mail` |
| Helpdesk reply | `reply` under the ticket |

## Embedding in other programs (ADR 0037)

As reply field in tickets, contacts and tasks. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Ctrl+Enter sends (configurable by the frontend); Enter adds a line in the mail variant.
- Tab order: recipients, subject, text, attachments, send.
- Autocomplete lists are announced by count.
