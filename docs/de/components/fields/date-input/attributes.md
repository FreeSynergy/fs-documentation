# Date Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Datum, Zeit oder beides je nach `type`) |
| `type` | enum | `date` | `date`, `time`, `datetime` (`time`/`datetime` ersetzen die früheren Eigenkomponenten) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `minDate` | string | - | Minimaldatum |
| `maxDate` | string | - | Maximaldatum |
| `placeholder` | string | `null` | Placeholder-Text |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `calendar` | Icon-Name |
| `format` | string | `YYYY-MM-DD` | Datumsformat |
| `format24h` | boolean | `true` | 24-Stunden-Format (bei `time`/`datetime`) |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onCalendarOpen` | function | Wird beim Öffnen des Kalenders ausgeführt |
| `onOpen` | function | Wird beim Öffnen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Validation-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Erforderlich? |
| `error` | string | - | Fehlermeldung |

## Range-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `range` | boolean | `false` | Datumsbereich auswählen? |
| `endDate` | string | - | Enddatum |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
