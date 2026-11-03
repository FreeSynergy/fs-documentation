# Skeleton - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `shape` | enum | `text` | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` |
| `width` | number \| string | - | width in px or percent |
| `height` | number | - | height in px |
| `lines` | number | `1` | number of bars for `text` |

## Presentation

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | enum | `shimmer` | `shimmer`, `pulse`, `none` |
| `round` | boolean | `true` | rounded corners |

## Events

No events are used; a skeleton is display only.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-hidden` | boolean | always `true` – the placeholder carries no information |
| – | – | the surrounding area gets `aria-busy="true"` |

## Inherited from

`id`, `visible`, `size`, `theme`, `rounded`, `animation`, `aria-*` →
[base component](../../basics/base.md)
