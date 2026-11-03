# Color Input

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `palette`, `spectrum`, `code` |
| **States** | `open`, `error` |
| **Gestures** | `tap`, `drag` |
| **Animations** | `fade-in`, `expand` |
| **Related** | `emoji-picker`, `field`, `base` |
| **Status** | documented |

## Description
A color input is a colour selection field with a colour picker.

## Purpose

- Choosing a colour
- Colour themes
- Colour code

## Variants

| Variant | Description |
|---------|-------------|
| **palette** | grid with preselected colours (brand and theme colours) |
| **spectrum** | free choice over a colour area and a hue slider |
| **code** | only a text field for a hex, RGB or HSL value |

## Features

- Colour palette
- Colour spectrum
- Hex code

## Distinction

- **Do not confuse with** [emoji-picker](../../../widgets/fields/emoji-picker/): both open a selection
  overlay, the emoji picker chooses characters, this one colour values.
- The actual overlay character (a colour area outside the field) means the colour is
  not a pure field: the field itself is `code`, the rest behaves like a picker.
- Purely showing colours (without a choice) belongs in [badge](../../feedback/badge/)
  or in the colour tokens, not here.

## Best Practices

- In applications, only offer `palette`; free colour choice (`spectrum`) stays reserved
  for design tools and the editor.
- Always show both forms: colour swatch and text value, so values stay correctable later.
- Check the contrast against the background; for very light or very dark colour values
  strengthen the border.

## See also

- [fields – overview](../index.md)
- [Base component](../../basics/base.md)
