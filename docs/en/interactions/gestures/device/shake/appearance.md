# Shake - Appearance

## Basic Layout

A shake is a quick back-and-forth movement of the device or element.

## Visual Feedback

```
┌─────────────────────────────────────────┐
│                                         │
│        ┌───┐                            │
│   ←──  │ □ │  ──→  ←──  ──→            │
│        └───┘                            │
│  Movement around the starting position  │
└─────────────────────────────────────────┘
```

## Feedback Options

| Option | Description |
|--------|-------------|
| **Wiggle** | Element tilts slightly back and forth |
| **Translate** | Element shifts horizontally |
| **Haptic** | Vibration on mobile devices |
| **Error Color** | Red border tint on invalid input |
| **None** | No feedback, callback only |

## Amplitude

| Intensity | Shift | Usage |
|-----------|-------|-------|
| Light | 2–4px | Confirmation |
| Medium | 5–10px | Standard feedback |
| Strong | 10–20px | Error, warning |

## Duration

- Typical: 300–1000ms
- Feedback animation: 300–500ms

## Difference from Swipe

- Swipe: one movement in one direction
- Shake: several movements back and forth
