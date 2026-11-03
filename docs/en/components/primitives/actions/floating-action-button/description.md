# Floating Action Button (FAB)

| Field | Value |
|-------|-------|
| **Category** | `actions` |
| **Inherits from** | `base` |
| **Variants** | `standard FAB`, `mini FAB`, `extended FAB` |
| **States** | `expanded`, `scroll-hidden` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `ripple`, `pop-in`, `press` |
| **Related** | `button`, `button-group`, `tooltip` |
| **Status** | documented |

## Description
A floating action button (FAB) is a round main-action button, usually placed
bottom right.

## Purpose

- Show the primary action
- Fast access to the main function
- Visual focus

## Variants

| Variant | Description |
|---------|-------------|
| **standard FAB** | large button (56px) |
| **mini FAB** | small button (40px) |
| **extended FAB** | with text (e.g. "New +") |

## Features

- Hover effect (enlargement)
- Ripple effect (wave effect on click)
- Shadow (shadow for elevation)
- Badge (with count/status)

## Distinction

- **Do not confuse with** [button](../button/): a button sits in a layout context
  (form, toolbar, card footer); the FAB floats above the content and carries the *one*
  main action of the view.
- **Do not confuse with** [button-group](../button-group/): several actions of equal
  rank belong in a group or a menu, not in several FABs side by side.
- The FAB opens secondary actions as an action fan (`expanded`), not as a second FAB.
- On large desktop surfaces the FAB is optional; there the action belongs in the
  [toolbar](../../../widgets/navigation/toolbar/) or in the header.

## Best Practices

- Only one FAB per screen
- Show the most important action
- Clear icon (e.g. + for new)
- Hover text (tooltip)

## Positioning

| Position | Description |
|----------|-------------|
| **bottom right** | standard |
| **bottom left** | bottom left (RTL languages) |
| **center** | in the middle (rare) |

## See also

- [actions – overview](../index.md)
- [Base component](../../basics/base.md)
