# Fingerprint

## Description

A fingerprint is **touching a biometric sensor**: either holding a finger
still until the scan completes, or sliding it across the sensor (swipe
method). The sensors work capacitively (surface), optically (camera), or by
ultrasound (3D image, under the display). What is registered is not a click
on an element but an authentication event.

## Finger Count

Exactly 1 – the sensor reads the pad of one finger.

## Usage

- Unlocking devices and apps
- Authorising actions (payments, deleting accounts, password managers)
- Login as an alternative to PIN or password
- Sliding across the sensor as an input channel (scrolling lists)

## Duration

- Scan: 100–500ms
- Hold the finger on the sensor until confirmation (vibration or checkmark)

## Detection

| Method | Description |
|--------|-------------|
| **Capacitive** | Surface sensor measures the ridge pattern (often in buttons) |
| **Optical** | Camera photographs the fingertip (in display or frame) |
| **Ultrasonic** | 3D tomography of the ridge structure, works with wet fingers too |

## Difference from Tap

- **Tap**: targets a UI element, measures pressure point and duration
- **Fingerprint**: targets the sensor, result is a match decision (true/false)

## Accessibility

Biometric sign-in always needs an equivalent alternative without biometrics
(PIN, pattern, password). A failed or blocked scan (moisture, dirt) must
lead to the fallback, never to a dead end.
