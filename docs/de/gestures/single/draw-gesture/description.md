# Draw Gesture (Zeichen-Geste)

## Beschreibung

Eine Draw Gesture ist das **Zeichnen einer Form oder eines Buchstabens** auf
dem Bildschirm. Das Erkennen vergleicht den gezeichneten Pfad mit bekannten
Vorlagen (Shape-Matching). Bekannt wurden Buchstaben-Verknüpfungen in
Edge („V“ = zurück, „C“ = Menü) und Buchstaben-Gesten auf Android-Geräten.

Sie gehört zu den **pfadbasierten Gesten** im Sinne von WCAG 2.5.1 und braucht
immer eine Ein-Finger-Alternative.

## Verwendung

- Buchstaben-Shortcuts (Browser-Befehle, Schnellzugriff)
- Form-Erkennung: Kreis = Auswahl, Häkchen = Erledigt, X = Löschen
- Handschriftliche Notiz → Befehl (Scribble-ähnlich)
- Muster-Entsperrung (Verbindungspunkte, seltener Geste, ähnliches Prinzip)

## Beispiele

| Form | Typische Aktion |
|------|-----------------|
| V | Zurück |
| C / B | Menü / Vor |
| Kreis | Element auswählen / heranzoomen |
| Häkchen | Bestätigen |
| X | Schließen / Löschen |

## Dauer

- Zeichnen: 200–1500ms
- Erkennungszeit: < 100ms nach dem Abheben

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Pfad-Sampling** | Punkte des Pfads normalisieren und vergleichen |
| **Template Matching** | Ähnlichkeit zu gespeicherten Vorlagen ($1/$2-Un recognizer) |
| **Primitives** | Strich, Bogen, Kreis als Bausteine kombinieren |

## Unterschied zu Swipe

- **Swipe**: gerichtete Strecke, Richtung entscheidet
- **Draw Gesture**: freie Form, die Geometrie entscheidet

## Unterschied zu Scribble

- **Draw Gesture**: Form wird als Befehl interpretiert
- **Scribble**: Schrift wird als Text interpretiert (Stift-Eingabe)
