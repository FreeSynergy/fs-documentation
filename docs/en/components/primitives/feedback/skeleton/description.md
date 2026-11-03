# Skeleton

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` |
| **States** | `loading` is the only state |
| **Gestures** | none – not operable |
| **Animations** | `pulse` |
| **Related** | `spinner`, `progress`, `list-view`, `base` |
| **Status** | documented |

## Description

A skeleton is a placeholder in the later layout shape. It shows where and how
large content will appear while it is being loaded.

## Purpose

- Structure views immediately, before the data arrives
- Suggest the shape of lists, tables and cards while loading
- Shorten the perceived loading time (the layout stands, content follows)

## Variants

| Variant | Description |
|---------|-------------|
| **text** | one or several text bars |
| **rect** | rectangle (image, card, chart) |
| **circle** | circle (avatar, status dot) |
| **card** | combined placeholder in a card layout |
| **list-item** | row with icon, text and meta |
| **table-row** | table row with cell widths |
| **avatar** | circle plus two text bars |

## Features

- Two kinds of animation: `shimmer` (a travelling sheen) and `pulse` (breathing)
- Combinable into whole scaffolds (one skeleton layout per view)
- Width and height freely settable so the later layout does not jump

## Distinction

- **Do not confuse with** [spinner](../spinner/): a spinner is a signal,
  a skeleton is a placeholder with a shape.

- **Do not confuse with** [empty-state](../empty-state/): empty-state shows "no data",
  skeleton shows "data still coming".

- **Do not confuse with** [progress](../progress/): progress accompanies a
  started action, skeleton only the waiting for a display.

## Best Practices

- Skeleton shapes match the real layout – otherwise the view jumps.
- At most two or three repetitions of a row, otherwise the list is
  mistaken for content.

- Replace without a jump after loading (keep the height).
- With reduced motion, set the animation to `none`.

## See also

- [Spinner](../spinner/)
- [Progress](../progress/)
- [List View](../../../widgets/data/list-view/)
- [Base component](../../basics/base.md)
