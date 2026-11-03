# Chart (Diagramm)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `line`, `bar`, `pie`, `doughnut`, `scatter`, `heatmap`, `radar` |
| **Zustände** | `leer`, `wartend` |
| **Gesten** | `tap`, `drag`, `pinch`, `swipe` |
| **Animationen** | `highlight`, `fade-in`, `progress` |
| **Verwandt** | `table`, `description-list`, `dashboard`, `skeleton` |
| **Status** | dokumentiert |

## Beschreibung
Ein Chart ist eine Datenvisualisierung (Diagramme).

## Verwendungszweck

- Statistiken
- Diagramme
- Grafiken

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **line** | Verlauf über die Zeit |
| **bar** | Vergleich einzelner Werte |
| **pie** | Anteil an einem Ganzen |
| **doughnut** | Anteil mit Freifläche für eine Gesamtzahl |
| **scatter** | zwei Größen gegeneinander |
| **heatmap** | Dichte über zwei Achsen |
| **radar** | mehrere Dimensionen einer Entität |

## Features

- Interaktiv
- Responsive
- Animations
- Export

## Abgrenzung

- **Nicht verwechseln mit** [table](../table/): die Tabelle ist die verlässliche Zahlenansicht,
  das Diagramm nur die ergänzende Form. Beides zusammen ist richtig, das Diagramm allein nicht.
- **Nicht verwechseln mit** [progress](../../feedback/progress/): ein Balken zeigt einen Anteil,
  ein Diagramm vergleicht Werte.
- **Nicht verwechseln mit** [dashboard](../../special/dashboard/): das Dashboard ordnet mehrere
  Diagramme und Karten, es zeichnet selbst nichts.

## Best Practices

- Zeitreihen als Linie, Vergleiche als Balken, Anteile nur bei maximal fünf Kategorien als Kreis.
- Achsen und Einheiten beschriften; ein Diagramm ohne Achsenbeschriftung ist Dekoration.
- Farben aus den Farbtoken der Anwendung, nicht frei gemischt; Legende neben der Zeichnung.
- Immer eine Zahlenalternative anbieten (Tabelle oder Einzelwerte), damit die Information
  nicht nur visuell verfügbar ist.
- Leere Daten als `leer` mit Hinweis beschriften, nicht als leere Fläche stehen lassen.

## Siehe auch

- [data – Übersicht](../index.md)
- [Table](../table/) — Zahlen in Zeilen und Spalten
- [Dashboard](../../special/dashboard/) — mehrere Diagramme anordnen
- [Basiskomponente](../../basics/base/)
