# Device Gestures (device)

Device gestures do not detect a touch but a **movement of the device itself**
via acceleration and gyro sensors (accelerometer, gyroscope).

## Elements

- **shake** - quick back-and-forth movement (undo, error feedback)
- **tilt** - tilting the device (steering, compass)
- **flip** - turning the device over (silent mode, muting a call)
- **wave** - moving a hand in front of the sensor (answering a call, assistant)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Undo / discard | shake |
| Tilting/steering content | tilt |
| Enable do not disturb | flip |
| Operating with free hands | wave |

## Accessibility

Device gestures fall under WCAG 2.5.4 (Motion Actuation): every sensor-based
action **must** have a regular UI alternative (button, menu item). Sensor
feedback (vibration) only with consent and switchable off (`hapticFeedback`,
`respectReducedMotion`).

## See also

- [Gesture overview](../index.md)
- [Shake animation](../../../de/animations/feedback/shake/description.md) - the same pattern as output feedback (German)
- [Wiggle animation](../../../de/animations/feedback/wiggle/description.md) - hold the device still, the element wobbles (German)
