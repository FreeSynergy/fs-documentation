# Ripple - Appearance

## Base layout

A semi-transparent circle starts at the point of contact, grows and fades away
inside the element.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms        150 ms      300 ms      450 ms      │
│    ●          ( ● )     (   ●   ) (     ●     )  │
│  R = 0       R = 40 %    R = 85 %    α = 0       │
│  starts at the contact point, fades out at the   │
│  end and is clipped at the contour               │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **From the touch point** | `wellenUrsprung: click` - the standard on touch devices |
| **Centred** | `wellenUrsprung: center` - uniform for keyboard use |
| **Coloured** | `farbe` strongly saturated - a clear confirmation |
| **Overflowing** | `containInElement: false` - the wave reaches past the contour |
| **Several** | `maxWellen` > 1 - a fast series of taps |

## Duration

- Typical: 450 ms per wave (range 350–600 ms)

## See also

- [Animations overview](../../index.md)
- [Highlight](../highlight/description.md)
- [Shake](../shake/description.md)
