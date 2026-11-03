# Toast - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `type` | enum | `info` | Typ: `info`, `success`, `warning`, `error` |
| `title` | string | - | Titel |
| `message` | string | - | Nachricht |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `autoDismiss` | boolean | `true` | Automatisch schließen? |
| `dismissDelay` | number | `3000` | Verzögerung in ms |
| `closable` | boolean | `true` | Schließbar? |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `position` | enum | `top-right` | Position: `top-right`, `bottom-right`, `top-left`, `bottom-left`, `center` |

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onDismiss` | function | Wird beim Auto-Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `alert` |

## Action-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `actionLabel` | string | Aktion-Label |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
