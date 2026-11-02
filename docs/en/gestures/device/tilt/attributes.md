# Tilt - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onTilt` | function | - | Executed on a change of inclination |
| `onTiltStart` | function | - | The dead zone was left |
| `onTiltEnd` | function | - | Device back in its resting position |

## Sensor Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `axes` | string | `beta` \| `gamma` \| `both` | Axes being evaluated |
| `deadZone` | number | `3` | Degrees until movement counts |
| `maxAngle` | number | `45` | Angle mapped to 100% input |
| `smoothing` | number | `0.2` | Smoothing 0–1 against wobbling |
| `sampleRate` | number | `60` | Sensor events per second |

## Control Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `mode` | string | `absolute` \| `relative` | Resting position as origin, or drift allowed? |
| `inverted` | boolean | `false` | Reverse the direction |
| `parallaxDepth` | number | `0` | Parallax depth in px (background offset) |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `levelIndicator` | boolean | `false` | Show a level indicator? |
| `hapticFeedback` | boolean | `false` | Vibration at the limits? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Buttons/sliders as a substitute (WCAG 2.5.4) |
| `disableTilt` | boolean | `false` | Sensor control fully switchable off? |
| `respectReducedMotion` | boolean | `true` | Disable parallax on reduced motion? |
