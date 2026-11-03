# Empty State (Leerer Zustand)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `leer`, `kein-treffer`, `fehler` |
| **Zustände** | `loading` |
| **Gesten** | `tap` |
| **Animationen** | `fade-in` |
| **Verwandt** | `skeleton`, `spinner`, `progress` |
| **Rolle** | `status` |
| **Status** | dokumentiert |

## Beschreibung

Ein leerer Zustand erklärt, warum eine Fläche ohne Inhalt ist, und zeigt den Weg zum
ersten Inhalt. Er ersetzt die leere Liste durch eine kurze Aussage und eine Aktion.

## Verwendungszweck

- Erste Nutzung eines Bereichs noch ohne Daten
- Suche oder Filter ohne Treffer
- Bereich zeitweise nicht verfügbar (Fehler, fehlende Berechtigung)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **leer** | noch keine Daten, Aktion zum Anlegen |
| **kein-treffer** | Filter liefert nichts, Aktion zum Zurücksetzen |
| **fehler** | Inhalt konnte nicht geladen werden, Aktion zum Wiederholen |

## Features

- Icon oder Illustration, ein Satz Erklärung, eine Hauptaktion
- Sekundärer Verweis für Hilfe oder Kürzel
- Zentriert in der verfügbaren Höhe, Höhe mindestens 200 px

## Abgrenzung

- **Nicht verwechseln mit** [skeleton](../skeleton/): Skeleton zeigt an, dass Inhalt
  unterwegs ist; der leere Zustand, dass keiner da ist.
- **Nicht verwechseln mit** [alert](../alert/): eine Meldung stört eine vorhandene
  Ansicht, der leere Zustand ist die Ansicht.

## Best Practices

- Genau eine Hauptaktion, in der Sprache des Bereichs („Erste Aufgabe anlegen“).
- Nicht erklären, was der Bereich allgemein kann — nur, warum er leer ist.
- Bei Filtern den Filterwert anzeigen und das Zurücksetzen anbieten.

## Siehe auch

- [Skeleton](../skeleton/)
- [Alert](../alert/)
- [Basiskomponente](../../basics/base/)
