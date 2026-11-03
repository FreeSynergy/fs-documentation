# Time Picker - Appearance

## Base layout

```
┌───────────────────┐
│  ⌂  09:00         │
├───────────────────┤
│  08:30            │
│  08:45            │
│ ▶ 09:00           │  current selection
│  09:15            │
│  …                │
└───────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **liste** | list with 7 visible rows, subtle scrollbar |
| **ziffernblatt** | circle with an hour hand, inner circle for minutes |

## Sizes

| Size | Row height | Width |
|------|------------|-------|
| `small` | 28 px | 140 px |
| `medium` | 36 px | 180 px |
| `large` | 44 px | 240 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | times neutral |
| `hover` | row lightly tinted |
| `active` | selected row in the primary colour |
| `open` | overlay with a shadow, selected row in the middle |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `ring` | focus frame on the active row |
| `fade-in` | the overlay fades in |

## Responsive

- On mobile devices the list appears as a bottom-anchored surface.
- `ziffernblatt` is replaced by the list below 400 px width.
