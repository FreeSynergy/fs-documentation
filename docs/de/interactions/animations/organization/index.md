# Organisation

Organisations-Animationen bewegen selbst nichts. Sie verteilen Startzeiten auf mehrere
untergeordnete Elemente und entscheiden so, in welcher Reihenfolge andere Animationen erscheinen.

## Elemente

- **stagger** – untergeordnete Elemente starten versetzt zueinander (fester Abstand je Index)
- **cascade** – ein versetzter Start entlang einer Richtung, mit wachsendem oder schrumpfendem Schritt

## Kombination

Die eigentliche Bewegung kommt aus einer anderen Kategorie:

| Kombination | Wirkung |
|-------------|---------|
| [Fade In](../entrance/fade-in/description.md) + Stagger | die Liste baut sich sanft auf |
| [Expand](../entrance/expand/description.md) + Cascade | das Menü kaskadiert von der Leiste nach unten |
| [Pop Out](../exit/pop-out/description.md) + Cascade | die Fläche leert sich wie eine Welle |
| [Scale In](../entrance/scale-in/description.md) + Stagger | das Raster füllt sich nacheinander |

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Einblenden](../entrance/), [Ausblenden](../exit/)
- [grid-view](../../../components/widgets/data/grid-view/description.md) – ein Raster stufenweise aufbauen
