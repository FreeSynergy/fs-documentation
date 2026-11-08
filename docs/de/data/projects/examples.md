# Projekte – Beispiele

Task-Felder sind ✅ geprüfte JSCalendar-Felder (RFC 8984, Liste in [events/standards.md](../events/standards.md)). Die Strukturmodelle sind **unsere eigene Entscheidung (zur Diskussion offen)** — Spezifikationskandidat Nr. 3.

## 1. Projekt und Board (unsere eigenen Modelle)

```json
{
  "id": "018ebf50-38ba-7611-b22c-d54cc2d3d077",
  "@type": "Project",
  "name": "FreeSynergy-Einführung",
  "team": "https://<instance>/contacts/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "roles": [
    { "contact": "https://<instance>/contacts/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a", "role": "owner" }
  ]
}
```

```json
{
  "id": "018ebf51-c11c-7585-92c4-1223d2c0f8fa",
  "@type": "Board",
  "project": "018ebf50-38ba-7611-b22c-d54cc2d3d077",
  "name": "Umsetzung"
}
```

## 2. Liste und die Board-Zuordnung einer Aufgabe

Die Aufgabe selbst ist ein JSCalendar-Objekt aus [events/examples.md → Beispiel 3](../events/examples.md). Die **Zuordnung** ist ein eigenes Objekt:

```json
{
  "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "list": "018ebf52-a937-7b4f-b150-cb46c3923c11",
  "position": 1500
}
```

## 3. Beziehung zwischen Aufgaben

```json
{
  "from": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "to": "018ebf54-748c-7683-84b8-702c8583f816",
  "kind": "blocks"
}
```

## 4. Meilenstein als JSCalendar-`Event` (nur ✅ geprüfte Felder + die Kategorie-Konvention)

```json
{
  "@type": "Event",
  "uid": "01HTZNB2H8L5R3Q7D9K4W6M0V1",
  "title": "Freigabe Beta-Release",
  "start": "2026-12-15",
  "showWithoutTime": true,
  "categories": ["milestone"],
  "freeBusyStatus": "free"
}
```

## 5. Board-Ereignis im Umschlag (Entscheidung 2): eine Aufgabe wird verschoben

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "object": {
    "@type": "task_link",
    "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
    "list": "018ebf52-a937-7b4f-b150-cb46c3923c11",
    "position": 2000
  }
}
```
