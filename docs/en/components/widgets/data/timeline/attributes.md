# Timeline - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `events` | array[] | - | array of event objects |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `interactive` | boolean | `false` | interactive? |

## Events
| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `date` | string | date |
| `title` | string | title |
| `description` | string | description |
| `icon` | string | icon name |

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `navigation` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
