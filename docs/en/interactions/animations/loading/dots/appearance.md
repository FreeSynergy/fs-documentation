# Dots - Appearance

## Base layout

Three equally sized dots stand in one row on a baseline and move offset in time.
The indicator is as tall as the surrounding text line and does not disturb the
flow of lines.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms        200 ms       400 ms       600 ms    │
│                                                  │
│    •           •            •           •        │
│   • •         • •          • ••        • • •     │
│  (still)     P1 lifts     P2 lifts     P3 lifts  │
│                                                  │
│  one cycle = 1400 ms, then from the start again  │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Lifting** | `modus: bounce` – the dots rise above the baseline (standard) |
| **Blinking** | `modus: fade` – the dots change opacity, no movement |
| **Growing** | `modus: scale` – the dots become larger and smaller |
| **Two dots** | `anzahl: 2` for very narrow places (buttons with an icon) |

## Duration

- Typical: 1200–1600 ms per cycle
- Default value: 1400 ms

## See also

- [Animations overview](../../index.md)
- [Typing](../typing/description.md)
- [Skeleton](../skeleton/description.md)
- [Progress](../progress/description.md)
