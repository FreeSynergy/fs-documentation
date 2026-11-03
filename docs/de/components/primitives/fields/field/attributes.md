# Field (Feld-Wrapper) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/). Das umschlossene Feld bringt seine eigenen
Attribute mit. Das geerbte `label` wird vom Wrapper an das Feld weitergegeben.

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `for` | string | - | `id` des umschlossenen Feldes (Pflicht, außer bei Verschachtelung) |
| `help` | string | `null` | Hilfetext unter dem Feld |
| `error` | string | `null` | Fehlermeldung; gesetzt ⇒ Fehlerzustand |
| `required` | boolean | `false` | Pflichtfeld-Markierung mit Text |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `vertikal` | `vertikal`, `horizontal`, `inline` |
| `optional` | boolean | `false` | Zusatz „optional“ statt Pflicht-Markierung |
| `errorIcon` | boolean | `true` | Icon vor der Fehlermeldung |
| `counter` | boolean | `false` | Zeichenzähler (Wert aus dem Feld) |
| `labelWidth` | number | `140` | Labelfreite bei `horizontal` in px |

## Events

Es werden keine eigenen Events genutzt; das Feld erzeugt die Events.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group` |
| – | – | Hilfetext und Fehler sind über `aria-describedby` am Feld verknüpft |
| – | – | `required` setzt `aria-required` am Feld |
| – | – | Fehler zusätzlich über `aria-invalid` am Feld |

## Geerbt von

`id`, `visible`, `size`, `theme`, `state`, `animation`, `aria-*` →
[Basiskomponente](../../basics/base/)
