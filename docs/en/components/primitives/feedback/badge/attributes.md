# Badge - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string \| number | - | the displayed text or count |
| `max` | number | `99` | ceiling, above that "99+" |
| `dot` | boolean | `false` | only a dot instead of a surface |
| `showZero` | boolean | `false` | show zero or hide it |

## Presentation

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `status` | `status`, `counter`, `dot`, `outline` |
| `status` | enum | `neutral` | `neutral`, `info`, `success`, `warning`, `error` |

## Events

No events are used; a badge is display only.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | required when `value` alone is not understandable ("3 new messages") |
| `aria-live` | string | `polite` when the count changes without user action |
| `role` | string | `status` for counts, otherwise no interactive role |

## Inherited from

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `animation`, `gesture`, `aria-*` →
[base component](../../basics/base.md)
