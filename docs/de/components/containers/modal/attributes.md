# Modal (Modaler Dialog) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `title` | string | - | Titel |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onClose` | function | - | Event beim Schließen |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `medium` | Größe: `small`, `medium`, `large`, `fullscreen` |
| `closable` | boolean | `true` | Schließbar? |
| `overlayClosable` | boolean | `true` | Klick auf Overlay schließt? |
| `keyboardClosable` | boolean | `true` | ESC schließt? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `dialog` |
| `aria-modal` | boolean | `true` | Modal-Modus? |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |

## Action-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `confirmLabel` | string | `Speichern` | Bestätigungs-Label |
| `cancelLabel` | string | `Abbrechen` | Abbrech-Label |
| `onConfirm` | function | Wird bei Bestätigung ausgeführt |
