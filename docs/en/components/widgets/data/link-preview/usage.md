# Link Preview - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Shows the preview of one link within a message.

## Examples

```jsx
<LinkPreview url={a.url} title={a.title} description={a.summary} image={a.image} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Chat | `card` below the text |
| Dense list | `compact` |

## Embedding in other programs (ADR 0037)

Previews are part of the embedded message view. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Focusable as a link; Enter opens it.
- Image has empty alt text (decorative); the title carries the meaning.
- External target is named in the accessible name.
