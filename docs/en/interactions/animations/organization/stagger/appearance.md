# Stagger - Appearance

## Base layout

The child elements each start their identical animation offset from one another –
like the starting line-up of a relay race.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│t = 0 ms        50 ms         100 ms        150 ms    │
│                                                      │
│[Child 1] ████████                                    │
│[Child 2]   ████████                                  │
│[Child 3]     ████████                                │
│[Child 4]       ████████                              │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Forwards** | starts at the first child (standard) |
| **Backwards** | the exit starts at the last child |
| **Random** | the order is reshuffled for each run |
| **Groups** | `gruppenLimit` reins long lists in |
| **Row by row** | grid: the offset comes from row × column |

## Duration

- Typical: 30–80 ms distance per element

## See also

- [Animations overview](../../index.md)
- [Parallax](../../movement/parallax/description.md)
- [list-view](../../../../components/widgets/data/list-view/description.md)
