# Übergang (Transition)

Übergangs-Animationen verändern einen bestehenden Zustand, ohne Elemente zu erzeugen oder zu entfernen.
Beide Zustände gehören zur selben Fläche; die Animation macht die Änderung nachvollziehbar.

## Elemente

- **flip** – um 180° drehen (Vorder- und Rückseite)
- **rotate** – um die eigene Achse drehen
- **morph** – eine Form sanft in eine andere Form überführen
- **cross-fade** – zwei Elemente blenden ineinander über
- **cross-slide** – zwei Elemente schieben einander aus dem Bild
- **reorder** – Listenelemente tauschen sanft ihre Plätze (FLIP)

## Auswahl

| Änderung | Animation |
|--------|-----------|
| gleiches Element, neue Form | morph |
| anderes Element, ohne Richtungsbezug | cross-fade |
| anderes Element, mit einer Reihenfolge | cross-slide |
| zwei Seiten eines Objekts | flip |
| die Reihenfolge ändert sich | reorder |
| der Winkel ändert sich | rotate (dauerhaft als [Spin](../loop/spin/description.md)) |

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Einblenden](../entrance/), [Ausblenden](../exit/)
- [Tabs](../../../components/widgets/navigation/tabs/description.md), [Akkordeon](../../../components/widgets/containers/accordion/description.md)
