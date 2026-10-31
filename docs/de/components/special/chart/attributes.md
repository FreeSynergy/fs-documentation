# Chart - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `data` | array[] | - | Array von Daten |
| `type` | string | `line` | Typ: `line`, `bar`, `pie`, `doughnut`, `scatter`, `radar` |

## Data-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `labels` | array[] | Labels |
| `values` | array[] | Werte |
| `colors` | array[] | Farben |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `interactive` | boolean | `true` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `img` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird beim Klick ausgeführt |
| `onHover` | function | Wird beim Hover ausgeführt |
| `onDataChange` | function | Wird bei Datenänderung ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showLegend` | boolean | `true` | Legende anzeigen? |
| `showTooltip` | boolean | `true` | Tooltip anzeigen? |
| `showGrid` | boolean | `true` | Gitter anzeigen? |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `1000` | Dauer in ms |
