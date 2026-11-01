# Dashboard - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `widgets` | array[] | - | Array von Widgets |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `dragAndDrop` | boolean | `true` | Drag & Drop aktivieren? |
| `responsive` | boolean | `true` | Responsives Layout? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `columns` | number | `3` | Anzahl Spalten |
| `gap` | number | `16` | Abstand zwischen Widgets |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onWidgetMove` | function | Wird beim Verschieben ausgeführt |
| `onWidgetResize` | function | Wird beim Resizen ausgeführt |
| `onWidgetRemove` | function | Wird beim Entfernen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Widget-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `type` | string | Widget-Typ |
| `title` | string | Titel |
| `content` | string/node | Inhalt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
