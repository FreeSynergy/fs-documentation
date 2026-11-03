# Repeater

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `liste`, `raster`, `eingabe` |
| **States** | `leer`, `gefiltert`, `wartend` |
| **Gestures** | `tap`, `swipe`, `long-press` |
| **Animations** | `fade-in`, `stagger`, `progress` |
| **Related** | `list-view`, `grid-view`, `table`, `pagination`, `search-field` |
| **Status** | documented |

## Description
A repeater is a repeating layout for lists.

## Purpose

- Products
- Contacts
- Articles
- Lists

## Variants

| Variant | Description |
|---------|-------------|
| **liste** | one entry per row (standard) |
| **raster** | entries as cards next to each other |
| **eingabe** | repeated form rows, e.g. line items with add/delete |

## Features

- Filter
- Sort
- Search
- Pagination

## Distinction

- **Do not confuse with** [list-view](../list-view/): the list view shows entries,
  the repeater is the whole assembly of search, filter, sorting, pages and template.
- **Do not confuse with** [table](../table/): the table brings its own column structure,
  the repeater repeats a freely defined template.
- The variant `eingabe` does not replace individual fields — it repeats a group of fields.

## Best Practices

- Keep the order of the controls uniform: search, filter, sorting, result count.
- When a filter applies it must be visible and removable with one button (`gefiltert`).
- Either page numbers or scrolling that loads more, both together confuse.
- Label empty data and an empty search result differently.
- Define the template only once; new entries inherit it instead of copying it.

## See also

- [data – overview](../index.md)
- [List View](../list-view/) — pure view without controls
- [Pagination](../../navigation/pagination/) — page navigation
- [Base component](../../../primitives/basics/base.md)
