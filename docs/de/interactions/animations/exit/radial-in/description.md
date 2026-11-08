# Radial In

## Beschreibung

Radial In ist die Gegenrichtung zu Radial Out: Die Punkte eines Kreismenüs wandern von ihren
Ringpositionen zurück zum Ankerkern, schrumpfen dabei auf `scale 0` und verschwinden durch
abnehmende Deckkraft. Die äußeren Ringe lösen sich zuerst auf, der innerste zuletzt. Das Menü
zieht sich radial in den Anker zurück, als wäre es nie weg gewesen. Der Ankerkern selbst bleibt
am längsten stehen oder verschwindet zuletzt.

## Verwendung

- ein Kreismenü schließen, wenn der Zeiger den Bereich verlässt (nach `closeDelay`)
- Unterpunkt-Ringe klappen ein, wenn sich der aktive Punkt ändert; nur der betroffene
  Zweig wandert zurück
- Speed Dial an einer Ecke oder Kante: Die Punkte treten wieder in die Fläche zurück
- `Esc` oder die Auswahl eines Punktes: Das Menü zieht sich radial zurück
- Markergruppen auf Karten wieder zu einem Punkt zusammenziehen

## Dauer

- Typisch: 120–200 ms (Austritte dürfen kürzer sein als Eintritte)
- Standardwert: 160 ms
- Versatz zwischen den Punkten: 8–15 ms
- Versatz zwischen den Ringen: 40–60 ms (von außen nach innen)

## Unterschied zu Radial Out und Pop Out

- Radial Out bewegt die Punkte vom Anker weg bis zu ihrer Endgröße; Radial In führt sie
  zurück und endet bei Größe 0.
- Pop Out lässt ein einzelnes Element an seiner Stelle verschwinden; Radial In bewegt alle
  Punkte zum gemeinsamen Anker zurück. Die Bewegung nach innen zeigt, woher das Menü kam.
- Nach `onAnimateEnd` wird das Menü aus dem Layout genommen; bis dahin bleibt die Trefferfläche
  erhalten (die Wegtoleranz des
  [Radial Menu](../../../../components/widgets/navigation/radial-menu/description.md)).
