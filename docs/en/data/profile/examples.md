# Profile – examples

AS2 fields ✅ Core/Vocabulary-verified (list in [standards.md → activities](../standards.md)); card fields ✅ RFC 9553.

## 1. Public actor view (what the world sees)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Person",
  "id": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "name": "Anna Weber",
  "preferredUsername": "anna",
  "publicKey": {
    "id": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a#mainKey",
    "owner": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a"
  }
}
```

## 2. Rules: which card field goes to which audience (our own decision, open for discussion)

```json
{
  "@type": "ProjectionRules",
  "profile": "018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "groups": {
    "public":   { "fields": ["name", "media:avatar"] },
    "work":     { "fields": ["titles", "emails:work", "organizations"] },
    "private":  { "fields": ["emails:home", "phones", "addresses"] },
    "sensitive": { "fields": ["personalInfo:orientation"] }
  },
  "views": {
    "public":    ["public"],
    "colleagues":["public", "work"],
    "dating":    ["public", "sensitive"]
  }
}
```

## 3. The same person, two computed views

**Work context** (calendar invitation, colleagues audience):

```json
{
  "name": "Anna Weber",
  "title": "Project lead",
  "email": "anna@company.example"
}
```

**Dating context** — the `work` fields are missing, `sensitive` is included; **in the work context `sensitive` would never be included** (the dating-danger rule from the conversation):

```json
{
  "name": "Anna",
  "keywords": ["hiking", "jazz"],
  "personalInfo": { "orientation": "queer" }
}
```

## 4. Rule change in the envelope (decision 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
  "object": {
    "@type": "Profile",
    "id": "https://<instance>/profile/018ebf32-b118-750d-ab8a-a9ec3e7d5c2a",
    "name": "Anna Weber"
  }
}
```

## 5. What would be wrong

❌ A `profile` table with copied field values (`profile.phone = ...`) — creates copies without end and undermines decision 4. Only correct: store the handle + the rules, project the values from the card.
