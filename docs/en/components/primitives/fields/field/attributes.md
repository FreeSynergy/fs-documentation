# Field - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md). The enclosed field brings its own attributes.
The inherited `label` is passed on by the wrapper to the field.

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `for` | string | - | `id` of the enclosed field (required, except when nested) |
| `help` | string | `null` | help text below the field |
| `error` | string | `null` | error message; set ⇒ error state |
| `required` | boolean | `false` | required-field marking with text |

## Presentation

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `vertikal` | `vertikal`, `horizontal`, `inline` |
| `optional` | boolean | `false` | the word "optional" instead of a required marking |
| `errorIcon` | boolean | `true` | icon before the error message |
| `counter` | boolean | `false` | character counter (value taken from the field) |
| `labelWidth` | number | `140` | label width for `horizontal` in px |

## Events

No own events are used; the field produces the events.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `group` |
| – | – | help text and error are linked to the field via `aria-describedby` |
| – | – | `required` sets `aria-required` on the field |
| – | – | errors additionally via `aria-invalid` on the field |

## Inherited from

`id`, `visible`, `size`, `theme`, `state`, `animation`, `aria-*` →
[base component](../../basics/base.md)
