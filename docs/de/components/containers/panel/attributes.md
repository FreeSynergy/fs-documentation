# Panel - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `title` | string | - | Titel |
| `content` | string/node | - | Inhalt |
| `footer` | string/node | - | Footer-Inhalt |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `false` | Kollabierbar? |
| `draggable` | boolean | `false` | Verschiebbar? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | Responsives Layout? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onCollapsibleToggle` | function | Wird beim Kollabieren ausgeführt |
| `onDrag` | function | Wird beim Ziehen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
