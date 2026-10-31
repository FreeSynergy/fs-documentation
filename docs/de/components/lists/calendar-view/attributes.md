# Calendar View - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `date` | string | - | Aktuelles Datum |
| `events` | array[] | - | Array von Event-Objekten |
| `onChange` | function | - | Event bei Datum-Änderung |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `date` | string | Datum |
| `description` | string | Beschreibung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `monthly` | Stil: `monthly`, `weekly`, `daily`, `agenda` |
| `interactive` | boolean | `false` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |

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
| `role` | string | ARIA-Rolle: `grid` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDateChange` | function | Wird bei Datum-Änderung ausgeführt |
| `onEventClick` | function | Wird bei Event-Klick ausgeführt |

## Navigation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showNavigation` | boolean | `true` | Navigation anzeigen? |
