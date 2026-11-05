# Pop Out - Appearance

## Base layout

The element stays at its layout position until the end of the animation and
shrinks in the rendering only. Only once the animation is finished is the space
given up.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│   0 ms           50 ms          120 ms       200 ms  │
│                                                      │
│  [ Chip ]      [  Chip  ]      ▒▒ Chip ▒▒    (empty) │
│  s = 1.00      s = 1.04        s = 0.45     s = 0    │
│  α = 1         α = 1           α = 0.6      α = 0    │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | anticipate 1.04, then shrink to 0 (200 ms) |
| **No anticipation** | `anticipation: 1` – more matter-of-fact, less playful |
| **Fast** | 120–180 ms for badges and counters |
| **Space stays** | `removeAfterEnd: false` – the gap remains (e.g. a grid) |

## Duration

- Typical: 150–250 ms
- Default value: 200 ms

## See also

- [Animations overview](../../index.md)
- [Pop In](../../entrance/pop-in/description.md)
- [Scale Out](../scale-out/description.md)
- [Cascade](../../organization/cascade/description.md)
