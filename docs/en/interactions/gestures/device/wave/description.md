# Wave (Waving Gesture)

## Description

Wave is **moving the hand in front of the device** without touching it. It is
detected via radar sensors (Google Soli / Motion Sense), ToF sensors, or a
front camera with gesture recognition. The gesture became known through "wave
to answer" (Pixel wave to answer, taking a call by waving) and "air gestures"
in Android Auto.

## Finger Count

No touch – the sensor reads the hand in front of the device.

## Usage

- Answering/declining a call without screen contact (hands occupied)
- Calling the assistant / controlling media in car and smart-display contexts
- Navigation without touch (kitchen, workshop, operating-room scenarios)
- Accessible control for people who cannot touch the device

## Movement Patterns

| Pattern | Typical action |
|---------|----------------|
| Waving a hand towards and away | Answer the call |
| Closing/opening a fist | Decline the call |
| Wiping the hand sideways | Next / mute |

## Duration

- Movement: 500–2000ms
- Preparation phase (raising the hand): a separate detection phase

## Detection

| Method | Description |
|--------|-------------|
| **Radar (mmWave)** | Soli/Motion Sense detects the hand in the sensor cone |
| **Camera + ML** | Optical hand-gesture recognition |
| **ToF** | Depth sensor detects the approach |

## Difference from Shake

- **Wave**: the hand moves, the device stays still, no contact
- **Shake**: the device moves, no contact with the surroundings needed

## Accessibility

Wave can be a good low-contact alternative, but under WCAG 2.5.4 (Motion
Actuation) it is only permitted with a regular UI alternative; in addition,
sensor availability is device-dependent and must always be made explicitly
configurable.
