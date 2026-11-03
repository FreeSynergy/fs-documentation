# Radio Group - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A radio group is a group of radio buttons (single choice).

- Choices
- Options
- Settings

## Examples

### Choices

```jsx
<RadioGroup options={entries} onChange={action} />
```

### Options

```jsx
<RadioGroup options={entries} name="name" />
```

### Settings

```jsx
<RadioGroup options={entries} showIcons={false} />
```
