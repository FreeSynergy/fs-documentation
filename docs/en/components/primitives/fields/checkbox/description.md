# Checkbox

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `Default`, `Toggle`, `Indeterminate` |
| **States** | `checked`, `indeterminate` |
| **Gestures** | `tap` |
| **Animations** | `tick-draw`, `press` |
| **Related** | `switch`, `radio-group`, `field`, `base` |
| **Status** | documented |

## Description
A checkbox is a yes/no or multiple-choice field.

## Purpose

- Settings
- Options
- Consent

## Variants

| Variant | Description |
|---------|-------------|
| **Default** | standard square with a tick |
| **Toggle** | box without a tick, the selection is highlighted as a surface |
| **Indeterminate** | mixed state – some, but not all, sub-options selected |

## Features

- Checked
- Indeterminate
- Disabled

## Distinction

- **Do not confuse with** [switch](../switch/): the switch applies the change
  immediately, the checkbox confirms a selection that only takes effect when the
  form is submitted.
- **Do not confuse with** [radio-group](../radio-group/): radio allows exactly one
  choice out of several, the checkbox allows several at once.
- A single checkbox for "on/off" still stays a checkbox when the user can save in
  between (form context).

## Best Practices

- Always bind the label to the box – clicking the text toggles it too.
- Use `indeterminate` only for group headers; the stored value stays `false`.
- Animate the state change (`tick-draw`), but never use movement as the only hint at the state.
- Only show errors after the field was left, not on the first empty state.

## See also

- [fields – overview](../index.md)
- [Base component](../../basics/base.md)
