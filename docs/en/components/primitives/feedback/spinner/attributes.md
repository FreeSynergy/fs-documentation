# Spinner - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `track` | boolean | `true` | background ring visible |
| `speed` | number | `1` | revolutions per second |
| `text` | string | `null` | visible accompanying text (variant `mit-text`) |
| `inline` | boolean | `false` | size fitted to the text line |

## Events

No events are used; a spinner is display only.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | only needed when the spinner names an action ("Saving") |
| `role` | string | `status` |
| – | – | the **waiting area** gets `aria-busy="true"`, not the spinner alone |

## Inherited from

`id`, `visible`, `size`, `theme`, `state`, `animation`, `aria-*` →
[base component](../../basics/base.md)
