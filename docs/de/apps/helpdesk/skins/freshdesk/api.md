# Freshdesk - API Dokumentation

## Übersicht

REST-API v2 unter `https://<firma>.freshdesk.com/api/v2/` (JSON). Ticket-/Konversations-CRUD, Contacts, Products, CBDs (custom fields), Automationen nur eingeschränkt. Webhooks liefern Events.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v2 | Tickets, Conversations, Contacts, Solutions, CCIs | offiziell |
| Webhooks (`/api/v2/webhooks`) | Event → POST (Ticket created/updated/reply…) | offiziell |
| Developer Platform | Serverless-Funktionen, Custom-Actions | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- **API-Key**: Basic-Auth `curl -u agent@mail.com:APIKEY` (key unter Admin → Mobile & API)
- **OAuth2**: für Marketplace-Apps/Developer Platform
- Rate-Limit pro Konto/Minute; `Retry-After` bei 429

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v2/tickets?filter=open&product_id=…` | Tickets (filter-Parameter) |
| `POST` | `/api/v2/tickets` | anlegen |
| `GET/PATCH/DELETE` | `/api/v2/tickets/{id}` | Detail / ändern / löschen |
| `POST` | `/api/v2/tickets/{id}/reply` | öffentliche Antwort |
| `POST` | `/api/v2/tickets/{id}/private_note` | interne Notiz |
| `POST` | `/api/v2/tickets/{id}/notes` | Notiz alt |
| `GET` | `/api/v2/tickets/{id}/conversations` | Historie |
| `GET/POST` | `/api/v2/contacts` | Kunden |
| `GET/POST` | `/api/v2/solutions/articles` | KB |
| `GET/POST` | `/api/v2/webhooks` | Webhooks verwalten |

## Beispiel

Request:

```http
POST /api/v2/tickets/1024/reply HTTP/1.1
Authorization: Basic base64(agent@mail.com:APIKEY)
Content-Type: application/json

{ "body": "Wir haben die Rechnung korrigiert.", "files": [] }
```

Response: `200 OK` mit Conversation-Objekt (`id`, `incoming:false`, `source:2`).

## Webhooks

Events u.a.: `ticket.create`, `ticket.update`, `reply.created`, `note.created`, `contact.create`. Payload = Ticket-/Conversation-JSON; Retry mit Backoff; Secret-Header konfigurierbar.

## Rate Limits

Dokumentation nennt **100 Requests/Minute pro API-Key** (Richtwert; bei Überschreitung HTTP 429 + `Retry-After`).

## SDKs und Client-Bibliotheken

- offiziell: Python `freshdesk` (Freshworks), Node `freshdesk-sdk` (alt, beachten), PHP
- Developer Platform: `fd`-CLI für Custom Functions

## Skin-Hinweis

Conversations/Ticket-Felder parallel zu Zendesk — gemeinsames Mapping in [modelle.md](../../../../data/modelle.md) (`Comment.public`, `Ticket.status`).
