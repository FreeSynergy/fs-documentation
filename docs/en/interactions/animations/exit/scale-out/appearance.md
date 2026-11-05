# Scale Out - Appearance

## Base layout

The element keeps its middle point and contracts down to a single point.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms     60 ms   120 ms    180 ms               │
│                                                  │
│  [────────] [─────] [─]     ·                    │
│  100 %      70 %    35 %    0 %                  │
│                                                  │
│  shrink point reached, the slot is released      │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Middle** | shrink point in the element's middle (standard) |
| **To the trigger** | shrinks towards the cart, X or menu button |
| **Plus fade** | opacity falls along with it, prevents hard edges |
| **Width only** | `axis: x` - collapses sideways |
| **Space stays** | `removeAfter: false` - the slot stays reserved |

## Duration

- Typical: 180 ms (range 120–250 ms)

## See also

- [Animations overview](../../index.md)
- [Scale In](../../entrance/scale-in/description.md)
- [Collapse](../collapse/description.md)
