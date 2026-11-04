# Rich Text Editor - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A rich text editor is an editor for formatted text.

- Documents
- Articles
- Messages

## Examples

### Documents

```jsx
<RichTextEditor value="Value" onChange={action} />
```

### Articles

```jsx
<RichTextEditor value="Value" placeholder="Placeholder" />
```

### Messages

```jsx
<RichTextEditor value="Value" placeholder="Placeholder" />
```

## Notes

- States: `placeholder` (in addition to the states from `base`)
