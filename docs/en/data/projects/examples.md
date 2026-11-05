# Projects – examples

Task fields are ✅ verified JSCalendar fields (RFC 8984, list in [events/standards.md](../events/standards.md)). The structure models are **our own decision (open for discussion)** — spec candidate no. 3.

## 1. Project and board (our own models)

```json
{
  "id": "01HTZN0E5T2R8V4B6N9K1D7M3Q",
  "@type": "Project",
  "name": "FreeSynergy rollout",
  "team": "https://<instance>/contacts/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "roles": [
    { "contact": "https://<instance>/contacts/01HTZK5C8R4M6YQ2N9XGZ7TQ1A", "role": "owner" }
  ]
}
```

```json
{
  "id": "01HTZN3G8W6P2S5H0J4F9C1Y7T",
  "@type": "Board",
  "project": "01HTZN0E5T2R8V4B6N9K1D7M3Q",
  "name": "Implementation"
}
```

## 2. List and the board assignment of a task

The task itself is a JSCalendar object from [events/examples.md → example 3](../events/examples.md). The **assignment** is an object of its own:

```json
{
  "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "list": "01HTZN5A9Q3D7K2M6B8V1S4F0H",
  "position": 1500
}
```

## 3. Relation between tasks

```json
{
  "from": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "to": "01HTZN8X4C6T1W9E3G5J2R7Y0P",
  "kind": "blocks"
}
```

## 4. Milestone as a JSCalendar `Event` (only ✅ verified fields + the category convention)

```json
{
  "@type": "Event",
  "uid": "01HTZNB2H8L5R3Q7D9K4W6M0V1",
  "title": "Beta release approval",
  "start": "2026-12-15",
  "showWithoutTime": true,
  "categories": ["milestone"],
  "freeBusyStatus": "free"
}
```

## 5. Board event in the envelope (decision 2): a task is moved

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instance>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "object": {
    "@type": "task_link",
    "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
    "list": "01HTZN5A9Q3D7K2M6B8V1S4F0H",
    "position": 2000
  }
}
```
