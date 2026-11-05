# Messages – examples

All AS2 fields from the ✅ read Core/Vocabulary list in [standards.md](standards.md).

> State 2026-11-05: threads use AS2 `context` (see [technical.md](technical.md)); examples with chat
> payloads in MIMI format and e-mail originals are still to be added.

## 1. Chat message: `Create` on `Note` (envelope + payload, decision 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "https://<instance>/messages/018ebf60-a8ed-74d3-8160-da46c6b2dc1c",
  "actor": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "published": "2026-11-02T10:15:00Z",
  "to": ["https://<instance>/profile/018ebf62-3d11-754c-84f4-8b3b4332e878"],
  "object": {
    "type": "Note",
    "id": "https://<instance>/messages/018ebf60-a8ed-74d3-8160-da46c6b2dc1c",
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
  "actor": "https://<instance>/profile/018ebf62-3d11-754c-84f4-8b3b4332e878",
  "to": ["https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a"],
  "object": {
    "type": "Note",
    "id": "https://<instance>/messages/018ebf63-c877-7705-92c5-2f3302d2501b",
    "inReplyTo": "https://<instance>/messages/018ebf60-a8ed-74d3-8160-da46c6b2dc1c",
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
  "inReplyTo": "https://<instance>/wiki/018ebf64-c0bb-72d1-9274-cc1b4ef06431",
  "content": "Section 3 needs an example.",
  "cc": ["https://<instance>/wiki/018ebf64-c0bb-72d1-9274-cc1b4ef06431/followers"]
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
    "source": "https://<instance>/wiki/018ebf64-c0bb-72d1-9274-cc1b4ef06431",
    "selector": [{
      "type": "TextQuoteSelector",
      "exact": "Process management follows ISO 21502",
      "prefix": "Section 3: ",
      "suffix": " — see details in "
    }]
  }
}
```
