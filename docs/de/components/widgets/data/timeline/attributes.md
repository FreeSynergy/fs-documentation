# Timeline - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `events` | array[] | - | Array von Ereignisobjekten |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | interaktiv? |

## Ereignisse
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `date` | string | Datum |
| `title` | string | Titel |
| `description` | string | Beschreibung |
| `icon` | string | Name des Symbols |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Überfahren ausgelöst |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `navigation` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
