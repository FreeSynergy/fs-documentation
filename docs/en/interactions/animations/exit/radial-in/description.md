# Radial In

## Description

Radial In is the opposite direction of Radial Out: the points of a circular
menu travel from their ring positions back to the anchor core, shrink to
`scale 0` on the way and disappear through decreasing opacity. The outer rings
dissolve first, the innermost one last — the menu retracts into the anchor as
though it had never been away. The anchor core itself stays longest, or
disappears last.

## Use

- close a circular menu when the pointer leaves the area (after `closeDelay`)
- sub-point rings fold in when the active point changes — only the affected
  branch travels back
- speed dial at a corner or edge: the points step back out of the surface
- `Esc` or selecting a point: the menu retracts radially
- gather marker groups on maps back into a single point

## Duration

- Typical: 120–200 ms (exits may be shorter than entrances)
- Default value: 160 ms
- Staggering between points: 8–15 ms
- Offset between rings: 40–60 ms (from the outside inward)

## Difference from Radial Out and Pop Out

- Radial Out moves points away from the anchor up to their final size; Radial
  In leads them back and ends at size 0.
- Pop Out folds a single element away at its position; Radial In moves all
  points back to the shared anchor — the way inward shows where the menu came
  from.
- After `onAnimateEnd` the menu is taken out of the layout; until then the hit
  area remains (the pull-off tolerance of the
  [Radial Menu](../../../../components/widgets/navigation/radial-menu/description.md)).
