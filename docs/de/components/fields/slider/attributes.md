# Slider - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | number | - | Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `min` | number | `0` | Minimalwert |
| `max` | number | `100` | Maximalwert |
| `step` | number | `1` | Schrittweite |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showLabels` | boolean | `false` | Labels anzeigen? |
| `showValue` | boolean | `true` | Wert anzeigen? |
| `vertical` | boolean | `false` | Vertikal? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChangeEnd` | function | Wird bei Änderungsende ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `slider` |

## Range-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `range` | boolean | `false` | Bereichsauswahl? |
| `minRange` | number | - | Minimale Bereichsgröße |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
