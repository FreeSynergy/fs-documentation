# Chart - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `data` | array[] | - | Array mit Daten |
| `type` | string | `line` | Typ: `line`, `bar`, `pie`, `doughnut`, `scatter`, `radar` |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `true` | interaktiv? |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showLegend` | boolean | `true` | Legende anzeigen? |
| `showTooltip` | boolean | `true` | Tooltip anzeigen? |
| `showGrid` | boolean | `true` | Gitter anzeigen? |

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `1000` | Dauer in ms |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Hover ausgeführt |
| `onDataChange` | function | wird ausgeführt, wenn sich die Daten ändern |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `img` |

## Daten-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `labels` | array[] | Beschriftungen |
| `values` | array[] | Werte |
| `colors` | array[] | Farben |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
