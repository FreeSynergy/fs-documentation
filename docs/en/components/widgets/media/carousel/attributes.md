# Carousel - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `images` | array[] | - | array of images |
| `autoplay` | boolean | `false` | autoplay? |
| `interval` | number | `5000` | interval in ms |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `loop` | boolean | `true` | endless loop? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onSlideChange` | function | runs when the slide changes |
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `region` |

## Image attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `src` | string | image URL |
| `alt` | string | alt text |
| `title` | string | title |

## Navigation attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showNavigation` | boolean | `true` | show navigation? |
| `showThumbnails` | boolean | `true` | show preview images? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
