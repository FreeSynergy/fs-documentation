# Mail View - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Shows one e-mail in a reading pane or as a compact preview.

## Examples

```jsx
<MailView mail={email} onOpenAttachment={save} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Mail reading pane | `full` |
| Search results | `compact` |
| Ticket history | `compact` in a [list-view](../list-view/) |

## Embedding in other programs (ADR 0037)

A compact mail view appears in a contact's history or a ticket. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Tab moves through header actions, body, attachments.
- Header fields are exposed as a description list.
- Signature and encryption state are part of the accessible name.
