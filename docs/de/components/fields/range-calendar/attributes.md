# Range Calendar (Bereichskalender) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `from` | date | `null` | Beginn des Zeitraums |
| `to` | date | `null` | Ende des Zeitraums |
| `presets` | array[] | `[7, 30, quartal]` | vorgegebene Bereiche |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `months` | number | `2` | sichtbare Monate |
| `minRange` | number | `1` | kürzeste Länge in Tagen |
| `maxRange` | number | `365` | längste Länge in Tagen |
| `min` | date | `null` | frühester Tag |
| `max` | date | `null` | spätester Tag |
| `showCount` | boolean | `true` | Tagesanzahl anzeigen |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChange` | function | Zeitraum geändert |
| `onPreset` | function | vorgegebener Bereich gewählt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `dialog` mit `grid` |
| `aria-selected` | boolean | Tage im Zeitraum |
| `label` | string | Pflicht, z. B. „Zeitraum“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
