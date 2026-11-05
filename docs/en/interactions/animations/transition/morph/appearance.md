# Morph - Appearance

## Base layout

An element keeps its position and area; its contour travels from one shape to
the next without a jump.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│angular       rounded       almost round  final form  │
│                                                      │
│+--------+  .--------.  ( -------- )  ( ........ )    │
│                                                      │
│corner radii and paths are interpolated throughout    │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Icon morph** | two icons become one continuous path |
| **Radius morph** | rectangle ↔ circle via the corner radius |
| **Area morph** | a small element grows into the panel shape (FAB) |
| **Colour morph** | the fill changes softly along with the shape |
| **Path morph** | free SVG paths with an assignment of support points |

## Duration

- Typical: 300–600 ms

## See also

- [Animations overview](../../index.md)
- [Cross Fade](../cross-fade/description.md)
- [Elastic](../../feedback/elastic/description.md)
