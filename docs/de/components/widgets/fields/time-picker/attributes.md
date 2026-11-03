# Time Picker (Zeitauswahl) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | time | `null` | gewählte Uhrzeit |
| `step` | number | `15` | Raster in Minuten |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `min` | time | `00:00` | früheste Zeit |
| `max` | time | `23:59` | späteste Zeit |
| `hour12` | boolean | `false` | 12-Stunden-Darstellung |
| `blocked` | array[] | `[]` | Zeiten, die nicht wählbar sind |
| `freeInput` | boolean | `true` | Tippen erlauben, auf Raster korrigieren |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChange` | function | Uhrzeit geändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `listbox`, Einträge `option` |
| `aria-selected` | boolean | gewählte Zeit |
| `label` | string | Pflicht, z. B. „Beginn“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
