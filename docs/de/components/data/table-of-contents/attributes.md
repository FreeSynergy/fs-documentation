# Table of Contents - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Item-Objekten (title, href, children) |
| `activeItem` | string | - | Aktiver Abschnitt |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |
| `interactive` | boolean | `false` | Interaktiv? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `navigation` |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `title` | string | Titel |
| `href` | string | Link |
| `children` | array[] | Unterpunkte |

## Scroll-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `scrollSpy` | boolean | `false` | Scroll-Spy aktivieren? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
