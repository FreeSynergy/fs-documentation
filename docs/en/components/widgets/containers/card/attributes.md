# Card - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | string | - | title |
| `subtitle` | string | - | subtitle |
| `content` | string/node | - | content |
| `actions` | array[] | - | array of action objects |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `default` | style: `default`, `flat`, `outlined`, `elevated` |
| `interactive` | boolean | `false` | interactive? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `responsive` | boolean | `true` | responsive layout? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onActionClick` | function | runs when an action is clicked |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `region` |

## Media attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `media` | string/object | - | image/thumbnail |
| `mediaPosition` | enum | `top` | position: `top`, `bottom`, `left` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../../primitives/basics/base.md)
