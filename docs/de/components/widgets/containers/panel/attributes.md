# Panel - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `title` | string | - | Titel |
| `content` | string/node | - | Inhalt |
| `footer` | string/node | - | Inhalt der Fußzeile |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `false` | einklappbar? |
| `draggable` | boolean | `false` | verschiebbar? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | responsives Layout? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onCollapsibleToggle` | function | wird beim Ein- oder Ausklappen ausgeführt |
| `onDrag` | function | wird während des Ziehens ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
