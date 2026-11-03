# Toast - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A toast is a pop-up notification that usually appears top right.

- Short notifications
- Success messages
- Error messages
- Information messages

## Examples

### Short notifications

```jsx
<Toast type="info" title="Title" message="Message" />
```

### Success messages

```jsx
<Toast type="info" title="Title" autoDismiss={true} />
```

### Error messages

```jsx
<Toast type="info" title="Title" dismissDelay={3000} />
```
