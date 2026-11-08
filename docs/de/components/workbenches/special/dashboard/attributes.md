# Dashboard – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `widgets` | array[] | - | Liste der Widgets |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `dragAndDrop` | boolean | `true` | Drag & Drop aktivieren? |
| `responsive` | boolean | `true` | responsives Layout? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `columns` | number | `3` | Anzahl der Spalten |
| `gap` | number | `16` | Abstand zwischen Widgets |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onWidgetMove` | function | läuft beim Verschieben |
| `onWidgetResize` | function | läuft beim Größenändern |
| `onWidgetRemove` | function | läuft beim Entfernen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `region` |

## Widget-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `type` | string | Widget-Typ |
| `title` | string | Titel |
| `content` | string/node | Inhalt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
