# Carousel

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base`, `gallery` |
| **Variants** | `Auto-play`, `Manual`, `Thumbnails`, `Fade Effect` |
| **States** | `spielend`, `pausiert` |
| **Gestures** | `swipe`, `tap`, `drag` |
| **Animations** | `cross-fade`, `cross-slide`, `slide-in` |
| **Related** | `gallery`, `grid-view`, `image`, `tabs` |
| **Status** | documented |

## Description
A carousel shows contents one after another in a single place: one slide
visible, the others ready, switched by button, swipe or automatically.

## Purpose

- Image galleries
- Product presentations
- Advertising
- Carousels

## Variants

| Variant | Description |
|---------|-------------|
| **automatik** | moves on by itself |
| **manuell** | buttons and swiping only |
| **miniaturen** | strip of preview images below the slide |
| **überblenden** | transition as a cross-fade instead of a slide |

## Features

- Navigation (forward/back)
- Autoplay
- Thumbs (preview images)
- Touch swipe (mobile)

## Distinction

- **Do not confuse with** [gallery](../gallery/): the gallery shows many images at the same time and
  enlarges them when needed, the carousel always shows only one (plan section 4, line 14).
- **Do not confuse with** [tabs](../../navigation/tabs/): tabs presuppose a selection,
  a carousel can run itself.
- The content of a slide is a component of its own — the text does not belong in the carousel.

## Best Practices

- Pause the automatic mode on hover, on focus and for motion sensitivity; no faster than
  five seconds per slide.
- A dot or number display always shows the total count and the current position.
- At most about seven slides; anything more belongs in a list or gallery.
- Offer the swipe gesture on mobile and hide the arrows so the surface stays free.

## See also

- [media – overview](../index.md)
- [Gallery](../gallery/) — many images at once
- [Grid View](../../data/grid-view/) — grid instead of sequence
- [Base component](../../../primitives/basics/base.md)
