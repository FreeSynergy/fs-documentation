# Radio Group - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `options` | array[] | - | Array von Options-Objekten |
| `value` | string/number | - | Aktueller Wert |
| `onChange` | function | - | Event bei Änderung |

## Option-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `value` | string/number | Wert |
| `label` | string | Label-Text |
| `icon` | string | Icon-Name |
| `disabled` | boolean | Deaktiviert? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `default` | Stil: `default`, `toggle` |
| `disabled` | boolean | `false` | Deaktiviert? |
| `name` | string | - | Name für Form |

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
| `role` | string | ARIA-Rolle: `radiogroup` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onBlur` | function | Wird beim Verlassen ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcons` | boolean | `false` | Icons anzeigen? |
