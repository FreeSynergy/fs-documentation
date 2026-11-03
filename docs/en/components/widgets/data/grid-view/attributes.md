# Grid View - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | array of item objects |
| `columns` | number | 3 | number of columns |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `interactive` | boolean | `false` | interactive? |

## Presentation
| Attribute | Type | Default | Description |
|---|---|---|---|
| `gap` | number | 16 | spacing between items |

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `responsive` | boolean | `true` | responsive layout? |
| `columns` | object | - | { xs: 1, sm: 2, md: 3, lg: 4 } |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `grid` |

## Item attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `title` | string | title |
| `content` | string/node | content |
| `image` | string | image URL |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
