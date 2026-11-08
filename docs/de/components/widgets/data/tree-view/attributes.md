# Tree View - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `data` | array[] | - | Array von Knotenobjekten |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | enum | `simple` | Stil: `simple`, `with-icons`, `with-checkboxes`, `draggable` |
| `multiple` | boolean | `false` | Mehrfachauswahl? |
| `interactive` | boolean | `false` | interaktiv? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Symbole anzeigen? |
| `showCheckboxes` | boolean | `false` | Checkboxen anzeigen? |
| `indent` | number | `24` | Einrückung in px |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onExpand` | function | wird beim Ausklappen ausgeführt |
| `onCollapse` | function | wird beim Einklappen ausgeführt |
| `onSelect` | function | wird bei Auswahl ausgeführt |
| `onDragStart` | function | wird zu Beginn eines Ziehens ausgeführt |
| `onDragEnd` | function | wird am Ende eines Ziehens ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `tree` |

## Knotenattribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `title` | string | Titel |
| `children` | array[] | untergeordnete Knoten |
| `icon` | string | Name des Symbols |
| `checked` | boolean | ausgewählt? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
