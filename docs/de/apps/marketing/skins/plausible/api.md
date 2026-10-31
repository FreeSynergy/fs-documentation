# Plausible - API Dokumentation

## Übersicht

Zwei schlanke Schnittstellen: **Events-API** (Tracking ohne/ergänzend zum Skript) und **Stats-API** (Lesezugriff auf Dashboard-Kennzahlen). Dazu CSV/JSON-Export der Rohdaten (self-hosted: direkt ClickHouse).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Events-API (`POST /api/event`) | benutzerdefinierte Ereignisse/Ziele aus Apps | offiziell |
| Stats-API (`GET /api/v1/stats/*`) | timeseries, top-values, aggregation | offiziell (API-Key) |
| Export (self-hosted) | JSON-Rohdatenexport-Endpoint | offiziell |
| GA-Import | Import-Assistent | offiziell |
| Webhooks/GraphQL | — | ❌ |

## Authentifizierung

- Events-API: keine (Domain-Bezug über `url`/Referrer-Prüfung; `X-API-Key` optional)
- Stats-API: `Authorization: Bearer <api-key>`

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/event` | Ereignis (`name`, `url`, `props`) |
| `GET` | `/api/v1/stats/realtime/visitors` | Live-Besucher |
| `GET` | `/api/v1/stats/timeseries` | Tagesreihe (Filter `period`, `date`, `filters`) |
| `GET` | `/api/v1/stats/aggregate` | Kennzahlen aggregiert |
| `GET` | `/api/v1/stats/top-pages` | Top-Seiten |

## Beispiel

Ziel melden:

```http
POST /api/event HTTP/1.1
Content-Type: application/json

{ "name": "Spende", "url": "https://org/danke",
  "domain": "org.example", "props": { "betrag": 25 } }
```

Response: `202`.

Kennzahlen:

```http
GET /api/v1/stats/aggregate?site_id=org.example&period=30d
    &metrics=visits,conversion_rate&filters=event:is:Spende
Authorization: Bearer <api-key>
```

## Rate Limits

Cloud: großzügige Limits (Events ~ pro Domain gedrosselt); Self-host: Server.

## SDKs und Client-Bibliotheken

- offizielle JS/HTTP-Doku, Community-Wrapper (Python), Plug-ins für CMS
- Events-Signatur-Header (self-hosted `reverse_proxy` Hinweise beachten)

## Skin-Hinweis

Goal-Name = Standardereigniswort in [felder.md](../../../../data/felder.md); Stats-API ideal für Wiki-KPI-Kacheln (Caching! 5–10 min).
