# Modal

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
Ein Modal ist ein Overlay-Fenster mit Fokus auf dem Inhalt.

## Verwendungszweck

- Bestätigungen
- Formulare
- Bearbeitungsdialoge

## Varianten

| Variante | Größe | Beschreibung |
|----------|-------|--------------|
| **Small** | - | Formulare, Bestätigungen |
| **Medium** | - | Bearbeitungsdialoge |
| **Large** | - | vollständige Ansichten |
| **Fullscreen** | - | vollständige Ansicht |

## Funktionen

- Kopfbereich
- Inhalt
- Fußbereich
- Schließen
- Wegwischbar

## Abgrenzung

- **Nicht verwechseln mit** [alert-dialog](../alert-dialog/): der Bestätigungsdialog verlangt eine
  Entscheidung, hat kaum Inhalt und lässt sich nicht per Klick außerhalb schließen; das Modal trägt
  Inhalte oder ein Formular.
- **Nicht verwechseln mit** [drawer](../drawer/): der Drawer kommt von einem Rand und bringt
  Navigation; das Modal steht zentriert und fordert Aufmerksamkeit.
- **Nicht verwechseln mit** [popover](../popover/): ein Popover sperrt den Rest der Seite nicht.
- **Nicht verwechseln mit** [wizard](../../containers/wizard/): mehrere Schritte hintereinander sind ein
  Wizard — auch dann, wenn er in einem Modal läuft.
- Gesperrter Fokus und blockiertes Scrollen des Hintergrunds gehören zu dieser Komponente, sie sind keine
  zusätzliche Bibliothek.

## Best Practices

- Klarer Inhalt
- Schließen-Schaltfläche
- Barrierefreiheit
- Rückmeldung

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Alert Dialog](../alert-dialog/) — Bestätigung ohne Inhalt
- [Drawer](../drawer/) — Overlay am Rand
- [Basiskomponente](../../../primitives/basics/base.md)
