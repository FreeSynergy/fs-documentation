# Lift

## Description

Lift apparently raises an element on hover or focus: it travels 1–2 px
upwards, the shadow grows larger and softer, and optionally the surface lightens
slightly. On leaving, the element sinks back just as quietly. The effect creates
depth without using up space in the layout.

## Use

- cards and tiles indicating that they are clickable, see [card](../../../../components/widgets/containers/card/description.md)
- rows in lists and tables on hover, see [list-view](../../../../components/widgets/data/list-view/description.md)
- buttons in secondary presentation that step forward on hover
- focus presentation for keyboard use (instead of only an outline)
- a drag source confirming its state when picked up
- navigation points that rise slightly as the pointer reaches them

## Duration

- Typical: 120–200 ms
- The return may be a little slower: 150–250 ms
- On touch devices lift does not apply – there [Press](../press/description.md)
  takes over

## Difference from Press and Highlight

- Press pushes the element inwards while it is actively pressed; Lift pulls it
  upwards on merely hovering over it.
- Highlight changes the background surface as a signal (found passage, change);
  Lift changes height and shadow, which says "usable".
