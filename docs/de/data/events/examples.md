# Termine – Beispiele

Alle Feldnamen aus der ✅ geprüften RFC-8984-Feldliste in [standards.md](standards.md).

## 1. `Event` mit Teilnehmern (kanonischer Speicher)

```json
{
  "@type": "Event",
  "uid": "01HTZM2Q6T8V3N9K5R7D1XWZ2P",
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
    "loc1": { "name": "Rathaus Berlin", "link": "https://<instanz>/geodata/01HTZK9F2W7P3D8S5V1BQ6XH4M" }
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

## 2. Wöchentliche Serie mit einem Override

```json
{
  "@type": "Event",
  "uid": "01HTZM4W0C5B8J2H6F9G0S1D3E",
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

## 3. `Task` (auch von [projects/](../projects/index.md) genutzt)

```json
{
  "@type": "Task",
  "uid": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "title": "Protokoll der Sprint-Review schreiben",
  "relatedTo": "01HTZM2Q6T8V3N9K5R7D1XWZ2P",
  "due": "2026-11-12T17:00:00Z",
  "priority": 1,
  "percentComplete": 0,
  "progressUpdated": "2026-11-10T16:30:00Z"
}
```

## 4. Teiländerung: Participant antwortet ab (RFC-8984-Pfadform, ✅)

```json
{
  "action": "replace",
  "path": "/participants/p2/participationStatus",
  "value": "declined"
}
```

## 5. Antwort im Envelope (Beschluss 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "object": {
    "@type": "Event",
    "uid": "01HTZM2Q6T8V3N9K5R7D1XWZ2P",
    "participants": {
      "p2": { "participationStatus": "declined", "participationComment": "Kollision mit Kunde." }
    }
  }
}
```
