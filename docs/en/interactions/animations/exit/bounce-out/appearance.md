# Bounce Out - Appearance

## Base layout

The element briefly compresses at its position, then shoots past it and springs
out of the surface.

## Visual progress (exit jump upwards)

```
┌────────────────────────────────────────────┐
│   0 ms    [█████]      scale 1.00 (rest)   │
│ 120 ms    [███]        scale 0.88 (pull)   │
│ 260 ms    [██] ↑       scale 0.50 (launch) │
│ 400 ms    (empty)      removed             │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Squash-Away** | first compress, then pull away flat (standard) |
| **Jump-Away** | a short jump upwards, then disappear |
| **Side-Flick** | a quick flick away to the side |
| **Shrink-Bounce** | disappear while shrinking with a small overshoot |

## Duration

- Typical: 300–500 ms
- Default value: 400 ms

## See also

- [Animations overview](../../index.md)
- [Bounce In](../../entrance/bounce-in/description.md)
- [Zoom Out](../zoom-out/description.md)
