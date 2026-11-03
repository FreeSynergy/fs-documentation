# Grid View - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A grid view is a card/grid display of elements.

- Image galleries
- Product catalogues
- Card views
- File directories

## Examples

### Image galleries

```jsx
<GridView items={entries} columns={3} />
```

### Product catalogues

```jsx
<GridView items={entries} interactive={false} />
```

### Card views

```jsx
<GridView items={entries} gap={16} />
```
