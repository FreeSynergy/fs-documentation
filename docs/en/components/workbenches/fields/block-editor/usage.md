# Block Editor - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Edit a structured document.

## Examples

```jsx
<BlockEditor value={doc} blockTypes={allowed} onChange={save} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Wiki page | `edit` |
| Form letter | `template` |
| Embedded note | `read` |

## Embedding in other programs (ADR 0037)

Documents open in the block editor wherever they are referenced. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Slash opens the block menu; Alt+Up/Down moves a block.
- Each block is announced with its type.
- Move and convert are available without drag.
