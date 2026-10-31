# Daten-API (standardisiert)

Alle Programme stellen ihre Daten nach demselben Muster bereit, damit Workflows, Importe und Skins ohne Sonderbehandlung funktionieren. Konkret dokumentierte Abweichungen stehen in der `api.md` des jeweiligen Programms (`apps/<kategorie>/skins/<programm>/api.md`).

## Übersicht

| Merkmal | Standard |
|---------|----------|
| Stil | REST, JSON |
| Basis | `https://<host>/api/v1` |
| Formate | Request und Response `application/json` (Bulk: `application/x-ndjson`) |
| Methoden | `GET`, `POST`, `PATCH`, `PUT`, `DELETE` |
| Authentifizierung | API-Key oder Bearer-Token, alternativ OAuth2 |
| Kodierung | UTF-8, JSON ohne Kommentare |

## Ressourcen-Muster

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/<resource>` | Liste mit Filter, Sortierung, Pagination |
| `POST` | `/api/v1/<resource>` | anlegen |
| `GET` | `/api/v1/<resource>/{id}` | einzeln laden |
| `PATCH` | `/api/v1/<resource>/{id}` | teilweise ändern |
| `PUT` | `/api/v1/<resource>/{id}` | vollständig ersetzen |
| `DELETE` | `/api/v1/<resource>/{id}` | löschen (Soft-Delete wenn vorhanden) |
| `GET` | `/api/v1/<resource>/{id}/revisions` | Versionsgeschichte |
| `POST` | `/api/v1/<resource>/{id}/restore` | Soft-Delete rückgängig |
| `POST` | `/api/v1/<resource>/batch` | mehrere Operationen in einem Request |
| `GET` | `/api/v1/<resource>/export` | Export (JSON, NDJSON, CSV) |
| `POST` | `/api/v1/<resource>/import` | Import (JSON, NDJSON, CSV) |

Beispiel-Ressourcen: `users`, `teams`, `messages`, `documents`, `events`, `tasks`, `contacts`, `files`, `tags`, `notifications`, `integrations`.

## Authentifizierung

### API-Key

```
GET /api/v1/documents HTTP/1.1
Host: hub.example.org
Authorization: Bearer fs_live_9f2c1a…
Accept: application/json
```

### Header-Standard

| Header | Beschreibung |
|--------|--------------|
| `Authorization` | `Bearer <token>` oder `Basic <base64>` |
| `X-Api-Key` | Alternative zum Bearer-Token |
| `X-Workspace-Id` | Ziel-Workspace bei Mandantenfähigkeit |
| `X-Request-Id` | UUID zur Nachverfolgung, wird zurückgegeben |
| `Accept-Language` | `de`, `en`, `fr` |
| `If-Match` | ETag für optimistische Sperre |
| `Idempotency-Key` | UUID für wiederholbare `POST` |

### OAuth2

| Schritt | Endpoint |
|---------|----------|
| Autorisierung | `GET /api/v1/oauth/authorize` |
| Token | `POST /api/v1/oauth/token` (`authorization_code`, `client_credentials`, `refresh_token`) |
| Scopes | `read:documents`, `write:documents`, `read:messages`, `admin` |

## Response-Envelope

```json
{
  "data": [ { "id": "doc_01HZXD", "title": "Einführung" } ],
  "meta": {
    "total": 132,
    "limit": 25,
    "nextCursor": "eyJvZmZzZXQiOjI1fQ",
    "requestId": "b2c1…"
  },
  "links": {
    "self": "/api/v1/documents?limit=25",
    "next": "/api/v1/documents?cursor=eyJvZmZzZXQiOjI1fQ"
  }
}
```

Einzelressource:

```json
{
  "data": {
    "id": "doc_01HZXD",
    "title": "Einführung",
    "status": "published",
    "createdAt": "2026-10-01T09:00:00+02:00",
    "updatedAt": "2026-10-28T11:04:00+01:00"
  },
  "meta": { "etag": "W/\"7-a1b2\"" }
}
```

## Pagination

| Parameter | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `limit` | number | `25` | 1–100 Einträge |
| `cursor` | string | - | Cursor der nächsten Seite |
| `offset` | number | `0` | alternativ zum Cursor |

```bash
curl -H "Authorization: Bearer $FS_TOKEN" \
  "https://hub.example.org/api/v1/tasks?limit=50&cursor=eyJvZmZzZXQiOjUwfQ"
```

## Filter, Sortierung, Suche

| Parameter | Beispiel | Beschreibung |
|-----------|----------|--------------|
| `filter` | `filter=status:eq:open` | `feld:op:wert` mit `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `like`, `null` |
| `filter` (mehrere) | `filter=status:eq:open;dueAt:lt:2026-12-01` | mit `;` kombiniert (UND) |
| `sort` | `sort=-dueAt,title` | `-` = absteigend |
| `q` | `q=budget` | Volltextsuche |
| `fields` | `fields=id,title,status` | Feldeinschränkung (Sparse Fieldsets) |
| `expand` | `expand=assignees,tags` | Referenzen ausrollen |
| `includeDeleted` | `true` | Soft-Gelöschte mitliefern |

```bash
curl -H "Authorization: Bearer $FS_TOKEN" \
  "https://hub.example.org/api/v1/tasks?filter=status:eq:open;assigneeId:eq:user_01HZXA&sort=-dueAt&fields=id,title,dueAt&limit=25"
```

