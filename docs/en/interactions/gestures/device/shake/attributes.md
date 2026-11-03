# Shake - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onShake` | function | - | Executed on Shake |
| `onShakeStart` | function | - | Executed at the start of the Shake |
| `onShakeEnd` | function | - | Executed at the end of the Shake |

## Feedback Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `shakeAnimation` | boolean | `true` | Show shake/wiggle feedback on the element? |
| `confirmBeforeAction` | boolean | `true` | Confirm the action before executing it? |
| `hapticFeedback` | boolean | `true` | Vibration on detection? |
| `soundFeedback` | boolean | `false` | Sound on detection? |

## Threshold Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `shakeThreshold` | number | `15` | Min. acceleration (m/s²) or movement in px |
| `minShakes` | number | `2` | Min. number of direction changes |
| `maxTime` | number | `1000` | Time window for Shake in ms |
| `cooldown` | number | `1000` | Pause after Shake in ms (prevents double triggering) |

## Direction Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `axis` | string | `x` \| `y` \| `xy` — axis of the movement |
| `requireAxis` | boolean | `true` | Axis required? |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | Descriptive text |
| `role` | string | ARIA role: `application` |
| `alternativeAction` | function | Equivalent action via button/keyboard |
| `respectReducedMotion` | boolean | `true` | Disable feedback with `prefers-reduced-motion`? |
