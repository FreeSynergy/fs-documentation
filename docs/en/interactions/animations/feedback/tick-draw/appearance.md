# Tick Draw - Appearance

## Base layout

The tick sits in a prepared surface (a circle or a box) and is built up as one
unbroken stroke: first the short leg leading downward, then the long one towards
the upper right. The thickness stays the same while drawing.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│  0 ms        150 ms        320 ms        550 ms      │
│                                                      │
│   ( )         ( )          ( /          ( ✓ )        │
│  empty     circle visible  leg          finished    │
│             α = 1          being drawn               │
│                                                      │
│  circle: 200 ms  ·  stroke: 400 ms, from the left    │
│  to the upper right, without lifting the pen         │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | the circle appears, then the tick in 400 ms |
| **Stroke only** | `hintergrund: none` – the tick draws directly onto the surface |
| **Box** | `hintergrund: flaeche` – fits checkboxes |
| **Emphatic** | `nachziehen: 1.5` – the stroke shoots minimally past the target at the end |

## Duration

- Typical: 300–500 ms for the stroke, plus 150–250 ms run-up
- Default value: 400 ms

## See also

- [Animations overview](../../index.md)
- [Ripple](../ripple/description.md)
- [Highlight](../highlight/description.md)
- [Checkbox](../../../../components/primitives/fields/checkbox/description.md)
