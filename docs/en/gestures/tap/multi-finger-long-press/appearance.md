# Multi-Finger Long Press - Appearance

## Basic Layout

Two or more fingers stay on the element; up to the threshold a progress ring
can appear, then the menu or selection mode.

```
┌─────────────────────────────────────────┐
│      ◉          ◉      (hold 500ms)     │
│      ┆ prog.    ┆ prog.                 │
│      ●──────────●                       │
│        Selection stretches              │
│              ┌──────────────┐           │
│              │ Menu / Multi  │          │
│              └──────────────┘           │
└─────────────────────────────────────────┘
```

## Feedback Options

| Option | Description |
|--------|-------------|
| **Progress Ring** | Ring fills up to the threshold |
| **Selection Handles** | Selection markers appear and follow the fingers |
| **Context Menu** | Menu at the center of the fingers |
| **Haptic Pop** | Vibration when crossing the threshold |

## Duration

- Hold until action: 500ms (like Long Press)
- Opening the menu: 150–250ms

## Difference from Long Press

- Long Press: one point, menu or marking
- Multi-Finger Long Press: several points, area/range possible afterwards
