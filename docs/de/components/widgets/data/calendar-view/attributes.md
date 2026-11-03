# Calendar View - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `date` | string | - | Aktuelles Datum |
| `events` | array[] | - | Array von Event-Objekten |
| `onChange` | function | - | Event bei Datum-Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | Interaktiv? |

## Events
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `date` | string | Datum |
| `description` | string | Beschreibung |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDateChange` | function | Wird bei Datum-Änderung ausgeführt |
| `onEventClick` | function | Wird bei Event-Klick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `grid` |

## Navigation-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showNavigation` | boolean | `true` | Navigation anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
