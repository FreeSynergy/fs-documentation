# Radial Out

## Beschreibung

Radial Out lässt die Punkte eines Kreismenüs aus dem Ankerkern heraus nach außen
treten: Jeder Punkt startet klein (`scale 0`) an der Ankermitte, wandert entlang
seines Winkelstrahls auf seine Ringposition und wächst dabei auf seine Endgröße.
Die Punkte eines Ringes starten gestaffelt im Uhrzeigersinn, ein weiterer Ring
setzt ein, kurz nachdem sein Elternpunkt steht. Das Menü „blüht“ radienförmig auf —
die Richtung zum Punkt ist von der ersten Millisekunde an lesbar.

## Verwendung

- Kreismenü öffnen (Hover, Tipp, Rechtsklick) — alle Punkte treten aus dem Anker heraus
- Unterpunkte schieben sich als nächster Ring aus dem aktiven Punkt nach außen
- Speed-Dial / Fächer an Ecke oder Kante: Punkte treten aus der Ecke in die Fläche
- Launcher in der Bildschirmmitte, Ringe bauen sich von innen nach außen auf
- Marker-Gruppen auf Karten entfalten sich radienförmig um einen Punkt

## Dauer

- Typisch: 180–260 ms pro Ring
- Standardwert: 220 ms
- Staffelung zwischen Punkten: 12–25 ms
- Versatz zwischen Ringen: 60–90 ms

## Unterschied zu Pop In und Stagger

- Pop In lässt ein Element an seiner festen Position überschießen; Radial Out bewegt
  Punkte von der Ankermitte zu ihren Ringpositionen — Position und Größe ändern gemeinsam.
- Stagger verteilt nur Startzeitpunkte innerhalb einer Bewegung; Radial Out ist die
  Bewegung selbst. Beides kombiniert: `staggerStep` staffelt die Punkte, `ringStep`
  die Ringe (siehe [Stagger](../../organization/stagger/description.md)).
