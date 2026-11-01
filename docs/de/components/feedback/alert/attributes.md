# Alert - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `type` | enum | `info` | Typ: `info`, `success`, `warning`, `error` |
| `title` | string | - | Titel |
| `message` | string | - | Nachricht |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `dismissible` | boolean | `false` | Schließbar? |
| `closable` | boolean | `false` | Schließbar? |
| `sticky` | boolean | `true` | Fixiert oben? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onAction` | function | Wird bei Aktion ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `alert` |

## Action-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `actionLabel` | string | Aktion-Label |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |
| `actionLabel2` | string | Zweite Aktion-Label |
| `onActionClick2` | function | Wird bei zweiter Aktion-Klick ausgeführt |

## Icon-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
