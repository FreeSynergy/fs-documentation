# Multi-Finger Long Press - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onMultiFingerLongPress` | function | - | Executed on Multi-Finger Long Press |
| `onMultiFingerLongPressMove` | function | - | Movement during the held press |
| `onMultiFingerLongPressEnd` | function | - | The fingers were lifted |

## Threshold Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `longPressThreshold` | number | `500` | Hold time in ms until detection |
| `pointerCount` | number | `2` | Required number of fingers (from 2) |
| `moveTolerance` | number | `10` | Allowed movement in px |
| `maxTouchDelay` | number | `100` | Max. time offset when touching down in ms |

## Selection Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `extendSelection` | boolean | `false` | Extend the selection by movement? |
| `multiSelect` | boolean | `false` | Activate multi-select mode afterwards? |
| `dragAfterHold` | boolean | `false` | Allow a drag start after holding? |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hapticFeedback` | boolean | `true` | Vibration when the threshold is reached? |
| `progressRing` | boolean | `false` | Show a progress ring up to the threshold? |
| `contextMenu` | node | - | Menu that appears after holding |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Single-finger long press or button as a substitute (WCAG 2.5.1) |
| `longPressEquivalent` | boolean | `true` | Does a single-finger long press trigger the same action? |
