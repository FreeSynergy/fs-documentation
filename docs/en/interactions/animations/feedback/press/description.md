# Press

## Description

Press lowers an element minimally while pressing (`scale` around 0.97) and
slightly raises the opacity or the shadow. On release it springs back into its
starting position. The animation is deliberately barely visible – it confirms
the point of contact without drawing attention away from the content.

## Use

- buttons, icons and chips while the key or finger is held down
- cards and rows that can be activated on tap, see [card](../../../../components/widgets/containers/card/description.md)
- toolbar buttons and segmented controls
- toggling switches (in addition to the change of state)
- touchscreens, where there is no hover state
- controls on a keyboard when the space bar or enter is held

## Duration

- Typical: 100–150 ms for going down, 120–180 ms for the return
- Holding: the end state stays until release
- No longer than 200 ms – otherwise the element feels sluggish

## Difference from Ripple and Elastic

- Ripple draws a wave from the point of contact and runs out after release; Press
  changes the whole element only while it is being pressed.
- Elastic overshoots past the final position after a movement; Press moves inwards
  within the final position.
