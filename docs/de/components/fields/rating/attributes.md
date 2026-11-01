# Rating - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | number | - | Wert (Bewertung) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `readonly` | boolean | `false` | Nur Anzeige? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `max` | number | `5` | Maximale Bewertung |
| `showCount` | boolean | `false` | Anzahl anzeigen? |
| `count` | number | - | Anzahl der Bewertungen |
| `decimal` | boolean | `false` | Dezimalstellen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `rating` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
