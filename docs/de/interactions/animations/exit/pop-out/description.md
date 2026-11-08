# Pop Out

## Beschreibung

Pop Out ist die Gegenrichtung zu Pop In: Das Element nimmt kurz Anlauf (eine winzige Vergrößerung),
schrumpft dann unter seine endgültige Größe und verschwindet dabei durch abnehmende Deckkraft.
Es wirkt wie „weggeschnippt“ und gibt seinen Platz im Layout erst am Ende der Animation auf.

## Verwendung

- Chips und Filtermarken entfernen, wenn der Nutzer die Auswahl aufhebt
- einen Avatar aus einer Teilnehmerliste nehmen (ein Teilnehmer verlässt den Raum)
- einen Zähler-Badge auf einem Icon auflösen
- eine Liste von Elementen auflösen, die nach und nach eingeklappt werden
- abgewählte Marker auf einer Karte entfernen
- Onboarding-Pins verschwinden lassen, nachdem ihre Erklärung abgeschlossen ist

## Dauer

- Typisch: 150–250 ms (Austritte dürfen kürzer sein als Eintritte)
- Mikro (Badge, Zähler): 120–180 ms
- Mehrere Elemente hintereinander: 150 ms plus ein Stagger, siehe
  [Cascade](../../organization/cascade/description.md)

## Unterschied zu Pop In

- Pop In schießt über die endgültige Größe hinaus und endet ruhig; Pop Out nimmt zuerst kurz
  Anlauf und endet bei Größe 0.
- Pop In endet sichtbar, Pop Out entfernt das Element aus dem Layout
  (`display: none` nach `onAnimateEnd`).
