# Toolbar

| Field | Value |
|-------|-------|
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `kontext`, `ribbon` |
| **States** | `aktiv`, `geklebt` |
| **Gestures** | `tap`, `long-press`, `drag` |
| **Animations** | `expand`, `collapse`, `fade-in` |
| **Related** | `button`, `button-group`, `menu`, `context-menu`, `rich-text-editor` |
| **Status** | documented |

!!! info "Standardisation"
    The former components `context-toolbar` and `ribbon` became variants of `toolbar`:
    `standard`, `kontext`, `ribbon`.

## Description
A toolbar is a row of buttons/icons for frequent actions. It is often placed directly below
the title bar.

## Purpose

- Quick access to frequent functions
- Consolidating actions in one bar
- Visual organisation of tools

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | fixed bar with the frequent actions |
| **kontext** | shows different actions depending on what is selected |
| **ribbon** | multi-row bar with named groups (desktop programs) |

## Features

- Customizable
- Keyboard shortcuts
- Tooltip (on hover)
- Disabled states

## Distinction

- **Do not confuse with** [menu](../menu/): the menu hides commands behind a label, the bar
  shows them immediately as an icon.
- **Do not confuse with** [context-menu](../../overlays/context-menu/): the context menu is an
  overlay at the click point, the variant `kontext` stays in the layout.
- **Do not confuse with** [bottom-navigation](../bottom-navigation/): a bar contains actions,
  a navigation contains destinations.
- Button pairs that belong together are a [button-group](../../../primitives/actions/button-group/);
  the bar itself is the whole row.

## Best Practices

- Only frequently used functions
- Consistent icon size
- Hover effect
- Show keyboard shortcuts

- Only frequent actions in the bar, the rest goes into the menu.
- Group and separate groups; keep the order identical across all views.
- Every icon needs a tooltip with its shortcut, otherwise users have to guess.
- Disabled buttons stay visible (no jump in the bar), but have no effect.
- On narrow screens move into a `+` menu, do not squeeze the buttons together.

## Action groups

| Type | Examples |
|------|----------|
| **File** | New, Save, Print |
| **Formatting** | Bold, Italic, Underline |
| **Navigation** | Back, Forward, Refresh |
| **Search and filter** | Search, Filter, display fields |
| **Dangerous** | Delete, Discard — only with confirmation |

## Positions

| Position | Description |
|----------|-------------|
| **Top** | below the title bar (standard) |
| **Sidebar** | in the sidebar |
| **Floating** | free-floating (e.g. in chat) |
| **Bottom** | at the bottom of the screen (mobile) |

## See also

- [navigation – overview](../index.md)
- [Button Group](../../../primitives/actions/button-group/) — buttons that belong together
- [Menu](../menu/) — commands in the menu
- [Base component](../../../primitives/basics/base.md)
