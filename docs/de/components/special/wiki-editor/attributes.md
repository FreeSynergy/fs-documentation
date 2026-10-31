# Wiki Editor - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Markdown/HTML) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `disabled` | boolean | `false` | Deaktiviert? |
| `placeholder` | string | `null` | Placeholder-Text |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Toolbar-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showToolbar` | boolean | `true` | Toolbar anzeigen? |
| `toolbarButtons` | array[] | - | Array von Buttons |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `textbox` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onBlur` | function | Wird beim Verlassen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onSave` | function | Wird beim Speichern ausgeführt |

## Features-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `enablePreview` | boolean | `true` | Vorschau erlauben? |
| `enableImages` | boolean | `true` | Bilder erlauben? |
| `enableLinks` | boolean | `true` | Links erlauben? |
