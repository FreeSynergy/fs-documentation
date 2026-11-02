# Rotate - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onRotate` | function | - | Executed on Rotate |

## Feedback Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `showAngle` | boolean | `false` | Show angle? |
| `rotateElement` | boolean | `true` | Element rotates? |

## Threshold Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `rotateThreshold` | number | `10` | Min. angle in degrees |
| `pointerCount` | number | `2` | Minimum number of participating fingers |
| `minAngle` | number | `-180` | Min. angle |
| `maxAngle` | number | `180` | Max. angle |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | Descriptive text |
| `role` | string | ARIA role: `slider` |
