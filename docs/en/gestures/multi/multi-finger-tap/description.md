# Multi-Finger Tap

## Description

A multi-finger tap is the simultaneous brief touching with **two or more
fingers** (usually two; three, four, or five fingers are equally valid). On
devices without a right mouse button it serves as the equivalent of the
secondary click; Android used to provide `onTwoFingerTapEvent` in the
`GestureDetector` for this.

The number of fingers is a setting (`pointerCount`) and not its own gesture
type: tapping with two, three, or five fingers is the same gesture.

## Usage

- Secondary action / context menu (like a right click)
- Zoom control on maps (tap = one zoom step)
- Double-tap zoom with several fingers in map apps
- AssistiveTouch and accessibility shortcuts

## Duration

- Touch: under 300ms
- All fingers must touch down within ~100ms of each other

## Detection

| Method | Description |
|--------|-------------|
| **Pointer Count** | Exactly `pointerCount` pointers down at the same time (default 2) |
| **Time Window** | Down/up of all pointers without noticeable movement |
| **Spacing** | Minimum distance between the fingers (approx. 20px) against accidental triggering |

## Difference from Tap

- **Tap**: one finger, primary action
- **Multi-Finger Tap**: two or more fingers, secondary action

## Difference from Pinch/Spread

- **Multi-Finger Tap**: without movement
- **Pinch/Spread**: with the fingers moving towards/apart from each other

## Accessibility

Since the gesture is not self-explanatory, always offer a visible alternative
(context menu button, long press) (WCAG 2.5.1).
