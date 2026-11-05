# Slide In - Appearance

## Base layout

The element starts outside the visible area and glides in a straight line to
its layout position, usually accompanied by a light fade.

## Visual progress (example direction: left)

```
┌────────────────────────────────────────────┐
│  0 ms     [Element] · · · · · · · · ·      │
│ 150 ms    · · · · · [Element] · · · ·      │
│ 300 ms    · · · · · · · · · [Element] ·    │
└────────────────────────────────────────────┘
```

`·` = visible area; the element travels from left to right into its final
position.

## Variants

| Variant | Description |
|---------|-------------|
| **Left** | comes from the left (standard, left drawer) |
| **Right** | comes from the right (right drawer, toasts) |
| **Up** | comes in from below (bottom sheet, list entries moving up) |
| **Down** | comes from above (menu bars, notification drawers) |

## Duration

- Typical: 200–400 ms
- Default value: 300 ms

## See also

- [Animations overview](../../index.md)
- [Slide Out](../../exit/slide-out/description.md)
- [Fade In](../fade-in/description.md)
