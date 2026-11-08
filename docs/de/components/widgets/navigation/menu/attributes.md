# Menu - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | Array der Menüeinträge |
| `activeItem` | string/number | - | aktiver Menüeintrag |
| `onChange` | function | - | Ereignis bei Auswahl |
| `isOpen` | boolean | `false` | ist es geöffnet? |
| `onToggle` | function | - | Ereignis beim Öffnen/Schließen |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `variant` | enum | `horizontal` | Stil: `horizontal`, `vertical` |
| `collapsible` | boolean | `false` | einklappbar? |
| `closable` | boolean | `false` | schließbar? |
| `closeOnOutsideClick` | boolean | `true` | Schließen bei Klick außerhalb? |
| `keyboardNavigation` | boolean | `true` | Tastaturnavigation? |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showLabels` | boolean | `true` | Beschriftungen anzeigen? |
| `color` | enum | `default` | Farbe: `default`, `light`, `primary` |

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsives Layout? |
| `hamburgerBreakpoint` | number | Haltepunkt für das Hamburger-Menü |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onSelect` | function | wird bei Auswahl ausgeführt |
| `onOpen` | function | wird beim Öffnen ausgeführt |
| `onClose` | function | wird beim Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `menubar` |
| `aria-expanded` | boolean | ist es aufgeklappt? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
