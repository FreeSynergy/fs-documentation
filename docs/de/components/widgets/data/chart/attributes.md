# Chart - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `data` | array[] | - | Array von Daten |
| `type` | string | `line` | Typ: `line`, `bar`, `pie`, `doughnut`, `scatter`, `radar` |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `true` | Interaktiv? |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showLegend` | boolean | `true` | Legende anzeigen? |
| `showTooltip` | boolean | `true` | Tooltip anzeigen? |
| `showGrid` | boolean | `true` | Gitter anzeigen? |

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `1000` | Dauer in ms |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |
| `onDataChange` | function | Wird bei Datenänderung ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `img` |

## Data-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `labels` | array[] | Labels |
| `values` | array[] | Werte |
| `colors` | array[] | Farben |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
