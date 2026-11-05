# Stagger

## Description

Stagger is not a movement of its own; it takes over the timing of the child
animations by adding a fixed offset per index (element 0 starts at 0 ms, element
1 at `offsetProElement`, element 2 at twice that). Which animation the children
perform – fade, slide, scale – remains their own decision. The effect arises
solely from shifting the start times.

## Use

- let list rows fly in one after another when opening
- blend in the cards of a dashboard in stages
- cascade menu entries when opening
- let a photo grid appear row by row
- the exit in reverse: the children disappear in the opposite order
- forms build their fields up row by row

## Duration

- Typical: 30–80 ms offset per element (total = animation duration + offset × count)

## Difference from Parallax and Delay

- Parallax: layers differ in the speed of their movement; Stagger only shifts the
  start time, the movement stays the same.
- Delay: a single, fixed waiting time for one animation; Stagger computes the
  offset per element index (also possible in reverse or at random).
