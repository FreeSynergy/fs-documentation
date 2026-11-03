# Image

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base` |
| **Variants** | `einfach`, `vignette`, `hintergrund` |
| **States** | `geladen`, `fehler` |
| **Gestures** | `tap`, `pinch`, `double-tap`, `drag` |
| **Animations** | `skeleton`, `fade-in`, `zoom-in` |
| **Related** | `gallery`, `icon`, `avatar`, `card`, `hover-card` |
| **Status** | documented |

## Description
An image element shows graphics, photos or other visual content. It is one of
the most fundamental media elements in FreeSynergy.

## Purpose

- Showing profile photos
- Product images in catalogues
- Images in articles and documents
- Background images
- Thumbnails

## Variants

| Variant | Description |
|---------|-------------|
| **einfach** | image in the content flow, own height or aspect ratio |
| **vignette** | cropped preview image in lists and cards |
| **hintergrund** | image behind other content (`backgroundSize`, `backgroundPosition`) |

Cropping and shape are not variants but the attributes `fit` and `shape`.

## Features

- Responsive image: a matching resolution per width (`srcSet`, `sizes`)
- Late loading (`lazy`) with a placeholder (`skeleton`) or a spinner
- A fallback when the file is missing (`onErrorFallback`)
- Alt text for screen readers, `role = presentation` for pure decoration

## Distinction

- **Do not confuse with** [icon](../icon/): icons are small, colourable symbols of the surface.
- **Do not confuse with** [gallery](../../../widgets/media/gallery/): a gallery is the grouping of
  several images including a large view, the image is a single element.
- **Do not confuse with** [avatar](../../../widgets/data/avatar/): an avatar identifies a person.
- Growing to full screen size belongs in the gallery or an overlay, not in the image.

## Best Practices

- The alt text describes the content, not the file name; decorative images get no alt text target.
- Always offer several resolutions and set the display size, so images do not jump.
- Set the aspect ratio firmly, otherwise the page shifts while loading.
- Clickable images need a clear symbol and a keyboard alternative.
- On error, show the fallback; never leave a broken image standing.

## Formats

| Format | Description | Use |
|--------|-------------|-----|
| **JPEG/JPG** | compressed, colourful | photos, coloured images |
| **PNG** | transparency, no compression | logos, icons, graphics |
| **GIF** | animation, transparency | small animations |
| **WEBP** | modern format, small file size | modern web applications |
| **SVG** | vector graphic, scalable | icons, logos, graphics |
| **AVIF** | newest format, very small | high quality images |

## Styling attributes

| Attribute | Value | Description |
|-----------|-------|-------------|
| `src` | string | image URL |
| `alt` | string | alt text for accessibility |
| `size` | enum | `thumbnail`, `small`, `medium`, `large`, `full` |
| `shape` | enum | `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover`, `contain`, `fill` |
| `loading` | enum | `lazy`, `eager` |
| `interactive` | boolean | is the image clickable? |

## Hover effects

| Effect | Description |
|--------|-------------|
| `zoom` | the image grows |
| `opacity` | the opacity changes |
| `border` | the border lights up |
| `shadow` | the shadow becomes stronger |

## See also

- [media – overview](../index.md)
- [Gallery](../../../widgets/media/gallery/) — several images with a large view
- [Icon](../icon/) — a symbol instead of a photo
- [Base component](../../basics/base.md)
