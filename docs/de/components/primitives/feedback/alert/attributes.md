# Alert – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `type` | enum | `info` | Typ: `info`, `success`, `warning`, `error` |
| `title` | string | - | Titel |
| `message` | string | - | Meldung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `dismissible` | boolean | `false` | schließbar? |
| `closable` | boolean | `false` | schließbar? |
| `sticky` | boolean | `true` | oben fixiert? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onClose` | function | läuft beim Schließen |
| `onAction` | function | läuft bei der Aktion |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle: `alert` |

## Aktions-Attribute

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `actionLabel` | string | Beschriftung der Aktion |
| `onActionClick` | function | läuft beim Klick auf die Aktion |
| `actionLabel2` | string | Beschriftung der zweiten Aktion |
| `onActionClick2` | function | läuft beim Klick auf die zweite Aktion |

## Icon-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
