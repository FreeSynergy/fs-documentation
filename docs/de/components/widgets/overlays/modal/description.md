# Modal (Modaler Dialog)

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base` |
| **Varianten** | `Small`, `Medium`, `Large`, `Fullscreen` |
| **Zustände** | `open`, `dirty` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in`, `pop-in`, `slide-out` |
| **Verwandt** | `alert-dialog`, `drawer`, `popover`, `wizard` |
| **Status** | dokumentiert |

## Beschreibung
Ein Modal ist ein Overlay-Fenster mit Fokus auf Inhalt.

## Verwendungszweck

- Bestätigungen
- Formulare
- Bearbeitungsdialoge

## Varianten

| Variant | Größe | Beschreibung |
|---------|-------|--------------|
| **Small** | - | Formulare, Bestätigungen |
| **Medium** | - | Bearbeitungsdialoge |
| **Large** | - | Komplette Ansichten |
| **Fullscreen** | - | Komplette Ansicht |

## Features

- Header
- Body
- Footer
- Close
- Dismissible

## Abgrenzung

- **Nicht verwechseln mit** [alert-dialog](../alert-dialog/): der Alert-Dialog fragt eine
  Entscheidung ab, hat kaum Inhalt und ist nicht durch Klick außerhalb schließbar; das Modal
  trägt Inhalt oder ein Formular.
- **Nicht verwechseln mit** [drawer](../drawer/): der Drawer kommt von einer Kante und bringt
  Navigation; das Modal sitzt zentriert und verlangt Aufmerksamkeit.
- **Nicht verwechseln mit** [popover](../popover/): ein Popover sperrt den Rest der Seite nicht.
- **Nicht verwechseln mit** [wizard](../../containers/wizard/): mehrere Schritte hinterein-
  ander sind ein Wizard — auch wenn er in einem Modal läuft.
- Gesperrter Fokus und Hintergrund-Scroll sind Teil dieser Komponente, keine Zusatzbibliothek.

## Best Practices

- Clear-Content
- Close-Button
- Accessibility
- Feedback

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Alert Dialog](../alert-dialog/) — Bestätigung ohne Inhalt
- [Drawer](../drawer/) — Overlay an der Kante
- [Basiskomponente](../../basics/base/)
