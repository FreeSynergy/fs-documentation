# Switch - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A switch is an on/off switch (toggle).

- Settings
- Features
- Status

## Examples

### Settings

```jsx
<Switch checked={false} onChange={action} />
```

### Features

```jsx
<Switch checked={false} animate={true} />
```

### Status

```jsx
<Switch checked={false} animationDuration={300} />
```

## Notes

- States: `checked` (in addition to the states from `base`)
