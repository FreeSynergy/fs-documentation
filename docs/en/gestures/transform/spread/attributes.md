# Spread - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onSpread` | function | - | Executed on Spread |

## Feedback Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `showZoomFactor` | boolean | `false` | Show zoom factor? |
| `scaleElement` | boolean | `true` | Element scales? |

## Threshold Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `spreadThreshold` | number | `20` | Min. distance in px |
| `pointerCount` | number | `2` | Minimum number of participating fingers |
| `minScale` | number | `0.5` | Min. zoom factor |
| `maxScale` | number | `2.0` | Max. zoom factor |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | Descriptive text |
| `role` | string | ARIA role: `slider` |
