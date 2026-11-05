# Morph

## Description

Morph softly transforms the shape of an element into another shape: SVG paths,
corner radii and proportions pass continuously into one another. The element
stays the same object meanwhile – it only changes its guise. Size and colour can
also be included in the same transition.

## Use

- icon morphing: play ↔ pause, hamburger ↔ close
- a FAB expands on tap into a dialog panel
- an avatar circle becomes a rounded rectangle when selected
- switch and slider handles change their shape depending on the state
- onboarding: an object gradually assumes its next shape
- status icons (e.g. cloud ↔ sun) without a hard jump

## Duration

- Typical: 300–600 ms

## Difference from Flip and Cross Fade

- Flip: turns the element by 180° and shows a different back side; Morph deforms
  the silhouette itself, without turning.
- Cross Fade: two independent elements swap via opacity; Morph is one element
  whose contour is interpolated throughout.
