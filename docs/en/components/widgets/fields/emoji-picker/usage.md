# Emoji Picker - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

An emoji picker is an emoji selection for chat/comments.

- Chat
- Comments
- Messages

## Examples

### Chat

```jsx
<EmojiPicker value="value" onChange={action} />
```

### Comments

```jsx
<EmojiPicker value="value" placeholder="Placeholder" />
```

### Messages

```jsx
<EmojiPicker value="value" showSearch={true} />
```

## Notes

- States: `placeholder` (in addition to the states from `base`)
