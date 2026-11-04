# Context Menu

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base`, `menu` |
| **Variants** | `Standard`, `Long Press`, `Overflow Menu` |
| **States** | `open`, `sub-open` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `pop-in`, `fade-out` |
| **Related** | `menu`, `toolbar`, `popover`, `select` |
| **State** | documented |

## Description
A context menu is opened by right-click or a long touch action and offers context-related options.

## Purpose

- Showing context-related actions
- Hiding less important functions
- Quick access to actions for selected elements

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | right-click menu (desktop) |
| **Long Press** | long touch action (mobile) |
| **Overflow Menu** | three-dots menu |

## Features

- Positioning at the mouse pointer (desktop)
- Scrolling (with many options)
- Keyboard navigation
- Accessibility

## Distinction

- **Do not confuse with** [menu](../../navigation/menu/): a menu hangs on a navigation bar and
  usually leads to views; the context menu invokes actions for the object at the pointer.
- **Do not confuse with** [toolbar](../../navigation/toolbar/): the toolbar shows actions
  permanently, the context menu only on demand (`long-press`, right-click).
- **Do not confuse with** [popover](../popover/): a popover carries content or a form, the
  context menu exclusively an action list.
- **Do not confuse with** [select](../../../primitives/fields/select/): here a field value is set,
  there an action is carried out.
- The overflow menu (three dots) is the variant for small surfaces, not a component of its own.

## Best Practices

- Only show relevant actions
- Consistent actions for identical elements
- Actions with icons
- Grey out disabled actions

## Content

- **Actions** - actions (edit, delete, share)
- **Dividers** - separators
- **Disabled Items** - disabled options
- **Icons** - icons for visual orientation

## See also

- [overlays – overview](../index.md)
- [Menu](../../navigation/menu/) — parent class
- [Popover](../popover/) — content instead of an action list
- [Base component](../../../primitives/basics/base.md)
