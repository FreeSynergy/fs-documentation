# Pop Out

## Beschreibung

Pop Out ist die Gegenrichtung von Pop In: Das Element holt kurz aus (winzige Vergrößerung), schrumpft dann unter die Endgröße und verschwindet dabei durch abnehmende Deckkraft. Es wirkt „weggeschnipst“ und gibt seinen Platz im Layout erst am Ende der Animation frei.

## Verwendung

- Chips und Filterlabels entfernen, wenn der Nutzer eine Auswahl aufhebt
- Avatar aus einer Teilnehmerliste nehmen (Teilnehmer verlässt den Raum)
- Zähler-Badge an einem Icon auflösen
- Liste von Elementen auflösen, die einzeln weggeklappt werden
- Abgewählte Markierungen auf einer Karte entfernen
- Onboarding-Pins nach der Erklärung verschwinden lassen

## Dauer

- Typisch: 150–250 ms (Ausgänge dürfen kürzer sein als Eingänge)
- Mikro (Badge, Zähler): 120–180 ms
- Mehrere Elemente in Folge: 150 ms plus Staffelung, siehe [Cascade](../../organization/cascade/description.md)

## Unterschied zu Pop In

- Pop In schießt über die Endgröße hinaus und endet ruhig; Pop Out holt zuerst kurz aus und endet bei Größe 0.
- Pop In endet sichtbar, Pop Out entfernt das Element aus dem Layout (`display: none` nach `onAnimateEnd`).
