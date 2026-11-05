# Fade In - Appearance

## Base layout

The element stays exactly at its layout position and becomes visible through
opacity only – no movement and no change of size.

## Visual progress

```
┌────────────────────────────────────────────┐
│   0 ms            125 ms          250 ms   │
│                                            │
│  (invisible)      ░░ Title ░░     [Title]  │
│    α = 0          α = 0.5         α = 1    │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | softly blended from 0 to 1 (250ms) |
| **Fast** | 100–150ms for hover, tooltip, micro feedback |
| **Soft** | 350–400ms with `ease-out` for overlays and modals |
| **Blur Fade** | fade combined with a decaying blur |

## Duration

- Typical: 150–400ms
- Default value: 250ms

## See also

- [Animations overview](../../index.md)
- [Fade Out](../../exit/fade-out/description.md)
- [Slide In](../slide-in/description.md)
