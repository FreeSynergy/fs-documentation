# Rating - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | number | - | Wert (Bewertung) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `readonly` | boolean | `false` | nur Anzeige? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `max` | number | `5` | höchste Bewertung |
| `showCount` | boolean | `false` | Anzahl anzeigen? |
| `count` | number | - | Anzahl der Bewertungen |
| `decimal` | boolean | `false` | Nachkommastellen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Überfahren ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `rating` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
