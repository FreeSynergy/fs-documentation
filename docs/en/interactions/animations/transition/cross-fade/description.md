# Cross Fade

## Description

Cross Fade cross-fades two independent elements in the same place: one fades
down while the other fades up. Both are briefly visible at the same time, and the
opacity transitions are exactly mirrored. The space stays filled throughout, and
no layout jump occurs.

## Use

- image changes in carousels and galleries
- icon or status change (cloud ↔ sun, online ↔ away)
- swap tab contents without a layout jump
- before/after comparison in editing views
- switch diagram variants (a different data series)
- theme change for images that are not redrawn

## Duration

- Typical: 250–500 ms

## Difference from Fade In/Fade Out and Morph

- Fade In/Fade Out: one element appears or disappears, and in between the space is
  empty; Cross Fade overlaps both elements without a gap.
- Morph: the same element changes its shape; Cross Fade replaces two independent
  elements through opacity alone.
