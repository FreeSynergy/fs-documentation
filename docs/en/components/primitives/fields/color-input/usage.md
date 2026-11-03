# Color Input - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A color input is a colour selection field with a colour picker.

- Choosing a colour
- Colour themes
- Colour code

## Examples

### Choosing a colour

```jsx
<ColorInput value="value" onChange={action} />
```

### Colour themes

```jsx
<ColorInput value="value" placeholder="placeholder" />
```

### Colour code

```jsx
<ColorInput value="value" showIcon={true} />
```

## Notes

- States: `placeholder` (in addition to the states from `base`)
