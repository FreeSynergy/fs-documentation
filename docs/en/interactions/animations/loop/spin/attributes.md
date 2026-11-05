# Spin - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the rotation starts |
| `onCycle` | function | - | Runs after each full revolution |
| `onAnimateEnd` | function | - | Runs when the rotation stops |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `1000` | Duration of one revolution in ms |
| `timingFunction` | string | `linear` | an even speed without jerking |
| `iterationCount` | number \| `infinite` | `infinite` | endless loop until stopped |
| `playState` | string | `running` | `running` or `paused` (e.g. on a tab change) |

## Rotation attributes (continuous running)

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `spinDirection` | string | `cw` | `cw` = clockwise, `ccw` = counter-clockwise |
| `arcSweep` | number | `270` | visible arc in degrees (360 = full disc) |
| `pauseWhenHidden` | boolean | `true` | pause the rotation when the element is not visible? |
| `stopOnTaskEnd` | boolean | `true` | end the rotation automatically when the task ends? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text, e.g. "Loading" |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `role` | string | - | `status` – also output the progress as text |
