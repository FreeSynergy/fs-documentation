# Split View - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `leftContent` | node/string | - | Linker Inhalt |
| `rightContent` | node/string | - | Rechter Inhalt |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | Responsives Layout? |
| `stackBreakpoint` | number | `768` | Breakpoint für Stack |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onResize` | function | Wird beim Resizen ausgeführt |
| `onCollapse` | function | Wird beim Kollabieren ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Resizing-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `minWidth` | number | `200` | Minimale Breite |
| `maxWidth` | number | `500` | Maximale Breite |
| `defaultWidth` | number | `250` | Standard-Breite |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
