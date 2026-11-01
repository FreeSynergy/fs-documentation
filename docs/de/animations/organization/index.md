# Organisation (organization)

Organisationsanimationen bewegen nichts selbst. Sie verteilen Startzeitpunkte über mehrere
Kind-Elemente und bestimmen damit, in welcher Reihenfolge andere Animationen erscheinen.

## Elemente

- **stagger** - Kind-Elemente starten nacheinander versetzt (fester Offset pro Index)
- **cascade** - versetzter Start entlang einer Richtung, mit wachsender oder schrumpfender Schrittweite

## Kombination

Die eigentliche Bewegung kommt aus einer anderen Kategorie:

| Kombination | Wirkung |
|-------------|---------|
| [Fade In](../entrance/fade-in/description.md) + Stagger | Liste baut sich weich auf |
| [Expand](../entrance/expand/description.md) + Cascade | Menü kaskadiert von der Leiste |
| [Pop Out](../exit/pop-out/description.md) + Cascade | Fläche leert sich als Welle |
| [Scale In](../entrance/scale-in/description.md) + Stagger | Raster füllt sich der Reihe nach |

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Eingang (entrance)](../entrance/), [Ausgang (exit)](../exit/)
- [grid-view](../../components/data/grid-view/description.md) - Raster gestaffelt aufbauen
