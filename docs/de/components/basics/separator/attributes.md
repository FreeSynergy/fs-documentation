# Separator (Trennlinie) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `orientation` | enum | `horizontal` | `horizontal`, `vertical` |
| `variant` | enum | `horizontal` | `horizontal`, `vertical`, `mit-beschriftung`, `dekorativ`, `inset` |
| `label` | string | `null` | Text mittig in der Linie (nur horizontal) |
| `inset` | number \| string | `0` | Einzug in px oder Prozent |
| `spacing` | number | `8` | Abstand zu den Nachbarn in px |

## Events

Es werden keine Events genutzt; ein Separator ist reine Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `separator` bei struktureller Trennung (Menügruppen, Toolgruppen) |
| – | – | Dekorative Trennlinien erhalten `aria-hidden="true"` |
| – | – | Senkrechte Trenner ohne Strukturwirkung sind immer `aria-hidden` |

## Geerbt von

`id`, `visible`, `size`, `theme`, `aria-*` →
[Basiskomponente](../base/)
