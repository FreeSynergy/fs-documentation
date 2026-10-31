# n8n - API Dokumentation

## Übersicht

Zwei API-Ebenen: die **Workflow-Ausführungs-API** (`/rest/v1`, Instanzverwaltung/Trigger) und **Webhooks** als Einlaufpunkte der Workflows. Self-hosted wie Cloud identisch.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/rest/v1/workflows|executions|credentials` | Verwaltung, Trigger (`/workflows/{id}/activate`) | offiziell |
| Workflow-Webhooks | `POST /webhook/<pfad>`, Test `/webhook-test/<pfad>` | offiziell |
| Webhook-Antworten | Workflow → HTTP-Response (sync/async) | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- **API-Key** (Instanz → Settings → API): Header `X-N8N-API-KEY: <key>`
- Webhooks: eigene Auth (Header-Token, Basic) oder Query-Geheimnis
- Cloud wie self-hosted

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET/POST` | `/rest/v1/workflows` | Workflows listen/anlegen (JSON-Definition) |
| `PATCH/DELETE` | `/rest/v1/workflows/{id}` | ändern/löschen |
| `POST` | `/rest/v1/workflows/{id}/activate` | aktivieren |
| `POST` | `/rest/v1/workflows/{id}/run` | manuell starten (mit `data`) |
| `GET` | `/rest/v1/executions` | Verlauf (Filter status/workflow) |
| `GET` | `/rest/v1/executions/{id}` | Einzel-Log inkl. Node-Daten |
| `POST` | `/webhook/<name>` | Workflow-Trigger |
| `POST` | `/webhook/<name>`, `respond: "allNodesFinished"` | async-Antwort später via `/webhook-response/<id>` |

## Beispiel

Workflow per API starten:

```http
POST /rest/v1/workflows/42/run HTTP/1.1
X-N8N-API-KEY: <key>
Content-Type: application/json
{ "data": { "ticket": 9982 } }
```

Webhook-Trigger:

```bash
curl -X POST https://n8n.example.org/webhook/ticket-in \
  -H 'Content-Type: application/json' -d '{"ticket":{"id":9982}}'
```

## Rate Limits

Standardmäßig keine API-Grundgrenze; Webhook-/Queue-Kapazität hängt an Instanz (Workers, Redis). Cloud-Pläne: Ausführungs-/Concurrency-Kontingente.

## SDKs und Client-Bibliotheken

- CLI `n8n` (Administration), **n8n-mcp**/Community-SDKs (Python `n8n-client`)
- Workflow-JSON als Austauschformat (Import/Export/Source-Control)

## Skin-Hinweis

n8n-Workflow-JSON = Referenz für Integrations-Skins: Trigger + Schritte + Fehlerpfade als standardisierte Abläufe ([modelle.md](../../../../data/modelle.md) → Workflow/Event).
