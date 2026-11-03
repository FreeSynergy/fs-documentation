# Rubber Band

## Beschreibung

Rubber Band zeigt den Widerstand einer scrollbaren Fläche beim Überziehen: Zieht der Nutzer über den Rand hinaus, folgt der Inhalt nur gedämpft.
Beim Loslassen federt er elastisch in die Randlage zurück.
Die Auslenkung entsteht ausschließlich durch die Geste – ohne Zug bleibt der Inhalt an seinem Rand.

## Verwendung

- Over-Scroll oben und unten in Listen und Artikeln
- Horizontale Listen am Ende der Strecke
- Karten und zoombare Bilder mit gedämpften Rändern
- Paging: der Einzug signalisiert das Ende der Liste
- Einzugsbereich als Start für Pull-to-Refresh
- Drag & Drop an Containergrenzen

## Dauer

- Typisch: Rückfederung 300–500 ms; Folgebewegung direkt (gesteengesteuert)

## Unterschied zu Elastic und Bounce Out

- Elastic: eine Bewegung ohne Gestik, die von selbst überschießt; Rubber Band
  folgt zuerst dem Finger und federt erst nach dem Loslassen zurück.
- Bounce Out: federt vor dem Verschwinden; Rubber Band endet immer in der
  Ruhelage, das Element bleibt sichtbar.
