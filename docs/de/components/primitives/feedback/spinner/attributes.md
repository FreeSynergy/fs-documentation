# Spinner (Ladeanzeige) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `track` | boolean | `true` | Hintergrundring sichtbar |
| `speed` | number | `1` | Umdrehungen pro Sekunde |
| `text` | string | `null` | sichtbarer Begleittext (Variante `mit-text`) |
| `inline` | boolean | `false` | Größe an Schriftzeile angepasst |

## Events

Es werden keine Events genutzt; ein Spinner ist reine Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | nur nötig, wenn der Spinner eine Aktion benennt („Wird gespeichert“) |
| `role` | string | `status` |
| – | – | Der **wartende Bereich** erhält `aria-busy="true"`, nicht der Spinner allein |

## Geerbt von

`id`, `visible`, `size`, `theme`, `state`, `animation`, `aria-*` →
[Basiskomponente](../../basics/base/)
