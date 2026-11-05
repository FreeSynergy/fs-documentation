# Expand - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `expand` | Name of the animation |
| `dimension` | string | `height` | `height`, `width` or `both` |
| `startHeight` | number | `0` | Starting height in px |
| `endHeight` | string \| number | `auto` | Target height (`auto` = measured content height) |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `300` | Duration in ms |
| `timingFunction` | string | `ease-in-out` | usually symmetrical for height changes |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `both` | Hold the start and end state outside the runtime |
| `onAnimateEnd` | function | - | Runs after the element is fully open |

## Height attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `overflow` | string | `hidden` | Content not yet visible is clipped away |
| `measureMode` | string | `scroll` | Measuring the target height: `scroll`, `explicit`, `lazy` |
| `maxHeight` | number | `none` | Upper bound in px, above it a scroll area |
| `innerFade` | number | `0` | Additionally fade in child elements (0 = off) |
| `deferRender` | boolean | `false` | Render the content only when opening |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `focusOnOpen` | boolean | `false` | Move focus into the new content after opening |
