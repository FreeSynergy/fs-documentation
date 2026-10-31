# Date Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Datum) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `minDate` | string | - | Minimaldatum |
| `maxDate` | string | - | Maximaldatum |
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
| `role` | string | ARIA-Rolle: `textbox` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onBlur` | function | Wird beim Verlassen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onCalendarOpen` | function | Wird beim Öffnen des Kalenders ausgeführt |

## Validation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `required` | boolean | `false` | Erforderlich? |
| `error` | string | - | Fehlermeldung |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `calendar` | Icon-Name |
| `format` | string | `YYYY-MM-DD` | Datumsformat |

## Range-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `range` | boolean | `false` | Datumsbereich auswählen? |
| `endDate` | string | - | Enddatum |
