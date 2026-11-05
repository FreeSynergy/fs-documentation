# Pulse - Appearance

## Base layout

A dot or icon in a fixed position changes its size and opacity in an even
rhythm.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  one cycle = 1200 ms                             │
│  ·      ╭───╮      ·      ╭───╮      ·           │
│         ╰───╯             ╰───╯                  │
│  1.00   1.06    1.00   1.06    1.00              │
│  trough peak    trough peak    trough            │
│                                                  │
│  exactly one peak per cycle, sinusoidal          │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Scale** | only `minScale`/`maxScale` - the element breathes |
| **Opacity** | opacity only - looks calmer |
| **Halo** | `haloRadius` - an expanding ring around the element |
| **Once** | `iterationCount: 1` - a short attention signal |
| **Gentle** | maxScale 1.02, opacity 0.85 - subtle |

## Duration

- Typical: 1200 ms per cycle (range 800–2000 ms)

## See also

- [Animations overview](../../index.md)
- [Heartbeat](../heartbeat/description.md)
- [Highlight](../../feedback/highlight/description.md)
