# Range Calendar - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `from` | date | `null` | Beginn des Zeitraums |
| `to` | date | `null` | Ende des Zeitraums |
| `presets` | array[] | `[7, 30, quarter]` | Schnellauswahl-Bereiche |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `months` | number | `2` | sichtbare Monate |
| `minRange` | number | `1` | kürzeste Länge in Tagen |
| `maxRange` | number | `365` | längste Länge in Tagen |
| `min` | date | `null` | frühester Tag |
| `max` | date | `null` | spätester Tag |
| `showCount` | boolean | `true` | Anzahl der Tage anzeigen |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChange` | function | Zeitraum wurde geändert |
| `onPreset` | function | ein Schnellauswahl-Bereich wurde gewählt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `dialog` mit `grid` |
| `aria-selected` | boolean | Tage innerhalb des Zeitraums |
| `label` | string | Pflicht, z. B. „Zeitraum“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
