# Color Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Farbe) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `disabled` | boolean | `false` | Deaktiviert? |
| `placeholder` | string | `null` | Placeholder-Text |

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
| `role` | string | ARIA-Rolle: `color` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onBlur` | function | Wird beim Verlassen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onOpen` | function | Wird beim Öffnen des Pickers ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `palette` | Icon-Name |
| `formats` | array[] | `['hex', 'rgb', 'hsl']` | Farbformate |

## Picker-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showAlpha` | boolean | `false` | Alpha-Kanal anzeigen? |
| `showPalette` | boolean | `true` | Farbpalette anzeigen? |
| `showSpectrum` | boolean | `true` | Farbspektrum anzeigen? |
