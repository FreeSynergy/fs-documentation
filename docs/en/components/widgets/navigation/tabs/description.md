# Tabs

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `reiter`, `pille`, `karte` |
| **States** | `aktiv` |
| **Gestures** | `tap`, `swipe`, `long-press` |
| **Animations** | `slide-in`, `highlight` |
| **Related** | `bottom-navigation`, `accordion`, `breadcrumb`, `radio-group`, `carousel` |
| **Status** | documented |

## Description
Tabs are tabs for switching between views.

## Purpose

- Views
- Categories
- Options

## Variants

| Variant | Description |
| ---------- | -------------- |
| **reiter** | classic tabs with the active one underlined |
| **pille** | rounded filled area, fits in toolbars |
| **karte** | tabs sit on a card, the frame belongs to the content |

## Features

- Active Tab
- Closable
- Keyboard-Navigation

## Distinction

- **Do not confuse with** [accordion](../../containers/accordion/): tabs always show only one
  area, the accordion several stacked below each other.
- **Do not confuse with** [breadcrumb](../breadcrumb/): tabs switch content, the breadcrumb
  shows one level in a hierarchy.
- **Do not confuse with** [bottom-navigation](../bottom-navigation/): that switches the view,
  tabs only switch the content **inside** the view.
- A selection for a form is a [radio-group](../../../primitives/fields/radio-group/), not a tab bar.

## Best Practices

- Two to seven tabs; beyond that the selection belongs in a list or navigation.
- Keep the content when switching (do not reload), remember the scroll position per tab.
- Arrow keys to switch, `role="tab"` and `aria-selected` for screen readers.
- Close button only when tabs represent open documents (e.g. editors).
- Truncate titles that are too long and show the full name as a tooltip.

## See also

- [navigation – overview](../index.md)
- [Accordion](../../containers/accordion/) — areas stacked below each other
- [Bottom Navigation](../bottom-navigation/) — switching views
- [Base component](../../../primitives/basics/base.md)
