# Date Picker (Datumsauswahl) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Der Wähler hängt an einem [date-input](../date-input/). Tippen ins Feld öffnet das
Overlay; das gewählte Datum steht anschließend im Feld.

Ist `sources` gesetzt, ist der Wähler zusätzlich ein kleiner Kalender: Er fragt beim
Öffnen und beim Monatswechsel die Einträge des sichtbaren Fensters ab, markiert
belegte Tage und zeigt zum gewählten Tag die Tagesliste. Von dort aus werden Einträge
geöffnet, angelegt, geändert, auf einen anderen Tag gezogen oder gelöscht — das
Ergebnis bleibt trotzdem ein Datum (oder ein Bereich), das im Feld landet.

## Beispiele

### Frist auswählen (ohne Anbindung)

```jsx
<DatePicker label="Frist" value={due} min={today} onChange={setDue} />
```

### Zeitraum für einen Bericht

```jsx
<DatePicker variant="bereich" rangeStart={from} rangeEnd={to} closeOnSelect={false} />
```

### Belegte Tage im Teamkalender

```jsx
<DatePicker label="Termin" value={day}
            sources={[events]} scopeId={teamCalendar}
            showEntries="beides" onEntryClick={openEvent} />
```

### Fälligkeiten von Aufgaben

```jsx
<DatePicker label="Fälligkeit" value={due}
            sources={[tasks]} dateField="dueAt" filter="status:eq:open"
            movable onEntryMove={(aufgabe, tag) => reschedule(aufgabe, tag)} />
```

### Alles mit Datum aus einem Projekt

Je Quelle darf ein anderes Datumsfeld zählen; die Angabe pro Quelle überschreibt
`dateField`.

```jsx
<DatePicker label="Stichtag" value={at} entryLimit={3}
            sources={[{resource: events, dateField: "start"},
                      {resource: tasks, dateField: "dueAt"},
                      {resource: documents, dateField: "createdAt"}]} />
```

### Eintrag direkt im Overlay anlegen

```jsx
<DatePicker label="Termin" value={day} sources={[events]}
            creatable createFields={[title, start, end]}
            onEntryCreate={(daten) => client.events.create(daten)} />
```

### Eintrag per Ziehen verschieben

```jsx
<DatePicker label="Termin" value={day} sources={[events]} movable
            onEntryMove={(termin, tag) => client.events.update(termin.id, {start: tag, end: tag})} />
```

## Daten laden und schreiben

| Vorgang | Anfrage nach [Daten-API](../../../data/api.md) |
|---------|------------------------------------------------|
| Overlay öffnet | `GET /api/v1/events?filter=start:gte:2026-11-01;start:lte:2026-12-31&fields=id,title,start,end,type&limit=100` |
| Monatswechsel | dieselbe Anfrage für das neue Fenster, Auslösung über `onMonthChange` |
| Bestand ändert sich | Delta-Abfrage mit `updatedSince`, oder Webhooks `event.created`, `task.updated` |
| Schnellaufnahme | `POST /api/v1/events` mit `Idempotency-Key` |
| Ziehen auf anderen Tag | `PATCH /api/v1/events/{id}` mit neuem `start` und `end`, `If-Match` aus dem ETag |
| Löschen aus der Liste | `DELETE /api/v1/events/{id}` (Soft-Delete) |

Ein geladener Ausschnitt sieht pro Eintrag so aus wie in
[Standardfelder](../../../data/felder.md) beschrieben:

```json
{
  "id": "event_01HZY9",
  "title": "Review",
  "start": "2026-11-14T15:00:00+01:00",
  "end": "2026-11-14T16:00:00+01:00",
  "allDay": false,
  "timezone": "Europe/Berlin",
  "type": "event"
}
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Termin in einem Task | `einzeln`, `quickPick` mit heute und morgen |
| Berichtszeitraum | `bereich`, `closeOnSelect = false` |
| Nur Zukunft erlaubt | `min = heute` |
| Terminfindung im Team | `sources = [events]`, `showEntries = beides`, `creatable = false` |
| Fälligkeiten umplanen | `sources = [tasks]`, `dateField = dueAt`, `movable = true` |
| Chronik eines Projekts | mehrere Quellen je mit eigenem `dateField`, `entryLimit = 3` |
| Reines Datumsfeld ohne Kontext | `sources = []` — der Wähler bleibt ein leerer Kalender |
