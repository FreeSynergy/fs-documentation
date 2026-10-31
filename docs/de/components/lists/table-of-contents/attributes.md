# Table of Contents - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Item-Objekten (title, href, children) |
| `activeItem` | string | - | Aktiver Abschnitt |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `href` | string | Link |
| `children` | array[] | Unterpunkte |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |
| `interactive` | boolean | `false` | Interaktiv? |
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
| `role` | string | ARIA-Rolle: `navigation` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird beim Klick ausgeführt |
| `onHover` | function | Wird beim Hover ausgeführt |

## Scroll-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `scrollSpy` | boolean | `false` | Scroll-Spy aktivieren? |
