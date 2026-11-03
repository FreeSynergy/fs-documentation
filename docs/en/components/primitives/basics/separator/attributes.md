# Separator - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `orientation` | enum | `horizontal` | `horizontal`, `vertical` |
| `variant` | enum | `horizontal` | `horizontal`, `vertical`, `mit-beschriftung`, `dekorativ`, `inset` |
| `label` | string | `null` | text centred in the line (horizontal only) |
| `inset` | number \| string | `0` | indent in px or percent |
| `spacing` | number | `8` | gap to the neighbours in px |

## Events

No events are used; a separator is display only.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `separator` for structural separation (menu groups, tool groups) |
| – | – | decorative divider lines get `aria-hidden="true"` |
| – | – | vertical dividers without structural effect are always `aria-hidden` |

## Inherited from

`id`, `visible`, `size`, `theme`, `aria-*` →
[base component](../base.md)
