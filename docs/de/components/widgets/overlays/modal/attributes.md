# Modal (Modaler Dialog) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `title` | string | - | Titel |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onClose` | function | - | Event beim Schließen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `closable` | boolean | `true` | Schließbar? |
| `overlayClosable` | boolean | `true` | Klick auf Overlay schließt? |
| `keyboardClosable` | boolean | `true` | ESC schließt? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `role` | string | - | ARIA-Rolle: `dialog` |
| `aria-modal` | boolean | `true` | Modal-Modus? |

## Action-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `confirmLabel` | string | `Speichern` | Bestätigungs-Label |
| `cancelLabel` | string | `Abbrechen` | Abbrech-Label |
| `onConfirm` | function | - | Wird bei Bestätigung ausgeführt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
