# Checkbox (Ankreuzfeld) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `checked` | boolean | `false` | Ausgewählt? |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `default` | Stil: `default`, `toggle` |
| `indeterminate` | boolean | `false` | Teilweise ausgewählt? |
| `disabled` | boolean | `false` | Deaktiviert? |
| `label` | string | - | Label-Text |

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
| `role` | string | ARIA-Rolle: `checkbox` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onBlur` | function | Wird beim Verlassen ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcon` | boolean | `false` | Icon anzeigen? |
| `labelPosition` | enum | `right` | Label-Position: `left`, `right` |
