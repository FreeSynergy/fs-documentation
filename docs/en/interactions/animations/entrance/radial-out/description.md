# Radial Out

## Description

Radial Out lets the points of a circular menu step outward out of the anchor
core: each point starts small (`scale 0`) at the anchor centre, travels along
its angle ray to its ring position and grows to its final size on the way. The
points of one ring start staggered clockwise; a further ring follows shortly
after its parent point has settled. The menu "blooms" open radially – the
direction towards a point is readable from the very first millisecond.

## Use

- open a circular menu (hover, tap, right click) — all points step out of the
  anchor
- sub-points push outward as the next ring out of the active point
- speed dial / fan at a corner or edge: points step from the corner into the
  surface
- launcher in the middle of the screen, rings build from the inside outward
- marker groups on maps unfold radially around a point

## Duration

- Typical: 180–260 ms per ring
- Default value: 220 ms
- Staggering between points: 12–25 ms
- Offset between rings: 60–90 ms

## Difference from Pop In and Stagger

- Pop In makes one element overshoot at its fixed position; Radial Out moves
  points from the anchor centre to their ring positions — position and size
  change together.
- Stagger only distributes start times within one movement; Radial Out is the
  movement itself. Both combined: `staggerStep` staggers the points, `ringStep`
  the rings (see [Stagger](../../organization/stagger/description.md)).
