# Slider - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | number | - | Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `min` | number | `0` | Minimalwert |
| `max` | number | `100` | Maximalwert |
| `step` | number | `1` | Schrittweite |
| `disabled` | boolean | `false` | Deaktiviert? |

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
| `role` | string | ARIA-Rolle: `slider` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onBlur` | function | Wird beim Verlassen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onChangeEnd` | function | Wird bei Änderungsende ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showLabels` | boolean | `false` | Labels anzeigen? |
| `showValue` | boolean | `true` | Wert anzeigen? |
| `vertical` | boolean | `false` | Vertikal? |

## Range-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `range` | boolean | `false` | Bereichsauswahl? |
| `minRange` | number | - | Minimale Bereichsgröße |
