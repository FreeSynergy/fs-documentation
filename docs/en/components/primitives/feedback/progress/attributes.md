# Progress - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | number | `0` | current progress |
| `min` | number | `0` | lower bound |
| `max` | number | `100` | upper bound |
| `indeterminate` | boolean | `false` | value unknown, animation running |

## Presentation

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `linear` | `linear`, `circular` |
| `showLabel` | boolean | `false` | show the percentage or a text |
| `strokeWidth` | number | - | bar height or ring weight |
| `status` | enum | `active` | `active`, `success`, `error` |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onComplete` | function | value reaches `max` |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `progressbar` |
| `aria-valuenow` | number | `value` |
| `aria-valuemin` / `aria-valuemax` | number | `min` / `max` |
| `aria-busy` | boolean | `true` as long as `indeterminate` |
| `aria-label` | string | what the progress refers to |

## Inherited from

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `animation`, `aria-*` →
[base component](../../basics/base.md)
