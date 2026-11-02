# Projekte – Beispiele

Task-Felder sind ✅ geprüfte JSCalendar-Felder (RFC 8984, Liste in [events/standards.md](../events/standards.md)). Die Struktur-Modelle sind **eigene Festlegung (zur Diskussion)** — Spec-Kandidat Nr. 3.

## 1. Projekt und Board (eigene Modelle)

```json
{
  "id": "01HTZN0E5T2R8V4B6N9K1D7M3Q",
  "@type": "Project",
  "name": "FreeSynergy Rollout",
  "team": "https://<instanz>/contacts/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "roles": [
    { "contact": "https://<instanz>/contacts/01HTZK5C8R4M6YQ2N9XGZ7TQ1A", "role": "owner" }
  ]
}
```

```json
{
  "id": "01HTZN3G8W6P2S5H0J4F9C1Y7T",
  "@type": "Board",
  "project": "01HTZN0E5T2R8V4B6N9K1D7M3Q",
  "name": "Umsetzung"
}
```

## 2. Liste und Board-Zuordnung eines Tasks

Der Task selbst ist ein JSCalendar-Objekt aus [events/examples.md → Beispiel 3](../events/examples.md). Die **Zuordnung** ist ein eigenes Objekt:

```json
{
  "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "list": "01HTZN5A9Q3D7K2M6B8V1S4F0H",
  "position": 1500
}
```

## 3. Beziehung zwischen Aufgaben

```json
{
  "from": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "to": "01HTZN8X4C6T1W9E3G5J2R7Y0P",
  "kind": "blocks"
}
```

## 4. Meilenstein als JSCalendar-`Event` (nur ✅ geprüfte Felder + Kategorie-Konvention)

```json
{
  "@type": "Event",
  "uid": "01HTZNB2H8L5R3Q7D9K4W6M0V1",
  "title": "Beta-Freigabe",
  "start": "2026-12-15",
  "showWithoutTime": true,
  "categories": ["milestone"],
  "freeBusyStatus": "free"
}
```

## 5. Board-Ereignis im Envelope (Beschluss 2): Task wird verschoben

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "object": {
    "@type": "task_link",
    "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
    "list": "01HTZN5A9Q3D7K2M6B8V1S4F0H",
    "position": 2000
  }
}
```
