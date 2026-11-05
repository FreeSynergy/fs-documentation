# Heartbeat

## Description

Heartbeat imitates a heartbeat: two fast peaks ("lub-dub") follow each other
directly, then there is a clear phase of rest. The rhythm corresponds to typical
heart rates of roughly 60 to 100 beats per minute.

## Use

- health, fitness and vital-sign views
- live status with a "living" feel
- emotional actions such as favourite or recommendation
- a critical countdown (subscription expiring, connection unstable)
- visualisation on wearables and monitors
- vital parameters with a recognisable rhythm

## Duration

- Typical: 700–1200 ms per cycle, usually endless (`iterationCount: infinite`)
- Default value: 1000 ms per cycle

## Difference from Pulse

- Pulse: one even peak per cycle, without a phase of rest
- Heartbeat: two peaks of differing strength per cycle plus a pause – which makes
  it recognisably rhythmic
- Ripple: a wave spreads spatially from the click point; Heartbeat scales the
  element itself
