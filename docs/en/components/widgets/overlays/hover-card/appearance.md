# Hover Card - Appearance

## Base layout

```
reference:  [ Anna Berger ]
                 │
          ┌──────▼───────────────────┐
          │ ◯  Anna Berger           │
          │    project planning      │
          │    last seen 12 min ago  │
          └──────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **profil** | avatar on the left, two lines of text on the right |
| **dokument** | title line, excerpt, meta line below |
| **vorschau** | image surface on top, title line below |

## Sizes

| Size | Width | Rows |
|------|-------|------|
| `small` | 240 px | 2 |
| `medium` | 320 px | 4 |
| `large` | 400 px | 6 |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | card with border and shadow, tip pointing at the trigger |
| `open` | card visible, trigger slightly filled |
| `loading` | skeleton in the card surface |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `bridge` | invisible bridge between trigger and card so the card does not snap shut |
| `shadow` | the shadow lifts the card off the content |

## Responsive

- On mobile devices a bottom bar replaces the card (long-press).
- The card opens towards the available side; at an edge it sits flush.
