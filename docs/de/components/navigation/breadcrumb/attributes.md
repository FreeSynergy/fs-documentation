# Breadcrumb - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Breadcrumb-Objekten (label, href, icon) |
| `separator` | string | `>` | Separator: `>`, `>`, `/`, `›`, `•` |
| `activeIndex` | number | - | Aktueller Index (für Highlighting) |
| `collapsed` | boolean | `false` | Eingeklappt bei wenig Platz? |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onHomeClick` | function | - | Wird beim Klick auf Home ausgeführt |
| `truncate` | boolean | `false` | Kürzen bei wenig Platz? |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `color` | string | `neutral` | Farbe |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsives Layout? |
| `truncateBreakpoint` | number | Breakpoint für Kürzen |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onNavigate` | function | Wird bei Navigation ausgeführt |
| `onTruncate` | function | Wird beim Kürzen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `navigation` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
