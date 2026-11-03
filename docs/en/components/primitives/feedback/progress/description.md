# Progress

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `linear`, `circular`, `mit-label`, `unbestimmt` |
| **States** | `indeterminate`, `completed` |
| **Gestures** | none – display only |
| **Animations** | `progress`, `pulse` |
| **Related** | `spinner`, `slider`, `skeleton`, `toast`, `base` |
| **Status** | documented |

## Description

A progress indicator shows how far a started action has come – or that it is
running, without the value being known.

## Purpose

- File transfers, import/export, generating reports
- Feedback on multi-step actions (wizard steps)
- Capacity display (storage, quota)

## Variants

| Variant | Description |
|---------|-------------|
| **linear** | bar from left to right |
| **circular** | ring, for compact surfaces |
| **mit-label** | percentage or text above or inside the bar |
| **unbestimmt** | animation without a value, when the duration is unknown |

## Features

- Freely configurable value range (`min`/`max`)
- Colour switches on success or error
- Smooth value change instead of a jump

## Distinction

- **Do not confuse with** [spinner](../spinner/): a spinner shows no amount of
  progress.

- **Do not confuse with** [slider](../../fields/slider/): a slider is an
  **input**, progress is display only.

- **Do not confuse with** [skeleton](../skeleton/): a skeleton shows a layout,
  progress a started action.

## Best Practices

- Use an indeterminate display only when a value really cannot be determined.
- Never leave progress as the only feedback – end with a message
  ([toast](../toast/)).

- Only show the value in percent when it is meaningful ("3 of 10 files"
  is better than "30 %").

## See also

- [Spinner](../spinner/)
- [Skeleton](../skeleton/)
- [Toast](../toast/)
- [Base component](../../basics/base.md)
