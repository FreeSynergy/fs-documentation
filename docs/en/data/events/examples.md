# Appointments – examples

All field names from the ✅ verified RFC 8984 field list in [standards.md](standards.md).

## 1. `Event` with participants (canonical storage)

```json
{
  "@type": "Event",
  "uid": "01HTZM2Q6T8V3N9K5R7D1XWZ2P",
  "created": "2026-11-02T09:00:00Z",
  "updated": "2026-11-02T09:00:00Z",
  "sequence": 0,
  "title": "Sprint review",
  "description": "Demo of the sprint outcome.",
  "start": "2026-11-10T15:00:00Z",
  "duration": "PT1H",
  "status": "confirmed",
  "freeBusyStatus": "busy",
  "locations": {
    "loc1": { "name": "Rathaus Berlin", "link": "https://<instance>/geodata/01HTZK9F2W7P3D8S5V1BQ6XH4M" }
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

## 2. Weekly series with one override

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

## 3. `Task` (also used by [projects/](../projects/index.md))

```json
{
  "@type": "Task",
  "uid": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "title": "Write the minutes of the sprint review",
  "relatedTo": "01HTZM2Q6T8V3N9K5R7D1XWZ2P",
  "due": "2026-11-12T17:00:00Z",
  "priority": 1,
  "percentComplete": 0,
  "progressUpdated": "2026-11-10T16:30:00Z"
}
```

## 4. Partial change: a participant declines (RFC 8984 path form, ✅)

```json
{
  "action": "replace",
  "path": "/participants/p2/participationStatus",
  "value": "declined"
}
```

## 5. Reply in the envelope (decision 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instance>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "object": {
    "@type": "Event",
    "uid": "01HTZM2Q6T8V3N9K5R7D1XWZ2P",
    "participants": {
      "p2": { "participationStatus": "declined", "participationComment": "Clashes with a customer appointment." }
    }
  }
}
```
