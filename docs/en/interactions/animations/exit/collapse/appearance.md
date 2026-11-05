# Collapse - Appearance

## Base layout

The top edge stays put, the bottom edge travels upward until only a line is
left.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms            125 ms          250 ms          │
│  ┌────────┐      ┌────────┐      ┌────────┐      │
│  ░░░░░░░░░░      ░░░░░░░░░░      └────────┘      │
│  ░░░░░░░░░░      └────────┘      height = 0      │
│  └────────┘      height 50 %     lower rows      │
│  height 100 %                    shift up        │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Vertical** | `dimension: height` - the standard for accordions |
| **Horizontal** | `dimension: width` - the sidebar slides back to the left |
| **Both** | `dimension: both` - the panel shrinks in both directions |
| **Staggered** | `staggerChildren` - child rows one after another |
| **With fade** | the content is additionally thinned out, a softer transition |

## Duration

- Typical: 250 ms (range 200–350 ms)

## See also

- [Animations overview](../../index.md)
- [Expand](../../entrance/expand/description.md)
- [Scale Out](../scale-out/description.md)
