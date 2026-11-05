# Glow - Appearance

## Base layout

The element stands still; around its contour lies a soft, coloured shine that
slowly swells and shrinks.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│frame 1        frame 2         frame 3        frame 4 │
│                                                      │
│[■]            ~[■]~          ~~[■]~~        ~[■]~    │
│off            faint          bright         faint    │
│                                                      │
│intensity: 0 → 50 → 100 → 50 % (endless loop)         │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Constant** | the shine stands at a fixed intensity (selection) |
| **Pulsing** | the shine breathes in the loop (live status, presence) |
| **Contour** | the shine follows the element shape exactly (SVG/border radius) |
| **Rectangular** | the shine as a blurred rectangle, cheaper to render |
| **Entry/exit** | the shine builds up and down softly when activated |

## Duration

- Typical: 1000–2000 ms per cycle, entry/exit 200–400 ms

## See also

- [Animations overview](../../index.md)
- [Skeleton](../../loading/skeleton/description.md)
- [Typing](../../loading/typing/description.md)
