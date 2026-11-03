# Table

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `Simple`, `Data`, `Tree`, `Inline Edit` |
| **States** | `selected`, `bearbeitet` |
| **Gestures** | `tap`, `drag`, `long-press`, `swipe` |
| **Animations** | `stagger`, `collapse`, `reorder` |
| **Related** | `list-view`, `repeater`, `tree-view`, `description-list`, `pagination` |
| **Status** | documented |

## Description
A table is a tabular display with rows and columns.

## Purpose

- Showing data
- Lists
- Overviews

## Variants

| Variant | Description |
|---------|-------------|
| **einfach** | static rows and columns without controls |
| **daten** | sorting, filtering, selection and page numbers |
| **baum** | rows with collapsing for nested data |
| **inline-bearbeitung** | editing cells directly in the table |

## Features

- Sorting and filtering per column
- Row selection with bulk actions
- Column width by dragging, first column can be pinned
- The header row stays put while scrolling

## Distinction

- **Do not confuse with** [list-view](../list-view/): a table compares values in columns,
  a list lays out each row freely.
- **Do not confuse with** [description-list](../description-list/): that one describes one object,
  the table many.
- **Do not confuse with** [tree-view](../tree-view/): nested data with a navigational
  character belongs there, nested records belong in the variant `baum`.
- Header controls do not replace a filter assembly of their own ([repeater](../repeater/)).

## Best Practices

- Numbers on the right, texts on the left, dates in one format; header bold and pinned.
- Only mark sortable columns with a sort symbol, remember the sorting across navigation.
- Select through checkboxes in the first column; bulk actions only appear once something
  is selected.
- Avoid horizontal scrolling: on narrow screens make the columns selectable or switch
  to cards.
- Give inline editing clear borders and `Esc` as cancel, otherwise the table looks empty.

## See also

- [data – overview](../index.md)
- [List View](../list-view/) — free-form rows
- [Tree View](../tree-view/) — hierarchy instead of a flat list
- [Base component](../../../primitives/basics/base.md)
