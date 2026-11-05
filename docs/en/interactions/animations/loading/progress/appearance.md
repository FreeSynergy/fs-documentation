# Progress - Appearance

## Base layout

A rail whose filled area grows along with the progress from left to right (for a
ring, clockwise).

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│0 %          25 %          50 %          100 %        │
│                                                      │
│[--------]   [###------]   [######---]   [########]   │
│                                                      │
│indeterminate: [~~>~~~~]   [~~~>~~~]   segment rocks  │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Bar** | the classic horizontal filling with a percentage |
| **Ring** | circular progress, e.g. inside round icons |
| **Segments** | discrete steps (1/5, 2/5 …) for assistants |
| **Indeterminate** | a travelling segment when the target size is unknown |
| **Compact** | a thin bar at the page edge (e.g. reading progress) |

## Duration

- Typical: 200–500 ms per change of value, loop 1000–1500 ms

## See also

- [Animations overview](../../index.md)
- [Skeleton](../skeleton/description.md)
- [Typing](../typing/description.md)
