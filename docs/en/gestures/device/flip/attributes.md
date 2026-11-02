# Flip - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onFlip` | function | - | Executed when turning over |
| `onFlipBack` | function | - | The device was turned back |
| `onFlipStart` | function | - | The turning movement begins |

## Sensor Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `flipAngle` | number | `150` | From which angle (degrees) does the position count as turned over? |
| `holdTime` | number | `1000` | Min. time in the turned-over position in ms |
| `maxFlipTime` | number | `2000` | Max. duration of turning over in ms |
| `requireProximity` | boolean | `false` | Also check the proximity sensor? |

## Action Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `action` | string | `mute` \| `dnd` \| `custom` | Action on flip |
| `autoRevert` | boolean | `true` | The action ends when turning back? |
| `onlyWhileRinging` | boolean | `false` | Active only for an incoming call? |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hapticFeedback` | boolean | `true` | Vibration on activation? |
| `soundFeedback` | boolean | `false` | Confirmation sound? |
| `confirmationToast` | boolean | `true` | "Do not disturb active" message? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Switch/button as an equivalent route (WCAG 2.5.4) |
| `enabled` | boolean | `true` | Gesture switchable off? |
