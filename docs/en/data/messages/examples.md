# Messages – examples

All AS2 fields from the ✅ read Core/Vocabulary list in [standards.md](standards.md).

## 1. Chat message: `Create` on `Note` (envelope + payload, decision 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "https://<instance>/messages/01HTZP1A7D4K9M2R6T8V3B5Q0W",
  "actor": "https://<instance>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "published": "2026-11-02T10:15:00Z",
  "to": ["https://<instance>/profile/01HTZP4F8H2N6C9X4B7D1K5T3R"],
  "object": {
    "type": "Note",
    "id": "https://<instance>/messages/01HTZP1A7D4K9M2R6T8V3B5Q0W",
    "name": "",
    "content": "Can we move the review to Thursday?",
    "published": "2026-11-02T10:15:00Z"
  }
}
```

## 2. Reply in the thread (our own threading rule: `inReplyTo` + `thread_id`)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "actor": "https://<instance>/profile/01HTZP4F8H2N6C9X4B7D1K5T3R",
  "to": ["https://<instance>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A"],
  "object": {
    "type": "Note",
    "id": "https://<instance>/messages/01HTZP7J3Q8W2S5H9F6C1D4M0V",
    "inReplyTo": "https://<instance>/messages/01HTZP1A7D4K9M2R6T8V3B5Q0W",
    "content": "Yes — 15:00 instead of 15:30.",
    "published": "2026-11-02T10:22:00Z"
  }
}
```

## 3. Commentable resource: comment on the wiki page as a `Note` with `inReplyTo` pointing at the page

```json
{
  "type": "Note",
  "id": "https://<instance>/messages/01HTZPA2L6T9R3Q7D5K8M1W4B0",
  "inReplyTo": "https://<instance>/wiki/01HTZP9G5V2B8N4X6C3D7F0S1H",
  "content": "Section 3 needs an example.",
  "cc": ["https://<instance>/wiki/01HTZP9G5V2B8N4X6C3D7F0S1H/followers"]
}
```

## 4. Multilingual message (`contentMap`, ✅ Core)

```json
{
  "type": "Note",
  "contentMap": {
    "en": "Meeting moved.",
    "es": "Reunión movida."
  }
}
```

## 5. Comment on a text fragment — Web Annotation instead of a message (✅ model read)

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "type": "Annotation",
  "body": { "type": "TextualBody", "value": "Section 3 unclear", "purpose": "commenting" },
  "target": {
    "source": "https://<instance>/wiki/01HTZP9G5V2B8N4X6C3D7F0S1H",
    "selector": [{
      "type": "TextQuoteSelector",
      "exact": "Process management follows ISO 21502",
      "prefix": "Section 3: ",
      "suffix": " — see details in "
    }]
  }
}
```
