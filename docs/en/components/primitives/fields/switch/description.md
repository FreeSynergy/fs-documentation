# Switch

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `round`, `pill` |
| **States** | `checked`, `loading` |
| **Gestures** | `tap`, `drag` |
| **Animations** | `elastic`, `press` |
| **Related** | `checkbox`, `button`, `field` |
| **Status** | documented |

## Description
A switch is an on/off switch (toggle).

## Purpose

- Settings
- Features
- Status

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | rectangle |
| **round** | round |
| **pill** | pill shape |

## Features

- Checked/unchecked
- Animation
- Hover effect

## Distinction

- **Do not confuse with** [checkbox](../checkbox/): the switch takes effect **immediately**,
  the checkbox confirms a selection that only applies when saving (plan section 4, row 9 —
  both stay separate, the common ground is the boolean field).
- **Do not confuse with** [button](../../actions/button/): a button triggers an action once,
  the switch holds a state.
- A pure status display ("online") is not a switch but a [badge](../../feedback/badge/).

## Best Practices

- Only use it when the change may take effect without a confirmation.
- The label describes the fact ("Notifications"), not the action;
  the state is visible on the switch.
- If the change is slow, show the handle as `loading` and block repeated clicking.
- Have dangerous switches (synchronisation off, delete account) confirmed additionally.

## See also

- [fields – overview](../index.md)
- [Checkbox](../checkbox/) — selection with saving
- [Badge](../../feedback/badge/) — showing a state
- [Base component](../../basics/base.md)
