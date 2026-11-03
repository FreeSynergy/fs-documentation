# Select

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `simple`, `multi-select`, `searchable`, `custom` |
| **States** | `open`, `no-results` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `expand`, `fade-in` |
| **Related** | `combobox`, `radio-group`, `tags-input`, `context-menu` |
| **Status** | documented |

## Description
A selection list: the field shows the chosen value, the options sit behind a click.

## Purpose

- Choosing
- Filters
- Categories

## Variants

| Variant | Description |
|---------|-------------|
| **simple** | simple list |
| **multi-select** | multiple choice |
| **searchable** | with search |
| **custom** | customised |

## Features

- Search
- Multi-select
- Customisable

## Distinction

- **Do not confuse with** [combobox](../combobox/): here you can only choose what the list
  offers; the combobox additionally allows free text (plan section 4, row 5).
- **Do not confuse with** [context-menu](../../../widgets/overlays/context-menu/): a context menu calls
  actions, this list sets a field value.
- **Do not confuse with** the native select: `native-select` is a variant that uses the
  system overlay of the operating system.
- Below seven options, [radio-group](../radio-group/) is usually the faster way to operate.

## Best Practices

- From about eight options use `select`, below that a radio group.
- Offer a group with `disabled` as the placeholder row ("please choose"), never a fake option "--".
- Structure long lists (`optgroup`) and make them searchable from 20 options on.
- Show multiple choice as chips and count them; offer "all" explicitly.
- Only preselect when that really is the expected answer.

## See also

- [fields – overview](../index.md)
- [Combobox](../combobox/) — list with free text
- [Radio Group](../radio-group/) — short option lists
- [Base component](../../basics/base.md)
