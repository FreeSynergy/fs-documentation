# Rich Text Editor - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (HTML) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Placeholder-Text |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSave` | function | Wird beim Speichern ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Toolbar-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showToolbar` | boolean | `true` | Toolbar anzeigen? |
| `toolbarButtons` | array[] | - | Array von Buttons |

## Features-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `enableImages` | boolean | `true` | Bilder erlauben? |
| `enableLinks` | boolean | `true` | Links erlauben? |
| `enableCode` | boolean | `true` | Code erlauben? |
| `enablePreview` | boolean | `true` | Vorschau erlauben? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
