# Multi-Finger Swipe - Appearance

## Basic Layout

Several fingers swipe together; the level changes with a card preview of the
neighbouring pages/apps.

```
┌─────────────────────────────────────────┐
│   ●   ●   ●                             │
│    ╲  │  ╱     → movement together      │
│     ▼ ▼ ▼                               │
│  ┌────┐ ┌────┐ ┌────┐                   │
│  │App1│▶│App2│ │App3│  ← card switch    │
│  └────┘ └────┘ └────┘                   │
└─────────────────────────────────────────┘
```

## Phases

| Phase | Description |
|-------|-------------|
| **Grab** | Fingers detected, preview cards appear |
| **Swipe** | Cards move with the fingers (interactive) |
| **Switch** | Above the threshold: the target becomes active, otherwise spring back |

## Feedback Options

| Option | Description |
|--------|-------------|
| **Card Preview** | Neighbouring levels as cards left/right |
| **Dimming** | The current level dims during the change |
| **Haptic** | Vibration at the switch point |

## Duration

- Interactive: follows the fingers, 150–500ms
- Switch animation: 250–400ms

## Difference from Swipe

- Swipe: content inside the app, one finger
- Multi-Finger Swipe: app/workspace level, several fingers, card preview
