# Kbd (Tastenkennung) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `shortcut` | string | - | Taste oder Kombination, z. B. `Strg+S` |
| `keys` | array[] | - | Einzelkappen einer Kombination (statt `key`) |
| `separator` | string | `+` | Zeichen zwischen den Kappen |
| `active` | boolean | `false` | gerade gedrückt? |

## Events

Es werden keine Events genutzt; das Abhören von Tasten gehört zur Anwendung.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| – | – | als ganzes Element vorlesbar machen (`aria-label="Strg plus S"`) |
| – | – | Modifikatoren ausgeschrieben benennen, Symbole nur zusätzlich |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `aria-*` →
[Basiskomponente](../base/)
