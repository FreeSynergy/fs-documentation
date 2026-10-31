# Mautic - API Dokumentation

## Übersicht

**REST-API unter `/api/…` (JSON)** deckt fast alle Objekte ab: contacts(+custom fields), segments, campaigns, emails, forms, reports. Dazu Webhooks (Ereignisse → eigenes Backend) und Form-/Tracking-Endpunkte für Einbettung.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/contacts|segments|campaigns|emails|forms|reports` | CRUD + Aktionen | offiziell |
| OAuth2 (Authorization Code/Client-Credentials) + Basic | Zugriff | offiziell |
| Webhooks | `mautic.contact_created/updated`, email sent… | offiziell |
| Form-POST (`{MauticUrl}/form/submit` bzw. `/c/{id}`) | externe Formulare | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

1. Konfiguration → API-Zugänge: OAuth2-Client erzeugen (Redirect `urn:ietf:wg:oauth:2.0:oob` für Skripte)
2. `POST /oauth/v2/token` → `access_token` → `Authorization: Bearer …`
   (Basic mit API-Benutzer für schnelle Setups möglich, OAuth2 empfohlen.)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET/POST` | `/api/contacts` | Kontakte (Filter über `search=`, `start/limit`) |
| `GET/PATCH/DELETE` | `/api/contacts/{id}` | Detail/Ändern/Löschen |
| `POST` | `/api/contacts/{id}/edit` | Ersatz-PUT |
| `POST` | `/api/segments/{id}/contacts/add` | Segmentmitgliedschaft |
| `GET/POST` | `/api/campaigns`, `/api/campaigns/{id}/contacts/{cid}/add` | Kampagnensteuerung |
| `GET` | `/api/reports/{id}/data` | Report-Daten (CSV/JSON) |
| `POST` | `/api/forms/{id}/submit` | Formular einreichen |

## Beispiel

Request:

```http
POST /api/contacts HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "email": "ada@example.org", "firstname": "Ada",
  "tags": [12], "custom_fields": { "verein_rolle": "Foerderer" } }
```

Response: `201` → `{ "contact": { "id": 4711, "points": 0, "datesegmente": … } }`

## Webhooks

Konfiguration → Webhooks: Ereignis (contact.updated) + URL + Secret (Payload signiert via `X-Mautic-Signature` HMAC); asynchron, Wiederholungen vorhanden.

## Rate Limits

nicht hart eingebaut; Instanz-Limits/Empfehlung: Batch-Importe über API + Cron.

## SDKs und Client-Bibliotheken

- offizielle PHP-SDK (`mautic/api-library`), Community (Python/Node)
- Import-/Export-Rezepte in Doku

## Skin-Hinweis

Custom-Field-Catalog (`/api/customfields`) speisen direkt in [felder.md](../../../../data/felder.md); Webhooks als Ereignisquelle im Event-Modell.
