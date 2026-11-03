# Repeater - Appearance

## Base layout
A repeater is a repeating layout for lists.

```
┌─────────────────────────────────────────┐
│ Item 1                                  │
│ Content 1                               │
├─────────────────────────────────────────┤
│ Item 2                                  │
│ Content 2                               │
├─────────────────────────────────────────┤
│ Item 3                                  │
│ Content 3                               │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **liste** | entries below each other, divider lines between them |
| **raster** | entries as cards in columns |
| **eingabe** | groups of fields below each other, ``+ add row`` at the bottom |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | small repeaters |
| medium | 300px | standard |
| large | 400px | large repeaters |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Item** | light | item background |
| **Hover** | lighter | hover state |
| **Active** | primary colour | active item |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `shadow` | the shadow becomes stronger |
| `transform` | slight lift |
| `border` | the border lights up |

## Responsive

- On narrow screens the control bar (search, filter, sorting) wraps into two rows
  and stays at the top while scrolling.
- The grid variant follows the same column thresholds as [grid-view](../grid-view/);
  the list variant stays one column.
- When the page changes, the top of the list is moved up inside the `scroll-area`,
  new entries appear with `fade-in`.
