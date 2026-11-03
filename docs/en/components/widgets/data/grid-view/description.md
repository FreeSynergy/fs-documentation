# Grid View

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `Fixed Grid`, `Responsive Grid`, `Masonry Grid` |
| **States** | `selected`, `dragging` |
| **Gestures** | `tap`, `drag`, `long-press`, `swipe` |
| **Animations** | `stagger`, `fade-in`, `reorder` |
| **Related** | `list-view`, `table`, `gallery`, `carousel` |
| **Status** | documented |

## Description
A grid view is a card/grid display of elements.

## Purpose

- Image galleries
- Product catalogues
- Card views
- File directories

## Variants

| Variant | Description |
|---------|-------------|
| **Fixed Grid** | fixed number of columns |
| **Responsive Grid** | adjustable columns |
| **Masonry Grid** | irregular cards |

## Features

- Responsive
- Hover effect
- Selection
- Drag and drop

## Distinction

- **Do not confuse with** [list-view](../list-view/): the list shows one row per entry,
  the grid view one card with several fields.
- **Do not confuse with** [table](../table/): a table compares values across columns,
  a grid places objects next to each other.
- **Do not confuse with** [gallery](../../media/gallery/): the gallery is one connected
  group of media with enlargement, the grid is a generic object view.
- **Do not confuse with** [carousel](../../media/carousel/): the carousel shows one after
  another, the grid at the same time.

## Best Practices

- Keep the cards evenly high; shorten titles that are too long instead of letting them wrap.
- The card itself is the main action; further actions only on hover or long press.
- Select through a checkbox in the corner, not through clicking the card — otherwise you
  slip while marking.
- Remember the view switch (grid ↔ list) and the sorting, do not reset them.
- On narrow screens two columns for images, one column for text cards.

## See also

- [data – overview](../index.md)
- [List View](../list-view/) — rows instead of cards
- [Gallery](../../media/gallery/) — media with enlargement
- [Base component](../../../primitives/basics/base.md)
