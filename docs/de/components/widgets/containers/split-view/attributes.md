# Split View - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `leftContent` | node/string | - | linker Inhalt |
| `rightContent` | node/string | - | rechter Inhalt |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `false` | einklappbar? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | responsives Layout? |
| `stackBreakpoint` | number | `768` | Schwelle für das Untereinander-Stapeln |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onResize` | function | wird beim Verändern der Größe ausgeführt |
| `onCollapse` | function | wird beim Einklappen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Attribute zum Verändern der Größe

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `minWidth` | number | `200` | minimale Breite |
| `maxWidth` | number | `500` | maximale Breite |
| `defaultWidth` | number | `250` | Standardbreite |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
