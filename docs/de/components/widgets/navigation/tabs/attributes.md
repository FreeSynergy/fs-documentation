# Tabs - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `tabs` | array[] | - | Array von Tab-Objekten (id, label, content) |
| `activeTab` | string/number | - | Aktiver Tab (id) |
| `onChange` | function | - | Event bei Tab-Wechsel |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `closable` | boolean | `false` | Tabs schließbar? |
| `scrollable` | boolean | `false` | Scrollbar? |
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showLabels` | boolean | `true` | Labels anzeigen? |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsives Layout? |
| `hideLabelsOnMobile` | boolean | Labels auf Mobile verstecken? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `tablist` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
