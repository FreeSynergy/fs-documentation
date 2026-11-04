# Matomo - API documentation

## Overview

Two API pairs: the **tracking API** (report events, `matomo.php`) and the **analytics reporting API** (`matomo.php?module=API…`, also REST `/api` in newer builds). Everything with `token_auth` (writing), or public for shared reports.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| Tracking HTTP (`matomo.php?idsite=1&rec=1&…`) | Pageview/event/goal/e-commerce | official |
| Reporting HTTP (`module=API&method=…`) | Reports as JSON/XML/CSV | official |
| REST API (newer versions, `/api/…`) | JSON-first alternative | official (check the version) |
| Webhooks | Plugin/event mechanisms | community |
| GraphQL | — | ❌ |

## Authentication

- `token_auth=<32 characters>` (personal, role-effective) — never in public tracking codes!
- Public dashboards: `module=API&…&token_auth=anonymous&idSite=…` (if switched on)

## Core methods

| Method | Description |
|--------|-------------|
| `Actions.getActionUrls` | Top pages |
| `VisitsSummary.get` | Visits/sessions per day |
| `CustomSegments.getSuggestedSegments` / your own | Segments |
| `Goals.getItems` / `EcommerceItems.getItems` | Conversions |
| Tracking parameters: `e_c/e_a/e_n` (event), `ec_id…` (shop) | Capture |

## Example

Report an event (server-side):

```bash
curl "https://matomo.example.org/matomo.php?idsite=1&rec=1&apv=1\
&e_c=Formular&e_a=abschicken&e_n=Spende&url=https://org/spenden"
```

Pull a report:

```http
GET /matomo.php?module=API&method=VisitsSummary.get&format=JSON
    &idSite=1&period=day&date=last30&token_auth=<token>
```

Response:

```json
{ "2026-10-01": { "nb_visits": 812, "nb_actions": 2411 },
  "2026-10-02": { "nb_visits": 903, "nb_actions": 2688 } }
```

## Rate limits

On the instance side (`login` throttling; tracking throttling via proxy).

## SDKs and client libraries

- Official client libs (Python `matomo`, PHP, JS), `matomo-tag-manager`
- GA data import via an import plugin

## Skin note

`idsite` = the property key in [modelle.md](../../../../../data/modelle.md); maintain the event names as a vocabulary centrally in [felder.md](../../../../../data/felder.md).
