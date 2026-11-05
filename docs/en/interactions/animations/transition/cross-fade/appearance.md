# Cross Fade - Appearance

## Base layout

Two elements lie exactly on top of each other; the opacity of one falls while
that of the other rises.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│A 100 %      A/B 70/30     A/B 25/75      B 100 %     │
│                                                      │
│██████       ███▒▒▒▒▒      ▒▒▒▒░░░░       ░░░░░░      │
│                                                      │
│A = old element, B = new; total opacity ≈ 100 %       │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Simultaneous** | both cross-fade at the same time (standard) |
| **Offset** | `overlap: 0`, first fade out, then fade in |
| **With zoom** | the new element scales along slightly (`skalaMit`) |
| **Short** | 150–200 ms for icons and status displays |
| **Hard** | an immediate swap (reduced motion) |

## Duration

- Typical: 250–500 ms

## See also

- [Animations overview](../../index.md)
- [Morph](../morph/description.md)
- [Parallax](../../movement/parallax/description.md)
