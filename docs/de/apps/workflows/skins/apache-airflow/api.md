# Apache Airflow - API Dokumentation

## Übersicht

**Stable REST API v2** (`/api/v2`, JSON) ersetzt die frühere unstable-API: DAGs, DAG-Runs, Task-Instances, Connections/Variables, Import von DAG-Dateien. Ergänzt um CLI (gleiche Mächtigkeit) und Event-getriebene Trigger (Datasets, Triggerer).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/v2/dags`, `/dagRuns`, `/taskInstances` | Verwaltung/Status | offiziell stable |
| `POST /api/v2/importDags` | DAG-Code hochladen (DAGs-Ordner beschreibbar) | offiziell |
| CLI `airflow …` | alles inkl. RBAC | offiziell |
| Webhooks eingehend | nicht eingebaut (via API-Trigger/Triggerer selbst bauen) | ❌ nativ |
| GraphQL | — | ❌ |

## Authentifizierung

- Session-Login (UI/Cookies), **HTTP Basic** (Rechner-Konten via FAB/RBAC), JWT (konfigurierbar)
- Empfehlungen: dedizierte API-User mit `Observer`/`Triggerer`-Rollen

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v2/dags` | DAG-Liste (Filter `paused`, `tags`) |
| `PATCH` | `/api/v2/dags/{dag_id}` | Pause an/aus |
| `POST` | `/api/v2/dags/{dag_id}/dagRuns` | Run starten (`logical_date`, `conf`) |
| `GET` | `/api/v2/dags/{dag_id}/dagRuns` | Historie |
| `GET` | `/api/v2/dags/{dag}/tasks/{task}/instances` | Task-States |
| `GET` | `/api/v2/…/taskInstances/{task}/{run}/logs/{try}` | Log-Datei |
| `POST` | `/api/v2/importDags/{file_token}` | DAG-Datei-Upload |
| `GET/POST/PATCH` | `/api/v2/connections`, `/variables` | Konfiguration |

## Beispiel

Run starten:

```http
POST /api/v2/dags/etl_nightly/dagRuns HTTP/1.1
Authorization: Basic <api_user>
Content-Type: application/json

{ "logical_date": "2026-10-30T00:00:00Z",
  "conf": { "kunde": 4711 } }
```

Response: `200` → `{ "dag_run_id": "manual__…", "state": "queued", "conf": {…} }`

## Ereignismuster (statt Webhooks)

- **Datasets**: `dag A >> outlet="s3://x/events"`, `dag B >> inlet=` → automatische Auslösung
- Triggerer-Sensoren starten DAGs bei externen Bedingungen (eigene Sensor-Klasse pollt API)

## Rate Limits

nicht eingebaut; Kapazität über API-Server/Reverse-Proxy.

## SDKs und Client-Bibliotheken

- `apache-airflow-client` (offizielles Python-SDK, aus OpenAPI generiert)
- OpenAPI-Spec (`/api/v2/openapi.json`) → eigene Clients

## Skin-Hinweis

DAG/Task-Instance-Modell als Referenz für geplante Abläufe in [modelle.md](../../../../data/modelle.md); Konfiguration über Connections/Variables spiegelt Credential-Modelle.
