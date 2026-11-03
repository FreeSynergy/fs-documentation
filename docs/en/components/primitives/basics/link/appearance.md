# Link - Appearance

## Base layout

```
standard:      unterstrichen:   external:
Privacy        a wiki link      OpenProject ↗
```

## Variants

| Variant | Appearance |
|---------|------------|
| **standard** | primary colour, underlined only on hover |
| **muted** | secondary text, same hover as standard |
| **icon** | icon on the left or right with a 4 px gap |
| **unterstrichen** | continuous line, also in the resting state |

## Sizes

The font size follows the surrounding text; `size` only adjusts the icon:

| Size | Icon |
|------|------|
| `small` | 12 px |
| `medium` | 14 px |
| `large` | 18 px |

## Colours and states

| State | Colour |
|-------|--------|
| `default` | primary colour |
| `hover` | primary colour darkened plus underline |
| `active` | strongly darkened while pressed |
| `focus` | 2 px focus ring |
| `visited` (external) | keeps the primary colour |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `underline` | the line appears on hover (standard) |
| `ring` | focus ring for keyboard navigation |

## Responsive

- Link targets stay at least line height high as a hit area
  (touch: 44 px, see the base component).
