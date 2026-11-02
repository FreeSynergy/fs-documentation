# Multi-Finger Gestures (multi)

Multi-finger gestures use two or more fingers at the same time (multitouch).
They mostly transform content (zoom, rotation) instead of navigating.

## Count is configuration, not a gesture type

Every gesture in this family works **from two pointers up** and is indifferent
to whether two, three, or five fingers are used: spreading works with five
fingers, rotating with three, and the multi-finger swipe with two as well.
Detection comes from the distance, the angle, and the movement of the pointers –
never from their number. `pointerCount` sets the minimum.

One more step on the count therefore adds **no new gesture**: a "three-finger
swipe" and a "four-finger swipe" are the same multi-finger-swipe with a
different `pointerCount`. New gestures arise only from new behaviour (a new
direction, a new action, a new sensor), not from additional fingers.

**Single-point is excluded**: with a single pointer neither distance nor angle
exists, so pinch, spread and rotate – and the multi-finger variants by
definition – are physically impossible with one finger. As with every
gesture, the ceiling is the device limit (typically five to ten fingers).

## Elements

- **pinch** - pointers pull together (zoom out), from two fingers up
- **spread** - pointers pull apart (zoom in), from two fingers up
- **rotate** - pointers turn around a center point (rotation), from two fingers up
- **multi-finger-tap** - touch with several fingers (secondary action)
- **multi-finger-long-press** - long press with several fingers (secondary menu, multiselect)
- **multi-finger-swipe** - swiping with several fingers (system navigation)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Shrink content | pinch |
| Enlarge content | spread |
| Rotate an object | rotate |
| Replace the right mouse button | multi-finger-tap, multi-finger-long-press |
| Switch app/desktop | multi-finger-swipe |

## Finger Count

| Gesture | Default `pointerCount` | Also works with | Single-Point |
|---------|------------------------|-----------------|------------|
| pinch / spread / rotate | 2 | 3, 4, 5 … fingers (device limit) | ✗ |
| multi-finger-tap / multi-finger-long-press | 2 | 3, 4, 5 … fingers (device limit) | ✗ |
| multi-finger-swipe | 3 | 2 or 4 fingers | ✗ |

## Accessibility

Multi-point gestures are permitted under WCAG 2.5.1 (Pointer Gestures) only
when an equivalent single-finger control exists (buttons, sliders, menus).
`pinch`/`spread` always need a zoom control, `rotate` a rotation slider or an
input field.

## See also

- [Gesture overview](../index.md)
- [Single-finger gestures](../single/) - single alternative to all of these
- [Transformations](../../animations/transition/) - visual answer to rotate & zoom
