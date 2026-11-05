# Unfold - Appearance

## Base layout

The top edge lies flat on the plane, the rest of the content swings forward out
of that edge.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms           225 ms          450 ms           │
│  ┌──────────┐   ╭──────────╮    ┌──────────┐     │
│  ▁▁▁▁▁▁▁▁▁▁     ╲          ╱    ░░░░░░░░░░       │
│  edge 90°       ╲        ╱      ░░░░░░░░░░       │
│                 ╲______╱        └──────────┘     │
│  height ~0      half open       flat 0°          │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **From above** | `foldOrigin: top` - the standard (sheet opening downward) |
| **From the side** | `foldOrigin: left` - the card opens to the right |
| **Several folds** | `segments: 3` - wavelike unfolding |
| **Flat** | very large `perspective` - looks almost like Expand |
| **Deep** | small `perspective` - strong 3D impression |

## Duration

- Typical: 450 ms (range 300–600 ms)

## See also

- [Animations overview](../../index.md)
- [Expand](../expand/description.md)
- [Collapse](../../exit/collapse/description.md)
