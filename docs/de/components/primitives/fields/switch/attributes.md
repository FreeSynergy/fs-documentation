# Switch - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `checked` | boolean | `false` | an oder aus? |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `label` | string | - | Beschriftungstext |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `switch` |

## Label-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `labelPosition` | enum | `right` | Position: `left`, `right` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
