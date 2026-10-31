# Zammad - API Dokumentation

## Übersicht

Zammad ist API-first: Jede UI-Aktion ist ein REST-Call unter `/api/v1`. Dazu kommen Webhooks (outbound) und ein Event-/Trigger-System. Authentifizierung per Person Access Token, OAuth2 oder Session.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON `/api/v1/...` | Tickets, Artikel, Kunden, Organisationen, Tags, Knowledge Base | offiziell |
| Webhooks | Event → HTTP-POST (konfigurierbare Conditions) | offiziell |
| WebSocket `/ws` | Live-UI-Updates | offiziell-intern |
| GraphQL | — | ❌ |

## Authentifizierung

- **Token**: `Authorization: Token <abc>` (Profile → Access Tokens, Scopes wie `ticket.r`)
- **OAuth2/OIDC**: Client-Credentials oder Authorization Code; `Authorization: Bearer <jwt>`
- Session-Cookie im Browser; Basic nur für LDAP-Login-Endpunkte

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/tickets` | Tickets (Filter/Sortierung per Parameter) |
| `GET` | `/api/v1/tickets/{id}` | Ticket Details |
| `POST` | `/api/v1/tickets` | Ticket erstellen |
| `PUT` | `/api/v1/tickets/{id}` | Attribute ändern |
| `DELETE` | `/api/v1/tickets/{id}` | löschen |
| `GET` | `/api/v1/tickets/{id}/articles` | Artikelliste |
| `POST` | `/api/v1/tickets/{id}/articles` | Artikel schreiben (`body`, `type`,Anhänge optional) |
| `GET/POST` | `/api/v1/users`, `/api/v1/organisations` | Kundenkontext |
| `GET` | `/api/v1/tags` · `POST /api/v1/tags/add` | Tagging |
| `GET` | `/api/v1/object_manager_attributes` | dynamische Felder auslesen |
| `POST` | `/api/v1/form_to_ticket` (Portal-Endpoint je Instanz) | Formular-Tickets |

## Beispiel

Request:

```http
POST /api/v1/tickets/42/articles HTTP/1.1
Authorization: Token <token>
Content-Type: application/json

{
  "body": "<p>Hallo, der Techniker kommt Donnerstag.</p>",
  "type": "note",
  "form_id": null
}
```

Response: `200 OK` mit Artikelobjekt (`id`, `ticket_id`, `created_by`, `type`).

## Webhooks

Konfiguration unter Admin → Webhooks. Event-Muster: `ticket.create`, `ticket_update`, `ticket.article_created` …

```json
{ "event": "ticket.article_created",
  "object": { "id": 128, "ticket_id": 42, "type": "customer", "from": "b@example.org" },
  "changed_by": 3, "timestamp": 1793421000 }
```

Optionale Signaturen (Shared Secret + HMAC) und Condition-Filter (Feld/Wert).

## Rate Limits

Keine eingebauten API-Limits (Schutz über Reverse Proxy/Empfehlung: Token-Scopes minimal).

## SDKs und Client-Bibliotheken

- **offiziell**: Ruby `zammad-sdk`, CLI `zammad-console`
- **Community**: Python `pyzammad`, Node `zammad-client`
- **Importe**: Zendesk/Freshdesk/RT/OTRS-Import über UI und CLI (`zammad rake`)

## Skin-Hinweis

Ticket-/Article-/User-Felder spiegeln das Standardmodell ([modelle.md](../../../../data/modelle.md)); dynamische Felder entsprechen [felder.md](../../../../data/felder.md) (`object_manager_attributes`).
