# Elastic - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `overshoot` | number | `30` | Overshoot in % of the distance travelled |
| `schwingungen` | number | `2` | Number of after-oscillations until the position of rest |
| `achse` | string | `beide` | `x`, `y`, `skala` or `beide` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `600` | Duration including the decay in ms |
| `timingFunction` | string | `spring` | spring function, alternatively `cubic-bezier(...)` |
| `delay` | number | `0` | delayed start in ms |

## Spring attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `elasticity` | number | `0.6` | spring stiffness: 0 = stiff, 1 = very soft |
| `abklingfaktor` | number | `0.5` | decrease of the amplitude per oscillation (0–1) |
| `amplitude` | number | `auto` | max. overshoot in px (overrides `overshoot`) |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
