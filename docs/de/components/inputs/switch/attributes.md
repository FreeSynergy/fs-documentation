# Switch - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `checked` | boolean | `false` | Ein oder Aus? |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `default` | Stil: `default`, `round`, `pill` |
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
| `role` | string | ARIA-Rolle: `switch` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onBlur` | function | Wird beim Verlassen ausgeführt |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Label-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `labelPosition` | enum | `right` | Position: `left`, `right` |
