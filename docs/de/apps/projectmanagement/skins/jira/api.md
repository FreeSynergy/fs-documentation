# Jira - API Dokumentation

## Übersicht

REST-API unter `https://<site>.atlassian.net/rest/api/3/…` (früher `/rest/api/2`; beide gepflegt, v3 offizieller). JQL in `search`, Issues/Fields/Boards separat; Webhooks über Connect-Apps bzw. plattformeigene Automation.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/rest/api/3/issue`, `/search`, `/field` | Issue-CRUD, JQL, Metadaten | offiziell |
| REST Agil `/rest/agile/1.0` | Boards, Sprints, Backlog | offiziell |
| Webhook-Abos (Connect/Forge) | issue_created/updated… | offiziell |
| GraphQL | nur ausgewählte Bereiche | ❌ allgemein |

## Authentifizierung

- **Cloud**: HTTP Basic `E-Mail:API-Token` oder OAuth2 (3LO/Apps); **Data Center**: PAT (`Authorization: Bearer`)
- Berechtigungen = Jira-Rollen (API sieht, was User sieht)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/rest/api/3/issue` | Issue anlegen (fields-Objekt) |
| `GET` | `/rest/api/3/issue/{key}` | Detail |
| `PUT/PATCH` | `/rest/api/3/issue/{key}` | ändern (`update`-Operationen) |
| `POST` | `/rest/api/3/issue/{key}/transitions` | Statuswechsel (Transition-ID) |
| `GET` | `/rest/api/3/search?jql=…` | JQL-Suche (auch POST /search/jql) |
| `GET` | `/rest/api/3/issue/{key}/comment` | Kommentare |
| `GET` | `/rest/agile/1.0/board/{id}/sprint` | Sprints |
| `GET` | `/rest/api/3/field` | Feldkatalog |
| `POST` | `/rest/api/3/issue/{key}/attachments` | Datei (Base64/Multipart) |

## Beispiel

Request:

```http
POST /rest/api/3/issue HTTP/1.1
Authorization: Basic base64(bot@mail.com:API_TOKEN)
Content-Type: application/json

{ "fields": {
  "project": {"key": "WEB"},
  "summary": "Login-Formular validieren",
  "issuetype": {"name": "Task"},
  "assignee": {"accountId": "5d1b…"},
  "labels": ["frontend"] } }
```

Response: `201` → `{ "id": "10042", "key": "WEB-15", "self": "…/issue/10042" }`

Statuswechsel:

```json
{ "transition": { "id": "31" } }
```

## Rate Limits

Cloud: gestaffelt (~4.000 Requests/10-s-Fenster pro Nutzer über alle Apps; App- und Produkt-Limits zusätzlich) — Header `X-RateLimit-*`/429 `Retry-After`.

## SDKs und Client-Bibliotheken

- offizielle Clients (Atlassian Python API community `atlassian-python-api`), Connect/Forge-Apps als App-Modell
- CLI: `atlas` (Atlassian Labs, Beta-Status), JQL in Skripten

## Skin-Hinweis

Status-Transitionen (Kanten mit Berechtigungen) sind das Referenzmuster für Workflow-Skins; JQL-Feldnamen → [felder.md](../../../../data/felder.md).
