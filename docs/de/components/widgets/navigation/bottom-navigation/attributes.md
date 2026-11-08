# Bottom Navigation - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | Array mit Navigationsobjekten (id, icon, label) |
| `activeItem` | string | - | aktiver Navigationseintrag |
| `onChange` | function | - | Ereignis bei Auswahl |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `circular` | boolean | `false` | runde Knöpfe? |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `color` | enum | `primary` | Farbe: `primary`, `secondary`, `neutral` |
| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `300` | Dauer in ms |

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `responsive` | boolean | `true` | responsives Layout? |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onSelect` | function | wird bei Auswahl ausgeführt |
| `onHover` | function | wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `navigation` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
