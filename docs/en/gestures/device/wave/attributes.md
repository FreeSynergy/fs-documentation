# Wave - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onWave` | function | - | Executed on Wave |
| `onWaveApproach` | function | - | The hand approaches the sensor |
| `onWavePattern` | function | - | Recognized pattern (`open`, `fist`, `swipe`) |

## Sensor Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `detectionRange` | number | `60` | Detection range in cm |
| `minDisplacement` | number | `20` | Min. hand movement in cm |
| `maxWaveTime` | number | `2000` | Time window for the movement in ms |
| `cooldown` | number | `3000` | Pause after detection in ms |

## Permission Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `requiresMotionPermission` | boolean | readonly | Sensor permission needed? |
| `userEnabled` | boolean | `false` | Off by default – the user must enable it |
| `privacyIndicator` | boolean | `true` | Show while the sensor is active? |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `countdownUI` | boolean | `true` | Show a countdown before answering? |
| `hapticFeedback` | boolean | `true` | Vibration on detection? |
| `soundFeedback` | boolean | `true` | Acoustic confirmation? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Buttons on the call/control dialog (WCAG 2.5.4) |
| `enabled` | boolean | `false` | Gesture switchable off, default off |
