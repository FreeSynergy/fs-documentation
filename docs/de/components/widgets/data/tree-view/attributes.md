# Tree View (Baumansicht) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `data` | array[] | - | Array von Node-Objekten |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `simple` | Stil: `simple`, `with-icons`, `with-checkboxes`, `draggable` |
| `multiple` | boolean | `false` | Mehrfachauswahl? |
| `interactive` | boolean | `false` | Interaktiv? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showCheckboxes` | boolean | `false` | Checkboxen anzeigen? |
| `indent` | number | `24` | Einrückung in px |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onExpand` | function | Wird beim Expandieren ausgeführt |
| `onCollapse` | function | Wird beim Kollabieren ausgeführt |
| `onSelect` | function | Wird bei Auswahl ausgeführt |
| `onDragStart` | function | Wird beim Drag-Start ausgeführt |
| `onDragEnd` | function | Wird beim Drag-Ende ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `tree` |

## Node-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `children` | array[] | Kinder-Nodes |
| `icon` | string | Icon-Name |
| `checked` | boolean | Ausgewählt? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
