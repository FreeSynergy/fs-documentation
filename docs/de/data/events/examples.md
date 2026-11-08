# Termine – Beispiele

Alle Feldnamen stammen aus der ✅ geprüften Feldliste von RFC 8984 in [standards.md](standards.md).

## 1. `Event` mit Teilnehmenden (kanonische Speicherung)

```json
{
  "@type": "Event",
  "uid": "018ebf41-5cda-76c7-94cc-b83b43de7c56",
  "created": "2026-11-02T09:00:00Z",
  "updated": "2026-11-02T09:00:00Z",
  "sequence": 0,
  "title": "Sprint-Review",
  "description": "Demo des Sprint-Ergebnisses.",
  "start": "2026-11-10T15:00:00Z",
  "duration": "PT1H",
  "status": "confirmed",
  "freeBusyStatus": "busy",
  "locations": {
    "loc1": { "name": "Rathaus Berlin", "link": "https://<instance>/geodata/018ebf34-bc5c-7d86-9464-bb0aee6ec494" }
  },
  "participants": {
    "p1": {
      "name": "Anna Weber",
      "email": "anna@example.org",
      "kind": "individual",
      "roles": ["owner"],
      "participationStatus": "accepted",
      "expectReply": false
    },
    "p2": {
      "name": "Ben Ortiz",
      "email": "ben@example.org",
      "kind": "individual",
      "roles": ["attendee"],
      "participationStatus": "needs-action",
      "expectReply": true
    }
  },
  "alerts": [
    { "action": "display", "trigger": "-PT15M" }
  ]
}
```

## 2. Wöchentliche Serie mit einer Ausnahme

```json
{
  "@type": "Event",
  "uid": "018ebf42-700c-7ad1-a144-cf4c0190b46e",
  "title": "Jour fixe",
  "start": "2026-11-03T10:00:00Z",
  "duration": "PT30M",
  "recurrenceRules": [
    { "frequency": "weekly", "count": 12 }
  ],
  "recurrenceOverrides": {
    "2026-11-17T10:00:00Z": { "excluded": true }
  }
}
```

## 3. `Task` (auch genutzt von [projects/](../projects/index.md))

```json
{
  "@type": "Task",
  "uid": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "title": "Protokoll des Sprint-Reviews schreiben",
  "relatedTo": "018ebf41-5cda-76c7-94cc-b83b43de7c56",
  "due": "2026-11-12T17:00:00Z",
  "priority": 1,
  "percentComplete": 0,
  "progressUpdated": "2026-11-10T16:30:00Z"
}
```

## 4. Teiländerung: ein Teilnehmer sagt ab (Pfadform nach RFC 8984, ✅)

```json
{
  "action": "replace",
  "path": "/participants/p2/participationStatus",
  "value": "declined"
}
```

## 5. Antwort im Umschlag (Entscheidung 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "object": {
    "@type": "Event",
    "uid": "018ebf41-5cda-76c7-94cc-b83b43de7c56",
    "participants": {
      "p2": { "participationStatus": "declined", "participationComment": "Kollidiert mit einem Kundentermin." }
    }
  }
}
```
