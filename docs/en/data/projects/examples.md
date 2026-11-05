# Projects – examples

Task fields are ✅ verified JSCalendar fields (RFC 8984, list in [events/standards.md](../events/standards.md)). The structure models are **our own decision (open for discussion)** — spec candidate no. 3.

## 1. Project and board (our own models)

```json
{
  "id": "018ebf50-38ba-7611-b22c-d54cc2d3d077",
  "@type": "Project",
  "name": "FreeSynergy rollout",
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
  "name": "Implementation"
}
```

## 2. List and the board assignment of a task

The task itself is a JSCalendar object from [events/examples.md → example 3](../events/examples.md). The **assignment** is an object of its own:

```json
{
  "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "list": "018ebf52-a937-7b4f-b150-cb46c3923c11",
  "position": 1500
}
```

## 3. Relation between tasks

```json
{
  "from": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
  "to": "018ebf54-748c-7683-84b8-702c8583f816",
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
  "actor": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "object": {
    "@type": "task_link",
    "task": "01HTZM7Y2L4P9Q8R0T6V3B5N7C",
    "list": "018ebf52-a937-7b4f-b150-cb46c3923c11",
    "position": 2000
  }
}
```
