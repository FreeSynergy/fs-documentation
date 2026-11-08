# Grid View - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Array von Elementobjekten |
| `columns` | number | 3 | Anzahl der Spalten |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | interaktiv? |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `gap` | number | 16 | Abstand zwischen den Elementen |

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|--------------|
| `responsive` | boolean | `true` | responsives Layout? |
| `columns` | object | - | { xs: 1, sm: 2, md: 3, lg: 4 } |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Überfahren ausgelöst |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `grid` |

## Attribute der Elemente

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `title` | string | Titel |
| `content` | string/node | Inhalt |
| `image` | string | URL des Bildes |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
