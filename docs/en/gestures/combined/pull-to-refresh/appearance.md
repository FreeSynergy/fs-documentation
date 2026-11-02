# Pull to Refresh - Appearance

## Basic Layout

The list hangs at the top edge; an indicator grows out of the edge.

```
┌─────────────────────────────────────────┐
│            ◌  (indicator, growing)      │
│  ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄          │
│  │ Entry 1                              │
│  │ Entry 2         ↑ List follows the   │
│  │ Entry 3           finger (rubber band)│
└─────────────────────────────────────────┘
```

## State Feedback

| State | Appearance |
|-------|------------|
| Pulling | Indicator semi-transparent, scales with distance |
| Armed | Indicator fully visible, arrow turns, haptic tick |
| Refreshing | Indicator rotates below the list |
| Done | Indicator shrinks, the list springs back |

## Indicator Variants

| Variant | Description |
|---------|-------------|
| **Spinner** | Classic circle point (Material) |
| **Arrow** | Arrow → spinner (iOS-like) |
| **Custom** | App logo/animation |

## Duration

- Up to the threshold: follows the finger
- Showing/hiding: 200–300ms
- Loading time: unlimited until the response

## Difference from Drag

- Pull to Refresh: movement at a fixed edge, triggers loading, springs back
- Drag: moving an element, the goal is a new position
