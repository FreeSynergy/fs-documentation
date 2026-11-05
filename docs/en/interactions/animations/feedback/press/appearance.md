# Press - Appearance

## Base layout

The element stays at its position in the layout and shrinks in the rendering
only. The pressed state holds until the user releases; only then does the size
return.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│  0 ms         60 ms        120 ms        300 ms      │
│                                                      │
│  [ OK ]      [  OK  ]     [  OK  ]     [ OK ]        │
│  s = 1.00    s = 0.98     s = 0.97     s = 1.00      │
│             finger down    held       released       │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | `pressScale: 0.97` for buttons and rows |
| **Distinct** | `pressScale: 0.94` for large surfaces and cards |
| **Colour only** | `pressScale: 1` with `pressOpacity` – entirely without movement |
| **With rebound** | `releaseOvershoot: 1.02` – the element springs back on release |

## Duration

- Typical: 100–150 ms going down, 120–180 ms returning
- Default value: 120 ms

## See also

- [Animations overview](../../index.md)
- [Lift](../lift/description.md)
- [Ripple](../ripple/description.md)
- [Elastic](../elastic/description.md)
