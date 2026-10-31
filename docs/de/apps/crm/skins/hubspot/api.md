# HubSpot - API Dokumentation

## Übersicht

**CRM REST v3** (`https://api.hubapi.com/…`, JSON) mit Private-App-Token; Webhooks für Objekt-/E-Mail-Ereignisse; dazu Hubs-spezifische APIs (Marketing, Forms, Conversations).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST CRM v3 (`/crm/v3/...`) | Contacts, Companies, Deals, Tickets, Objects | offiziell |
| Search-API (`/crm/v3/objects/{type}/search`) | Filter durch Eigenschaften | offiziell |
| Assoziierungen (`/crm/v3/associations/...`) | Objektbeziehungen | offiziell |
| Webhooks | crm.contact.created/updated/deleted, contactPropertiesChanged… | offiziell (signiert) |
| GraphQL | — | ❌ |

## Authentifizierung

- **Private App Token** (`Authorization: Bearer pat-…`) mit feinen Scopes (`crm.objects.contacts.read/write` …)
- OAuth2 (public apps), Legacy-API-Keys abgeschafft

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/crm/v3/objects/contacts?properties=email,firstname&after=…` | Liste (Cursor) |
| `POST` | `/crm/v3/objects/contacts` | anlegen |
| `GET/PATCH/DELETE` | `/crm/v3/objects/contacts/{id}` | Detail |
| `POST` | `/crm/v3/objects/contacts/search` | Suche nach Eigenschaften |
| `POST` | `/crm/v3/associations/Contact/Company/default` | assoziieren |
| `GET` | `/crm/v3/properties/contacts` | Feldeigenschaften (Metadata) |
| `POST` | `/webhooks/v3/{appId}/subscriptions` | Webhook-Abo |

## Beispiel

Request:

```http
POST /crm/v3/objects/contacts HTTP/1.1
Authorization: Bearer pat-abc
Content-Type: application/json

{ "properties": { "email": "a@example.org", "firstname": "Andrea",
                  "lastname": "Berg", "lifecyclestage": "lead" } }
```

Response: `201`

```json
{ "id": "1234567890", "properties": { "email": "a@example.org", "lifecyclestage": "lead",
  "createdate": "2026-10-31T16:55:02.123Z" }, "createdAt": "2026-10-31T16:55:02.123Z" }
```

## Webhooks

`POST /webhooks/v3/{appId}/settings` + Subscriptions; Payload signiert (HMAC `x-hubspot-signature`), Retry-Logik vorhanden.

## Rate Limits

**~100 Requests/10 s pro Portal/Token** (je Plan mehr, Burst-Header `x-rate-limit-*`); 429 mit Reset-Zeit.

## SDKs und Client-Bibliotheken

- offizielle Client-SDKs: Node (`@hubspot/api-client`), Python (`hubspot-api-client`), PHP, Java
- HubL/Client-JS für Website-Kontext

## Skin-Hinweis

Eigenschafts-API = Feldkatalog fürs automatische Mapping ([felder.md](../../../../data/felder.md)); Lifecycle-Stages → Standard-Pipeline-Feld.
