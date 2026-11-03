# Fingerprint - Appearance

## Basic Layout

The sensor zone is marked (an icon, a recess, or a glowing ring on display
sensors). Touching it starts the scan animation inside the sensor zone –
outside every UI element.

```
┌─────────────────────────────────────────┐
│                                         │
│              ╭─────────╮                │
│             (  ridges  )  fingertip     │
│              ╰─────────╯                │
│          Scan ring in sensor zone       │
└─────────────────────────────────────────┘
```

## States

| State | Display |
|-------|---------|
| **Ready** | Sensor icon or ring, static |
| **Scanning** | Ring pulses or fills up |
| **Success** | Checkmark, brief glow |
| **Failure** | Ring marked red (shake), hint to try again |

## Feedback Options

| Option | Description |
|--------|-------------|
| **Haptic** | Short vibration on success, double on failure |
| **Ring animation** | Pulsing or progress fill |
| **1:1 movement** | The list moves 1:1 along in swipe mode |

## Duration

- Scan animation: 100–500ms until the result
- Result display: 300–1000ms, then the UI closes or stays open

## Difference from Tap (Appearance)

The feedback always appears in the sensor zone, never on a touched UI
element; the Press-Animation does not apply here.
