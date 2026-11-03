# Toast

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `info`, `success`, `warning`, `error` |
| **States** | `paused`, `dismissing` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `slide-in`, `fade-out`, `stagger` |
| **Related** | `alert`, `badge`, `popover` |
| **Status** | documented |

## Description
A toast is a pop-up notification that usually appears top right.

## Purpose

- Short notifications
- Success messages
- Error messages
- Information messages

## Variants

| Variant | Colour | Description |
|---------|--------|-------------|
| **info** | blue | information message |
| **success** | green | success message |
| **warning** | orange/yellow | warning message |
| **error** | red | error message |

## Features

- Auto-dismiss (closes automatically)
- Dismissible (user-defined closing)
- Action button
- Position (top right, bottom right, etc.)

## Distinction

- **Do not confuse with** [alert](../alert/): a toast disappears on its own and asks for
  no reaction; an alert message stays until it is closed or resolved.
- **Do not confuse with** [alert-dialog](../../../widgets/overlays/alert-dialog/): when the user
  has to decide, a dialog is needed – a toast does not bridge a decision.
- **Do not confuse with** [popover](../../../widgets/overlays/popover/): a popover is tied to an
  element, the toast to a screen corner.
- **Do not confuse with** [badge](../badge/): a badge marks something permanently, a toast
  reports an event once.

## Best Practices

- Clear text
- Short
- Non-intrusive
- Feedback

## Layout

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Title                           │
│      Description text...                │
└─────────────────────────────────────────┘
```

## See also

- [feedback – overview](../index.md)
- [Alert](../alert/) — a message that stays
- [Alert Dialog](../../../widgets/overlays/alert-dialog/) — when the user has to decide
- [Base component](../../basics/base.md)
