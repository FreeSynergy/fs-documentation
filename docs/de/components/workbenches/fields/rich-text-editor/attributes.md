# Rich Text Editor - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `value` | string | - | Wert (HTML) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `placeholder` | string | `null` | Platzhaltertext |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onSave` | function | läuft beim Speichern |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `textbox` |

## Toolbar-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showToolbar` | boolean | `true` | Toolbar anzeigen? |
| `toolbarButtons` | array[] | - | Liste der Schaltflächen |

## Funktions-Attribute

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `enableImages` | boolean | `true` | Bilder erlauben? |
| `enableLinks` | boolean | `true` | Links erlauben? |
| `enableCode` | boolean | `true` | Code erlauben? |
| `enablePreview` | boolean | `true` | Vorschau erlauben? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
