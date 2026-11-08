# Lift

## Beschreibung

Lift hebt ein Element bei Hover oder Fokus scheinbar an: Es wandert 1–2 px nach oben, der Schatten
wird größer und weicher, und wahlweise hellt sich die Fläche leicht auf. Beim Verlassen sinkt das
Element genauso leise zurück. Der Effekt erzeugt Tiefe, ohne Platz im Layout zu beanspruchen.

## Verwendung

- Karten und Kacheln, die anzeigen, dass sie anklickbar sind, siehe [card](../../../../components/widgets/containers/card/description.md)
- Zeilen in Listen und Tabellen beim Hover, siehe [list-view](../../../../components/widgets/data/list-view/description.md)
- Schaltflächen in zweitrangiger Darstellung, die sich beim Hover nach vorn schieben
- Fokusdarstellung für die Tastaturbedienung (statt nur eines Umrisses)
- eine Ziehquelle, die beim Aufnehmen ihren Zustand bestätigt
- Navigationspunkte, die sich leicht heben, sobald der Zeiger sie erreicht

## Dauer

- Typisch: 120–200 ms
- Das Zurücksinken darf etwas langsamer sein: 150–250 ms
- Auf Touchgeräten gilt Lift nicht – dort übernimmt [Press](../press/description.md)

## Unterschied zu Press und Highlight

- Press drückt das Element nach innen, während es aktiv gedrückt wird; Lift hebt es schon beim
  bloßen Darüberfahren an.
- Highlight verändert die Hintergrundfläche als Signal (gefundene Stelle, Änderung); Lift verändert
  Höhe und Schatten, was „bedienbar“ signalisiert.
