# Pinch - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onPinch` | function | - | Executed on Pinch |

## Feedback Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `showZoomFactor` | boolean | `false` | Show zoom factor? |
| `scaleElement` | boolean | `true` | Element scales? |

## Threshold Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `pinchThreshold` | number | `20` | Min. distance in px |
| `pointerCount` | number | `2` | Minimum number of participating fingers |
| `minScale` | number | `0.5` | Min. zoom factor |
| `maxScale` | number | `2.0` | Max. zoom factor |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | Descriptive text |
| `role` | string | ARIA role: `slider` |
