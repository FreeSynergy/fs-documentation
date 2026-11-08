# Separator – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `orientation` | enum | `horizontal` | `horizontal`, `vertical` |
| `variant` | enum | `horizontal` | `horizontal`, `vertical`, `mit-beschriftung`, `dekorativ`, `inset` |
| `label` | string | `null` | Text, mittig in der Linie (nur horizontal) |
| `inset` | number \| string | `0` | Einzug in px oder Prozent |
| `spacing` | number | `8` | Abstand zu den Nachbarn in px |

## Ereignisse

Es werden keine Ereignisse genutzt; ein Separator dient nur der Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | `separator` für strukturelle Trennung (Menügruppen, Werkzeuggruppen) |
| – | – | dekorative Trennlinien erhalten `aria-hidden="true"` |
| – | – | senkrechte Trenner ohne strukturelle Wirkung sind immer `aria-hidden` |

## Geerbt von

`id`, `visible`, `size`, `theme`, `aria-*` →
[Basiskomponente](../base.md)
