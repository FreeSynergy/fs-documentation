# Label – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../base.md). Das Attribut `label` der Basisklasse ist hier der sichtbare
Inhalt.

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `for` | string | - | `id` des beschrifteten Elements |
| `required` | boolean | `false` | Pflichtkennzeichnung mit Text |
| `hidden` | boolean | `false` | optisch versteckt, für Screenreader aktiv |
| `shortcut` | string | `null` | Zugriffstaste, unterstrichen dargestellt |

## Ereignisse

Keine eigenen Ereignisse; ein Klick auf das Label wirkt auf das verknüpfte Element.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | `label` |
| – | – | Verknüpfung über `for`/`id` oder durch Verschachtelung |
| – | – | Pflicht zusätzlich mit Text („Pflichtfeld“), nicht nur mit „*“ |

## Geerbt von

`id`, `label`, `visible`, `size`, `theme`, `state`, `aria-*` →
[Basiskomponente](../base.md)
