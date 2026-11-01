# Number Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | number | - | Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `min` | number | - | Minimalwert |
| `max` | number | - | Maximalwert |
| `step` | number | `1` | Schrittweite |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showStepButtons` | boolean | `true` | Step-Buttons anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onKeyDown` | function | Wird bei Tastendruck ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `spinbutton` |

## Validation-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Erforderlich? |
| `error` | string | - | Fehlermeldung |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
