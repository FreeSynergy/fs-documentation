# Collapse - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `collapse` | Name of the animation |
| `dimension` | string | `height` | `height`, `width` or `both` |
| `startHeight` | string \| number | `auto` | Starting height (`auto` = measured content height) |
| `endHeight` | number | `0` | Target height in px (standard 0) |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Duration in ms |
| `timingFunction` | string | `ease-in-out` | symmetrical acceleration and braking |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Hold the end state (height 0) until the layout is reflowed |
| `onAnimateEnd` | function | - | Runs after the element has closed |

## Height attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `overflow` | string | `hidden` | Clip the content during the animation |
| `includePadding` | boolean | `true` | Pull in padding and margins as well |
| `minHeight` | number | `0` | Lower bound, if it does not close entirely |
| `detachAfter` | boolean | `true` | Remove the element from the DOM after closing |
| `staggerChildren` | number | `0` | Collapse child elements one after another in ms steps |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `ariaExpandedSync` | boolean | `true` | Set `aria-expanded` in sync with the state |
