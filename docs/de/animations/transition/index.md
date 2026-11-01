# Zustandswechsel (transition)

Übergangsanimationen verändern einen bestehenden Zustand, ohne Elemente zu erzeugen oder
zu entfernen. Beide Zustände sind derselben Fläche zugeordnet; die Animation macht den
Wechsel nachvollziehbar.

## Elemente

- **flip** - um 180° drehen (Vorder- und Rückseite)
- **rotate** - um die eigene Achse drehen
- **morph** - Form weich in eine andere Form wandeln
- **cross-fade** - zwei Elemente überblenden einander
- **cross-slide** - zwei Elemente schieben sich gegenseitig aus dem Bild
- **reorder** - Listenelemente tauschen weich ihre Plätze (FLIP)

## Auswahl

| Wechsel | Animation |
|---------|-----------|
| gleiches Element, neue Form | morph |
| anderes Element, kein Richtungsbezug | cross-fade |
| anderes Element, mit Reihenfolge | cross-slide |
| zwei Seiten eines Objekts | flip |
| Reihenfolge ändert sich | reorder |
| Winkel ändert sich | rotate (dauerhaft als [Spin](../loop/spin/description.md)) |

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Eingang (entrance)](../entrance/), [Ausgang (exit)](../exit/)
- [Tabs](../../components/navigation/tabs/description.md), [Accordion](../../components/containers/accordion/description.md)
