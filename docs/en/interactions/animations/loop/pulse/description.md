# Pulse

## Description

Pulse evenly swells up and back down: size and/or opacity rise softly to a
maximum and then fall symmetrically again. Per cycle there is exactly one peak.

## Use

- a recording, transmitting or live indicator
- attention for a primary action (call to action)
- location markers on maps
- a notification dot on an icon
- a waiting state in which "something is about to happen"
- preparation for an expected change

## Duration

- Typical: 800–2000 ms per cycle, usually endless (`iterationCount: infinite`)
- Default value: 1200 ms per cycle

## Difference from Heartbeat

- Heartbeat: two peaks per cycle in the heartbeat pattern ("lub-dub") with a clear
  rest phase afterwards
- Pulse: a single, even peak without a pause, sinusoidal
- Glow: a swelling glow around the contour; the size of the element stays constant
