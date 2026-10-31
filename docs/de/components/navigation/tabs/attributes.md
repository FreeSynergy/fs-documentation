# Tabs - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `tabs` | array[] | - | Array von Tab-Objekten (id, label, content) |
| `activeTab` | string/number | - | Aktiver Tab (id) |
| `onChange` | function | - | Event bei Tab-Wechsel |
| `variant` | enum | `default` | Stil: `default`, `pill`, `card` |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `closable` | boolean | `false` | Tabs schließbar? |
| `scrollable` | boolean | `false` | Scrollbar? |
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |
| `disabled` | boolean | `false` | Gesamte Tabs deaktivieren? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showLabels` | boolean | `true` | Labels anzeigen? |
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `tablist` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsives Layout? |
| `hideLabelsOnMobile` | boolean | Labels auf Mobile verstecken? |
