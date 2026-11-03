# Tags Input

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `text-input` |
| **Variants** | `frei`, `vorschlag`, `nur-lesbar` |
| **States** | `open`, `error` |
| **Gestures** | `tap`, `drag` |
| **Animations** | `pop-in`, `collapse` |
| **Related** | `mention-input`, `combobox`, `badge`, `select` |
| **Status** | documented |

## Description
A tags input is a list of tags/labels.

## Purpose

- Hashtags
- Categories
- Keywords

## Variants

| Variant | Description |
|---------|-------------|
| **frei** | a new tag is created from the input (comma or Enter) |
| **vorschlag** | only existing tags, chosen from a suggestion list |
| **nur-lesbar** | show tags without deleting or adding |

## Features

- Auto-complete
- Filter
- Remove

## Distinction

- **Do not confuse with** [badge](../../feedback/badge/): a badge shows a status, a tag
  is editable content with a delete button.
- **Do not confuse with** [mention-input](../mention-input/): tags are free terms,
  a mention points at a contact.
- **Do not confuse with** [select](../select/) with multiple choice: there only what the
  list offers exists; here new values arise from the input.

## Best Practices

- Prevent duplicates (case does not matter), highlight the existing tag instead.
- Backspace in an empty input removes the last tag – that is the fastest way.
- Set and show a maximum ("8 of 10"), otherwise the records become unusable.
- Reject forbidden characters and give the reason, do not remove them silently.

## See also

- [fields – overview](../index.md)
- [Badge](../../feedback/badge/) — display without editing
- [Mention Input](../mention-input/) — contacts instead of terms
- [Base component](../../basics/base.md)
