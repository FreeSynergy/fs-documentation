# Empty State

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `leer`, `kein-treffer`, `fehler` |
| **States** | `loading` |
| **Gestures** | `tap` |
| **Animations** | `fade-in` |
| **Related** | `skeleton`, `spinner`, `progress` |
| **Role** | `status` |
| **Status** | documented |

## Description

An empty state explains why a surface has no content and shows the way to the
first content. It replaces the empty list with a short statement and an action.

## Purpose

- First use of an area, still without data
- A search or filter without a hit
- Area temporarily unavailable (error, missing permission)

## Variants

| Variant | Description |
|---------|-------------|
| **leer** | no data yet, an action to create something |
| **kein-treffer** | the filter returns nothing, an action to reset it |
| **fehler** | content could not be loaded, an action to retry |

## Features

- Icon or illustration, one sentence of explanation, one main action
- A secondary reference for help or a shortcut
- Centred in the available height, minimum height 200 px

## Distinction

- **Do not confuse with** [skeleton](../skeleton/): a skeleton shows that content is
  on its way; the empty state shows that there is none.
- **Do not confuse with** [alert](../alert/): a message disturbs an existing
  view, the empty state is the view.

## Best Practices

- Exactly one main action, in the wording of the area ("Create your first task").
- Do not explain what the area can do in general – only why it is empty.
- With filters, show the filter value and offer to reset it.

## See also

- [Skeleton](../skeleton/)
- [Alert](../alert/)
- [Base component](../../basics/base.md)
