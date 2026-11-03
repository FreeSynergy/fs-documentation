# Image - Appearance

## Base layout

Images are shown in different shapes and sizes, often with hover effects and
loading states.

## Variants

```css
/* rectangular - standard */
.image-rectangular {
  border-radius: 4px;
}

/* circular */
.image-circular {
  border-radius: 50%;
}

/* pill */
.image-pill {
  border-radius: 999px;
}
```

## Sizes

| Size | Width/height | Use |
|------|--------------|-----|
| thumbnail | 100px | lists, grids |
| small | 200px | profiles, small cards |
| medium | 400px | cards, panels |
| large | 600px | featured images |
| full | 1920px+ | hero sections, backgrounds |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | the image fills the cell, a light shadow depending on `shadow` |
| `hover` | zoom or an overlay with actions, according to `hoverEffect` |
| `geladen` | placeholder in the base colour until loading ends |
| `fehler` | frame with a symbol, fallback image if one is set |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `zoom` | the image grows (1.1x) |
| `overlay` | overlay with info/icons |
| `border` | the border lights up |
| `opacity` | the opacity changes |

## Responsive

- `responsive = true` delivers a matching resolution per width; the display area stays
  the same size so the page does not jump while loading.
- In grids and cards `fit = cover` keeps the aspect ratio, `fit = contain` adds
  margins on narrow screens.
- Background images scale with the viewport (`full`); the text above them stays at
  at least 4.5:1 contrast — otherwise put a dark veil over it.

## Loading state

### Skeleton (placeholder)

```
┌────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
└────────────────────────┘
```

### Spinner (loading animation)

```
┌────────────────────────┐
│                        │
│      🔄                │
│                        │
└────────────────────────┘
```

## Fit-mode variants

| Mode | Description | Use |
|------|-------------|-----|
| `cover` | the image fills the container, excess area is cut off | hero images |
| `contain` | the image fits completely in the container, possibly with a margin | product images |
| `fill` | the image is stretched to fill the container | background images |

## Border and shadow

| Variant | Description |
|---------|-------------|
| `default` | no border, light shadow |
| `outlined` | light border, no shadow |
| `elevated` | strong shadow, no border |
| `rounded` | rounded corners (8px) |
