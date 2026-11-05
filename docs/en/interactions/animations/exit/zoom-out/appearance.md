# Zoom Out - Appearance

## Base layout

The element shrinks at its position from 100 % to close to 0 % and becomes
invisible meanwhile – an inversion of Zoom In.

## Visual progress

```
┌────────────────────────────────────────────┐
│   0 ms      [█████]      scale 1.0 · α 1.0 │
│ 100 ms      [███]        scale 0.6 · α 0.5 │
│ 200 ms      [▫]          scale 0.0 · α 0.0 │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | 1 → 0 with a synchronous fade (200ms) |
| **Minimal** | only 1 → 0.5 with a fade out, looks less dramatic |
| **To-origin** | visibly shrinks towards the `transformOrigin` (minimising into a dock/icon) |
| **Pure zoom** | only scaling, without a change of opacity |

## Duration

- Typical: 150–300ms
- Default value: 200ms

## See also

- [Animations overview](../../index.md)
- [Zoom In](../../entrance/zoom-in/description.md)
- [Fade Out](../fade-out/description.md)
