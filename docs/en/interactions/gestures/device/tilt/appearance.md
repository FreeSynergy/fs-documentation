# Tilt - Appearance

## Basic Layout

The device is tilted; content moves along, or an indicator travels from the
resting position to the target.

```
┌───────────────────────────────┐
│      ╱ Device tilts           │
│    ╱                          │
│  ●─────┐  Level indicator    │
│        └──●───────┐           │
│   Content moves along ═►      │
└───────────────────────────────┘
```

## Feedback Options

| Option | Description |
|--------|-------------|
| **Parallax** | Layers shift at different speeds |
| **Level Indicator** | Spirit level/cross shows the inclination |
| **Clamp Bounce** | Slight overshoot at the maximum angle |
| **None** | No visible signal, only a control value |

## Sensitivity

| Mode | Dead zone | Usage |
|------|-----------|-------|
| Fine | 1–2° | Photo grid, panorama |
| Standard | 3–5° | Steering, parallax |
| Sluggish | 6–10° | Coarse selections |

## Duration

- Continuous measurement, reaction < 100ms
- Resting position detection: 500ms without change

## Difference from Shake

- Tilt: a state ("how far tilted?"), slow, one target value
- Shake: an event ("how often shaken?"), fast, binary
