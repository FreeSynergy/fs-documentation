# Menu (Menü) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Menüpunkten |
| `activeItem` | string/number | - | Aktiver Menüpunkt |
| `onChange` | function | - | Event bei Auswahl |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onToggle` | function | - | Event beim Öffnen/Schließen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `horizontal` | Stil: `horizontal`, `vertical` |
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |
| `closable` | boolean | `false` | Schließbar? |
| `closeOnOutsideClick` | boolean | `true` | Bei Klick außerhalb schließen? |
| `keyboardNavigation` | boolean | `true` | Keyboard-Navigation? |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showLabels` | boolean | `true` | Labels anzeigen? |
| `color` | enum | `default` | Farbe: `default`, `light`, `primary` |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsives Layout? |
| `hamburgerBreakpoint` | number | Breakpoint für Hamburger |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `menubar` |
| `aria-expanded` | boolean | Ist erweitert? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
