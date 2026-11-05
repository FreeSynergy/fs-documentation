# Reorder - Appearance

## Base layout

All affected elements stay in their container; their position is not shown as a
recalculation but is followed as a movement. The element being dragged lies
slightly raised (shadow), the others give way sideways or vertically.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│  0 ms (re-sorted)      160 ms          320 ms       │
│                                                      │
│  A A                    A _ B              A B C     │
│  B B        ->          B A                A B C     │
│  C C                    C C                A B C     │
│                                                      │
│  B travels up, A moves down; C stays where it is    │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | all displaced elements travel at the same time (320 ms) |
| **Displacement only** | `messung: transform` – the cheapest variant, no recalculation |
| **With click-in** | `einrasten: 2` – the element settles slightly over and springs back |
| **After filtering** | removed elements via [Fade Out](../../exit/fade-out/description.md), the rest move up via Reorder |

## Duration

- Typical: 250–400 ms
- Default value: 320 ms

## See also

- [Animations overview](../../index.md)
- [Stagger](../../organization/stagger/description.md)
- [Rubber Band](../../feedback/rubber-band/description.md)
- [Drag (gesture)](../../../gestures/swipe/drag/description.md)
