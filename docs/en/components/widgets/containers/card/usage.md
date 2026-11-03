# Card - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The card is a container element that presents content in a structured box with a
title, content and optional actions.

- Grouping information that belongs together
- Visual separation of content
- Showing mini overviews (e.g. customer, task, message)

## Examples

### Grouping information that belongs together

```jsx
<Card title="Title" subtitle="Subtitle" content="Content" />
```

### Visual separation of content

```jsx
<Card title="Title" subtitle="Subtitle" interactive={false} />
```

### Showing mini overviews (e.g. customer, task, message)

```jsx
<Card title="Title" subtitle="Subtitle" responsive={true} />
```
