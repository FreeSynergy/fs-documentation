# Parallax - Appearance

## Base layout

At least two layers (e.g. text over an image) cover different distances for the
same scroll distance.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│scroll 0        scroll 1        scroll 2              │
│                                                      │
│FG ████████    FG  ████████   FG   ████████           │
│BG ▒▒▒▒▒▒▒▒    BG ▒▒▒▒▒▒▒▒    BG  ▒▒▒▒▒▒▒▒            │
│                                                      │
│FG = foreground (fast), BG = background (slow)        │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Scroll** | the standard when scrolling long pages |
| **Pointer** | the layers tilt/shift when the pointer moves over them |
| **Device** | the gyroscope tilts the layers (mobile) |
| **Subtle** | `maxAusschlag: 16`, barely perceptible depth |
| **Perspective** | `tiefe` produces a genuine 3D layer impression |

## Duration

- Follows the input; transitions 100–300 ms

## See also

- [Animations overview](../../index.md)
- [Stagger](../../organization/stagger/description.md)
- [Skeleton](../../loading/skeleton/description.md)
