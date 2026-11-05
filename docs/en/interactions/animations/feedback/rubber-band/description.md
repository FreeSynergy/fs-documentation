# Rubber Band

## Description

Rubber Band shows the resistance of a scrollable surface when it is pulled too
far: if the user pulls past the edge, the content only follows in a damped way.
On release it springs back elastically into the edge position. The deflection
arises solely from the gesture – without pulling, the content stays at its edge.

## Use

- over-scroll at the top and bottom in lists and articles
- horizontal lists at the end of the track
- cards and zoomable images with damped edges
- paging: the pull-in signals the end of the list
- the pull-in area as the start of pull-to-refresh
- drag & drop at container boundaries

## Duration

- Typical: springing back 300–500 ms; the following movement directly
  (gesture-controlled)

## Difference from Elastic and Bounce Out

- Elastic: a movement without a gesture that overshoots on its own; Rubber Band
  first follows the finger and only springs back after release.
- Bounce Out: springs before disappearing; Rubber Band always ends in the
  position of rest, the element stays visible.
