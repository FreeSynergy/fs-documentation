# Tree View (Baumansicht) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `data` | array[] | - | Array von Node-Objekten |

## Node-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `children` | array[] | Kinder-Nodes |
| `icon` | string | Icon-Name |
| `checked` | boolean | Ausgewählt? |
| `disabled` | boolean | Deaktiviert? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `simple` | Stil: `simple`, `with-icons`, `with-checkboxes`, `draggable` |
| `multiple` | boolean | `false` | Mehrfachauswahl? |
| `interactive` | boolean | `false` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |

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
| `role` | string | ARIA-Rolle: `tree` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird beim Klick ausgeführt |
| `onExpand` | function | Wird beim Expandieren ausgeführt |
| `onCollapse` | function | Wird beim Kollabieren ausgeführt |
| `onSelect` | function | Wird bei Auswahl ausgeführt |
| `onDragStart` | function | Wird beim Drag-Start ausgeführt |
| `onDragEnd` | function | Wird beim Drag-Ende ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showCheckboxes` | boolean | `false` | Checkboxen anzeigen? |
| `indent` | number | `24` | Einrückung in px |
