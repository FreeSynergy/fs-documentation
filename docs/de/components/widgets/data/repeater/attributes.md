# Repeater - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Item-Objekten |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | Interaktiv? |
| `variant` | enum | `default` | Stil: `default`, `card`, `list` |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `list` |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `content` | string/node | Inhalt |
| `image` | string | Bild-URL |

## Filter-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `filter` | string | Filter-String |
| `onFilter` | function | Filter-Funktion |

## Sort-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `sort` | string | Sort-Feld |
| `sortOrder` | enum | `asc`, `desc` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
