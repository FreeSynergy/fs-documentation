# Modal - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `title` | string | - | Titel |
| `isOpen` | boolean | `false` | ist es geöffnet? |
| `onClose` | function | - | Ereignis beim Schließen |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `closable` | boolean | `true` | schließbar? |
| `overlayClosable` | boolean | `true` | schließt ein Klick auf das Overlay das Modal? |
| `keyboardClosable` | boolean | `true` | schließt ESC das Modal? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | wird beim Öffnen ausgeführt |
| `onClose` | function | wird beim Schließen ausgeführt |
| `onActionClick` | function | wird bei einem Klick auf eine Aktion ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `role` | string | - | ARIA-Rolle: `dialog` |
| `aria-modal` | boolean | `true` | Modal-Modus? |

## Aktionsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `confirmLabel` | string | `Save` | Beschriftung der Bestätigung |
| `cancelLabel` | string | `Cancel` | Beschriftung des Abbruchs |
| `onConfirm` | function | - | wird bei Bestätigung ausgeführt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
