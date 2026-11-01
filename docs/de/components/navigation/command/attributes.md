# Command (Befehlspalette) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `commands` | array[] | - | Befehle mit Titel, Gruppe, Kürzel und Ziel |
| `query` | string | `""` | eingegebener Suchtext |
| `open` | boolean | `false` | Palette ist sichtbar |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hotkey` | string | `ctrl+k` | Tastenkürzel zum Öffnen |
| `grouped` | boolean | `true` | Treffer nach Gruppe anzeigen |
| `maxResults` | number | `50` | Obergrenze der Treffer |
| `recentCount` | number | `5` | zuletzt genutzte Befehle ohne Eingabe |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onQuery` | function | Suchtext geändert |
| `onSelect` | function | Befehl ausgeführt |
| `onOpen` | function | Palette geöffnet |
| `onClose` | function | Palette geschlossen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `dialog` |
| `aria-activedescendant` | string | id des markierten Treffers |
| `label` | string | Pflicht, z. B. „Befehle suchen“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
