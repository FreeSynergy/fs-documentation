# Empty State (Leerzustand)

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

Ein Empty State erklärt, warum eine Fläche keinen Inhalt hat. Er zeigt den Weg zum
ersten Inhalt. Er ersetzt die leere Liste durch eine kurze Aussage und eine Aktion.

## Verwendungszweck

- Erste Nutzung eines Bereichs, noch ohne Daten
- Suche oder Filter ohne Treffer
- Bereich vorübergehend nicht verfügbar (Fehler, fehlende Berechtigung)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **leer** | noch keine Daten, eine Aktion zum Anlegen |
| **kein-treffer** | der Filter liefert nichts, eine Aktion zum Zurücksetzen |
| **fehler** | Inhalt konnte nicht geladen werden, eine Aktion zum Wiederholen |

## Funktionen

- Icon oder Illustration, ein Satz Erklärung, eine Hauptaktion
- Ein sekundärer Verweis für Hilfe oder Tastenkürzel
- Zentriert in der verfügbaren Höhe, Mindesthöhe 200 px

## Abgrenzung

- **Nicht verwechseln mit** [skeleton](../skeleton/): Ein Skeleton zeigt, dass Inhalt
  unterwegs ist. Der Empty State zeigt, dass keiner da ist.
- **Nicht verwechseln mit** [alert](../alert/): Eine Meldung stört eine bestehende
  Ansicht. Der Empty State ist selbst die Ansicht.

## Best Practices

- Genau eine Hauptaktion, im Wortlaut des Bereichs („Erste Aufgabe anlegen“).
- Nicht allgemein erklären, was der Bereich kann. Nur sagen, warum er leer ist.
- Bei Filtern den Filterwert zeigen und anbieten, ihn zurückzusetzen.

## Siehe auch

- [Skeleton](../skeleton/)
- [Alert](../alert/)
- [Base-Komponente](../../basics/base.md)
