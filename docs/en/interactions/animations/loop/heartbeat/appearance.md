# Heartbeat - Appearance

## Base layout

The element stands still, makes two short beats, and then stays unchanged for the
rest of the cycle.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  one cycle = 1000 ms (72 bpm)                    │
│                                                  │
│  time   0     100    170    240      1000 ms     │
│  scale  1.00  1.12   1.05   1.09    1.00         │
│         ▁     ▆      ▃      ▅       ▁            │
│         lub   dub    - rest phase 450 ms -       │
│                                                  │
│  two beats per cycle, then rest                  │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | `lub-dub`, 72 bpm, two peaks with a rest phase |
| **Amplified** | `schlagSkala` 1.25 - a clearly more visible beat |
| **Calm** | 55 bpm, a small amplitude for a lasting live display |
| **Frantic** | 110 bpm, `pauseAnteil` 0.2 - an alarm character |
| **Once** | `iterationCount: 1` when confirming an action |

## Duration

- Typical: 1000 ms per cycle (range 700–1200 ms)

## See also

- [Animations overview](../../index.md)
- [Pulse](../pulse/description.md)
- [Ripple](../../feedback/ripple/description.md)
