# Pull to Refresh - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onRefresh` | function | - | Executed after releasing in the armed state |
| `onPullProgress` | function | - | Progress 0–1 while pulling |
| `onArm` | function | - | Threshold reached (armed) |
| `refreshing` | boolean | `false` | Loading state (indicator visible until `false`) |

## Trigger Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `edge` | string | `top` \| `bottom` \| `left` \| `right` | Start edge of the pull |
| `triggerDistance` | number | `80` | Distance in px until armed |
| `maxPull` | number | `200` | Max. deflection in px |
| `rubberBand` | boolean | `true` | Resistance with a rubber-band curve? |
| `enabled` | boolean | `true` | Gesture active? |

## Indicator Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `indicatorStyle` | string | `spinner` \| `progress` \| `custom` | Appearance of the indicator |
| `indicatorColor` | color | Accent color | Color of the indicator |
| `holdDuringRefresh` | boolean | `true` | List locked while loading? |
| `autoHideDelay` | number | `300` | Hide delay after completion in ms |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hapticFeedback` | boolean | `true` | Vibration when it locks in? |
| `releaseLabel` | string | "Release to refresh" | Text in the armed state |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `refreshButton` | boolean | `true` | Explicit refresh button as an alternative? |
| `aria-live` | string | `polite` | Announce status changes |
| `respectReducedMotion` | boolean | `true` | Without rubber-band/rotation animation? |
