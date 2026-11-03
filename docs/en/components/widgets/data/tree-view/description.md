# Tree View

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `Simple`, `With Icons`, `With Checkboxes`, `Draggable` |
| **States** | `checked`, `halbausgewählt`, `geöffnet` |
| **Gestures** | `tap`, `double-tap`, `drag`, `long-press` |
| **Animations** | `expand`, `collapse`, `reorder` |
| **Related** | `list-view`, `table`, `menu`, `table-of-contents`, `sidebar` |
| **Status** | documented |

## Description
A tree view is a hierarchical directory structure with collapse/expand.

## Purpose

- File directories
- Categories
- Org charts

## Variants

| Variant | Description |
|---------|-------------|
| **einfach** | names with a collapse triangle |
| **icon** | symbol by object type (folder, file, category) |
| **kästchen** | multi-select, parent node half-checked on a partial selection |
| **verschiebbar** | reattach nodes by dragging |

## Features

- Expand/collapse
- Checkbox selection
- Drag and drop
- Search

## Distinction

- **Do not confuse with** [menu](../../navigation/menu/): a menu invokes actions,
  this tree shows a data structure.
- **Do not confuse with** [table](../table/) in the variant `baum`: there the columns and
  comparison values belong to it, here only the hierarchy.
- **Do not confuse with** [list-view](../list-view/): the list is flat.
- **Do not confuse with** [table-of-contents](../table-of-contents/): the contents list jumps
  within one text.

## Best Practices

- Arrow to expand and collapse, click on the name to select — not both in the same place.
- The parent checkbox shows the mixed state, never simply ticked.
- Search opens the path to the hit automatically and marks the hit.
- Moving shows the target clearly and can be undone.
- More than five levels need indent lines, otherwise the structure is no longer recognisable.

## See also

- [data – overview](../index.md)
- [List View](../list-view/) — flat data
- [Menu](../../navigation/menu/) — actions instead of structure
- [Base component](../../../primitives/basics/base.md)
