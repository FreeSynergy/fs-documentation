# Zendesk - API Dokumentation

## Übersicht

Zendesk REST **API v2** (`https://<subdomain>.zendesk.com/api/v2/…`, JSON) gilt als eine der vollständigsten Helpdesk-APIs: Tickets, User, Orgs, Help Center, Custom Objects, Business Rules. Dazu Webhooks und Trigger-Out (via Webhook-Conditions).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON v2 | volles CRUD, cursor-Paginierung | offiziell |
| Webhooks (REST out/in) | Event-Streams, inbound-Endpoints | offiziell |
| Sunshine Platform (Custom Objects, Actions) | externe Daten einbinden | offiziell (planabhängig) |
| GraphQL | nur ausgewählte Bereiche (Talk/Custom Objects Betas) | ❌ nicht flächendeckend |

## Authentifizierung

| Weg | Verwendung |
|-----|------------|
| `ZDK-API-TOKEN: <token>` + `login/email/token` Basic | Server-zu-Server |
| OAuth 2.0 (Authorization Code, PKCE) | Apps/User-Delegiert |
| JWT (Apps/SSO) | App-Kontext |
| OAuth-App-Credentials + Admin scopes | Admin-Aktionen |

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v2/tickets.json` | Liste (Filter `?status=open&per_page=100`) |
| `POST` | `/api/v2/tickets.json` | Ticket erstellen |
| `GET/PATCH/DELETE` | `/api/v2/tickets/{id}.json` | Detail/Ändern/Löschen |
| `POST` | `/api/v2/tickets/{id}/comments.json` | Comment/Reply/Notiz (`public` true/false) |
| `GET` | `/api/v2/users.json`, `/api/v2/organizations.json` | Kontext |
| `POST` | `/api/v2/macros/{id}/apply.json?sid=…` | Macro anwenden |
| `GET/POST` | `/api/v2/help_center/articles.json` | Knowledge Base |
| `GET` | `/api/v2/slas.json`, `/api/v2/business_rules_jobs…` | Business Rules |
| `POST` | `/api/v2/webhooks` | Webhook verwalten (mit `webhook_endpoint`) |
| `GET` | `/api/v2/webhooks/webhooks_events` | Zustellereignisse |

## Beispiel

Request:

```http
POST /api/v2/tickets.json HTTP/1.1
Authorization: Basic base64(agent@mail.com/token/API_TOKEN)
Content-Type: application/json

{ "ticket": {
    "subject": "Drucker offline",
    "comment": { "body": "Seit 09:00 kein Druck.", "public": true },
    "requester_id": 12345,
    "tags": ["drucker", "hw"],
    "priority": "high" } }
```

Response: `201 Created` mit Ticket-JSON (`id`, `status:"new"`, `via`, `audit_ids`).

## Webhooks

- Ausgehend: Events `ticket.created`, `comment.created`, `ticket.updated` … (Signature: `x-zendesk-webhook-signature` HMAC)
- inbound: eigener Endpoint als Trigger-Quelle (`/api/v2/webhooks`, „Webhooks“ im Admin-Center)

## Rate Limits

- Basic-Auth-Requests: **700 requests/5 min pro Konto**;
- OAuth-User-tokens: 500/5 min/Client;
- bei 429: `Retry-After`-Header befolgen.

## SDKs und Client-Bibliotheken

- offizielle Client-Libs: Ruby `zendesk zendesk_api_client_rb`, Python `zendesk`, Node `node-zendesk`, Java
- Zendesk App Framework für UI-Erweiterungen (iframe-Apps, `client.request`)

## Skin-Hinweis

`ticket.comment`, `audit`, `user` entsprechen direkt dem [Kommentar-/User-Modell](../../../../data/modelle.md) — Zendesk-v2 ist ein guter Pate für FreeSynergy-Ticketfelder ([felder.md](../../../../data/felder.md)).
