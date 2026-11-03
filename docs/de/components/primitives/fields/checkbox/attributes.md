# Checkbox (Ankreuzfeld) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `checked` | boolean | `false` | Ausgewählt? |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `default` | Stil: `default`, `toggle` |
| `indeterminate` | boolean | `false` | Teilweise ausgewählt? |
| `label` | string | - | Label-Text |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `false` | Icon anzeigen? |
| `labelPosition` | enum | `right` | Label-Position: `left`, `right` |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `checkbox` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
