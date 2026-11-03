# Skeleton - Appearance

## Base layout

```
text:
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓

list-item:
○ ▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓

card:
┌──────────────┐
│ ▓▓▓▓▓▓▓▓▓▓  │
│ ▓▓▓▓▓▓▓      │
└──────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **text** | rounded bars at line height |
| **rect** | surface with `round` corners |
| **circle** | circle in `size` |
| **card** | several rectangles in a card arrangement |
| **list-item** | circle on the left, bars on the right |
| **table-row** | bars per column, width following the column width |
| **avatar** | circle plus two bars |

## Sizes

Width and height come from the attributes; if none is given, the size of the
target component applies. Text bars follow the size scale:

| Size | Line height |
|------|-------------|
| `small` | 14 px |
| `medium` | 18 px |
| `large` | 24 px |

## Colours and states

| Part | Colour |
|------|--------|
| surface | neutral surface, grey in the light theme, lighter in the dark one |
| `shimmer` | a lighter stripe travels across the surface |
| `pulse` | the surface breathes between two opacity levels |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| – | none; a skeleton is not operable |

## Responsive

- Skeletons inherit the responsive width of the parent area.
- With `prefers-reduced-motion` the animation goes to `none`; the surface stays static.
