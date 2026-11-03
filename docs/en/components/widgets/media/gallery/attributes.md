# Gallery - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `images` | array[] | - | array of images (src, alt, title) |
| `variant` | enum | `grid` | layout: `grid`, `masonry`, `carousel`, `lightbox` |
| `columns` | number | `3` | number of columns (grid) |
| `gap` | number | `16` | spacing between images |
| `responsive` | boolean | `true` | responsive layout? |

## Behaviour

| Attribute | Type | Description |
|-----------|------|-------------|
| `onClickImage` | function | runs when an image is clicked |
| `onSwipe` | function | runs on swipe |
| `onZoom` | function | runs on zoom |
| `lightBox` | boolean | open a lightbox on click? |

## Presentation

| Attribute | Type | Description |
|-----------|------|-------------|
| `animationDuration` | number | duration in ms |
| `transition` | enum | transition: `fade`, `slide`, `scale` |
| `showLoading` | boolean | show loading state? |

| Attribute | Type | Description |
|-----------|------|-------------|
| `aspectRatio` | string | aspect ratio (e.g. "4/3") |
| `fit` | enum | `cover`, `contain`, `fill` |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onImageLoad` | function | runs when the image has loaded |
| `onGalleryChange` | function | runs when the gallery changes |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-live` | string | live announcement |

## Carousel attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `autoplay` | boolean | `false` | automatic slideshow? |
| `interval` | number | `5000` | interval in ms |
| `loop` | boolean | `true` | endless loop? |
| `showNavigation` | boolean | `true` | forward/back buttons? |
| `showThumbnails` | boolean | `true` | preview images? |

## Filter attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `categoryFilter` | string | filter by category |
| `searchQuery` | string | search query |
| `showFilter` | boolean | show the filter? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
