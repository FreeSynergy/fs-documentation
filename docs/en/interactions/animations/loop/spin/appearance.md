# Spin - Appearance

## Base layout

A circular element (a ring, an arc or an icon) keeps turning evenly and without
an end point until the task is completed.

## Visual progress (marker rotates clockwise)

```
┌────────────────────────────────────────────┐
│   0 ms      ·█·        marker top (0°)     │
│             ···                             │
│             ···                             │
│                                             │
│ 250 ms      ···        marker right (90°)   │
│             ··█                             │
│             ···                             │
│                                             │
│ 500 ms      ···        marker bottom (180°) │
│             ···                             │
│             ·█·                             │
└────────────────────────────────────────────┘
```

`█` = the rotating arc or marker of the circular spinner; the movement continues
without an end point.

## Variants

| Variant | Description |
|---------|-------------|
| **Circular spinner** | the classic ring with a gap (standard) |
| **Half circle** | an arc of 180° (`arcSweep: 180`) |
| **Accelerating** | the arc grows and shrinks per beat (Material style) |
| **Backwards** | `spinDirection: ccw` (e.g. cancelling, undo) |

## Duration

- Per revolution: 800–1500 ms, default value 1000 ms
- Runs endlessly until the task ends or `playState: paused` is set

## See also

- [Animations overview](../../index.md)
- [Rotate](../../transition/rotate/description.md)
- [Fade In](../../entrance/fade-in/description.md) (fade the spinner in and out softly)
