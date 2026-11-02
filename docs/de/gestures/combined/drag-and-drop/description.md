# Drag and Drop (Ziehen und Ablegen)

## Beschreibung

Drag and Drop kombiniert **Greifen, Ziehen und Ablegen**: Ein Element wird
aufgenommen (Tap, Long Press oder sofortiger Drag), über den Bildschirm
bewegt und auf einer Ablagezone (Drop Target) losgelassen. iOS nutzt
Long-Press-zum-Greifen, Desktop eher sofortiges Ziehen; Web: HTML5 Drag &
Drop API und Pointer-Events mit `setPointerCapture`.

## Verwendung

- Dateien/Elemente zwischen Bereichen verschieben (Listen, Ordner, Boards)
- Reihenfolge ändern (Reorder)
- Inhalte kombinieren (Bild in Editor, Text in Feld)
- Mülleimer-Aktion: Element auf Ablage „Löschen“ ziehen

## Greif-Arten

| Art | Beschreibung |
|-----|--------------|
| **Instant Drag** | Ziehen beginnt sofort (Desktop, Listen-Griffpunkte) |
| **Long Press Drag** | Greifen erst nach Halten (Touch-Standard, kollidiert nicht mit Scroll) |
| **Double Tap & Hold** | Doppeltipp + Halten hebt Element an (iOS Accessibility) |

## Dauer

- Greif-Delay (Long Press): 250–500ms
- Ziehen: beliebig
- Ablege-Animation: 200–350ms

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Drag Source** | Element meldet Greifen, liefert Daten/Repräsentation |
| **Drop Target** | Zone signalisiert Annahmebereitschaft (Highlight) |
| **Ghost/Drag Image** | Vorschau folgt dem Finger/Zeiger |

## Abbruch

| Weg | Verhalten |
|-----|-----------|
| Zurück an Startposition | federt zurück, keine Änderung |
| Escape-Taste | bricht ab |
| Ablagezone ohne Annahme | Element kehrt zurück |

## Unterschied zu Drag

- **Drag**: Bewegung eines Inhalts/Elements an sich (Scroll, Pan)
- **Drag and Drop**: Bewegung **zwischen** Quelle und Ziel mit Datenübergabe

## Barrierefreiheit

WCAG 2.5.7 (Dragging Movements): jede Drag-Aktion braucht eine
Einzelzeiger-Alternative (Auswählen + Ausschneiden/Einfügen, Auf-/Ab-Button).
