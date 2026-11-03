# Slider - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A slider is a value range with a sliding control.

- Volume
- Rating
- Settings

## Examples

### Volume

```jsx
<Slider onChange={action} />
```

### Rating

```jsx
<Slider onChange={action} min={0} />
```

### Settings

```jsx
<Slider onChange={action} max={100} />
```
