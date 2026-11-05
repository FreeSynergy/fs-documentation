# Breadcrumb

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `pfad`, `gestutzt`, `zurueck` |
| **States** | `aktiv`, `gestutzt` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `expand`, `fade-in` |
| **Related** | `menu`, `sidebar`, `tree-view`, `pagination`, `tabs` |
| **Status** | documented |

## Description
A breadcrumb is a path navigation (Home > Wiki > Page).

## Purpose

- Showing the path
- Navigation
- Orientation

## Variants

| Variant | Description |
| ---------- | -------------- |
| **pfad** | full sequence from the root to the current location |
| **gestutzt** | long paths show `…` in the middle with an expandable menu |
| **zurueck** | only the previous step as a button (narrow screens) |

The separator is not a variant but the attribute `separator` (`›`, `/`, `>`).

## Features

- Clickable
- Separator
- Active State

## Distinction

- **Do not confuse with** [sidebar](../sidebar/) or [menu](../menu/): those show what exists,
  the breadcrumb only the route already travelled to the current location.
- **Do not confuse with** [pagination](../pagination/): there one pages through a list,
  here one changes levels.
- **Do not confuse with** [tabs](../tabs/): tabs switch the content of one view,
  they show no hierarchy.

## Best Practices

- The current location is not a link — one is already there.
- Always keep the root visible; shorten long paths in the middle.
- Use the names exactly as in the tree, do not reword them.
- Label it as its own landmark (`aria-label="Breadcrumb"`), current entry with `aria-current`.
- Keep the separator consistent across the whole application.

## See also

- [navigation – overview](../index.md)
- [Tree View](../../data/tree-view/) — the hierarchy itself
- [Menu](../menu/) — expandable menu between the levels
- [Base component](../../../primitives/basics/base.md)
