# Accordion - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Liste der Accordion-Einträge |
| `activeItem` | string/number | - | aktiver Eintrag |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `collapsible` | boolean | `true` | einklappbar? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onExpand` | function | wird beim Aufklappen ausgeführt |
| `onCollapse` | function | wird beim Zuklappen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `tablist` |

## Eintrag-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `header` | string/node | Text der Kopfzeile |
| `content` | string/node | Inhalt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
