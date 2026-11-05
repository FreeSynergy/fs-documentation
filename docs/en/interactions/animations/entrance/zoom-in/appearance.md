# Zoom In - Appearance

## Base layout

The element appears at its position while scaling from a size below 100 % to
100 % – usually with opacity rising in sync.

## Visual progress

```
┌────────────────────────────────────────────┐
│   0 ms      [▫]          scale 0.5 · α 0.0 │
│ 125 ms      [███]        scale 0.8 · α 0.6 │
│ 250 ms      [█████]      scale 1.0 · α 1.0 │
└────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | starts at 0.5, with fade (250ms) |
| **Subtle** | starts at 0.8, barely visible movement |
| **From a corner** | `transformOrigin: top left`, opens out of the corner |
| **Pure zoom** | only scaling, without a change of opacity (`opacitySync: false`) |

## Duration

- Typical: 200–350ms
- Default value: 250ms

## See also

- [Animations overview](../../index.md)
- [Zoom Out](../../exit/zoom-out/description.md)
- [Scale In](../scale-in/description.md)
- [Fade In](../fade-in/description.md)
