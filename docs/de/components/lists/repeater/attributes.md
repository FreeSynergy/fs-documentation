# Repeater - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Item-Objekten |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `content` | string/node | Inhalt |
| `image` | string | Bild-URL |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `interactive` | boolean | `false` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |
| `variant` | enum | `default` | Stil: `default`, `card`, `list` |

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
| `role` | string | ARIA-Rolle: `list` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird beim Klick ausgeführt |
| `onHover` | function | Wird beim Hover ausgeführt |

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
