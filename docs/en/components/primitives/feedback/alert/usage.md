# Alert - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

An alert is a status message (info, warning, error, success).

- Show status messages
- Show errors
- Show successes
- Show warnings

## Examples

### Showing a status message

```jsx
<Alert type="info" title="Title" message="Message" />
```

### Showing an error

```jsx
<Alert type="info" title="Title" dismissible={false} />
```

### Showing a success

```jsx
<Alert type="info" title="Title" closable={false} />
```

## Notes

- Accessibility: role `alert`; name the controls additionally with `label` or `aria-label`
- Gestures: `tap`
- Transitions: `fade-in`, `collapse`
- See also: [toast](../../feedback/toast/), [badge](../../feedback/badge/), [progress](../../feedback/progress/)
