# Flick - Appearance

## Basic Layout

The finger swipes quickly and lifts off; the content rolls on with decreasing
velocity.

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────┐          │
│  │ ░░░ Content               │  ←───┐   │
│  │ ░░░░░                     │      │ Finger lifts off
│  │ ░░░░░░░        ·····►     │   (Velocity)
│  └───────────────────────────┘  Run-out, decelerating
└─────────────────────────────────────────┘
```

## Phases

| Phase | Description |
|-------|-------------|
| **Accelerate** | Content follows the finger, velocity rises |
| **Release** | Velocity is measured, over-scroll possible |
| **Run-out** | Content decelerates, possibly snapping to an element |

## Feedback Options

| Option | Description |
|--------|-------------|
| **Momentum** | Rolling out with decreasing velocity |
| **Snap** | Snap to the next list element |
| **Rubber Band** | Springing past the boundary (see rubber-band animation) |
| **Haptic** | Vibration when snapping / at the boundary |

## Velocity

| Intensity | Velocity | Usage |
|-----------|----------|-------|
| Light | 1000–2000 px/s | Paging on by a few entries |
| Medium | 2000–4000 px/s | Typical throw-scrolling |
| Strong | > 4000 px/s | "Jumping" quickly downwards |

## Difference from Swipe

- Swipe: distance decides, the movement ends with the finger
- Flick: velocity decides, the movement lives on
