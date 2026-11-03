# Panel - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A panel is a large container with a header, content and footer.

- Large content blocks
- Layout containers
- Filter panel
- Dashboard widget

## Examples

### Large content blocks

```jsx
<Panel title="Title" content="Content" footer="footer" />
```

### Layout container

```jsx
<Panel title="Title" content="Content" collapsible={false} />
```

### Filter panel

```jsx
<Panel title="Title" content="Content" draggable={false} />
```
