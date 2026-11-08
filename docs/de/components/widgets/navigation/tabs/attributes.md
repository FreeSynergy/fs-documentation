# Tabs - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `tabs` | array[] | - | Liste der Reiter-Objekte (id, label, content) |
| `activeTab` | string/number | - | aktiver Reiter (id) |
| `onChange` | function | - | Ereignis beim Reiterwechsel |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `closable` | boolean | `false` | sind Reiter schließbar? |
| `scrollable` | boolean | `false` | scrollbar? |
| `collapsible` | boolean | `false` | einklappbar? |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showLabels` | boolean | `true` | Beschriftungen anzeigen? |

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsives Layout? |
| `hideLabelsOnMobile` | boolean | Beschriftungen auf dem Smartphone ausblenden? |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onSelect` | function | läuft bei Auswahl |
| `onClose` | function | läuft beim Schließen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `tablist` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
