# Search Field

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `text-input` |
| **Variants** | `simple`, `filter`, `auto-complete` |
| **States** | `open`, `loading`, `no-results` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `expand`, `highlight` |
| **Related** | `combobox`, `command`, `text-input`, `select` |
| **Status** | documented |

!!! info "Standardisation"
    The former component `search-input` was merged into `search-field` as a variant:
    `simple`, `autocomplete`, `filter`.

## Description
A search field is a search box with filter options.

## Purpose

- Search
- Filters
- Quick search

## Variants

| Variant | Description |
|---------|-------------|
| **simple** | simple search |
| **filter** | with filters |
| **auto-complete** | with suggestions |

## Features

- Filters
- Auto-complete
- Recent searches

## Distinction

- **Do not confuse with** [combobox](../combobox/): the search field changes a view or
  returns results, the combobox writes a value into a form field.
- **Do not confuse with** [command](../../../widgets/navigation/command/): the command palette starts
  actions and is a full-screen overlay, the search field filters the content of a view.
- **Do not confuse with** [text-input](../text-input/): without a search icon, without a
  clear button and without immediate triggering it is simply a text field.

## Best Practices

- Evaluate input in batches (200–300 ms), do not reload on every character.
- Make the result count visible ("12 matches"), label an empty result as `no-results`.
- Clearing with a clear button **and** `Esc`; filter settings are kept when you come back.
- On mobile, full width and the search keyboard; the search field stays at least 44 px high.
- Remember searched terms, but do not prefill the field – the user should know why
  the list is filtered.

## See also

- [fields – overview](../index.md)
- [Combobox](../combobox/) — choosing a value instead of filtering
- [Command](../../../widgets/navigation/command/) — starting commands
- [Base component](../../basics/base.md)
