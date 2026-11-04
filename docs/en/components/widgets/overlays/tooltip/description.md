# Tooltip

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `top`, `bottom`, `left`, `right`, `auto` |
| **States** | `open` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `fade-in`, `fade-out` |
| **Related** | `popover`, `label`, `base`, `field` |
| **State** | documented |

## Description

A tooltip shows a short explanation of an element — as text, without interactive
content. It appears on hover or long-press and disappears by itself.

## Purpose

- Explaining icon-only buttons and abbreviated values
- A short addition to a field (not as a replacement for a label)
- Full text when a field only displays its content

## Variants

| Variant | Description |
|---------|-------------|
| **top** | above the element (standard) |
| **bottom** | below the element |
| **left** / **right** | to the side |
| **auto** | picks the best side itself when space is tight |

## Features

- Delay (`delay`) against accidental triggering
- Arrow (`arrow`) marks the reference element
- Mobile: triggered by long-press

## Distinction

- **Do not confuse with** [popover](../popover/): a popover contains interactive content,
  a tooltip only text.
- **Do not confuse with** [hover-card](../hover-card/): the hover card shows a preview as a
  card and stays open as long as the pointer stays in the content.
- **Do not confuse with** [label](../../../primitives/basics/label/): a label is permanently
  visible and linked to the element.

## Best Practices

- Under 100 characters; sentences rather than paragraphs.
- Never hide decisive information exclusively in the tooltip.
- Keyboard users reach the tooltip via `focus`.
- Icon-only buttons additionally need an `aria-label`.

## See also

- [overlays – overview](../index.md)
- [Popover](../popover/)
- [Base component](../../../primitives/basics/base.md)
- [Gestures](../../../../interactions/gestures/)
- [Animations](../../../../interactions/animations/)
