# Calendar View (Kalenderansicht)

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
Eine Calendar View zeigt Termine in einem Kalender an.

## Verwendungszweck

- Termine anzeigen
- Kalender
- Planung
- Scheduling

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Monthly View** | Monatsansicht |
| **Weekly View** | Wochenansicht |
| **Daily View** | Tagesansicht |
| **Agenda View** | Listenansicht |

## Features

- Navigation (Vor/Zurück)
- Drag-and-Drop (Termine verschieben)
- Resize (Terminlänge ändern)
- Events anzeigen

## Abgrenzung

- **Nicht verwechseln mit** [date-picker](../../fields/date-picker/): diese Ansicht zeigt Termine,
  sie wählt kein Datum aus.
- **Nicht verwechseln mit** [range-calendar](../../fields/range-calendar/): dort wählt man einen Zeitraum
  als Filter, hier ist der Zeitraum die Ansicht.
- **Nicht verwechseln mit** [timeline](../timeline/): eine Zeitlinie erklärt Abläufe,
  der Kalender zeigt Belegung.
- Wer keine Zeitskala braucht, ist mit [list-view](../list-view/) besser bedient.

## Best Practices

- Heutigen Tag und die aktuelle Uhrzeit durchgehend markieren.
- Überlappende Termine seitlich aufteilen, nie übereinander legen.
- Verschieben per `drag` auf ein Raster einrasten lassen (15 Minuten) und Rückgängig anbieten.
- Höchstens sechs Kategorienfarben; darüber ist die Ansicht nicht mehr lesbar.
- Auf schmalen Bildschirmen automatisch in die Agenda-Ansicht wechseln.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — Agenda ohne Zeitskala
- [Range Calendar](../../fields/range-calendar/) — Zeitraum wählen
- [Basiskomponente](../../basics/base/)
