# Toast - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `type` | enum | `info` | Typ: `info`, `success`, `warning`, `error` |
| `title` | string | - | Titel |
| `message` | string | - | Nachricht |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `autoDismiss` | boolean | `true` | Automatisch schließen? |
| `dismissDelay` | number | `3000` | Verzögerung in ms |
| `closable` | boolean | `true` | Schließbar? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Positionierung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `position` | enum | `top-right` | Position: `top-right`, `bottom-right`, `top-left`, `bottom-left`, `center` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `alert` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onDismiss` | function | Wird beim Auto-Schließen ausgeführt |

## Action-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `actionLabel` | string | Aktion-Label |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |
