# Dashboard - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A dashboard is an overview page with widgets.

- Overview
- Analytics
- Project

## Examples

### Overview

```jsx
<Dashboard widgets={items} />
```

### Analytics

```jsx
<Dashboard widgets={items} dragAndDrop={true} />
```

### Project

```jsx
<Dashboard widgets={items} responsive={true} />
```

## Notes

- Gestures: `drag`
