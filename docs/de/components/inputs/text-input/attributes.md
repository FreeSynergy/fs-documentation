# Text Input (Einzeiliges Textfeld) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `standard` | Stil: `standard`, `floating-label`, `underline` |
| `type` | string | `text` | Input-Typ: `text`, `password`, `email`, `url`, etc. |
| `disabled` | boolean | `false` | Deaktiviert? |
| `placeholder` | string | `null` | Placeholder-Text |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |

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
| `onKeyDown` | function | Wird bei Tastendruck ausgeführt |
| `onSubmit` | function | Wird bei Submit ausgeführt |

## Validation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `required` | boolean | `false` | Erforderlich? |
| `error` | string | - | Fehlermeldung |
| `minLength` | number | - | Minimale Länge |
| `maxLength` | number | - | Maximale Länge |
| `pattern` | string | - | Regex-Muster |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showLabel` | boolean | `true` | Label anzeigen? |
| `showIcon` | boolean | `false` | Icon anzeigen? |
| `prefix` | string | - | Präfix |
| `suffix` | string | - | Suffix |
