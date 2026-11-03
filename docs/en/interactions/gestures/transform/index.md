# Transform Gestures (transform)

Transform gestures move **two or more pointers relative to each other**: the
distance or angle of the pointers changes the content (zoom, rotation).

Single-point is impossible here – distance and angle only exist from two
pointers on. The exact finger count is a setting (`pointerCount`), limited
above by the device: spreading with five fingers is the same gesture as with
two.

## Elements

- **pinch** - pointers move together (zoom out)
- **spread** - pointers move apart (zoom in)
- **rotate** - pointers turn around a centre (rotation)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Shrink content | pinch |
| Enlarge content | spread |
| Rotating (maps, images, canvas) | rotate |

## Accessibility

Per WCAG 2.5.1 every transformation needs a single-pointer alternative (zoom
buttons, rotation handle, slider). Keep browser pinch-zoom controllable via
`touch-action`.

## See also

- [Gesture overview](../index.md)
- [Zoom-in animation](../../animations/entrance/zoom-in/description.md) - answer to zoom gestures
- [Rotate animation](rotate/description.md) - answer to rotation gestures
