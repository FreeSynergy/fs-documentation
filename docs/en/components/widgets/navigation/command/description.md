# Command

| Field | Value |
|-------|-------|
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `palette`, `inline` |
| **States** | `open`, `empty` |
| **Gestures** | `tap`, `type` |
| **Animations** | `fade-in`, `expand` |
| **Related** | `search-field`, `menu`, `modal` |
| **Role** | `dialog` |
| **Status** | documented |

## Description

The command palette is an overlay with an input field and a list of matches. It starts
programs, switches views and carries out actions — reached via a keyboard shortcut instead
of searching through menus.

## Purpose

- Quick access to programs and views in the desktop client
- Carrying out actions without leaving the context
- Short help: which commands are available in this view

## Variants

| Variant | Description |
|---------|-------------|
| **palette** | centred overlay, via `Ctrl`/`Cmd` + `K` |
| **inline** | palette embedded in a sidebar or toolbar |

## Features

- Search terms are started out of context ("new task" finds the target)
- Matches grouped by program, view and action
- Recent and frequent commands sit at the top, even without input
- Keyboard navigation: `arrow up/down`, `Enter` runs, `Esc` closes

## Distinction

- **Do not confuse with** [search-field](../../../primitives/fields/search-field/): search finds content,
  the palette carries out actions.
- **Do not confuse with** [menu](../menu/): menus show the whole offering, the palette only
  matching hits.

## Best Practices

- Name commands verb then object ("Create task", not "New").
- Show one shortcut per command if one exists.
- Cut the results off after 50 hits and ask the user to be more precise.

## See also

- [Search Field](../../../primitives/fields/search-field/)
- [Menu](../menu/)
- [Base component](../../../primitives/basics/base.md)
