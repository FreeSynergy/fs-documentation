# List View

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `Simple`, `With Icons`, `With Avatars`, `With Badges`, `With Actions` |
| **States** | `selected`, `leer` |
| **Gestures** | `tap`, `swipe`, `long-press`, `drag` |
| **Animations** | `stagger`, `collapse`, `reorder` |
| **Related** | `table`, `grid-view`, `tree-view`, `repeater`, `description-list` |
| **Status** | documented |

## Description
A list view is a simple list display of elements.

## Purpose

- Lists
- Overviews
- Categories

## Variants

| Variant | Description |
|---------|-------------|
| **einfach** | text per row, optional second line |
| **icon** | symbol on the left, e.g. file type |
| **avatar** | image on the left, e.g. people or chats |
| **badge** | status or counter on the right |
| **aktion** | controls on the right, visible on hover or always |

## Features

- Group headers and separators
- Multi-select with a counter
- Loading more while scrolling (virtualisation for long lists)
- Renaming, moving and reordering directly in the row

## Distinction

- **Do not confuse with** [table](../table/): a list lays out each row freely, a table
  compares values across columns.
- **Do not confuse with** [repeater](../repeater/): the repeater repeats a template for
  inputs, this list shows records.
- **Do not confuse with** [tree-view](../tree-view/): hierarchical data needs collapsing.
- **Do not confuse with** [description-list](../description-list/): that one describes **one** object
  in label-value pairs, this one shows many objects.

## Best Practices

- Rows at least 44 px high; clicking the row is the main action, further actions on the right.
- Label an empty list and offer to create an entry, never leave it just empty.
- Swipe actions on mobile must be undoable.
- Count the selection visibly and only reveal bulk actions (delete, move) once something
  is selected.

## See also

- [data – overview](../index.md)
- [Table](../table/) — comparing by columns
- [Grid View](../grid-view/) — cards instead of rows
- [Base component](../../../primitives/basics/base.md)
