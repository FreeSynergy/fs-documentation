# Date Picker (Datumsauswahl)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `date-input` |
| **Varianten** | `einzeln`, `bereich`, `wiederkehrend` |
| **Zustände** | `open`, `outOfRange`, `loading` |
| **Gesten** | `tap`, `swipe`, `drag`, `long-press` |
| **Animationen** | `fade-in`, `slide-in` |
| **Verwandt** | `date-input`, `time-picker`, `range-calendar`, `calendar-view`, `list-view` |
| **Rolle** | `dialog` |
| **Status** | dokumentiert |

## Beschreibung

Der Datumswähler öffnet ein Kalenderoverlay, in dem ein Datum oder ein Bereich
ausgewählt wird. Er ergänzt das [date-input](../date-input/), das die Eingabe durch
Tippen ermöglicht.

Über das reine Auswählen hinaus ist der Wähler an die **Daten angebunden**: Er liest den
standardisierten Datenbestand (siehe [Standardisierte Daten](../../../data/)) und zeigt
in den Tagen die Einträge, die auf diesem Tag liegen — Termine, Aufgaben mit
Fälligkeit, Dokumente mit Erstellungsdatum. Der gewählte Tag öffnet die Tagesliste,
und über die Schnellaufnahme werden Einträge dort direkt angelegt oder per Ziehen auf
einen anderen Tag verschoben. Alles, was ein Datum hat, kann angezeigt,
ausgewählt und geschrieben werden; welches Datum gemeint ist, bestimmt `dateField`.

## Verwendungszweck

- Termin-, Aufgaben- und Fristdaten auswählen
- Bereiche wählen (von/bis), etwa für Berichte
- Wiederholungen festlegen (wöchentlich, monatlich)
- Vor der Auswahl sehen, was an einem Tag schon verplant ist
- Einen Termin oder eine Aufgabe direkt im Overlay anlegen, ändern oder verschieben,
  ohne das Formular zu verlassen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | ein Datum |
| **bereich** | Start und Ende, dazwischen markiert |
| **wiederkehrend** | Datum plus Regeln für Wiederholung |

## Features

- Monats-, Jahres- und Dekadensicht in einem Overlay
- Schnellauswahl: heute, morgen, nächste Woche
- Freie Eingabe im Overlay-Feld bleibt möglich
- Belegte Tage sind sichtbar markiert: Punkt pro Eintrag, Farbe nach Typ, Zähler bei vielen
- Tagesliste unter dem Raster: Titel, Uhrzeit und Status der Einträge des gewählten Tages
- Schnellaufnahme: Titel und Zeit genügen, Speichern ohne das Overlay zu verlassen
- Ziehen eines Eintrags auf einen anderen Tag verschiebt ihn (Schreibrecht vorausgesetzt)
- Serien (`recurrenceRule` nach RFC 5545) werden aufgelöst angezeigt und als Serie gekennzeichnet

## Abgrenzung

- **Nicht verwechseln mit** [date-input](../date-input/): das Feld nimmt Tippeingaben an,
  der Wähler zeigt den Kalender.
- **Nicht verwechseln mit** [calendar-view](../../data/calendar-view/): die Ansicht ist
  das Planungswerkzeug mit Wochen- und Tagesraster, Zeitleiste und Umbrechen von
  Zeiträumen; der Wähler bleibt ein Auswahl-Overlay, das Einträge nur **kompakt**
  mitzeigt (Punkte, Tagesliste, Schnellaufnahme) und als Ergebnis ein Datum liefert.
- **Nicht verwechseln mit** [list-view](../../data/list-view/): eine Liste zeigt
  Einträge ohne Datumsschwerpunkt, die Tagesliste des Wählers hängt am gewählten Tag.

## Best Practices

- Voreinstellung auf das Datum legen, das am wahrscheinlichsten ist.
- Erlaubte Bereichsgrenzen (`min`, `max`) immer setzen, wenn die Domäne sie kennt.
- Auf Mobilgeräten die Liste der nächsten Daten anbieten, nicht nur das Raster.
- Nie den ganzen Bestand laden: nur das Fenster mit `loadWindow`, pro Tag höchstens
  `entryLimit` Einträge, der Rest als „+ n weitere“.
- Zeiten mit Zeitzonen-Offset, Ganztagesdaten mit `allDay = true`
  (siehe [Standardfelder](../../../data/felder.md)).
- `creatable` und `movable` nur einschalten, wenn das Schreibrecht besteht; sonst bleibt
  der Wähler lesend und die Tagesliste ist reine Information.
- Ohne Kontext (`sources` leer) verhält sich der Wähler wie ein reiner Kalender —
  nicht jedes Datumsfeld braucht eine Anbindung.

## Datenanbindung

Der Wähler liest über das einheitliche Daten-Muster
([Daten-API](../../../data/api.md)) und schreibt nach demselben Muster zurück
(`POST` zum Anlegen, `PATCH` beim Verschieben). Gebunden wird ein Modell plus das Feld,
das den Tag liefert — deshalb ist der Wähler nicht auf Termine beschränkt:

| Modell | Datumsfeld (`dateField`) | Darstellung am Tag |
|--------|--------------------------|--------------------|
| `Event` | `start`, Ende in `end` | Punkt gefüllt, Farbe nach Kalender |
| `Task` | `dueAt` | Punkt mit Häkchen, wenn `status = done` |
| `Document` | `createdAt`, `updatedAt` | Strich am unteren Tagrand |
| `Message` | `createdAt` | Sammelzähler pro Tag |
| `Revision` | `createdAt` | nur bei expliziter Anforderung |
| eigenes Modell | beliebiges `date`- oder `datetime`-Feld | wie `Event`, die Beschriftung kommt aus `type` |

Geladen wird immer nur das sichtbare Fenster plus `loadWindow` Monate; Änderungen am
Bestand folgen dem Fenster über `updatedSince` oder Webhooks
(`event.created`, `task.updated`). Es gelten die Rechte des Datensatzes: Was die
Person sehen darf, bestimmt die Quelle — gesperrte Einträge fehlen in Raster und Zähler
vollständig.

## Siehe auch

- [Date Input](../date-input/)
- [Range Calendar](../range-calendar/)
- [Calendar View](../../data/calendar-view/)
- [Termine — Datendomäne](../../../data/events/)
- [Standardfelder](../../../data/felder.md)
- [Daten-API](../../../data/api.md)
- [Basiskomponente](../../basics/base/)
