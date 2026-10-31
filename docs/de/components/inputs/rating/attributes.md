# Rating - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | number | - | Wert (Bewertung) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `star` | Stil: `star`, `heart`, `number` |
| `readonly` | boolean | `false` | Nur Anzeige? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `rating` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |
| `onClick` | function | Wird beim Klick ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `max` | number | `5` | Maximale Bewertung |
| `showCount` | boolean | `false` | Anzahl anzeigen? |
| `count` | number | - | Anzahl der Bewertungen |
| `decimal` | boolean | `false` | Dezimalstellen? |
