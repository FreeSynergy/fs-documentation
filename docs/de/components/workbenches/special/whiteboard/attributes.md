# Whiteboard – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `toolbar` | array[] | - | Liste der Werkzeugleisten-Buttons |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `interactive` | boolean | `true` | interaktiv? |
| `grid` | boolean | `true` | Raster anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onDraw` | function | läuft beim Zeichnen |
| `onClear` | function | läuft beim Löschen |
| `onExport` | function | läuft beim Export |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `region` |

## Funktionsattribute

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `undoRedo` | boolean | `true` | Rückgängig/Wiederholen? |
| `collaborative` | boolean | `false` | gemeinsam bearbeitbar? |

## Export-Attribute

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `exportFormats` | array[] | `['png', 'jpg', 'pdf']` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
