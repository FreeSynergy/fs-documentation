# Slider

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `number-input` |
| **Variants** | `einfach`, `bereich` |
| **States** | `dragging` |
| **Gestures** | `drag`, `tap`, `double-tap` |
| **Animations** | `press`, `elastic` |
| **Related** | `number-input`, `rating`, `progress` |
| **Status** | documented |

!!! info "Standardisation"
    The former component `range-slider` was merged into `slider` as a variant: `einfach`
    (one value) and `bereich` (two values).

## Description
A slider is a value range with a sliding control.

## Purpose

- Volume
- Rating
- Settings

## Variants

| Variant | Description |
|---------|-------------|
| **einfach** | one handle for one value |
| **bereich** | two handles, choosing a range (merged from `range-slider`) |

## Features

- Min/max
- Step
- Value

## Distinction

- **Do not confuse with** [progress](../../feedback/progress/): the progress bar is
  display only, the slider is an input.
- **Do not confuse with** [rating](../rating/): a scale with steps, here the value is
  continuous or finely divided.
- The slider shares its value logic with [number-input](../number-input/) (`min`, `max`,
  `step`); where the exact value matters, the number field is the right choice.

## Best Practices

- Show the current value with its unit, do not just let people move the handle.
- Choose `step` so that the number of steps lies between 5 and 20.
- Label the ends of the scale ("quiet – loud"), otherwise the direction is unclear.
- Keyboard operable: arrow keys move in `step`, PageUp/PageDown move further, set `aria-valuenow`.
- Paired handles (`bereich`) must not overtake each other; a double tap sets the midpoint.

## See also

- [fields – overview](../index.md)
- [Number Input](../number-input/) — entering an exact value
- [Progress](../../feedback/progress/) — showing progress
- [Base component](../../basics/base.md)
