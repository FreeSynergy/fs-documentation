# Datumsfeld – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `value` | string | - | Wert (Datum, Uhrzeit oder beides, je nach `type`) |
| `type` | enum | `date` | `date`, `time`, `datetime` (`time`/`datetime` ersetzen die früheren eigenen Komponenten) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `minDate` | string | - | frühestes Datum |
| `maxDate` | string | - | spätestes Datum |
| `placeholder` | string | `null` | Platzhaltertext |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `calendar` | Icon-Name |
| `format` | string | `YYYY-MM-DD` | Datumsformat |
| `format24h` | boolean | `true` | 24-Stunden-Format (für `time`/`datetime`) |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onCalendarOpen` | function | läuft, wenn sich der Kalender öffnet |
| `onOpen` | function | läuft beim Öffnen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Validierungsattribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Pflichtfeld? |
| `error` | string | - | Fehlermeldung |

## Bereichsattribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `range` | boolean | `false` | einen Datumsbereich wählen? |
| `endDate` | string | - | Enddatum |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
