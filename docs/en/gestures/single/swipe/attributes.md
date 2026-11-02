# Swipe - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onSwipe` | function | - | Executed on Swipe |

## Feedback Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `showDirection` | boolean | `true` | Show arrow? |
| `showVelocity` | boolean | `false` | Show velocity? |

## Threshold Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `swipeThreshold` | number | `50` | Min. distance in px |
| `maxTime` | number | `300` | Max. time in ms |

## Direction Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `allowedDirections` | array[] | `[left, right, up, down]` | Allowed directions |
| `requireDirection` | boolean | `true` | Direction required? |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | Descriptive text |
| `role` | string | ARIA role: `slider` |
