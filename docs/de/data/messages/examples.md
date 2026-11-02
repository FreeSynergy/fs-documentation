# Nachrichten – Beispiele

Alle AS2-Felder aus der ✅ gelesenen Core/Vocabulary-Liste in [standards.md](standards.md).

## 1. Chat-Nachricht: `Create` auf `Note` (Envelope + Payload, Beschluss 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "https://<instanz>/messages/01HTZP1A7D4K9M2R6T8V3B5Q0W",
  "actor": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "published": "2026-11-02T10:15:00Z",
  "to": ["https://<instanz>/profile/01HTZP4F8H2N6C9X4B7D1K5T3R"],
  "object": {
    "type": "Note",
    "id": "https://<instanz>/messages/01HTZP1A7D4K9M2R6T8V3B5Q0W",
    "name": "",
    "content": "Können wir den Review auf Donnerstag verschieben?",
    "published": "2026-11-02T10:15:00Z"
  }
}
```

## 2. Antwort im Thread (eigene Thread-Regel: `inReplyTo` + `thread_id`)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "actor": "https://<instanz>/profile/01HTZP4F8H2N6C9X4B7D1K5T3R",
  "to": ["https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A"],
  "object": {
    "type": "Note",
    "id": "https://<instanz>/messages/01HTZP7J3Q8W2S5H9F6C1D4M0V",
    "inReplyTo": "https://<instanz>/messages/01HTZP1A7D4K9M2R6T8V3B5Q0W",
    "content": "Ja — 15 Uhr statt 15:30.",
    "published": "2026-11-02T10:22:00Z"
  }
}
```

## 3. Kommentierbare Ressource: Kommentar zur Wiki-Seite als `Note` mit `inReplyTo` auf die Seite

```json
{
  "type": "Note",
  "id": "https://<instanz>/messages/01HTZPA2L6T9R3Q7D5K8M1W4B0",
  "inReplyTo": "https://<instanz>/wiki/01HTZP9G5V2B8N4X6C3D7F0S1H",
  "content": "Abschnitt 3 braucht ein Beispiel.",
  "cc": ["https://<instanz>/wiki/01HTZP9G5V2B8N4X6C3D7F0S1H/followers"]
}
```

## 4. Mehrsprachige Nachricht (`contentMap`, ✅ Core)

```json
{
  "type": "Note",
  "contentMap": {
    "de": "Meeting verschoben.",
    "en": "Meeting moved."
  }
}
```

## 5. Kommentar zu einem Textteil — Web Annotation statt Nachricht (✅ Modell gelesen)

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "type": "Annotation",
  "body": { "type": "TextualBody", "value": "Abschnitt 3 unklar", "purpose": "commenting" },
  "target": {
    "source": "https://<instanz>/wiki/01HTZP9G5V2B8N4X6C3D7F0S1H",
    "selector": [{
      "type": "TextQuoteSelector",
      "exact": "Prozessführung folgt ISO 21502",
      "prefix": "Abschnitt 3: ",
      "suffix": " — Details siehe "
    }]
  }
}
```
