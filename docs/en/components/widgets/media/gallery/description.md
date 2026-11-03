# Gallery

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base` |
| **Variants** | `raster`, `mosaik`, `zeile` |
| **States** | `geöffnet`, `geladen` |
| **Gestures** | `tap`, `double-tap`, `swipe`, `pinch`, `drag` |
| **Animations** | `stagger`, `zoom-in`, `fade-in` |
| **Related** | `image`, `carousel`, `grid-view`, `hover-card` |
| **Status** | documented |

## Description
A gallery is a container element that shows several images in a grid or in a
slideshow. It often offers interactions such as a lightbox, zoom and navigation.

## Purpose

- Show photo galleries
- Present product images
- Portfolio pages
- Show screenshots
- Tell picture stories

## Variants

| Variant | Description |
|---------|-------------|
| **raster** | equally sized tiles in columns (standard) |
| **mosaik** | differing heights, columns fill by height |
| **zeile** | one row scrollable sideways, for a few images |

The sequence of single images is no longer a gallery variant but the separate
component [carousel](../carousel/).

## Features

- Hover zoom (the image grows on hover)
- Lightbox (a click opens the large view)
- Swipe (touch swipe on mobile)
- Keyboard navigation (arrow keys)
- Touch gestures
- Lazy loading (load only visible images)
- Filter (filter by categories)

## Distinction

- **Do not confuse with** [carousel](../carousel/): the carousel shows one after another,
  the gallery side by side (plan section 4, line 14).
- **Do not confuse with** [grid-view](../../data/grid-view/): the grid shows arbitrary objects,
  the gallery only images along with enlargement.
- **Do not confuse with** [image](../../../primitives/media/image/): a single image is not a gallery member.
- The large view is an overlay like [popover](../../overlays/popover/), not a separate page.

## Best Practices

- Always give an `alt` text for accessibility
- Lazy loading for performance
- Responsive layout for mobile
- Fast loading times (optimised images)
- Clear visual hierarchy

## Navigation attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `images` | array[] | array of images |
| `columns` | number | number of columns |
| `autoplay` | boolean | automatic slideshow? |
| `interval` | number | interval in ms (with autoplay) |
| `loop` | boolean | endless loop? |
| `showNavigation` | boolean | show forward/back navigation? |
| `showThumbnails` | boolean | show preview images? |

## Interaction attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `onClickImage` | function | runs when an image is clicked |
| `onZoom` | function | runs on zoom |
| `onSwipe` | function | runs on swipe |
| `lightBox` | boolean | open a lightbox on click? |

## Hover effects

| Effect | Description |
|--------|-------------|
| `zoom` | the image grows |
| `overlay` | overlay with information |
| `border` | the border lights up |
| `scale` | the image scales |

## See also

- [media – overview](../index.md)
- [Base component](../../../primitives/basics/base.md)
