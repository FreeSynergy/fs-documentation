# Breadcrumb - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Breadcrumb-Objekten (label, href, icon) |
| `separator` | string | `>` | Separator: `>`, `>`, `/`, `›`, `•` |
| `activeIndex` | number | - | Aktueller Index (für Highlighting) |
| `collapsed` | boolean | `false` | Eingeklappt bei wenig Platz? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `color` | string | `neutral` | Farbe |
| `rounded` | boolean | `false` | Abgerundete Ecken? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird beim Klick ausgeführt |
| `onHomeClick` | function | Wird beim Klick auf Home ausgeführt |
| `truncate` | boolean | `false` | Kürzen bei wenig Platz? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text (z.B. "Pfad") |
| `role` | string | ARIA-Rolle: `navigation` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onNavigate` | function | Wird bei Navigation ausgeführt |
| `onTruncate` | function | Wird beim Kürzen ausgeführt |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsives Layout? |
| `truncateBreakpoint` | number | Breakpoint für Kürzen |
