# Bounce In - Appearance

## Base layout

The element arrives from outside or from a small scale, shoots past the final
position, and settles with a springy oscillation.

## Visual progress (scale bounce)

```
┌────────────────────────────────────────────┐
│   0 ms    [▫]          scale 0.5 (arrival) │
│ 220 ms    [██████]     scale 1.12 (past)   │
│ 360 ms    [████]       scale 0.94 (back)   │
│ 500 ms    [█████]      scale 1.00 (rest)   │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Pop** | starts at `startScale: 0` and pops up |
| **Drop** | falls in from above (`dropHeight` greater than 0) and springs on impact |
| **Slide-Bounce** | comes from the side and springs into the final position |
| **Soft** | only 1 spring-back with a small overshoot (6–8 %) |

## Duration

- Typical: 400–700 ms
- Default value: 500 ms

## See also

- [Animations overview](../../index.md)
- [Bounce Out](../../exit/bounce-out/description.md)
- [Slide In](../slide-in/description.md)
