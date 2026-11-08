# Calendar View

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `Monthly View`, `Weekly View`, `Daily View`, `Agenda View` |
| **Zustände** | `dragging`, `leer` |
| **Gesten** | `tap`, `drag`, `swipe`, `long-press`, `pinch` |
| **Animationen** | `slide-in`, `expand` |
| **Verwandt** | `list-view`, `timeline`, `date-picker`, `range-calendar` |
| **Status** | dokumentiert |

## Beschreibung
Eine Calendar View zeigt Termine in einem Kalender.

## Verwendungszweck

- Termine anzeigen
- Kalender
- Planung
- Terminierung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Monthly View** | Monatsansicht |
| **Weekly View** | Wochenansicht |
| **Daily View** | Tagesansicht |
| **Agenda View** | Listenansicht |

## Features

- Navigation (vor/zurück)
- Drag and Drop (Termine verschieben)
- Resize (Länge eines Termins ändern)
- Anzeige von Ereignissen

## Abgrenzung

- **Nicht verwechseln mit** [date-picker](../../fields/date-picker/): diese Ansicht zeigt Termine,
  sie wählt kein Datum aus. Der Kern ist derselbe – Raster, Markierungen, Einträge nach
  Typ und Farbe –, die Ansicht ist nur größer und hat Platz für Zeiträume.
- **Kein Menü, kein Export.** Die Ansicht ist ein Widget (Stufe 2). Eine Kalender-App
  (Stufe 4) bettet sie in einen ganzen Bildschirm ein und bringt Menü, Ansichten, Bearbeitung,
  Export und Ausgabeformate mit – die Ansicht selbst bleibt dieselbe und wird nicht
  ein zweites Mal gebaut.
- **Nicht verwechseln mit** [range-calendar](../../fields/range-calendar/): dort wählt man einen Zeitraum
  als Filter, hier ist der Zeitraum die Ansicht.
- **Nicht verwechseln mit** [timeline](../timeline/): eine Timeline erklärt Abfolgen,
  der Kalender zeigt Belegung.
- Wer keine Zeitskala braucht, ist mit der [list-view](../list-view/) besser bedient.

## Best Practices

- Das heutige Datum und die aktuelle Uhrzeit einheitlich markieren.
- Überlappende Termine seitlich aufteilen, niemals übereinanderstapeln.
- Ein `drag` auf ein Raster (15 Minuten) einrasten lassen und Rückgängig anbieten.
- Höchstens sechs Kategorienfarben; darüber ist die Ansicht nicht mehr lesbar.
- Auf schmalen Bildschirmen automatisch zur Agenda-Ansicht wechseln.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — Agenda ohne Zeitskala
- [Range Calendar](../../fields/range-calendar/) — Zeitraum auswählen
- [Basiskomponente](../../../primitives/basics/base.md)
