# Spinner - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `track` | boolean | `true` | Hintergrundring sichtbar |
| `speed` | number | `1` | Umdrehungen pro Sekunde |
| `text` | string | `null` | sichtbarer Begleittext (Variante `mit-text`) |
| `inline` | boolean | `false` | Größe an die Textzeile angepasst |

## Ereignisse

Es werden keine Ereignisse genutzt. Ein Spinner dient nur der Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | nur nötig, wenn der Spinner eine Aktion benennt („Speichern“) |
| `role` | string | `status` |
| – | – | der **wartende Bereich** bekommt `aria-busy="true"`, nicht nur der Spinner |

## Geerbt von

`id`, `visible`, `size`, `theme`, `state`, `animation`, `aria-*` →
[Base-Komponente](../../basics/base.md)
