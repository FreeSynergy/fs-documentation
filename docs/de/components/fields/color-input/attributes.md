# Color Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Farbe) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Placeholder-Text |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `palette` | Icon-Name |
| `formats` | array[] | `['hex', 'rgb', 'hsl']` | Farbformate |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen des Pickers ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `color` |

## Picker-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showAlpha` | boolean | `false` | Alpha-Kanal anzeigen? |
| `showPalette` | boolean | `true` | Farbpalette anzeigen? |
| `showSpectrum` | boolean | `true` | Farbspektrum anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
