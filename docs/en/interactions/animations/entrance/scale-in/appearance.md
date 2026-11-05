# Scale In - Appearance

## Base layout

The element stays anchored at its position and fills its layout slot outward
from a single point.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms     70 ms   140 ms    200 ms               │
│                                                  │
│  ·        [───]   [──────]  [────────]           │
│  0 %      35 %    70 %      100 %                │
│                                                  │
│  Fixed middle point, width and height grow       │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Middle** | growth point in the element's middle (standard) |
| **Trigger** | growth point at the button; the menu seems to grow out of it |
| **Width only** | `axis: x` - the height stays constant meanwhile |
| **Height only** | `axis: y` - the width stays constant meanwhile |
| **Plus fade** | opacity rises in parallel, looks softer |

## Duration

- Typical: 200 ms (range 150–300 ms)

## See also

- [Animations overview](../../index.md)
- [Scale Out](../../exit/scale-out/description.md)
- [Expand](../expand/description.md)
