# Radial In

## Beschreibung

Radial In ist die Gegenrichtung von Radial Out: Die Punkte eines Kreismenüs wandern
von ihren Ringpositionen zurück zum Ankerkern, schrumpfen dabei auf `scale 0` und
verschwinden durch abnehmende Deckkraft. Äußere Ringe lösen sich zuerst auf, der
innenliegende zuletzt — das Menü zieht sich in den Anker zurück, als wäre es nie
weggewesen. Der Ankerkern selbst bleibt am längsten stehen oder verschwindet zuletzt.

## Verwendung

- Kreismenü schließen, wenn der Zeiger den Bereich verlässt (nach `closeDelay`)
- Unterpunkt-Ringe klappen ein, wenn der aktive Punkt wechselt — nur der betroffene
  Zweig wandert zurück
- Speed-Dial an Ecke oder Kante: Punkte treten zurück aus der Fläche heraus
- `Esc` oder Auswahl eines Punktes: Menü zieht sich radienförmig zurück
- Marker-Gruppen auf Karten wieder zu einem Punkt einsammeln

## Dauer

- Typisch: 120–200 ms (Ausgänge dürfen kürzer sein als Eingänge)
- Standardwert: 160 ms
- Staffelung zwischen Punkten: 8–15 ms
- Versatz zwischen Ringen: 40–60 ms (von außen nach innen)

## Unterschied zu Radial Out und Pop Out

- Radial Out bewegt Punkte vom Anker weg bis auf Endgröße; Radial In führt sie zurück
  und endet bei Größe 0.
- Pop Out klappt ein einzelnes Element an seiner Position weg; Radial In bewegt alle
  Punkte zurück zum gemeinsamen Anker — der Weg nach innen zeigt, wo das Menü herkam.
- Nach `onAnimateEnd` wird das Menü aus dem Layout genommen; bis dahin bleibt der
  Trefferbereich bestehen (Wegfahr-Toleranz des [Radial Menu](../../../components/navigation/radial-menu/description.md)).
