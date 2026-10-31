# Bottom Navigation - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Nav-Objekten (id, icon, label) |
| `activeItem` | string | - | Aktiver Nav-Punkt |
| `onChange` | function | - | Event bei Auswahl |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `icon-text` | Stil: `icon-text`, `text`, `icon-only` |
| `disabled` | boolean | `false` | Deaktiviert? |
| `circular` | boolean | `false` | Runde Buttons? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `color` | enum | `primary` | Farbe: `primary`, `secondary`, `neutral` |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `navigation` |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird bei Auswahl ausgeführt |
| `onHover` | function | Wird beim Hover ausgeführt |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | `true` | Responsives Layout? |
