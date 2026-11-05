# Press - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `press` | Name of the animation |
| `onPressStart` | function | - | Runs when the element goes down |
| `onPressEnd` | function | - | Runs after the return |
| `enabled` | boolean | `true` | Feedback while the pressed state holds |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `120` | Duration of going down in ms |
| `timingFunction` | string | `ease-out` | react at once, land softly |
| `delay` | number | `0` | no run-up, the reaction is immediate |
| `fillMode` | string | `forwards` | the pressed state stays until release |

## Pressure attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `pressScale` | number | `0.97` | Target size in the pressed state |
| `pressOffsetY` | number | `1` | additional lowering downwards in px |
| `pressOpacity` | number | `0.9` | slight dimming in the pressed state |
| `releaseScale` | number | `1` | Final size after release |
| `releaseOvershoot` | number | `1` | a short rebound past 1 (1 = none) |
| `nurBeiZeiger` | boolean | `false` | animate only with a mouse, not with touch |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `farbe` | the size change goes away, the state colour stays |
