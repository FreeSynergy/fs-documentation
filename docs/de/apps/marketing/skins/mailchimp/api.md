# Mailchimp - API Dokumentation

## Übersicht

REST v3 pro Rechenzentren-Subdomain (`https://<dc>.api.mailchimp.com/3.0/`, dc im API-Key). Objekte: lists, members, tags, segments, campaigns, journeys, reports. Webhooks für Member-/Campaign-Ereignisse.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v3 | CRUD + Aktionen (`/actions/subscribe`) | offiziell |
| OAuth2 | App-Zugriff | offiziell |
| Webhooks | list.member.* , campaign.* | offiziell |
| Bulk-Operations (`/bulk-queue`) | asynchrone Massenjobs | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- API-Key: HTTP Basic (`anystring:<api-key>`); OAuth2 für Marktplatz-Apps
- Endpoint-Subdomain aus Key-Suffix (`…us21`) ziehen!

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET/POST` | `/lists/{list_id}/members` | Kontakte |
| `POST` | `/lists/{id}/members` (`status: "subscribed"`) | hinzufügen |
| `PUT` | `/lists/{id}/members/{subscriber_hash}` | anlegen/ersetzen (MD5-Mail) |
| `POST` | `/lists/{id}/members/{hash}/tags` | Tags setzen |
| `GET` | `/lists/{id}/segments` | Segmente |
| `POST` | `/campaigns` + `/actions/send` | Kampagne starten |
| `GET` | `/reports` | Kennzahlen |
| `POST` | `/lists/{id}/webhooks` | Webhook-Abo |

## Beispiel

Request:

```http
POST /3.0/lists/a1b2c3/members HTTP/1.1
Authorization: Basic b3R0ZXI6<api-key>
Content-Type: application/json

{ "email_address": "ada@example.org", "status": "subscribed",
  "tags": ["spender"], "merge_fields": { "FNAME": "Ada", "LNAME": "Byron" } }
```

Response: `200` Member-JSON (`id`=MD5, `subscribe_url`, Stats).

## Webhooks

Events `subscribe`, `unsubscribe`, `cleaned`, `profile` — HMAC-Signatur mit API-Key-Half prüfen (Doku-Beispiel).

## Rate Limits

**15 Requests/Sekunde pro Account** (Reports: gesondert), 429 + Backoff; Bulk-Endpoints für Massen.

## SDKs und Client-Bibliotheken

- offizielle Clients: Python (`mailchimp-marketing`), PHP, Node; Postman-Sammlung
- `subscriber_hash` = MD5(lowercased email) — wichtig fürs Upsert-Muster

## Skin-Hinweis

Member-Modell (E-Mail als Primärschlüssel + Tags) spiegelt Kontaktstandard in [data/felder.md](../../../../data/felder.md); Sync-IDs immer Subscriber-Hash verwenden.
