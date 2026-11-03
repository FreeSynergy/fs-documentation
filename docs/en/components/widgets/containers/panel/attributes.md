# Panel - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | string | - | title |
| `content` | string/node | - | content |
| `footer` | string/node | - | footer content |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `collapsible` | boolean | `false` | collapsible? |
| `draggable` | boolean | `false` | movable? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `responsive` | boolean | `true` | responsive layout? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onCollapsibleToggle` | function | runs when collapsing |
| `onDrag` | function | runs while dragging |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `region` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../../primitives/basics/base.md)
