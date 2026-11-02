# Edge Swipe - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onEdgeSwipe` | function | - | Executed on Edge Swipe |
| `onEdgeSwipeStart` | function | - | Executed at the start |
| `onEdgeSwipeProgress` | function | - | Progress 0–1 while swiping |
| `onEdgeSwipeCancel` | function | - | The swipe was cancelled |

## Edge Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `edge` | string | `left` \| `right` \| `top` \| `bottom` | Active edge |
| `edgeSize` | number | `24` | Width of the edge zone in px |
| `swipeThreshold` | number | `50` | From this distance the gesture counts as completed |
| `predictive` | boolean | `true` | Evaluate the predictive path (iOS/Android)? |

## Navigation Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `action` | string | `back` \| `panel` \| `home` | Action of the edge swipe |
| `interactive` | boolean | `true` | Transition follows the finger (interactive navigating)? |
| `cancelOnReturn` | boolean | `true` | Pulling back below the threshold cancels |
| `enabled` | boolean | `true` | Gesture active? |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `shadowPreview` | boolean | `true` | Pre-shadow of the view underneath |
| `hapticFeedback` | boolean | `false` | Vibration when the threshold is exceeded |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Back button / keyboard shortcut as a substitute |
| `aria-label` | string | - | Description of the edge action |
| `respectReducedMotion` | boolean | `true` | Transition without animation? |
