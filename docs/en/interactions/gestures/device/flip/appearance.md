# Flip - Appearance

## Basic Layout

The device turns around a horizontal axis; the UI shows the new mode as an icon
state, not as an animation on the device itself.

```
┌───────────────────────────────┐
│   📱 (display up)              │
│      │  Flip 180°             │
│      ▼                        │
│   📵 (display down)           │
│   Toast: "Do not disturb"     │
└───────────────────────────────┘
```

## Feedback Options

| Option | Description |
|--------|-------------|
| **Toast** | Short status message ("do not disturb active") |
| **Haptic** | Vibration when the reversal is detected |
| **Status Icon** | Mode icon in the status bar stays visible |
| **None** | Silent, only a state change |

## States

| State | Display |
|-------|---------|
| Normal | no icon |
| Turned over | struck-through bell / moon icon |
| Turned back | icon disappears (with `autoRevert`) |

## Duration

- Detection: after `holdTime` (typically 1s)
- Toast visibility: 2–3s

## Difference from Shake

- Flip: 180° turn, stable new state, usually "mute"
- Shake: back and forth, a one-off event, usually "undo"
