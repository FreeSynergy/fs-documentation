# Shake - Appearance

## Base layout

The element stays at its position in the layout and oscillates in small steps
around that middle point.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  rattling around the rest position, amplitude    │
│  decays                                          │
│                                                  │
│  -8 px → [LOGIN]                                 │
│      +6 px → [LOGIN]                             │
│    -4 px → [LOGIN]                               │
│        +2 px → [LOGIN]                           │
│  0 px  → [LOGIN]   at rest after 400 ms          │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | horizontal, 8 px, 3 cycles with decay |
| **Vertical** | `achse: y` - nods at a rejected confirmation |
| **Rotating** | `achse: rotate` - a slight twist of a few degrees |
| **Hard** | `waveform: linear`, `decay: false` - a mechanical impression |
| **Subtle** | 3 px amplitude, 2 cycles for subtle hints |

## Duration

- Typical: 400 ms (range 300–500 ms)

## See also

- [Animations overview](../../index.md)
- [Wiggle](../wiggle/description.md)
- [Ripple](../ripple/description.md)
