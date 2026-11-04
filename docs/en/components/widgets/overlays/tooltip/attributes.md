# Tooltip - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | string | - | displayed text, no HTML and no actions |
| `placement` | enum | `auto` | `top`, `right`, `bottom`, `left`, `auto` |
| `open` | boolean | `null` | controlled visibility (`null` = automatic) |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `trigger` | enum | `hover` | `hover`, `focus`, `longpress` |
| `delay` | number | `400` | delay before fading in, in ms |
| `hideDelay` | number | `100` | delay before fading out, in ms |

## Presentation

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `arrow` | boolean | `true` | arrow pointing at the reference element |
| `maxWidth` | number | `240` | maximum width in px |
| `offset` | number | `8` | distance to the element in px |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onShow` | function | the tooltip was shown |
| `onHide` | function | the tooltip was hidden |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `tooltip` |
| – | – | the reference element gets `aria-describedby` pointing at the tooltip |
| – | – | interactive content is not allowed |

## Inherited from

`id`, `visible`, `size`, `theme`, `rounded`, `animation`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
