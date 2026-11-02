# Multi-Finger Tap - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onMultiFingerTap` | function | - | Executed on Multi-Finger Tap |

## Detection Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `pointerCount` | number | `2` | Number of required fingers (2, 3, 4, 5 …) |
| `maxTouchDelay` | number | `100` | Max. time offset between the fingers touching down in ms |
| `tapThreshold` | number | `300` | Max. touch duration in ms |
| `moveTolerance` | number | `10` | Allowed movement in px |
| `minFingerDistance` | number | `20` | Minimum distance between fingers in px |

## Context Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `action` | string | `secondary` | Action type (`secondary`, `zoom`, `custom`) |
| `contextMenu` | node | - | Menu opened for `secondary` |
| `enabled` | boolean | `true` | Gesture active? |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hapticFeedback` | boolean | `false` | Vibration on the secondary action? |
| `ripple` | boolean | `true` | Ripple at each touch point? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Context menu button / long press as a substitute |
| `longPressEquivalent` | boolean | `true` | Does Long Press react with the same action? |
| `aria-label` | string | - | Description of the secondary action |
