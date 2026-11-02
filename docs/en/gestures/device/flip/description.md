# Flip (Turning-Over Gesture)

## Description

Flip is **turning the device over** with the display facing down (or the back
facing up). Detection runs via the accelerometer: the direction of gravity
tips from "display points away from the ground" to "display points to the
ground".

## Usage

- Muting a call (classic: turning the phone over = answer and mute)
- Enabling do-not-disturb mode (flip to silence / flip to shhh)
- Meeting mode: suppressing notifications
- Acknowledging an alarm (smartphones with a proximity sensor: cover + turn over)

## Direction

| Movement | Typical action |
|----------|----------------|
| Display down | Mute / do not disturb |
| Display up (back) | The mode ends automatically |

## Duration

- Turning over: 300–1500ms
- Holding phase face down: usually ≥ 1000ms, so it does not trigger accidentally

## Detection

| Method | Description |
|--------|-------------|
| **Accelerometer** | The Z axis flips its sign |
| **Gyroscope** | Rotation around a horizontal axis |
| **Proximity** | Additionally: nothing in front of the display (filters putting it down on a table) |

## Difference from Shake

- **Flip**: one 180° turn with a stable end state
- **Shake**: a fast back-and-forth movement with no end state

## Difference from Tilt

- **Flip**: a complete reversal of the orientation
- **Tilt**: a partial inclination as a control value

## Accessibility

WCAG 2.5.4: a regular switch (mute button, do-not-disturb switch) must always
trigger the same action.
