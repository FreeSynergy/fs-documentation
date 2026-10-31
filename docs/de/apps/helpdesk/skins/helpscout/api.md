# Help Scout - API Dokumentation

## Übersicht

REST **v2** unter `https://api.helpscout.net/v2/` (JSON, OAuth2-Client-Credentials). Objekte: Mailboxes, Conversations, Threads, Customers, Tags, Docs. Webhooks für Events.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v2 | Conversations/Threads/Customers/Tags/Docs CRUD | offiziell |
| Webhooks | `conversation.created`, `thread.created`, … | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- OAuth2 **Client Credentials**: `POST /v2/auth/access_token` mit `grant_type=client_credentials` (+ client id/secret oder JWT-Signierung für Partner)
- Folgende Requests: `Authorization: Bearer <token>`

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v2/mailboxes` | Mailboxen |
| `GET` | `/v2/conversations?mailbox=…&status=active` | Conversations |
| `GET` | `/v2/conversations/{id}` | Detail inkl. Threads |
| `POST` | `/v2/conversations/{id}/reply` | öffentliche Antwort (Form/JSON) |
| `POST` | `/v2/conversations/{id}/note` | interne Notiz |
| `PATCH` | `/v2/conversations/{id}` | Status/Assignee/Tags |
| `GET/POST` | `/v2/customers`, `/v2/tags` | Personen, Tags |
| `GET/POST` | `/v2/docs/articles` | Knowledge Base |
| `POST` | `/v2/users/…` (Admin) | Team |

## Beispiel

Request:

```http
POST /v2/conversations/123/reply HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "type": "reply", "body": "<p>Hallo, anbei die Korrektur.</p>", "assignTo": 456 }
```

Response: `201 Created` mit Thread-Objekt.

## Webhooks

Abonnement pro Event; Delivery mit Retry; Signature-Prüfung über geteiltes Secret.

## Rate Limits

keine offiziell harte Zahl publiziert; Drosselung > ~20 req/s typischerweise mit 429 beantwortet — Backoff empfohlen.

## SDKs und Client-Bibliotheken

- offizielle JS-Lib (`@helpscout/api`-Wrapper), Python-Community (`helpscout`-Pakete)
- Zapier/Make-Konnektoren für No-Code

## Skin-Hinweis

Conversation = Thread-Baum statt Ticket+Comment; Mapping-Variante in [modelle.md](../../../../data/modelle.md) unter „Conversation-Modell“.
