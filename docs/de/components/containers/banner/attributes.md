# Banner - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `type` | enum | `info` | Typ: `info`, `success`, `warning`, `error` |
| `title` | string | - | Titel |
| `message` | string | - | Nachricht |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `dismissible` | boolean | `false` | Schließbar? |
| `sticky` | boolean | `true` | Fixiert oben? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `false` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `alert` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |

## Action-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `actionLabel` | string | Aktion-Label |
| `actionLabel2` | string | Zweite Aktion-Label |
| `onActionClick` | function | Wird bei Aktion-Klick ausgeführt |
| `onActionClick2` | function | Wird bei zweiter Aktion-Klick ausgeführt |

## Icon-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcon` | boolean | `true` | Icon anzeigen? |
