# Multi-Finger Swipe - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onMultiFingerSwipe` | function | - | Executed on Multi-Finger Swipe |
| `onMultiFingerSwipeStart` | function | - | Fingers touch down, movement begins |
| `onMultiFingerSwipeEnd` | function | - | Fingers lifted, direction is set |

## Detection Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `pointerCount` | number | `3` | Required number of fingers (from 2) |
| `syncWindow` | number | `150` | Common down window in ms |
| `swipeThreshold` | number | `80` | Min. distance in px |
| `direction` | string | `left`\|`right`\|`up`\|`down`\|`any` | Allowed direction |
| `maxDuration` | number | `800` | Max. duration of the gesture in ms |

## System Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `systemGesture` | boolean | `true` | The gesture belongs to system navigation? |
| `reservedByOS` | boolean | readonly | `true` when the OS captures the gesture globally |
| `action` | string | `task-switch` \| `workspace` \| `back` | Action of the gesture |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `previewCards` | boolean | `true` | Show preview cards of the targets? |
| `hapticFeedback` | boolean | `false` | Vibration when triggering? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Button/gesture with fewer fingers as a substitute |
| `reducedPointerFallback` | boolean | `false` | Allow a variant with fewer fingers? |
| `voiceOverMapping` | string | - | VoiceOver equivalent, if one exists |
