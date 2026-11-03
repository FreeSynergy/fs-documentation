# Radio Group

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `einzeln`, `toggle`, `karte` |
| **States** | `checked` |
| **Gestures** | `tap` |
| **Animations** | `press`, `highlight` |
| **Related** | `checkbox`, `select`, `button-group`, `field` |
| **Status** | documented |

## Description
A radio group is a group of radio buttons (single choice).

## Purpose

- Choices
- Options
- Settings

## Variants

| Variant | Description |
|---------|-------------|
| **einzeln** | classic circle with labels stacked below each other |
| **toggle** | options as adjoining buttons (segmented) |
| **karte** | options as cards with a title and a description |

## Features

- One selection
- Labels
- Icons

## Distinction

- **Do not confuse with** [checkbox](../checkbox/): here exactly one option is valid,
  there several are possible at the same time.
- **Do not confuse with** [select](../select/): radio options are all visible,
  the selection list hides them behind a click.
- **Do not confuse with** [button-group](../../actions/button-group/): a button group triggers
  actions, this group sets a form value.

## Best Practices

- Use radio up to about seven options, `select` above that.
- Set a preselection or explicitly provide "no preference" as its own option.
- Label the group as a whole (`fieldset`/`legend`) – the individual option needs no label.
- Offer dangerous options last and with a confirmation.

## See also

- [fields – overview](../index.md)
- [Checkbox](../checkbox/) — multiple choice
- [Select](../select/) — selection list
- [Base component](../../basics/base.md)
