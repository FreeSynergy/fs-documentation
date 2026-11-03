# Modal (Modaler Dialog) - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `title` | string | - | Titel |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onClose` | function | - | Event beim Schließen |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `closable` | boolean | `true` | Schließbar? |
| `overlayClosable` | boolean | `true` | Klick auf Overlay schließt? |
| `keyboardClosable` | boolean | `true` | ESC schließt? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |

## Accessibility

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `role` | string | - | ARIA role: `dialog` |
| `aria-modal` | boolean | `true` | Modal-Modus? |

## Action-Attribute

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `confirmLabel` | string | `Speichern` | Bestätigungs-Label |
| `cancelLabel` | string | `Abbrechen` | Abbrech-Label |
| `onConfirm` | function | - | Wird bei Bestätigung ausgeführt |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
