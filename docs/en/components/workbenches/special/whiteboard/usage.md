# Whiteboard - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A whiteboard is a drawing surface for collaboration.

- Brainstorming
- Planning
- Collaboration

## Examples

### Brainstorming

```jsx
<Whiteboard toolbar={entries} onChange={action} />
```

### Planning

```jsx
<Whiteboard toolbar={entries} interactive={true} />
```

### Collaboration

```jsx
<Whiteboard toolbar={entries} grid={true} />
```
