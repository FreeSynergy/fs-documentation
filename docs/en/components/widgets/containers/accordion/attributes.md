# Accordion - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | array of accordion items |
| `activeItem` | string/number | - | active item |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `collapsible` | boolean | `true` | collapsible? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `300` | duration in ms |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onExpand` | function | runs when expanding |
| `onCollapse` | function | runs when collapsing |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `tablist` |

## Item attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `header` | string/node | header text |
| `content` | string/node | content |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../../primitives/basics/base.md)
