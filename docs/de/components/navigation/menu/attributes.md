# Menu (Menü) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Menüpunkten |
| `activeItem` | string/number | - | Aktiver Menüpunkt |
| `onChange` | function | - | Event bei Auswahl |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `horizontal` | Stil: `horizontal`, `vertical` |
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |
| `closable` | boolean | `false` | Schließbar? |
| `disabled` | boolean | `false` | Gesamtes Menu deaktivieren? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showLabels` | boolean | `true` | Labels anzeigen? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `menubar` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsives Layout? |
| `hamburgerBreakpoint` | number | Breakpoint für Hamburger |
