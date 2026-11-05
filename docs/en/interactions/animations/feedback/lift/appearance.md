# Lift - Appearance

## Base layout

The element does not leave its layout position, it is only raised in the
rendering. The growing shadow creates the impression of a layer above the
surface.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│  0 ms         80 ms        160 ms        400 ms      │
│                                                      │
│  ┌──────┐    ┌──────┐     ┌──────┐     ┌──────┐      │
│  │ Card │    │ Card │     │ Card │     │ Card │      │
│  └──────┘    ▒▒▒▒▒▒▒▒    ░░░░░░░░      └──────┘      │
│   y = 0      y = -1      y = -2        y = 0         │
│   S = 0      S = 50 %    S = 100 %     pointer gone  │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | 2 px raise, shadow 8/16 px (160 ms) |
| **Flat** | `nurSchatten: true` – the height stays, only the shadow grows |
| **Strong** | `liftOffsetY: -4` for large cards and tiles |
| **Focus** | `ausloeser: focus` – raises on keyboard focus, not on hover |

## Duration

- Typical: 120–200 ms
- Default value: 160 ms

## See also

- [Animations overview](../../index.md)
- [Press](../press/description.md)
- [Highlight](../highlight/description.md)
- [Card](../../../../components/widgets/containers/card/description.md)
