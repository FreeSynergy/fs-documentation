# Drawer (Seitenleiste) - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `title` | string | - | Titel |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onClose` | function | - | Event beim Schließen |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `position` | enum | `left` | Position: `left`, `right`, `top`, `bottom` |
| `closable` | boolean | `true` | Schließbar? |
| `overlay` | boolean | `true` | Overlay anzeigen? |
| `overlayClosable` | boolean | `true` | Klick auf Overlay schließt? |

## Presentation

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `300` | duration in ms |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `dialog` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
