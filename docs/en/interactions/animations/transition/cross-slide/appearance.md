# Cross Slide - Appearance

## Base layout

Both elements lie in the same surface, which is bounded sideways and clipped.
They move in opposite directions at the same speed, without a change of size or
opacity.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│  0 ms             140 ms              280 ms         │
│                                                      │
│  ┌─────┐          ┌─────┐             ┌─────┐       │
│  │ Tab1│ Tab2     │Tab1 │Tab2    Tab1 │ Tab2│       │
│  └─────┘          └─────┘             └─────┘       │
│   T1 at 0         each 50 % of way    T2 at 0        │
│                                                      │
│  richtung: left – content slides out to the left     │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | `richtung: left`, full width, simultaneous movement |
| **Backwards** | `richtung: right` – clearly readable as "back" |
| **Vertical** | `richtung: up` for stacks, notifications, month lists |
| **Offset** | `anteilUeberlappung: 0.3` – the `altesElement` goes first, then the new one arrives |

## Duration

- Typical: 200–350 ms
- Default value: 280 ms

## See also

- [Animations overview](../../index.md)
- [Cross Fade](../cross-fade/description.md)
- [Slide In](../../entrance/slide-in/description.md)
- [Slide Out](../../exit/slide-out/description.md)
