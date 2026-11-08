# Time Picker - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | time | `null` | gewählte Uhrzeit |
| `step` | number | `15` | Raster in Minuten |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `min` | time | `00:00` | früheste Uhrzeit |
| `max` | time | `23:59` | späteste Uhrzeit |
| `hour12` | boolean | `false` | Anzeige im 12-Stunden-Format |
| `blocked` | array[] | `[]` | Uhrzeiten, die nicht gewählt werden können |
| `freeInput` | boolean | `true` | Eingabe per Tippen erlauben, auf das Raster korrigieren |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChange` | function | Uhrzeit wurde geändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `listbox`, Einträge `option` |
| `aria-selected` | boolean | gewählte Uhrzeit |
| `label` | string | Pflicht, z. B. „Start“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
