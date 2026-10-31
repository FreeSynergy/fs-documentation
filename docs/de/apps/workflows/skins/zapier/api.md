# Zapier - API Dokumentation

## Übersicht

Zapier hat APIs für zwei Richtungen: (1) **Zapier-Plattform-APIs** (eigene Apps bauen, Prefill-Webhooks, REST-Hooks als Trigger), (2) **Organisations-/Zap-Verwaltung-APIs** (Zaps per REST auflisten/ausführen; Zugangsdaten via API-Secret).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/v1/zaps` (Organization) | Zaps verwalten/trigger | offiziell (Team/Enterprise) |
| REST Hooks (Objects) | Push-Trigger: Zap hört auf eigene REST-Endpunkte | offiziell |
| Prefill-Webhooks | Felder für Zap-Formulare füllen | offiziell |
| OAuth2 (Platform) | eigene Connectors | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- Platform: OAuth2 (Client-Credentials/Authorization Code)
- Organisations-API: API-Secret (`Authorization: Bearer <jwt>` nach Login via `identities/jwt`)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/zaps` | Zaps des Kontos |
| `POST` | `/api/v1/zaps/{zapId}/run` | Zap ausführen (Input-Felder) |
| `POST` | `/resthooks/v2/subscriptions` | REST-Hook abonnieren (eigene API als Trigger) |
| `POST` | `/prefill/webhook/…` | Prefill beantworten |
| `POST` | `/platform/v1/deployments` | eigene App-Apps deployen (CLI `zapier` nutzt dies) |

## Beispiel

Zap ausführen:

```http
POST /api/v1/zaps/1234567/run HTTP/1.1
Authorization: Bearer <jwt>
Content-Type: application/json

{ "fields": { "Name": "Ada", "E-Mail": "ada@example.org" } }
```

Response: `200` → `{ "zapRun": { "status": "in_progress", "id": "run_…" } }`

## Prefill (Push-Trigger-Unterstützung)

```json
{ "bundle": { "trigger_data": {…} }, "authentication": {…} }
→ Antwort: { "fields": { "ticket_id": 9982 } }
```

## Rate Limits

dokumentiert pro API (moderat, 429 mit Backoff); Platform-Aufrufe je App-Limit.

## SDKs und Client-Bibliotheken

- **CLI `zapier`** (offiziell, Platform-Entwicklung: `zapier build/validate/push`)
- REST-Hooks mit eigenem HMAC-Signatur-Schema (Schema `x-zapier-hook`)

## Skin-Hinweis

Zap-Struktur (Trigger + Steps + Paths) = vereinfachtes Flow-Modell für Einsteiger-Templates ([modelle.md](../../../../data/modelle.md)).
