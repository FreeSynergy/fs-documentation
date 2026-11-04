# Modal - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | string | - | title |
| `isOpen` | boolean | `false` | is it open? |
| `onClose` | function | - | event on closing |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `closable` | boolean | `true` | closable? |
| `overlayClosable` | boolean | `true` | does a click on the overlay close it? |
| `keyboardClosable` | boolean | `true` | does ESC close it? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |
| `onActionClick` | function | runs on an action click |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `role` | string | - | ARIA role: `dialog` |
| `aria-modal` | boolean | `true` | modal mode? |

## Action attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `confirmLabel` | string | `Save` | confirm label |
| `cancelLabel` | string | `Cancel` | cancel label |
| `onConfirm` | function | - | runs on confirmation |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
