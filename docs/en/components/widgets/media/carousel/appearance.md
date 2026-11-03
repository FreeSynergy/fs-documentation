# Carousel - Appearance

## Base layout
One slide visible, arrows on the left and right, a row of dots below it.

```
┌─────────────────────────────────────────┐
│ [◀]   🖼️   [▶]                         │
│      Image 1                            │
│  ● ○ ○ ○                                │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **automatik** | pause button appears above the slide |
| **manuell** | arrows and dots only |
| **miniaturen** | strip of small preview images below the slide |
| **überblenden** | no sliding movement, a soft cross-fade |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| Small | 300px | Small slideshows |
| Medium | 500px | Standard |
| Large | 700px | Large slideshows |
| Full | 100% | Full width |

## Colours and states

| State | Colour | Description |
|-------|--------|-------------|
| **Active Dot** | primary colour | active dot |
| **Inactive Dot** | grey | inactive dots |
| **Hover** | lighter | hover state |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `zoom` | the image grows |
| `overlay` | overlay with information |

## Responsive

- The carousel keeps its aspect ratio; below `small` screen width it goes full width
  and the arrows are replaced by swiping.
- The thumbnail strip scrolls sideways and centres the active preview; on narrow
  screens it is dropped in favour of the row of dots.
- The transition is `cross-slide` (sliding) or `cross-fade` (variant `überblenden`);
  with reduced motion the slides are swapped without effect.
