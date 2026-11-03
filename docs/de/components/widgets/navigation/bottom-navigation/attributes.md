# Bottom Navigation - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Nav-Objekten (id, icon, label) |
| `activeItem` | string | - | Aktiver Nav-Punkt |
| `onChange` | function | - | Event bei Auswahl |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `circular` | boolean | `false` | Runde Buttons? |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `color` | enum | `primary` | Farbe: `primary`, `secondary`, `neutral` |
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | Responsives Layout? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird bei Auswahl ausgeführt |
| `onHover` | function | Wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `navigation` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
