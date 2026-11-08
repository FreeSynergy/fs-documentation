# Card - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `title` | string | - | Titel |
| `subtitle` | string | - | Untertitel |
| `content` | string/node | - | Inhalt |
| `actions` | array[] | - | Liste der Aktionsobjekte |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | enum | `default` | Stil: `default`, `flat`, `outlined`, `elevated` |
| `interactive` | boolean | `false` | interaktiv? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | responsives Layout? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onActionClick` | function | wird ausgeführt, wenn eine Aktion angeklickt wird |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Medien-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `media` | string/object | - | Bild oder Vorschaubild |
| `mediaPosition` | enum | `top` | Position: `top`, `bottom`, `left` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
