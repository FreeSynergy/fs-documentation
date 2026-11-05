# Scale Out

## Description

Scale Out shrinks an element from 100 % to 0 % until it has disappeared
completely. The shrink point is usually in the middle, but it can be set to the
trigger in order to show the connection to the gesture.

## Use

- closing dialogs, menus and popovers
- removing a toast or a notification
- deleting a list entry or chip
- hiding a badge after the interaction
- handing the element over to another place ("the element flies to the cart")
- a chip is removed when the selection ends

## Duration

- Typical: 120–250 ms
- Default value: 180 ms

## Difference from Fade Out

- Fade Out: only the opacity falls, the element keeps its size and therefore
  its layout space for the time being
- Zoom Out: ends at an intermediate value and uses perspective; the element
  appears to travel into the depth
- Scale Out: ends at exactly 0 %, the element flattens itself together onto a
  single point
