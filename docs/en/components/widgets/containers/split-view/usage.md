# Split View - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A split view is a layout with two areas side by side.

- List + detail view
- Comparison views
- Sidebar + main content
- Previews

## Examples

### List + detail view

```jsx
<SplitView leftContent="Content" rightContent="Content" />
```

### Comparison views

```jsx
<SplitView leftContent="Content" collapsible={false} />
```

### Sidebar + main content

```jsx
<SplitView leftContent="Content" responsive={true} />
```
