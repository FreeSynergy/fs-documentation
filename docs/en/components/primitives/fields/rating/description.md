# Rating

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `star rating`, `heart rating`, `number rating` |
| **States** | `halb`, `read-only` |
| **Gestures** | `tap`, `drag` |
| **Animations** | `pop-in`, `elastic` |
| **Related** | `slider`, `number-input`, `badge` |
| **Status** | documented |

## Description
A rating is a star or point evaluation.

## Purpose

- Product ratings
- Service ratings
- Stars

## Variants

| Variant | Description |
|---------|-------------|
| **star rating** | stars |
| **heart rating** | hearts |
| **number rating** | numbers |

## Features

- Max stars (usually 5)
- Read-only
- Interactive

## Distinction

- **Do not confuse with** [slider](../slider/): the slider is a continuous scale with no
  value judgement, the rating strip is a discrete evaluation with a meaning per step.
- **Do not confuse with** [number-input](../number-input/): there you enter a value,
  here you choose a step.
- Purely displaying an existing rating (count, average) belongs as a
  [badge](../../feedback/badge/) in lists – the read-only rating shows the distribution.

## Best Practices

- Five steps as the standard; label every step ("1 = poor … 5 = very good"),
  stars alone are ambiguous.
- Only allow half steps when the evaluation really needs them.
- In lists, show them read-only and put the number of ratings next to them.
- Keyboard: arrow keys change the step, `aria-valuenow` describes the current value.

## See also

- [fields – overview](../index.md)
- [Slider](../slider/) — continuous scale
- [Badge](../../feedback/badge/) — a number instead of a strip
- [Base component](../../basics/base.md)
