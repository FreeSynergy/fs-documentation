# Split View - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `leftContent` | node/string | - | left content |
| `rightContent` | node/string | - | right content |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `collapsible` | boolean | `false` | collapsible? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `responsive` | boolean | `true` | responsive layout? |
| `stackBreakpoint` | number | `768` | breakpoint for stacking |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onResize` | function | runs when resizing |
| `onCollapse` | function | runs when collapsing |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `region` |

## Resizing attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `minWidth` | number | `200` | minimum width |
| `maxWidth` | number | `500` | maximum width |
| `defaultWidth` | number | `250` | standard width |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
