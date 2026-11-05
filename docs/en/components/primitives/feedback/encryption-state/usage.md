# Encryption State - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Shows the protection of one message or one conversation and leads to the guide.

## Examples

```jsx
<EncryptionState kind={conversation.encryption} />
```

```jsx
<EncryptionState variant="warning" kind="none" onActivate={openGuide} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Conversation header | `icon-text`, `medium` |
| Unencrypted incoming message | `warning`, directly at the message |
| Compact list row | `icon` only |

## Embedding in other programs (ADR 0037)

The same marker appears in every embedded message view. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Focusable; Enter and Space activate.
- The accessible name names the kind and the action ("Open guide").
- Unencrypted state is announced when a conversation is opened, not on every message.
