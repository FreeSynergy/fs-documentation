# Checkbox

| Feld | Wert |
|-------|-------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `Default`, `Toggle`, `Indeterminate` |
| **Zustände** | `checked`, `indeterminate` |
| **Gesten** | `tap` |
| **Animationen** | `tick-draw`, `press` |
| **Verwandt** | `switch`, `radio-group`, `field`, `base` |
| **Status** | dokumentiert |

## Beschreibung
Eine Checkbox ist ein Ja/Nein- oder Mehrfachauswahl-Feld.

## Verwendungszweck
- Einstellungen
- Optionen
- Zustimmung

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Default** | normales Quadrat mit Haken |
| **Toggle** | Kästchen ohne Haken, die Auswahl wird als Fläche hervorgehoben |
| **Indeterminate** | gemischter Zustand – einige, aber nicht alle Unteroptionen ausgewählt |

## Funktionen

- Ausgewählt
- Teilweise ausgewählt
- Deaktiviert

## Abgrenzung

- **Nicht verwechseln mit** [switch](../switch/): der Schalter wirkt
  sofort, die Checkbox bestätigt eine Auswahl, die erst beim Absenden des
  Formulars greift.
- **Nicht verwechseln mit** [radio-group](../radio-group/): Radio erlaubt genau eine
  Wahl aus mehreren, die Checkbox erlaubt mehrere gleichzeitig.
- Eine einzelne Checkbox für „an/aus“ bleibt eine Checkbox, wenn die Person dazwischen speichern kann
  (Formularkontext).

## Best Practices

- Die Beschriftung immer mit dem Kästchen verbinden – ein Klick auf den Text schaltet es ebenfalls um.
- `indeterminate` nur für Gruppenköpfe nutzen; der gespeicherte Wert bleibt `false`.
- Den Zustandswechsel animieren (`tick-draw`), aber Bewegung nie als einzigen Hinweis auf den Zustand nutzen.
- Fehler erst zeigen, wenn das Feld verlassen wurde, nicht schon beim ersten leeren Zustand.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Basiskomponente](../../basics/base.md)
