# Rubber Band

## Beschreibung

Rubber Band zeigt den Widerstand einer scrollbaren Fläche, wenn sie zu weit gezogen wird. Zieht
der Nutzer über den Rand hinaus, folgt der Inhalt nur gedämpft. Nach dem Loslassen federt er
elastisch in die Randposition zurück. Die Auslenkung entsteht allein durch die Geste. Ohne Ziehen
bleibt der Inhalt an seinem Rand.

## Verwendung

- Überscrollen oben und unten in Listen und Artikeln
- horizontale Listen am Ende der Strecke
- Karten und zoombare Bilder mit gedämpften Rändern
- Blättern: Das Herausziehen zeigt das Ende der Liste an
- der Bereich beim Herausziehen als Anfang von Zum-Aktualisieren-Ziehen
- Drag & Drop an Behältergrenzen

## Dauer

- Typisch: Zurückfedern 300–500 ms; die Bewegung davor folgt direkt der Geste

## Unterschied zu Elastic und Bounce Out

- Elastic: eine Bewegung ohne Geste, die von allein über das Ziel hinausschießt; Rubber Band folgt
  zuerst dem Finger und federt erst nach dem Loslassen zurück.
- Bounce Out: federt, bevor das Element verschwindet; Rubber Band endet immer in der Ruheposition,
  das Element bleibt sichtbar.
