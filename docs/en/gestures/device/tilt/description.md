# Tilt (Tilting Gesture)

## Description

Tilt is **tilting the device** around one or two axes. Detection runs via the
accelerometer (orientation relative to gravity) or the gyroscope. With a pen,
`PointerEvent.tiltX`/`tiltY` measures the inclination of the pen – the same
idea, a different axis.

## Usage

- Tilting as control (games, steering, compass)
- "Tilting through" content: a list/shelf moves with the device (parallax)
- Spirit level, photo grid, panorama guidance
- Pen inclination for hatching/erasers in drawing apps

## Tilt Angles

| Axis | Range | Name |
|------|-------|------|
| Alpha | 0–360° | Compass direction (azimuth) |
| Beta | -180–180° | Tilting forwards/backwards |
| Gamma | -90–90° | Tilting left/right |

## Duration

- Detection: continuous, events every 10–100ms
- Dead zone: ±2–5° against wobbling

## Detection

| Method | Description |
|--------|-------------|
| **Accelerometer** | `deviceorientation` / SensorManager |
| **Gyroscope** | Rotation rate for fast tilting movements |
| **Pen Tilt** | `tiltX`/`tiltY` in pointer events |

## Difference from Shake

- **Tilt**: slow, stable direction, a state ("the device lies at an angle")
- **Shake**: fast, repeated, an event

## Accessibility

WCAG 2.5.4 (Motion Actuation): tilting actions always need a UI alternative
(buttons, sliders). Make calibration and sensitivity configurable.
