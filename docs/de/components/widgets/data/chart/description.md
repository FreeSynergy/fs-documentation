# Chart

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
| **radar** | mehrere Dimensionen eines Objekts |

## Funktionen

- Interaktiv
- Responsiv
- Animationen
- Export

## Abgrenzung

- **Nicht verwechseln mit** [table](../table/): die Tabelle ist die verlässliche Art, Zahlen zu sehen,
  das Chart nur die ergänzende Form. Beides zusammen ist richtig, das Chart allein nicht.
- **Nicht verwechseln mit** [progress](../../../primitives/feedback/progress/): ein Balken zeigt einen Anteil,
  ein Chart vergleicht Werte.
- **Nicht verwechseln mit** [dashboard](../../../workbenches/special/dashboard/): das Dashboard ordnet mehrere
  Charts und Karten an, es zeichnet selbst nichts.

## Best Practices

- Zeitreihen als Linie, Vergleiche als Balken, Anteile als Kreis nur bei höchstens fünf Kategorien.
- Beschrifte die Achsen und Einheiten; ein Chart ohne Achsenbeschriftung ist Dekoration.
- Nimm die Farben aus den Farb-Tokens der Anwendung und mische sie nicht frei; setze die Legende
  neben die Zeichnung.
- Biete immer eine numerische Alternative (Tabelle oder einzelne Werte) an, damit die Information
  nicht nur visuell verfügbar ist.
- Kennzeichne leere Daten als `leer` mit einem Hinweis, lass keine leere Fläche stehen.

## Siehe auch

- [data – Übersicht](../index.md)
- [Table](../table/) — Zahlen in Zeilen und Spalten
- [Dashboard](../../../workbenches/special/dashboard/) — Anordnung mehrerer Charts
- [Basiskomponente](../../../primitives/basics/base.md)
