# Radial Out

## Beschreibung

Radial Out lässt die Punkte eines kreisförmigen Menüs aus dem Ankerkern nach außen treten. Jeder Punkt startet klein (`scale 0`) in der Mitte des Ankers, wandert auf dem Strahl seines Winkels zu seiner Ringposition und wächst dabei auf seine Endgröße. Die Punkte eines Rings starten versetzt im Uhrzeigersinn. Ein weiterer Ring folgt kurz danach, sobald sein Elternpunkt sich gesetzt hat. Das Menü "öffnet sich" radial – die Richtung zu einem Punkt ist schon von der ersten Millisekunde an erkennbar.

## Verwendung

- ein kreisförmiges Menü öffnen (Hover, Tippen, Rechtsklick) – alle Punkte treten aus dem Anker
- Unterpunkte schieben sich als nächster Ring vom aktiven Punkt nach außen
- Speed-Dial oder Fächer an einer Ecke oder Kante: die Punkte treten aus der Ecke in die Fläche
- Launcher in der Bildschirmmitte: die Ringe bauen sich von innen nach außen auf
- Markergruppen auf Karten entfalten sich radial um einen Punkt

## Dauer

- Typisch: 180–260 ms pro Ring
- Standardwert: 220 ms
- Versatz zwischen den Punkten: 12–25 ms
- Versatz zwischen den Ringen: 60–90 ms

## Unterschied zu Pop In und Stagger

- Pop In lässt ein Element an seiner festen Position überschwingen. Radial Out bewegt die Punkte vom Ankermittelpunkt zu ihren Ringpositionen – Position und Größe ändern sich zusammen.
- Stagger verteilt nur die Startzeiten innerhalb einer Bewegung. Radial Out ist selbst die Bewegung. Beides zusammen: `staggerStep` staffelt die Punkte, `ringStep` die Ringe (siehe [Stagger](../../organization/stagger/description.md)).
