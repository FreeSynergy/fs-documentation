# Tooltip - Appearance

## Base layout

```
        ┌────────────────────┐
        │ Settings           │   placement = top
        └─────────┬──────────┘
                  ▼
              ┌───────┐
              │  ⚙   │
              └───────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **top** | above the element |
| **right** | to the right of the element |
| **bottom** | below the element |
| **left** | to the left of the element |
| **auto** | free choice, flips when close to an edge |

## Sizes

| Size | Font | max. width |
|------|------|------------|
| `small` | 11 px | 180 px |
| `medium` | 12 px | 240 px |
| `large` | 14 px | 300 px |

## Colours and states

| Part | Colour |
|------|--------|
| surface | dark surface, dark grey in the light theme, lighter in the dark one |
| text | high contrast against the surface |
| `arrow` | same colour as the surface |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `fade-in` | fades in after `delay` (standard 400 ms) |
| `fade-out` | short fade-out when the pointer leaves the element |

## Responsive

- The tooltip stays inside the viewport and automatically flips to the opposite side.

- With `prefers-reduced-motion` it becomes visible immediately without animation.
