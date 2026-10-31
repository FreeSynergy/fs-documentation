# Accordion - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Accordion-Items |
| `activeItem` | string/number | - | Aktives Item |
| `onChange` | function | - | Event bei Wechsel |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `header` | string/node | Header-Text |
| `content` | string/node | Inhalt |
| `disabled` | boolean | Deaktiviert? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `single` | Stil: `single`, `multiple` |
| `collapsible` | boolean | `true` | Kollabierbar? |
| `disabled` | boolean | `false` | Gesamtes Accordion deaktivieren? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `tablist` |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onExpand` | function | Wird beim Expandieren ausgeführt |
| `onCollapse` | function | Wird beim Kollabieren ausgeführt |
