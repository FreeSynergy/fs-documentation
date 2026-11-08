# Repeater - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Array mit Eintrags-Objekten |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `false` | interaktiv? |
| `variant` | enum | `default` | Stil: `default`, `card`, `list` |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `list` |

## Eintrags-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `title` | string | Titel |
| `content` | string/node | Inhalt |
| `image` | string | URL des Bildes |

## Filter-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `filter` | string | Filterzeichenfolge |
| `onFilter` | function | Filterfunktion |

## Sortier-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `sort` | string | Sortierfeld |
| `sortOrder` | enum | `asc`, `desc` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
