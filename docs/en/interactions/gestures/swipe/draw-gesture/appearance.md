# Draw Gesture - Appearance

## Basic Layout

A transparent drawing layer lies over the surface; the stroke is drawn live,
and a confirmation follows the recognized shape.

```
┌─────────────────────────────────────────┐
│      ╲                                   │
│       ╲   (drawn "V")                    │
│        ╲ ╱                               │
│         ▼                                │
│   ┌──────────────┐                       │
│   │ ✓ Back        │  ← Confirmation      │
│   └──────────────┘                       │
└─────────────────────────────────────────┘
```

## Feedback Options

| Option | Description |
|--------|-------------|
| **Trail** | Stroke in the accent color follows the finger/pen |
| **Shape Snap** | The recognized shape is shown as a clean template |
| **Badge** | Short confirmation chip with the action name |
| **None** | Draw invisibly, the action happens directly |

## Stroke Widths

| Width | Usage |
|-------|-------|
| 2–3px | Gestures over content, subtle |
| 4–6px | Drawing apps, marker |
| Pressure-dependent | Pen with pressure support |

## Duration

- Recognition badge: visible for 600–1000ms
- Shape snapping: 150–250ms

## Difference from Scribble

- Draw Gesture: shape/letter = command, no text output
- Scribble: handwriting = text input, the field fills itself
