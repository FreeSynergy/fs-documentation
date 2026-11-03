# Scroll Area - Appearance

## Base layout

```
┌──────────────────────────────┐
│ Content row 1                │
│ Content row 2                │
│ Content row 3                │
│ ⋮        ▮                   │  scrollbar on the right, fades out at rest
│ Content row n         ▮      │
└──────────────────────────────┘
   gradient at top and bottom when there is more
```

## Variants

| Variant | Appearance |
|---------|------------|
| **vertikal** | scrollbar on the right, gradients at top and bottom |
| **horizontal** | scrollbar at the bottom, gradients left and right |
| **beides** | both scrollbars, corners left out |

## Sizes

| Size | Scrollbar width | Gradient |
|------|-----------------|----------|
| `small` | 6 px | 12 px |
| `medium` | 8 px | 20 px |
| `large` | 12 px | 28 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | scrollbar hidden, gradient only when needed |
| `hover` | scrollbar appears in a neutral grey |
| `dragging` | scrollbar darker, width +2 px |
| `atTop` / `atBottom` | the gradient on that side disappears |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `fade` | gradients at the edges signal further content |
| `ring` | focus ring when the area can be operated by keyboard |

## Responsive

- On touch devices the scrollbar never appears; scrolling happens by gesture.
- With reduced motion, gradients and smooth following are dropped.
