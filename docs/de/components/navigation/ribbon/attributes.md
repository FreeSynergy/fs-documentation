# Ribbon - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `tabs` | array[] | - | Array von Tab-Objekten |
| `activeTab` | string | - | Aktiver Tab |
| `onChange` | function | - | Event bei Tab-Wechsel |

## Group-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `groups` | array[] | Array von Group-Objekten |
| `commands` | array[] | Array von Command-Objekten |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `minimized` | boolean | `false` | Minimiert? |
| `collapsible` | boolean | `true` | Ein-/Ausklappbar? |
| `showIcons` | boolean | `true` | Icons anzeigen? |
| `showLabels` | boolean | `true` | Labels anzeigen? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `standard` | Größe: `compact`, `standard`, `large` |
| `rounded` | boolean | `false` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark`, `light` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `toolbar` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onExpand` | function | Wird beim Erweitern ausgeführt |
| `onMinimize` | function | Wird beim Minimieren ausgeführt |

## Keyboard-Shortcuts

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `keyboardShortcuts` | boolean | `true` | Keyboard-Shortcuts aktivieren? |
