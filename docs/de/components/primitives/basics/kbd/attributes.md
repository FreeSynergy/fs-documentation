# Kbd – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `shortcut` | string | - | Taste oder Kombination, z. B. `Ctrl+S` |
| `keys` | array[] | - | einzelne Tastenkappen einer Kombination (statt `key`) |
| `separator` | string | `+` | Zeichen zwischen den Tastenkappen |
| `active` | boolean | `false` | gerade gedrückt? |

## Ereignisse

Es werden keine Ereignisse genutzt; das Abhören von Tasten gehört zur Anwendung.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| – | – | das ganze Element lesbar machen (`aria-label="Ctrl plus S"`) |
| – | – | Modifikatoren in ausgeschriebenen Wörtern nennen, Symbole nur zusätzlich |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `aria-*` →
[Basiskomponente](../base.md)
