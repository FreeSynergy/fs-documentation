# Grid View - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Item-Objekten |
| `columns` | number | 3 | Anzahl Spalten |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | Interaktiv? |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `gap` | number | 16 | Abstand zwischen Items |

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `responsive` | boolean | `true` | Responsives Layout? |
| `columns` | object | - | { xs: 1, sm: 2, md: 3, lg: 4 } |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `grid` |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `content` | string/node | Inhalt |
| `image` | string | Bild-URL |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
