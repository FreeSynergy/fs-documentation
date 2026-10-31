# Hamburger Menu - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onToggle` | function | - | Event beim Öffnen/Schließen |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `disabled` | boolean | `false` | Deaktiviert? |
| `closeOnOutsideClick` | boolean | `true` | Bei Klick außerhalb schließen? |
| `keyboardNavigation` | boolean | `true` | Keyboard-Navigation? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `color` | enum | `default` | Farbe: `default`, `light`, `primary` |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `button` |
| `aria-expanded` | boolean | Ist erweitert? |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onClick` | function | Wird beim Klick ausgeführt |

## Menu-Items (optional)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `items` | array[] | Array von Menüpunkten |
| `showIcons` | boolean | Icons anzeigen? |
