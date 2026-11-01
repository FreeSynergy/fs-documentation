# Color Input (Farbfeld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `palette`, `spectrum`, `code` |
| **Zustände** | `open`, `error` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `fade-in`, `expand` |
| **Verwandt** | `emoji-picker`, `field`, `base` |
| **Status** | dokumentiert |

## Beschreibung
Ein Color Input ist ein Farbauswahl-Feld mit Farbpicker.

## Verwendungszweck

- Farbe wählen
- Farb-themes
- Farb-Code

## Features

- Farbpalette
- Farbspektrum
- Hex-Code

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **palette** | Raster mit vorausgewählten Farben (Marken- und Themenfarben) |
| **spectrum** | Freie Wahl über Farbfläche und Farbton-Slider |
| **code** | nur Textfeld für Hex-, RGB- oder HSL-Wert |

## Abgrenzung

- **Nicht verwechseln mit** [emoji-picker](../emoji-picker/): beide öffnen ein Auswahl-Overlay,
  der Emoji-Picker wählt Zeichen, dieser Farbwerte.
- Der eigentliche Overlay-Charakter (Farbfläche außerhalb des Feldes) macht die Farbe
  nicht zu einem reinen Feld: Das Feld selbst ist `code`, der Rest verhält sich wie ein Picker.
- Reine Anzeige von Farben (ohne Auswahl) gehört in [badge](../../feedback/badge/)
  bzw. in die Farb-Token, nicht hierher.

## Best Practices

- In Anwendungen nur `palette` anbieten; freie Farbwahl (`spectrum`) bleibt Design-Werkzeugen
  und dem Editor vorbehalten.
- Immer beide Formen zeigen: Farbfeld und Textwert, damit Werte nachträglich korrigierbar bleiben.
- Kontrast zum Untergrund prüfen; bei sehr hellen oder sehr dunklen Farbwerten den Rand verstärken.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)
