# Wiggle - Appearance

## Base layout

The element stands in its place and tilts alternately to the left and to the
right through a small angle.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms        150 ms      300 ms      450 ms      │
│                                                  │
│   ╭───╮       ╭───╮        ╭───╮         ╭───╮   │
│  ╰───╯        ╰───╯         ╰───╯       ╰───╯    │
│  -2 °         0 °          +2 °         0 °      │
│                                                  │
│  pivot at the bottom middle, direction alternate │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Rotation** | `achse: rotate` - the standard, rocking through a few degrees |
| **Displaced** | `achse: x` - rocking sideways without tilting |
| **Group** | `phaseOffset` - all icons rock offset from one another |
| **Running out** | `decay: true` - calming down after release |
| **Whole mode** | `iterationCount: infinite` during editing |

## Duration

- Typical: 600 ms per cycle (range 400–800 ms)

## See also

- [Animations overview](../../index.md)
- [Shake](../shake/description.md)
- [Pulse](../../loop/pulse/description.md)
