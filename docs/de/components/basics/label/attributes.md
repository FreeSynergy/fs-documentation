# Label (Beschriftung) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/). Das `label`-Attribut der Basisklasse ist hier der
sichtbare Inhalt.

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `for` | string | - | `id` des beschrifteten Elements |
| `required` | boolean | `false` | Pflicht-Markierung mit Text |
| `hidden` | boolean | `false` | visuell versteckt, für Screenreader wirksam |
| `shortcut` | string | `null` | Zugrifftaste, wird unterstrichen dargestellt |

## Events

Es werden keine eigenen Events genutzt; ein Klick auf das Label wirkt auf
das verknüpfte Element.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `label` |
| – | – | Verknüpfung über `for`/`id` oder durch Verschachtelung |
| – | – | Pflicht zusätzlich mit Text („erforderlich“), nicht nur „*“ |

## Geerbt von

`id`, `label`, `visible`, `size`, `theme`, `state`, `aria-*` →
[Basiskomponente](../base/)
