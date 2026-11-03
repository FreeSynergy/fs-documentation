# Multi-Finger Tap - Appearance

## Basic Layout

Two or more fingers tap at the same time; all touch points become visible
(ripples), then the context menu appears at the touch position.

```
┌─────────────────────────────────────────┐
│        ●        ●     (2+ fingers)      │
│        ┆        ┆                       │
│     Ripple   Ripple                     │
│              ┌──────────────┐           │
│              │ Menu opens    │          │
│              └──────────────┘           │
└─────────────────────────────────────────┘
```

## Feedback Options

| Option | Description |
|--------|-------------|
| **Multi Ripple** | Wave at each touch point |
| **Context Menu** | Menu appears at the center of the fingers |
| **Zoom Step** | Map zooms one step (context: map app) |
| **None** | No feedback, callback only |

## Menu Position

| Rule | Description |
|------|-------------|
| Finger center | Default (center of all touched points) |
| Element center | If the hit element defines a menu anchor |

## Duration

- Ripple: 300–400ms
- Showing the menu: 150–250ms

## Difference from Multi-Finger Long Press

- Multi-Finger Tap: short, menu immediately
- Multi-Finger Long Press: holding, menu after a delay