## Erstellen und Ändern

```bash
curl -X POST "https://hub.example.org/api/v1/tasks" \
  -H "Authorization: Bearer $FS_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 6f0f…" \
  -d '{
    "title": "Dokumentation fertigstellen",
    "boardId": "board_01HZY2",
    "assigneeIds": ["user_01HZXA"],
    "priority": "high",
    "dueAt": "2026-11-15T17:00:00+01:00"
  }'
```

```bash
curl -X PATCH "https://hub.example.org/api/v1/tasks/task_01HZXG" \
  -H "Authorization: Bearer $FS_TOKEN" \
  -H "Content-Type: application/json" \
  -H 'If-Match: W/"3-88ac"' \
  -d '{ "status": "done" }'
```

## Batch

```json
{
  "operations": [
    { "op": "create", "resource": "tasks", "data": { "title": "A" } },
    { "op": "update", "resource": "tasks", "id": "task_01HZXG", "data": { "status": "done" } },
    { "op": "delete", "resource": "tasks", "id": "task_01HZXH" }
  ]
}
```

Antwort pro Operation mit `index`, `status` und `data` oder `error`; Abbruch bei `stopOnError: true`.

## Fehlerformat

```json
{
  "error": {
    "code": "validation_error",
    "message": "Pflichtfeld 'title' fehlt",
    "status": 400,
    "requestId": "b2c1…",
    "fields": [{ "field": "title", "issue": "required" }]
  }
}
```

| HTTP | code | Bedeutung |
|------|------|-----------|
| 400 | `validation_error` | Payload ungültig |
| 401 | `unauthorized` | kein oder falscher Token |
| 403 | `forbidden` | Recht fehlt |
| 404 | `not_found` | Ressource existiert nicht |
| 409 | `conflict` | ETag-Konflikt, Duplikat oder Sperre |
| 413 | `payload_too_large` | Körper zu groß |
| 422 | `unprocessable` | Schema gültig, Fachregel verletzt |
| 429 | `rate_limited` | Kontingent erschöpft |
| 500 | `internal_error` | Serverfehler |
| 503 | `unavailable` | Wartung, Replikationsverzug |

## Synchronisation

| Mechanismus | Beschreibung |
|-------------|--------------|
| `ETag` + `If-Match` | optimistische Sperre bei `PATCH`/`PUT` |
| `Last-Modified` + `If-None-Match` | Cache, Antwort `304` |
| `updatedSince` | Delta-Abfrage: `GET /tasks?updatedSince=2026-10-30T00:00:00Z` |
| `deletedSince` | Synchronisation mit gelöschten Datensätzen |
| `syncToken` | persistenter Marker für Voll-/Delta-Abgleich |

## Rate Limits

| Bereich | Standard |
|---------|----------|
| Standard-Token | 600 Anfragen / Minute |
| Write-Operationen | 120 / Minute |
| Batch | 30 Anfragen / Minute, max. 100 Operationen |
| Import/Export | 10 / Stunde |

Header: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`.

## Webhooks

```bash
curl -X POST "https://hub.example.org/api/v1/integrations" \
  -H "Authorization: Bearer $FS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "kind": "webhook",
    "targetUrl": "https://hooks.example.org/fs",
    "events": ["document.created", "task.updated"],
    "secret": "whsec_…"
  }'
```

| Event | Auslösung |
|-------|-----------|
| `document.created` / `.updated` / `.published` / `.deleted` | Wiki-Seite |
| `message.created` / `.updated` / `.deleted` | Chat-Nachricht |
| `task.created` / `.updated` / `.moved` / `.deleted` | Aufgabe |
| `event.created` / `.updated` / `.cancelled` | Termin |
| `contact.created` / `.updated` | Kontakt |
| `file.uploaded` / `.deleted` | Datei |
| `user.invited` / `.disabled` | Konto |

Payload:

```json
{
  "id": "evt_01HZY9",
  "type": "task.updated",
  "createdAt": "2026-10-31T06:20:00+01:00",
  "data": {
    "id": "task_01HZXG",
    "changes": [{ "field": "status", "from": "open", "to": "done" }]
  }
}
```

Signatur-Header: `X-FS-Signature: sha256=<hmac(secret, body)>`; Zustellversuche mit Backoff (1 min, 5 min, 30 min, 2 h, 6 h).

## SDKs und Clients

| Sprache | Paket | Beispiel |
|---------|-------|----------|
| JavaScript/TypeScript | `@freesynergy/client` | `client.tasks.list({ filter: "status:eq:open" })` |
| Python | `freesynergy` | `client.tasks.list(status="open")` |
| PHP | `freesynergy/sdk` | `$client->tasks->list(['status' => 'open'])` |
| CLI | `fs` | `fs tasks list --status open --limit 25` |

### Python-Beispiel

```python
from freesynergy import Client

client = Client(token="fs_live_9f2c1a")

for task in client.tasks.list(filter="status:eq:open", sort="-dueAt"):
    print(task.id, task.title, task.due_at)

client.tasks.update(
    task.id,
    data={"status": "done"},
    if_match=task.etag,
)
```

## Siehe auch

- [Standardmodelle](modelle.md)
- [Standardfelder](felder.md)
- [Datenformate](formate.md)
- [Konventionen](konventionen.md)
- [Desktop-Skins — API-Beispiele](../apps/desktop/skins/)
- [Workflows](../apps/workflows/)
