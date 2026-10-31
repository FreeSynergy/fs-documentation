# Make - API Dokumentation

## Übersicht

REST-API unter `https://api.eu1.make.com/api/v2` (EU-Instanzen; `api.make.com` global), JSON, Token-basiert. Sie verwaltet Szenarien (start/pause/scheduling), Nutzer/Organisationen, Connections; Data stores über „Make table tools“-App.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v2 | users, scenarios (CRUD + scheduling), logs, webhooks | offiziell (API-Plan vorausgesetzt) |
| Custom Webhooks (Szenario-Triggers) | `hooks.make.com/<id>` | offiziell |
| „Make table tools“ App-API | Records in Make-Tabellen | offiziell (App) |
| GraphQL | — | ❌ |

## Authentifizierung

- API-Token (org- oder user-scope): Header `Authorization: Token <key>`
- OAuth2 für eigene Apps/Integrationen (Developer-Konto)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/users/{userId}/scenarios` | Szenarien auflisten |
| `POST` | `/users/{userId}/scenarios` | Szenario anlegen (Szenario-JSON/Code) |
| `POST` | `/users/{userId}/scenarios/{id}/schedule` | Scheduling (Minutes/Every/Never) |
| `POST` | `/users/{userId}/scenarios/{id}/start` / `stop` | an/aus |
| `GET` | `/users/{userId}/scenarios/{id}/executions` | Ausführungen |
| `GET/POST` | `/users/{userId}/connections` | Connections (App-Zugänge) |
| `POST` | `/users/{userId}/webhooks` | Webhook-Endpunkte erzeugen |

## Beispiel

```http
POST /api/v2/users/123456/scenarios/7890/schedule HTTP/1.1
Authorization: Token <api-token>
Content-Type: application/json

{ "schedule": { "type": "Every", "every": 15 } }
```

Response: `201` / aktualisierter Szenario-Datensatz (`id`, `isPaused:false`, `scheduling`).

## Rate Limits

Dokumentierte Kontingente je Plan (Requests/Minute moderat, 429 + Retry); Präzision in der API-Doku.

## SDKs und Client-Bibliotheken

- offizielle Postman-Sammlung; Community-Wrapper (Python/Node)
- Szenario-Import/Export: Szenario-Code (Share-Link/JSON) + API `POST scenarios`

## Skin-Hinweis

Szenario-Objekt (Trigger, Module, Routen, Scheduling) als Flow-Modell-Vorlage ([modelle.md](../../../../data/modelle.md)).
