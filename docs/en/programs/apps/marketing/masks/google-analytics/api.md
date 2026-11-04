# Google Analytics - API documentation

## Overview

The **Data API v4** (`https://analyticsdata.googleapis.com`, REST/JSON, `runReport`) delivers report results; the **Management API** administers properties; the BigQuery export provides raw events. The measurement itself runs via gtag.js/GTM, not via a write API.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| Data API v4 `runReport`/`batchRunReports` | Pull reports (dimensions/metrics/filters) | official |
| Management API | Accounts/properties/streams | official |
| BigQuery export (GA4) | Raw event data (SQL) | official |
| Realtime via API (`runRealtimeReport`) | Live metrics | official |
| Webhooks | — | ❌ |

## Authentication

- OAuth2 (a service account is recommended; scope `analytics.readonly`) → bearer token
- Property resource name: `properties/123456`

## Core methods

| Method | Description |
|--------|-------------|
| `POST /v4/properties/{id}/runReport` | Report (`dimensions`, `metrics`, `dateRanges`, `dimensionFilter`) |
| `POST …/runRealtimeReport` | Realtime |
| `POST …/batchRunReports` | Several reports |
| Management: `GET /accounts/{a}/properties` | Structure |

## Example

```http
POST /v4/properties/123456:runReport HTTP/1.1
Authorization: Bearer <oauth-token>
Content-Type: application/json

{ "dateRanges": [{ "startDate": "2026-10-01", "endDate": "2026-10-30" }],
  "dimensions": [{ "dimensionName": "pagePath" }],
  "metrics": [{ "metricName": "sessions" }],
  "limit": 20 }
```

Response: `rows[]` + `totals[]` (JSON rows).

## BigQuery schema (quick reference)

Tables `events_YYYYMMDD`, `events_intraday_…`; columns: `event_name`, `user_pseudo_id`, `event_params` (RECORD), `geo`…

## Rate limits

Data API: standard quotas per property/project (moderate; backoff on 429/429 family).

## SDKs and client libraries

- Official clients (Python `google-analytics-data`, Node, Java)
- GTM server integration for more data-sparing measurement

## Skin note

Report skins: use the Data API only for **aggregated** metrics; evaluating personal data remains the domain of self-hosting alternatives ([modelle.md](../../../../../data/modelle.md) → data-protection note).
