# Modal

| Field | Value |
| ------ | ------ |
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `Small`, `Medium`, `Large`, `Fullscreen` |
| **States** | `open`, `dirty` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `pop-in`, `slide-out` |
| **Related** | `alert-dialog`, `drawer`, `popover`, `wizard` |
| **State** | documented |

## Description
Ein Modal ist ein Overlay-Fenster mit Fokus auf Inhalt.

## Purpose

- Bestätigungen
- Formulare
- Bearbeitungsdialoge

## Variants

| Variant | Size | Description |
| --------- | ------- | -------------- |
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

## Distinction

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

## See also

- [overlays – overview](../index.md)
- [Alert Dialog](../alert-dialog/) — Bestätigung ohne Inhalt
- [Drawer](../drawer/) — Overlay an der Kante
- [Base component](../../../primitives/basics/base.md)
