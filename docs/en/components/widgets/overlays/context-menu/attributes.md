# Context Menu - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | Array von Menüpunkten |
| `onSelect` | function | - | event on selection |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `closable` | boolean | `true` | Schließbar? |
| `keyboardShortcuts` | boolean | `true` | Keyboard-Shortcuts? |

## Presentation

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `position` | object | { x, y } |
| `anchorEl` | DOM element | Anchor-Element |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |
| `onItemClick` | function | Wird beim Klick ausgeführt |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `menu` |

## Item attributes

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `id` | string | Eindeutige ID |
| `label` | string | Menüpunkt-Label |
| `icon` | string | Icon-Name |
| `danger` | boolean | Gefährliche Aktion? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
