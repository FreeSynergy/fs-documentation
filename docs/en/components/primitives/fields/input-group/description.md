# Input Group

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `praefix`, `suffix`, `aktion`, `auswahl` |
| **States** | `focus-within`, `filled` |
| **Gestures** | `tap`, `type` |
| **Animations** | `highlight`, `expand` |
| **Related** | `text-input`, `field`, `button`, `button-group`, `search-field` |
| **Role** | `group` |
| **Status** | documented |

## Description

An input group joins an input field and the parts that immediately belong to it
into one connected surface: a prefix character, a unit, a dropdown for the
country code, or a button directly on the field. It stays one value; the
neighbouring parts explain or limit it.

## Purpose

- Showing units and signs (`€`, `kg`, `https://`)
- Placing a fitting action directly on the field (search, copy, sign in)
- A short preset on the field (country code, protocol)
- Securing passwords with a toggle icon

## Variants

| Variant | Description |
|---------|-------------|
| **praefix** | fixed prefix on the left inside the field (icon, unit, sign) |
| **suffix** | fixed suffix on the right inside the field (unit, status icon) |
| **aktion** | button on the field, usually on the right |
| **auswahl** | small dropdown as the prefix, e.g. the country code |

## Features

- Shared height, edge and radius as the field itself
- Focus still sits with the field; the group marks it
- Prefix and suffix are display only, the action is a focusable button
- Combinable on the left and the right, at most one part per side

## Distinction

- **Do not confuse with** [field](../field/): the wrapper belongs *around* the field
  (label, help text, error message), the group sits *inside* the field next to the
  value. Both are combined, not substituted for each other.
- **Do not confuse with** [button-group](../../actions/button-group/): there all
  parts are actions of equal rank; here one part carries the value, the others explain it.
- **Do not confuse with** [search-field](../search-field/): the search field brings
  search logic with it (suggestions, clearing, keyboard). The group is only the build
  shape of icon, field and button.
- **Do not confuse with** [tags-input](../tags-input/): here one value with decoration
  is created, there a set of values.

## Best Practices

- Only one tab order: the group and the prefix get no focus of their own.
- Decisive information belongs in the [label](../../basics/label/), never in a
  prefix – prefixes are additional text for screen readers.
- The button in the group acts on the field value, not on the page.
- With more than two additional parts, rather use two fields in one row.

## See also

- [fields – overview](../index.md)
- [Text Input](../text-input/) — the field inside the group
- [Field](../field/) — label and error message outside
- [Base component](../../basics/base.md)
