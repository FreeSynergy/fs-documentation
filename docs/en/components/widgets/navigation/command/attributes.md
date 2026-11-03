# Command (Befehlspalette) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `commands` | array[] | - | Befehle mit Titel, Gruppe, Kürzel und Ziel |
| `query` | string | `""` | eingegebener Suchtext |
| `open` | boolean | `false` | Palette ist sichtbar |

## Behaviour

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `hotkey` | string | `ctrl+k` | Tastenkürzel zum Öffnen |
| `grouped` | boolean | `true` | Treffer nach Gruppe anzeigen |
| `maxResults` | number | `50` | Obergrenze der Treffer |
| `recentCount` | number | `5` | zuletzt genutzte Befehle ohne Eingabe |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onQuery` | function | Suchtext geändert |
| `onSelect` | function | Befehl ausgeführt |
| `onOpen` | function | Palette geöffnet |
| `onClose` | function | Palette geschlossen |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | `dialog` |
| `aria-activedescendant` | string | id des markierten Treffers |
| `label` | string | Pflicht, z. B. „Befehle suchen“ |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
