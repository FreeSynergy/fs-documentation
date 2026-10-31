# Asana - API Dokumentation

## Übersicht

REST v1 unter `https://app.asana.com/api/1.0` (JSON). Objekte: workspaces, projects, sections, tasks, subtasks, users, teams, custom fields, portfolios. Webhooks für Task-/Projektänderungen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v1 | CRUD + Relationships, Batch | offiziell |
| Webhooks | `x-hook-secret` Challenge, Task-Updates | offiziell |
| Batch-API (`/batch`) | bis 10 Calls pro Request | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- **Persönlicher Access-Token** (Admin/Entwickler-Einstellungen): `Authorization: Bearer <token>`
- **OAuth2** für Apps (Authorization Code)
- Datenzugriff folgt Workspace-Mitgliedschaften

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/workspaces` | Workspaces |
| `GET` | `/projects?workspace=…` | Projekte |
| `POST` | `/projects/{id}/tasks` | Aufgabe anlegen |
| `GET/PATCH/DELETE` | `/tasks/{id}` | Detail/Ändern/Löschen |
| `POST` | `/tasks/{parent}/subtasks` | Unteraufgabe |
| `GET/POST` | `/tasks/{id}/comments` | Kommentare |
| `POST` | `/tasks/{id}/assignments` | zuweisen (mehrere) |
| `GET` | `/tasks?project=…&assignee=me&due_on=2026-11-04` | gefilterte Liste |
| `GET` | `/workspaces/{id}/sections` (via project) | Bereiche |
| `POST` | `/webhooks` | Webhook-Abo (resource=id) |

## Beispiel

Request:

```http
POST /api/1.0/projects/12345/tasks HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "data": { "name": "Impressum prüfen", "due_on": "2026-11-04",
  "assignee": 9876, "notes": "Rechtsfreigabe danach" } }
```

Response: `201` → `{ "data": { "gid": "112233", "name": "Impressum prüfen", "completed": false } }`

## Webhooks

Anmeldung liefert `x-hook-secret` (einmalig speichern!). Events: Task completed/changed; Payload mit `x-hook-secret`-Validierung.

## Rate Limits

zeitbasierte Limits pro App/Nutzer; bei 429 `Retry-After`-Header; Response enthält `Asana-Reason`-Header zur Diagnose.

## SDKs und Client-Bibliotheken

- offizielle Clients: Python (`asana`), Node (`asana`), Java/PHP; Batch-Beispiele in der Doku
- Zapier/Make/Konnektoren vorhanden

## Skin-Hinweis

`gid`- IDs + Abschnitt/Portfolio entsprechen [Task-Struktur](../../../../data/modelle.md); Custom Fields → [felder.md](../../../../data/felder.md).
