# Dashboard

| Field | Value |
|-------|-------|
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `vorlage`, `anordbar`, `bericht` |
| **States** | `bearbeiten`, `leer` |
| **Gestures** | `drag`, `tap`, `long-press` |
| **Animations** | `reorder`, `cascade`, `stagger` |
| **Related** | `card`, `chart`, `grid-view`, `split-view`, `scroll-area` |
| **State** | documented |

## Description
A dashboard is an overview page with widgets.

## Purpose

- Overview
- Analytics
- Project

## Variants

| Variant | Description |
|---------|-------------|
| **vorlage** | fixed arrangement, not changeable by the user |
| **anordbar** | move widgets, resize them, choose your own selection |
| **bericht** | display only without an edit mode, for shared views |

## Features

- Widgets
- Drag & Drop
- Resize
- Customize

## Distinction

- **Do not confuse with** [grid-view](../../../widgets/data/grid-view/): the grid shows similar
  entries, the dashboard different widgets in different sizes.
- **Do not confuse with** [card](../../../widgets/containers/card/): the card is one building
  block, the dashboard is the arrangement of several blocks including its settings.
- **Do not confuse with** [chart](../../../widgets/data/chart/): drawing happens in the chart,
  here things are only placed.

## Best Practices

- Start with a sensible default view, configuration is optional.
- Editing as its own mode (`bearbeiten`) — nothing shifts in reading mode.
- Grid with columns and rows, each widget brings a minimum and maximum size.
- Handle each widget's loading state individually, do not lock the whole page.
- Save the arrangement per person and offer a reset.

## See also

- [special – overview](../index.md)
- [Card](../../../widgets/containers/card/) — the building block
- [Chart](../../../widgets/data/chart/) — the chart
- [Base component](../../../primitives/basics/base.md)
