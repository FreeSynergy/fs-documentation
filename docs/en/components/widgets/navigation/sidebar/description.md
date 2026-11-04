# Sidebar

| Field | Value |
|-------|-------|
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `angeheftet`, `ikonenleiste`, `einklappbar` |
| **States** | `geöffnet`, `geschlossen` |
| **Gestures** | `tap`, `drag`, `long-press`, `swipe` |
| **Animations** | `expand`, `collapse`, `slide-in` |
| **Related** | `menu`, `bottom-navigation`, `drawer`, `toolbar`, `tree-view` |
| **State** | documented |

## Description
The sidebar is a vertical navigation column, normally positioned on the left or right edge
of the application. It gives quick access to main functions and is often used in desktop
applications and messengers.

## Purpose

- Quick access to main functions
- Organising menu items into groups
- Showing status information (e.g. user profile, message counter)

## Variants

| Variant | Description |
|---------|-------------|
| **angeheftet** | permanently at the edge, content area next to it |
| **ikonenleiste** | narrow bar with icons, names only on hover or selection |
| **einklappbar** | wide with names, reduced to the icon bar by a button |

On small screens the sidebar becomes a [drawer](../../overlays/drawer/), it is then an
overlay and no longer pushes the content aside.

## Features

- Groups with headings and separators
- Counters or status on the items ([badge](../../../primitives/feedback/badge/))
- Profile header at the top, settings at the bottom
- Searchable with many items, keyboard navigation with arrow keys

## Distinction

- **Do not confuse with** [drawer](../../overlays/drawer/): the drawer covers the content,
  the sidebar permanently takes space away from it.
- **Do not confuse with** [bottom-navigation](../bottom-navigation/): one sits at the edge,
  the other at the bottom edge of small screens.
- **Do not confuse with** [tree-view](../../data/tree-view/): here are destinations and actions,
  there arbitrary data.

## Best Practices

- Important things at the top, groups with a heading, at most two levels.
- The active item is recognisable permanently (area plus text, not only colour).
- Collapsing remembers the state; in the icon bar every item needs a tooltip.
- On small screens open it as a drawer and close it again after the selection.
- Only resize the width by dragging if the minimum width stays readable (at least 200 px).

## Typical positions

- Left (standard for LTR languages)
- Right (for RTL languages or specific layouts)
- Top (as a horizontal bar – then usually called a "topbar")

## See also

- [navigation – overview](../index.md)
- [Drawer](../../overlays/drawer/) — sidebar as an overlay
- [Menu](../menu/) — menu items in the bar
- [Base component](../../../primitives/basics/base.md)
