# Context Menu - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | array of menu items |
| `onSelect` | function | - | event on selection |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `closable` | boolean | `true` | closable? |
| `keyboardShortcuts` | boolean | `true` | keyboard shortcuts? |

## Presentation

| Attribute | Type | Description |
|-----------|------|-------------|
| `position` | object | { x, y } |
| `anchorEl` | DOM element | anchor element |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |
| `onItemClick` | function | runs on click |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `menu` |

## Item attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `label` | string | menu item label |
| `icon` | string | icon name |
| `danger` | boolean | dangerous action? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
