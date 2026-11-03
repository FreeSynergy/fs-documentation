# List View - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | array of item objects |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `simple` | style: `simple`, `with-icons`, `with-avatars`, `with-badges`, `with-actions` |
| `interactive` | boolean | `false` | interactive? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcons` | boolean | `false` | show icons? |
| `showAvatars` | boolean | `false` | show avatars? |
| `showBadges` | boolean | `false` | show badges? |
| `showActions` | boolean | `false` | show actions? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |
| `onActionClick` | function | runs on clicking an action |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `list` |

## Item attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `label` | string | label text |
| `icon` | string | icon name |
| `avatar` | string | avatar URL |
| `badge` | string/number | badge text |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
