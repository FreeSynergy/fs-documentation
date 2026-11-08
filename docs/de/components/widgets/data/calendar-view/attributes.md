# Calendar View - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `date` | string | - | aktuelles Datum |
| `events` | array[] | - | Array mit Termin-Objekten |
| `onChange` | function | - | Ereignis bei Datumsänderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | interaktiv? |

## Ereignisse
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `title` | string | Titel |
| `date` | string | Datum |
| `description` | string | Beschreibung |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDateChange` | function | wird ausgeführt, wenn sich das Datum ändert |
| `onEventClick` | function | wird beim Klick auf einen Termin ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `grid` |

## Navigations-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showNavigation` | boolean | `true` | Navigation anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
