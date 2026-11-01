# Lift

## Beschreibung

Lift hebt ein Element bei Hover oder Fokus scheinbar an: Es wandert 1–2 px nach oben, der Schatten wird größer und weicher, optional hellt sich die Fläche leicht auf. Beim Verlassen sinkt das Element ebenso leise zurück. Der Effekt erzeugt Tiefe, ohne Platz im Layout zu verbrauchen.

## Verwendung

- Karten und Kacheln als Anzeige, dass sie klickbar sind, siehe [card](../../../components/containers/card/description.md)
- Zeilen in Listen und Tabellen beim Überfahren, siehe [list-view](../../../components/data/list-view/description.md)
- Buttons mit Sekundärdarstellung, die beim Hover hervortreten
- Fokusdarstellung bei Tastaturbedienung (statt nur Rahmen)
- Drag-Quelle, die ihren Zustand beim Aufnehmen bestätigt
- Navigationspunkte, die beim Anfahren leicht steigen

## Dauer

- Typisch: 120–200 ms
- Rückkehr gern etwas langsamer: 150–250 ms
- Bei Touchgeräten entfällt Lift – dort übernimmt [Press](../press/description.md)

## Unterschied zu Press und Highlight

- Press drückt das Element beim aktiven Drücken nach innen; Lift zieht es beim bloßen Überfahren nach oben.
- Highlight verändert die Hintergrundfläche als Signal (Fundstelle, Änderung); Lift verändert Höhe und Schatten und sagt damit „bedienbar“ aus.
