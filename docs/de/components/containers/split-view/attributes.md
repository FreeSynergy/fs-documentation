# Split View - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `leftContent` | node/string | - | Linker Inhalt |
| `rightContent` | node/string | - | Rechter Inhalt |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `fixed` | Stil: `fixed`, `resizable`, `responsive` |
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | `true` | Responsives Layout? |
| `stackBreakpoint` | number | `768` | Breakpoint für Stack |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `region` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onResize` | function | Wird beim Resizen ausgeführt |
| `onCollapse` | function | Wird beim Kollabieren ausgeführt |

## Resizing-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `minWidth` | number | `200` | Minimale Breite |
| `maxWidth` | number | `500` | Maximale Breite |
| `defaultWidth` | number | `250` | Standard-Breite |
