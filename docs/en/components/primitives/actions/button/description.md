# Button

| Field | Value |
|-------|-------|
| **Category** | `actions` |
| **Inherits from** | `base` |
| **Variants** | `primary`, `secondary`, `outline`, `ghost`, `danger`, `link` |
| **States** | `loading` (with double-click lock) |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `press`, `lift` |
| **Related** | `link`, `switch`, `floating-action-button`, `button-group`, `spinner`, `base` |
| **Status** | documented |

## Description

A button triggers a single action. It is the most frequently used component of
all and the starting point of almost every interaction in FreeSynergy.

## Purpose

- Confirming or carrying out actions (save, send, create)
- Central action in dialogs, forms and toolbars
- Actions that belong together grouped via `button-group`

## Variants

| Variant | Description |
|---------|-------------|
| **primary** | main action, only once per view |
| **secondary** | secondary action |
| **outline** | border without fill, weak emphasis |
| **ghost** | no border, only appears on hover |
| **danger** | destructive action (delete, leave) |
| **link** | looks like a link, behaves like a button |

## Features

- Icon on the left or right, also **icon-only** (then with tooltip and `aria-label`)
- Loading state: replaces the label with a spinner and blocks repeated triggering
- Full width (`fullWidth`) for mobile views
- Split button with dropdown arrow as a variant of `button-group`

## Distinction

- **Do not confuse with** [link](../../basics/link/): a link changes the address
  (`href`), a button performs an action without changing the address.

- **Do not confuse with** [switch](../../fields/switch/): a switch takes effect
  immediately, a button triggers an action.

- **Do not confuse with** [floating-action-button](../floating-action-button/):
  floating main action in mobile views.

## Best Practices

- Exactly **one** `primary` per view; actions in dialogs aligned right.
- Label as a verb ("Save" rather than "OK").
- `danger` only with a confirmation, e.g. via [alert-dialog](../../../widgets/overlays/alert-dialog/).
- Icon-only buttons always need `aria-label` and a tooltip.

## See also

- [Button Group](../button-group/)
- [Link](../../basics/link/)
- [Spinner](../../feedback/spinner/) (loading state)
- [Base component](../../basics/base.md)
