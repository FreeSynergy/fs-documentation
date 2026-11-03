# Checkbox (Ankreuzfeld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `Default`, `Toggle`, `Indeterminate` |
| **Zustände** | `checked`, `indeterminate` |
| **Gesten** | `tap` |
| **Animationen** | `tick-draw`, `press` |
| **Verwandt** | `switch`, `radio-group`, `field`, `base` |
| **Status** | dokumentiert |

## Beschreibung
Ein Checkbox ist ein Ja/Nein- oder Mehrfachauswahlfeld.

## Verwendungszweck

- Einstellungen
- Optionen
- Zustimmung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Default** | Standard-Quadrat mit Häkchen |
| **Toggle** | Kasten ohne Häkchen, Auswahl ist flächig hervorgehoben |
| **Indeterminate** | Gemischter Zustand – einige, aber nicht alle Unteroptionen ausgewählt |

## Features

- Checked
- Indeterminate
- Disabled

## Abgrenzung

- **Nicht verwechseln mit** [switch](../switch/): der Schalter wendet die Änderung sofort an,
  die Checkbox bestätigt eine Auswahl, die erst beim Absenden des Formulars wirkt.
- **Nicht verwechseln mit** [radio-group](../radio-group/): Radio erlaubt genau eine Auswahl
  aus mehreren, die Checkbox mehrere gleichzeitig.
- Eine Einzel-Checkbox für "ein/aus" bleibt trotzdem eine Checkbox, wenn der Nutzer
  zwischendurch speichern kann (Formular-Kontext).

## Best Practices

- Label immer an die Box binden – ein Klick auf den Text schaltet mit.
- `indeterminate` nur für Gruppenköpfe verwenden; der gespeicherte Wert bleibt `false`.
- Zustandsänderung animieren (`tick-draw`), aber Bewegung nie als einzigen Hinweis auf den Zustand.
- Fehler erst nach dem Verlassen des Feldes anzeigen, nicht beim ersten leeren Zustand.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)
