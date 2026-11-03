# Card - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `title` | string | - | Titel |
| `subtitle` | string | - | Untertitel |
| `content` | string/node | - | Inhalt |
| `actions` | array[] | - | Array von Action-Objekten |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `default` | Stil: `default`, `flat`, `outlined`, `elevated` |
| `interactive` | boolean | `false` | Interaktiv? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | Responsives Layout? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onActionClick` | function | Wird beim Action-Klick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Media-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `media` | string/object | - | Bild/Thumbnail |
| `mediaPosition` | enum | `top` | Position: `top`, `bottom`, `left` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
