# Fade Out - Appearance

## Base layout

The element stays at its layout position and becomes invisible through opacity
only – no layout shift takes place.

## Visual progress

```
┌────────────────────────────────────────────┐
│   0 ms            100 ms          200 ms   │
│                                            │
│   [Title]         ░░ Title ░░  (invisible) │
│   α = 1           α = 0.5         α = 0    │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | fade out softly, the element stays in the DOM |
| **Fast** | 100–150ms for micro feedback and small elements |
| **With remove** | remove from the DOM after fading out (`removeOnEnd`) |
| **Blur Fade** | with increasing blur while fading out |

## Duration

- Typical: 150–300ms
- Default value: 200ms

## See also

- [Animations overview](../../index.md)
- [Fade In](../../entrance/fade-in/description.md)
- [Zoom Out](../zoom-out/description.md)
