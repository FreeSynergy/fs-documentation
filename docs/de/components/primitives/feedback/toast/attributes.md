# Toast - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `type` | enum | `info` | Typ: `info`, `success`, `warning`, `error` |
| `title` | string | - | Titel |
| `message` | string | - | Meldungstext |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `autoDismiss` | boolean | `true` | automatisch schließen? |
| `dismissDelay` | number | `3000` | Verzögerung in ms |
| `closable` | boolean | `true` | schließbar? |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `position` | enum | `top-right` | Position: `top-right`, `bottom-right`, `top-left`, `bottom-left`, `center` |

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClose` | function | wird beim Schließen ausgeführt |
| `onDismiss` | function | wird beim automatischen Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `alert` |

## Aktions-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `actionLabel` | string | Beschriftung der Aktion |
| `onActionClick` | function | wird ausgeführt, wenn die Aktion angeklickt wird |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
