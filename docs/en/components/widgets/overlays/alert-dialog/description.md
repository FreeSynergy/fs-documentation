# Alert Dialog

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base`, `modal` |
| **Variants** | `bestaetigung`, `zerstoererisch` |
| **States** | `open`, `loading` |
| **Gestures** | `tap` |
| **Animations** | `fade-in`, `scale-in` |
| **Related** | `modal`, `alert`, `toast` |
| **Role** | `alertdialog` |
| **Status** | documented |

## Description

A confirmation dialog asks before an action is carried out. It is the combination of
[modal](../modal/) (own focus, blocks the content behind it) and
[alert](../../../primitives/feedback/alert/) (a message with a type and an action).

## Purpose

- Securing destructive actions (delete, leave, discard)
- Confirming actions with no way back (send, publish)
- Carrying out shortcuts that cannot be undone

## Variants

| Variant | Description |
|---------|-------------|
| **bestaetigung** | neutral question, confirm and cancel button |
| **zerstoererisch** | error colour, the confirm button only becomes possible after typing |

## Features

- Focus sits on the cancel action, `Esc` cancels
- The confirm button can require a typed confirmation (the name of the object)
- The loading state blocks both actions while the request runs
- No close icon of its own: the decision is made with one of the two actions

## Distinction

- **Do not confuse with** [modal](../modal/): a modal is an arbitrary dialog, the confirmation
  dialog has exactly two exits and does not block losing `Esc`.
- **Do not confuse with** [toast](../../../primitives/feedback/toast/): a toast reports after the
  fact and offers undo, the dialog asks beforehand.

## Best Practices

- Name the intention in the title ("Discard page?"), the effect in the text.
- Confirm button as a verb ("Discard"), never "OK".
- Do not ask for reversible actions — use a toast with undo instead.

## See also

- [Modal](../modal/)
- [Alert](../../../primitives/feedback/alert/)
- [Base component](../../../primitives/basics/base.md)
