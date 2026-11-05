# HTML View - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Display of foreign HTML.

## Examples

```jsx
<HtmlView html={mail.htmlPart} baseParts={mail.inlineParts} onLinkClick={openLink} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Mail body | `sanitised` |
| Newsletter with consent | `remote-allowed` |

## Embedding in other programs (ADR 0037)

Any program that shows mails uses the same view. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Content is navigable by the screen reader's document mode.
- Links are focusable and announce their target domain.
- Images without alt text are skipped.
