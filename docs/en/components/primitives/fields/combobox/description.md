# Combobox

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `select` |
| **Variants** | `einzeln`, `freitext`, `mehrfach` |
| **States** | `open`, `loading`, `no-results` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `expand`, `highlight` |
| **Related** | `select`, `search-field`, `tags-input`, `command` |
| **Status** | documented |

## Description
A combobox is a text field plus a dropdown.

## Purpose

- Address lookup
- Categories
- Search box

## Variants

| Variant | Description |
|---------|-------------|
| **einzeln** | choice from suggestions, own text only as a search filter |
| **freitext** | any value allowed, suggestions are offers |
| **mehrfach** | several values as tags, the suggestion list stays open |

## Features

- Typing
- Selection
- Auto-complete

## Distinction

- **Do not confuse with** [select](../select/): `select` offers only existing
  options and closes after the choice. The combobox adds free text and suggestions
  for an entered text – that is the decisive difference (plan section 4, row 5).
- **Do not confuse with** [search-field](../search-field/): a search field triggers a
  search and changes the view, the combobox writes a value into the form.
- **Do not confuse with** [command](../../../widgets/navigation/command/): the command palette is a
  full-screen overlay for actions, not field input.

## Best Practices

- Only load suggestions from two characters on, and with a short delay; show waiting as
  a `loading` state, never as an empty list.
- Only offer free text when the domain allows free values; otherwise use `select`.
- Label an empty suggestion list as `no-results` with a hint ("no matches for …").
- Keep it fully keyboard-operable: arrow keys, Enter chooses, Esc closes, focus stays in the field.

## See also

- [fields – overview](../index.md)
- [Select](../select/) — the pure selection list
- [Search Field](../search-field/) — search instead of choosing a value
- [Base component](../../basics/base.md)
