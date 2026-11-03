# Combobox - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A combobox is a text field plus a dropdown.

- Address lookup
- Categories
- Search box

## Examples

### Address lookup

```jsx
<Combobox value="value" onChange={action} />
```

### Categories

```jsx
<Combobox value="value" options={entries} />
```

### Search box

```jsx
<Combobox value="value" placeholder="placeholder" />
```

## Notes

- States: `placeholder` (in addition to the states from `base`)
