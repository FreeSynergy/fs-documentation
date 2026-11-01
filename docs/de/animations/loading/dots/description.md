# Dots

## Beschreibung

Dots zeigt drei punktförmige Elemente, die in festem Takt ansteigen, abfallen oder aufleuchten. Der Indikator sagt: Etwas läuft gerade, aber es gibt keinen messbaren Fortschritt. Er ist die kompakte Alternative zum Spinner, wenn der Platz klein oder der erwartete Zeitraum kurz ist.

## Verwendung

- Ladezustand in einem Button („Speichern …“)
- Kurze Anfragen in Panels, für die sich kein Skeleton lohnt
- Warten auf eine Antwort in einer Liste oder einem Suchfeld
- Anzeige, dass eine Verbindung gerade aufgebaut wird
- Inaktive Tabs, deren Inhalt noch nicht geladen ist
- Als Baustein für den Tipp-Indikator, siehe [Typing](../typing/description.md)

## Dauer

- Typisch: 1200–1600 ms pro Zyklus
- Einzelner Impuls: 400–600 ms
- Ab 10 s ohne Ergebnis auf [Skeleton](../skeleton/description.md) oder [Progress](../progress/description.md) wechseln

## Unterschied zu Typing und Spinner

- Typing imitiert mit unregelmäßigem Rhythmus das Tippen eines Menschen und antwortet auf eine Nachricht; Dots läuft gleichmäßig und signalisiert Systemaktivität.
- Spin dreht eine Fläche um ihre Achse und braucht eine gewisse Größe; Dots funktioniert schon in Zeilenhöhe und neben Text.
