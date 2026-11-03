# Accordion - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Accordion-Items |
| `activeItem` | string/number | - | Aktives Item |
| `onChange` | function | - | Event bei Wechsel |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `true` | Kollabierbar? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onExpand` | function | Wird beim Expandieren ausgeführt |
| `onCollapse` | function | Wird beim Kollabieren ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `tablist` |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `header` | string/node | Header-Text |
| `content` | string/node | Inhalt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
