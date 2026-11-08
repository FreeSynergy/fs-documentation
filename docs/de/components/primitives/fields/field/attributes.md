# Feld – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../../basics/base.md). Das eingeschlossene Feld bringt seine eigenen Attribute mit.
Das geerbte `label` gibt die Hülle an das Feld weiter.

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `for` | string | - | `id` des eingeschlossenen Feldes (Pflicht, außer bei Verschachtelung) |
| `help` | string | `null` | Hilfetext unter dem Feld |
| `error` | string | `null` | Fehlermeldung; gesetzt ⇒ Fehlerzustand |
| `required` | boolean | `false` | Pflichtfeld-Kennzeichnung mit Text |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `variant` | enum | `vertikal` | `vertikal`, `horizontal`, `inline` |
| `optional` | boolean | `false` | das Wort „optional“ statt einer Pflichtkennzeichnung |
| `errorIcon` | boolean | `true` | Icon vor der Fehlermeldung |
| `counter` | boolean | `false` | Zeichenzähler (Wert wird aus dem Feld übernommen) |
| `labelWidth` | number | `140` | Breite des Labels bei `horizontal` in px |

## Ereignisse

Keine eigenen Ereignisse; die Ereignisse erzeugt das Feld.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | `group` |
| – | – | Hilfetext und Fehler sind über `aria-describedby` mit dem Feld verknüpft |
| – | – | `required` setzt `aria-required` am Feld |
| – | – | Fehler zusätzlich über `aria-invalid` am Feld |

## Geerbt von

`id`, `visible`, `size`, `theme`, `state`, `animation`, `aria-*` →
[Basiskomponente](../../basics/base.md)
