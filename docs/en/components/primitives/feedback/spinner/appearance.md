# Spinner - Appearance

## Base layout

```
einfach:          mit-text:               inline:
   ◌              ◌  Loading…             text … ◌
```

The ring consists of an open circle whose leading segment rotates.

## Variants

| Variant | Appearance |
|---------|------------|
| **einfach** | open ring, one segment in the primary colour |
| **mit-text** | spinner on the left, text in the secondary colour on the right |
| **inline** | ring at text height, without extra spacing |

## Sizes

| Size | Diameter | Ring weight |
|------|----------|-------------|
| `small` | 16 px | 2 px |
| `medium` | 24 px | 3 px |
| `large` | 40 px | 4 px |

## Colours and states

| Part | Colour |
|------|--------|
| rotating segment | primary colour |
| `track` (background ring) | neutral track, 30 % opacity |
| accompanying text | secondary colour |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| – | none; a spinner is not operable |

## Responsive

- With reduced motion (`prefers-reduced-motion`) the rotation is replaced by
  a pulsating segment.
