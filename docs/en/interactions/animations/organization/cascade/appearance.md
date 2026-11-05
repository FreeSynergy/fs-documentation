# Cascade - Appearance

## Base layout

The child elements each start their identical animation one after another, but
the order follows the layout rather than the order in the list. The distance
between two starts is not constant, it grows or shrinks.

## Visual progress

```
┌──────────────────────────────────────────────────────────┐
│t = 0 ms      50 ms      120 ms      210 ms      320 ms   │
│                                                          │
│[K1] ████████                                             │
│[K2]    ████████              distance:  50 ms            │
│[K3]       ████████                    +70 ms             │
│[K4]          ████████               +90 ms  (growing)    │
│[K5]             ████████                                 │
└──────────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **From the top left** | `richtung: top-left`, `achse: auto` (standard) |
| **From the outside inward** | `richtung: center-out` – the edges first |
| **Slowing down** | `stepGrowth` negative – a big initial impulse, a calm end |
| **Waves** | `wellenLaenge` 3–4 – whole groups start together |

## Duration

- Typical: 50 ms base distance, growing up to `stepLimit`
- Never more than about 800 ms in total, otherwise the surface feels sluggish

## See also

- [Animations overview](../../index.md)
- [Stagger](../stagger/description.md)
- [Expand](../../entrance/expand/description.md)
- [grid-view](../../../../components/widgets/data/grid-view/description.md)
