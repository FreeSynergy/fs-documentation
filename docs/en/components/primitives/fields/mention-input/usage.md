# Mention Input - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A mention input is a text field with user/contact mentions.

- Chat
- Comments
- Messages

## Examples

### Chat

```jsx
<MentionInput value="value" onChange={action} />
```

### Comments

```jsx
<MentionInput value="value" users={entries} />
```

### Messages

```jsx
<MentionInput value="value" placeholder="placeholder" />
```

## Notes

- States: `placeholder` (in addition to the states from `base`)
