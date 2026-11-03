# Repeater - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | array of item objects |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `interactive` | boolean | `false` | interactive? |
| `variant` | enum | `default` | style: `default`, `card`, `list` |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `list` |

## Item attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `title` | string | title |
| `content` | string/node | content |
| `image` | string | image URL |

## Filter attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `filter` | string | filter string |
| `onFilter` | function | filter function |

## Sort attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `sort` | string | sort field |
| `sortOrder` | enum | `asc`, `desc` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
