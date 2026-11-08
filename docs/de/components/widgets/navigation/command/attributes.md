# Command - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `commands` | array[] | - | Befehle mit Titel, Gruppe, Tastenkürzel und Ziel |
| `query` | string | `""` | eingegebener Suchtext |
| `open` | boolean | `false` | die Palette ist sichtbar |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `hotkey` | string | `ctrl+k` | Tastenkürzel zum Öffnen |
| `grouped` | boolean | `true` | Treffer gruppiert anzeigen |
| `maxResults` | number | `50` | obere Grenze für Treffer |
| `recentCount` | number | `5` | zuletzt genutzte Befehle ohne Eingabe |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onQuery` | function | Suchtext wurde geändert |
| `onSelect` | function | Befehl wurde ausgeführt |
| `onOpen` | function | Palette wurde geöffnet |
| `onClose` | function | Palette wurde geschlossen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `dialog` |
| `aria-activedescendant` | string | ID des markierten Treffers |
| `label` | string | Pflicht, z. B. „Befehle suchen“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
