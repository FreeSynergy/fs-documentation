# Rotate - Appearance

## Base layout

An element turns once around its pivot point to a fixed target angle and then
remains in the new orientation.

## Visual progress (chevron, angle: 180)

```
┌────────────────────────────────────────────┐
│   0 ms      ▾          collapsed (0°)      │
│ 150 ms      ◄          half a turn (90°)   │
│ 300 ms      ▴          expanded (180°)    │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Quarter** | a turn of 90° (icons, carousel arrows) |
| **Half** | a turn of 180° (chevron, sort direction) |
| **Full** | a full 360° turn as a one-time acknowledgement |
| **Corner pivot** | the pivot at a corner (`transformOrigin`), a flap-like effect |

## Duration

- Typical: 200–500 ms
- Default value: 300 ms

## See also

- [Animations overview](../../index.md)
- [Flip](../flip/description.md)
- [Spin](../../loop/spin/description.md)
