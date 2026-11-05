# Slide Out - Appearance

## Base layout

The element glides from its layout position in a straight line past the edge of
the visible area and disappears there.

## Visual progress (example direction: right)

```
┌────────────────────────────────────────────┐
│  0 ms     · · · · · · [Element] · · ·      │
│ 125 ms    · · · · · · · · · [Element]·     │
│ 250 ms    · · · · · · · · · · · ·  (empty) │
└────────────────────────────────────────────┘
```

`·` = visible area; the element travels to the right and leaves the view area.

## Variants

| Variant | Description |
|---------|-------------|
| **Left** | glides out to the left (closing a left drawer) |
| **Right** | glides out to the right (standard, swipe-to-remove) |
| **Up** | glides upward out of view (mobile dialogs) |
| **Down** | glides downward out of view (bottom sheets, menus) |

## Duration

- Typical: 200–350 ms
- Default value: 250 ms

## See also

- [Animations overview](../../index.md)
- [Slide In](../../entrance/slide-in/description.md)
- [Fade Out](../fade-out/description.md)
