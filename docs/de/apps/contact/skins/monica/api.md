# Monica - API Dokumentation

## Übersicht

Monica hat eine stabile **REST-API** (`/api/`) mit persönlichem Token — sie bedeckt Kontakte, Aktivitäten, Aufgaben, Notizen, Geschenke und Beziehungen. Webhooks liefern Änderungen heraus.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON `/api/...` | volles CRUD | offiziell |
| Webhooks | push bei Ereignissen | offiziell (pro Nutzer konfigurierbar) |
| GraphQL | — | ❌ |
| CalDAV/CardDAV | — | ❌ (Export nur als Datei) |

## Authentifizierung

- Token (Einstellungen → API) als `Authorization: Bearer <token>`
- Alle Endpunkte nutzerbezogen (Circle-Isolation)

## Endpunkte (Kern)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/contacts` | Kontakte (paginiert, Filter `query`) |
| `POST` | `/api/contacts` | Kontakt anlegen |
| `GET` | `/api/contacts/{id}` | Detail |
| `PUT` | `/api/contacts/{id}` | ändern |
| `DELETE` | `/api/contacts/{id}` | löschen |
| `GET/POST` | `/api/contacts/{id}/activities` | Aktivitäten lesen/erstellen |
| `GET/POST` | `/api/tasks` | Aufgaben |
| `GET/POST` | `/api/notes` | Notizen |
| `GET/POST` | `/api/gifts` | Geschenke |
| `GET` | `/api/activity-types`, `/api/relationship-types` | Typkataloge |

## Beispiel

Request:

```http
POST /api/contacts HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "first_name": "Andrea",
  "last_name": "Berg",
  "gender_id": 1,
  "description": "Wandergruppe"
}
```

Response:

```json
{
  "data": {
    "id": 341,
    "first_name": "Andrea",
    "last_name": "Berg",
    "complete_name": "Andrea Berg",
    "description": "Wandergruppe",
    "url": "https://monica.example.org/contact/341"
  }
}
```

## Webhooks

Konfiguration unter Einstellungen → Webhooks (URL + Secret). Ereignisse u.a.: `contact.created`, `activity.added`, `task.completed` — JSON-Body mit Objekt und `event`-Feld, Signatur per `X-Monica-Signature` (HMAC-SHA256).

## Rate Limits

Standard: **keine** harte API-Rate-Limitierung; instanzseitig über Webserver setzen.

## SDKs und Client-Bibliotheken

- Offizielle SDKs: ❌
- Community: PHP/JS-Beispiele im Monica-Wiki; REST + `curl` genügt

## Skin-Hinweis

Monica-Struktur ist Referenz für das Contact-mit-Event-Modell ([modelle.md](../../../../data/modelle.md)); Webhooks entsprechen den Standard-Event-Feldern ([felder.md](../../../../data/felder.md)).
