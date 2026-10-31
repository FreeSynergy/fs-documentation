# Taiga - API Dokumentation

## Übersicht

REST-API unter `/api/v1/` (JSON) — deckt Userstories, Tasks, Issues, Epics, Sprints, Wiki ab. Authentifizierung OAuth2-lastig (Password-Grant für Skripte, Bearer-Tokens); Webhooks und ein offizielles CLI.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/v1/userstories|tasks|issues|epics|milestones…` | CRUD + Filter | offiziell |
| OAuth2-Token (`Authorization: Bearer`) | Zugriff | offiziell |
| Webhooks | Projekt → HTTP-POST (Create/Change/Delete) | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

```
POST /api/v1/auth  {"username":"bot","password":"…"}
→ {"access_token": "…", "refresh_token": "…"}
```

danach `Authorization: Bearer <access_token>`; Refresh-Flow für langlebige Jobs.

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/projects?slug=api-umbau` | Projekt suchen |
| `GET/POST` | `/api/v1/userstories?project=…` | Stories |
| `GET/POST` | `/api/v1/tasks?user_story=…` | Subtasks |
| `GET/POST` | `/api/v1/issues` | Issues |
| `GET/POST` | `/api/v1/epics` (+ `epiccustomfields`) | Epics |
| `GET/POST` | `/api/v1/milestones` | Sprints |
| `POST` | `/api/v1/userstories/{ref}/assign_points` | Points setzen |
| `GET/POST` | `/api/v1/webhooks/{project_id}` | Webhooks verwalten |

## Beispiel

Request:

```http
POST /api/v1/userstories HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "project": 41, "ref": 14, "subject": "Rate-Limit-Header",
  "story_points": 3, "assigned_to": 7, "milestone": 12 }
```

Response: `201` mit Story-JSON (`id`, `ref`, `status`, `finish_date` null …).

## Webhooks

Payload: `{ "type": "userstory.change", "project_id":…, "payload":… }` — Konfiguration im Projekt-Integrationspanel (Secret/Events).

## Rate Limits

standardmäßig keine harten Limits; Instanz-Betreiber drosseln über Reverse Proxy.

## SDKs und Client-Bibliotheken

- **offiziell**: `taiga`-CLI (pip), taiga-events (Python), JS-Beispiele
- REST-Beispiele in der Projekt-Doku; Postman-Sammlung vorhanden

## Skin-Hinweis

Story/Task/Issue/Epic/Milestone = direkt abbildbar auf [Task-/Sprint-Modelle](../../../../data/modelle.md).
