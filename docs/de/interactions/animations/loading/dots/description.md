# Dots

## Beschreibung

Dots zeigt drei punktförmige Elemente, die sich in gleichmäßigem Rhythmus heben, senken oder aufleuchten. Der Indikator sagt: Gerade läuft etwas, aber es gibt keinen messbaren Fortschritt. Er ist die kompakte Alternative zum Spinner, wenn der Platz klein ist oder die Wartezeit kurz ist.

## Verwendung

- Ladezustand in einem Button ("Speichern …")
- kurze Anfragen in Panels, für die sich ein Skeleton nicht lohnt
- Warten auf eine Antwort in einer Liste oder einem Suchfeld
- Anzeige, dass gerade eine Verbindung aufgebaut wird
- inaktive Tabs, deren Inhalt noch nicht geladen ist
- als Baustein für den Schreibindikator, siehe [Typing](../typing/description.md)

## Dauer

- Typisch: 1200–1600 ms pro Zyklus
- Ein einzelner Puls: 400–600 ms
- Ab 10 s ohne Ergebnis auf [Skeleton](../skeleton/description.md) oder
  [Progress](../progress/description.md) wechseln

## Unterschied zu Typing und Spinner

- Typing ahmt einen tippenden Menschen mit unregelmäßigem Rhythmus nach und reagiert auf eine Nachricht. Dots läuft gleichmäßig und zeigt Systemaktivität.
- Spin dreht eine Fläche um ihre Achse und braucht eine bestimmte Größe. Dots funktioniert schon in Zeilenhöhe und neben Text.
