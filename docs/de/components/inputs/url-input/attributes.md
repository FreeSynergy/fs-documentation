# URL Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (URL) |
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
| `onSubmit` | function | Wird bei Submit ausgeführt |

## Validation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `required` | boolean | `false` | Erforderlich? |
| `error` | string | - | Fehlermeldung |
| `isValidURL` | function | Validierungsfunktion |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `link` | Icon-Name |
