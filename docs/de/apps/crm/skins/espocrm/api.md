# EspoCRM - API Dokumentation

## Übersicht

EspoCRM ist API-first: die SPA spricht selbst gegen **REST /api/v1**. Metadaten (Felder, Entities) sind über die API auslesbar — ideal für Skin-Mapping. Webhooks liefern Änderungen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/v1/{entity}` | CRUD, Find, Mass, Custom-Actions | offiziell |
| Webhooks (aus Workflows/Admin) | Event → POST | offiziell |
| Hooks (serverseitig) | Events im Core | offiziell (Erweiterungen) |
| GraphQL | — | ❌ |

## Authentifizierung

- **API-Token** (`Authorization: <token>` — im Feld „API Access Tokens“ erzeugt) oder **HMAC** (key/secret, Signatur über Pfad+Body), oder Basis-Auth (nur Test)
- Rollen steuern API-Rechte wie UI-Rechte

## Endpunkte (generisch je Entity)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/Contact?max=50&offset=0&orderBy=createdAt&where=[{"type":"EQUALS","field":"…"}]` | Liste/Filter (Where als JSON) |
| `POST` | `/api/v1/Contact` | anlegen |
| `GET/PATCH/DELETE` | `/api/v1/Contact/{id}` | lesen / ändern / löschen |
| `POST` | `/api/v1/Contact/{id}/rel/Accounts` | Relation hinzufügen |
| `GET` | `/api/v1/Metadata` | komplettes Datenmodell (Felder/Layouts) |
| `GET` | `/api/v1/Collection/GlobalSearch?whereStr=…` | globale Suche |
| `POST` | `/api/v1/Contact/{id}/action/{customAction}` | Custom Actions (Extensions) |

## Beispiel

Request:

```http
POST /api/v1/Lead HTTP/1.1
Authorization: <api-token>
Content-Type: application/json

{ "name": "Messekontakt", "accountName": "Beta GmbH",
  "emailAddress": ["kontakt@beta.example"], "status": "New" }
```

Response: `201 Created`

```json
{ "id": "634f…", "name": "Messekontakt", "status": "New", "createdAt": "2026-10-31 16:20:11" }
```

## Webhooks

Admin → Webhooks: Event (`Entity:Create/Update/Delete`) + URL + Secret; Body enthält Entity-Payload + `action`. Retry mit Backoff.

## Rate Limits

Keine eingebauten; Webserver-Limits empfohlen.

## SDKs und Client-Bibliotheken

- **offiziell**: JS-Client der SPA (Referenz), PHP Clientlib, Postman-Sammlung
- Community: Python/Node-Wrapper für REST; Make/Zapier via REST

## Skin-Hinweis

`GET /api/v1/Metadata` liefert die Feldtaxonomy — perfekt zum automatischen Mapping auf [felder.md](../../../../data/felder.md).
