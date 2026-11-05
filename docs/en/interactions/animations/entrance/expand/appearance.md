# Expand - Appearance

## Base layout

Starting from a single line, the slot grows downward; the content stays
un-scaled and is laid bare.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms            150 ms          300 ms          │
│  ╭────────╮      ┌────────┐      ┌────────┐      │
│  height = 0      ░░░░░░░░░░      ░░░░░░░░░░      │
│                  └────────┘      ░░░░░░░░░░      │
│                  height 50 %     └────────┘      │
│  content is                      height = content│
│  revealed, not scaled                            │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Vertical** | `dimension: height` - the standard for accordions |
| **Horizontal** | `dimension: width` - the panel opens to the right |
| **With scroll** | `maxHeight` caps it, the rest is scrollable |
| **With fade** | `innerFade` additionally fades in the child elements |
| **Lazy** | `deferRender` - the content only appears when opening |

## Duration

- Typical: 300 ms (range 200–400 ms)

## See also

- [Animations overview](../../index.md)
- [Collapse](../../exit/collapse/description.md)
- [Unfold](../unfold/description.md)
