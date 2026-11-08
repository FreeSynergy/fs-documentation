# Table of Contents - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Array mit Eintrags-Objekten (title, href, children) |
| `activeItem` | string | - | aktueller Abschnitt |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `false` | einklappbar? |
| `interactive` | boolean | `false` | interaktiv? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `navigation` |

## Eintrags-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `title` | string | Titel |
| `href` | string | Link |
| `children` | array[] | Unterpunkte |

## Scroll-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `scrollSpy` | boolean | `false` | Scroll-Spy aktivieren? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
