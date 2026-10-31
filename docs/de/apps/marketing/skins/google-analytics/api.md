# Google Analytics - API Dokumentation

## Übersicht

**Data API v4** (`https://analyticsdata.googleapis.com`, REST/JSON, `runReport`) liefert Report-Ergebnisse; **Management API** verwaltet Properties; BigQuery-Export bringt Roh-Events. Messung selbst läuft über gtag.js/GTM, nicht über eine Schreib-API.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Data API v4 `runReport`/`batchRunReports` | Berichte ziehen (Dimensions/Metrics/Filters) | offiziell |
| Management API | Konten/Properties/Streams | offiziell |
| BigQuery-Export (GA4) | Event-Rohdaten (SQL) | offiziell |
| Realtime via API (`runRealtimeReport`) | Live-Kennzahlen | offiziell |
| Webhooks | — | ❌ |

## Authentifizierung

- OAuth2 (Service Account empfohlen; Scope `analytics.readonly`) → Bearer-Token
- Property-Ressourcen-Name: `properties/123456`

## Kernmethoden

| Methode | Beschreibung |
|---------|--------------|
| `POST /v4/properties/{id}/runReport` | Report (`dimensions`, `metrics`, `dateRanges`, `dimensionFilter`) |
| `POST …/runRealtimeReport` | Echtzeit |
| `POST …/batchRunReports` | mehrere Reports |
| Management: `GET /accounts/{a}/properties` | Struktur |

## Beispiel

```http
POST /v4/properties/123456:runReport HTTP/1.1
Authorization: Bearer <oauth-token>
Content-Type: application/json

{ "dateRanges": [{ "startDate": "2026-10-01", "endDate": "2026-10-30" }],
  "dimensions": [{ "dimensionName": "pagePath" }],
  "metrics": [{ "metricName": "sessions" }],
  "limit": 20 }
```

Response: `rows[]` + `totals[]` (JSON-Zeilen).

## BigQuery-Schema (Kurzreferenz)

Tabellen `events_YYYYMMDD`, `events_intraday_…`; Spalten: `event_name`, `user_pseudo_id`, `event_params` (RECORD), `geo`…

## Rate Limits

Data API: Standard-Quotas pro Property/Projekt (moderat; Backoff bei 429/429-Familie).

## SDKs und Client-Bibliotheken

- offizielle Clients (Python `google-analytics-data`, Node, Java)
- GTM-Server-Anbindung für datensparsere Messung

## Skin-Hinweis

Report-Skins: Data-API nur für **aggregierte** Kennzahlen; personenbezogene Auswertung bleibt Sache von Self-Hosting-Alternativen ([modelle.md](../../../../data/modelle.md) → Datenschutz-Notiz).
