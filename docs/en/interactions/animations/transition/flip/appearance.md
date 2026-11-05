# Flip - Appearance

## Base layout

A card-like surface with a front and a back side turns around its middle axis; at
90° the content is swapped.

## Visual progress (axis: y)

```
┌────────────────────────────────────────────┐
│   0 ms    ┌───────┐    front side "A"      │
│  110 ms   ┌┘     └┐    turning (45°)       │
│  225 ms   ▌       ▐    90°: side swaps     │
│  450 ms   ┌───────┘    back side "B"       │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Horizontal** | turn around the vertical axis (`axis: y`), the standard |
| **Vertical** | turn around the horizontal axis (`axis: x`), tilting up/down |
| **With 3D perspective** | `perspective` greater than 0, looks spatial |
| **Flat** | `perspective: 0`, a pure 2D turn without a depth effect |

## Duration

- Typical: 300–600 ms
- Default value: 450 ms

## See also

- [Animations overview](../../index.md)
- [Rotate](../rotate/description.md)
- [Fade In](../../entrance/fade-in/description.md) (cross-fade the content change as an alternative)
