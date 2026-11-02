# Shake (Shaking)

## Description

A shake is a quick back-and-forth movement of the device or of an element. The gesture is usually detected via the accelerometer; with mouse/touchpad it is also detected via a quick horizontal movement of the pointer.

## Usage

- Undo / discard (classic: "shake to undo")
- Indicate an error (shake a form field when the input is invalid)
- Switch app (iOS: Shake for "Find a match")
- Reshuffle content / roll dice
- Unlock hidden features (Easter eggs)

## Duration

- Typical: 300–1000ms
- At least 2 direction changes within the time window

## Detection

| Method | Description |
|--------|-------------|
| **Accelerometer** | Sensor measures acceleration changes (mobile) |
| **Pointer Movement** | Fast X-movement with mouse/finger (desktop) |
| **Threshold** | Deviation from the mean value must be exceeded |

## Difference from Swipe

- **Swipe**: one movement in one direction (distance > 50px)
- **Shake**: several movements back and forth (direction changes count)

## Difference from Wiggle (Animation)

- **Shake (gesture)**: the user moves the device/element
- **Wiggle (animation)**: the element moves by itself as feedback
