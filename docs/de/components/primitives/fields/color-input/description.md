# Farbfeld

| Feld | Wert |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `palette`, `spectrum`, `code` |
| **States** | `open`, `error` |
| **Gestures** | `tap`, `drag` |
| **Animations** | `fade-in`, `expand` |
| **Related** | `emoji-picker`, `field`, `base` |
| **Status** | documented |

## Beschreibung
Ein Farbfeld ist ein Feld zur Farbauswahl mit einem Farbwähler.

## Zweck

- Eine Farbe auswählen
- Farbthemen
- Farbcode

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **palette** | Raster mit vorgewählten Farben (Marken- und Themenfarben) |
| **spectrum** | freie Wahl über eine Farbfläche und einen Farbtonregler |
| **code** | nur ein Textfeld für einen Hex-, RGB- oder HSL-Wert |

## Funktionen

- Farbpalette
- Farbspektrum
- Hex-Code

## Abgrenzung

- **Nicht verwechseln mit** [emoji-picker](../../../widgets/fields/emoji-picker/): beide öffnen ein
  Auswahl-Overlay, der Emoji-Picker wählt Zeichen, dieses Feld Farbwerte.
- Das eigentliche Overlay (eine Farbfläche außerhalb des Feldes) macht die Farbe nicht zu einem reinen Feld: das Feld selbst ist
  `code`, der Rest verhält sich wie ein Picker.
- Farben nur anzeigen (ohne Auswahl) gehört zu [badge](../../feedback/badge/)
  oder zu den Farb-Tokens, nicht hierher.

## Best Practices

- In Anwendungen nur `palette` anbieten; die freie Farbwahl (`spectrum`) bleibt Designwerkzeugen und dem Editor vorbehalten.
- Immer beide Formen zeigen: Farbmuster und Textwert, damit Werte später korrigierbar bleiben.
- Den Kontrast zum Hintergrund prüfen; bei sehr hellen oder sehr dunklen Farbwerten den Rahmen verstärken.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Basiskomponente](../../basics/base.md)
