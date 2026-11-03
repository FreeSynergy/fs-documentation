# Alert

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `inline`, `banner` |
| **Types** | `info`, `success`, `warning`, `error` |
| **States** | `dismissing` |
| **Gestures** | `tap` |
| **Animations** | `fade-in`, `collapse` |
| **Related** | `toast`, `badge`, `progress` |
| **Role** | `alert` |
| **Status** | documented |

!!! info "Standardisation"
    The former component `banner` was merged into `alert` as a variant: `inline` (inside
    a content) and `banner` (above a view, fixed).

## Description
An alert is a status message (info, warning, error, success).

## Purpose

- Show status messages
- Show errors
- Show successes
- Show warnings

## Variants

| Variant | Description |
|---------|-------------|
| **inline** | message inside the content, where it occurs (standard) |
| **banner** | across a view, fixed (`sticky`) |

## Features

- Dismissible (can be closed)
- Icon
- Title
- Description
- Action button

## Distinction

- **Do not confuse with** [toast](../toast/): a toast appears briefly and disappears on
  its own, an `alert` stays until it is closed or resolved.
- **Do not confuse with** [badge](../badge/): a badge marks an element,
  a message needs text.

## Best Practices

- Clear text
- Consistent colours
- Action buttons
- Accessibility

## Types (`type`)

| Type | Colour | Description |
|------|--------|-------------|
| `info` | blue | information message |
| `success` | green | success message |
| `warning` | orange/yellow | warning message |
| `error` | red | error message |

## See also

- [feedback – overview](../index.md)
- [Base component](../../basics/base.md)
