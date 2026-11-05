# Highlight - Appearance

## Base layout

A rectangular colour background lies beneath the content and changes only its
opacity.

## Visual progress

```
┌──────────────────────────────────────────────────┐
│  0 ms        225 ms      450 ms      900 ms      │
│  [        ]  [░░░░░░░░]  [▓▓▓▓▓▓▓▓]  [░░░░░░░░]  │
│  0 %         50 %        100 %       20 %        │
│  normal      rise        maximum     decay       │
│                                                  │
│  the surface lights up, the position stays the   │
└──────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Background** | `modus: background` - the standard for found passages |
| **Outline** | `modus: outline` - only the contour glows |
| **Twice** | `iterationCount: 2` - two short pulses |
| **Decaying** | `anstiegAnteil` small, a long decay phase |
| **Persistent** | `fillMode: forwards` - stays marked (e.g. a selection) |

## Duration

- Typical: 900 ms (range 600–1200 ms)

## See also

- [Animations overview](../../index.md)
- [Ripple](../ripple/description.md)
- [Pulse](../../loop/pulse/description.md)
