# Profil – Beispiele

AS2-Felder ✅ Core/Vocabulary-geprüft (Liste in [standards.md → Aktivitäten](../standards.md)); Card-Felder ✅ RFC 9553.

## 1. Öffentliche Actor-Ansicht (was die Welt sieht)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Person",
  "id": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "name": "Anna Weber",
  "preferredUsername": "anna",
  "publicKey": {
    "id": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A#mainKey",
    "owner": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A"
  }
}
```

## 2. Regeln: welche Card-Felder an welches Publikum (eigene Festlegung, zur Diskussion)

```json
{
  "@type": "ProjectionRules",
  "profile": "01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
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

## 3. Dieselbe Person, zwei berechnete Ansichten

**Arbeits-Kontext** (Kalender-Einladung, Kollegen-Publikum):

```json
{
  "name": "Anna Weber",
  "title": "Projektleitung",
  "email": "anna@firma.example"
}
```

**Dating-Kontext** — `work`-Felder fehlen, `sensitive` ist dabei; **im Arbeits-Kontext wäre `sensitive` niemals enthalten** (Dating-Gefahren-Regel aus dem Gespräch):

```json
{
  "name": "Anna",
  "keywords": ["Wandern", "Jazz"],
  "personalInfo": { "orientation": "queer" }
}
```

## 4. Regelwechsel im Envelope (Beschluss 2)

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "actor": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
  "object": {
    "@type": "Profile",
    "id": "https://<instanz>/profile/01HTZK5C8R4M6YQ2N9XGZ7TQ1A",
    "name": "Anna Weber"
  }
}
```

## 5. Was falsch wäre

❌ Eine `profile`-Tabelle mit kopierten Feldwerten (`profile.telefon = ...`) — erzeugt Kopien ohne Ende und untergräbt Beschluss 4. Korrekt ist nur: Handle + Regeln speichern, Werte aus der Card projizieren.
