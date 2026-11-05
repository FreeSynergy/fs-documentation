# Rule Editor - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Edits the rule set of one account or conversation.

## Examples

```jsx
<RuleEditor rules={rules} vocabulary="mail" onChange={update} onSave={store} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Mail filters | `list`, settings page |
| Word filter | `simple` |
| From the filter context menu | pre-filled new rule |

## Embedding in other programs (ADR 0037)

Rules apply to folders and groups; helpdesk can embed a reduced editor for ticket routing. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Tab through the fields of a row; Alt+Up/Down moves a rule.
- Each row has a sentence-style accessible name.
- Validation errors are linked to their fields.
