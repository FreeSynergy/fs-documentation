# Matomo - API Dokumentation

## Übersicht

Zwei API-Paare: **Tracking-API** (Ereignisse melden, `matomo.php`) und **Analytics-Reporting-API** (`matomo.php?module=API…`, auch REST `/api` in neueren Bauten). Alles mit `token_auth` (schreibend) bzw. öffentlich bei freigegebenen Reports.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Tracking-HTTP (`matomo.php?idsite=1&rec=1&…`) | Pageview/Event/Goal/E-Commerce | offiziell |
| Reporting-HTTP (`module=API&method=…`) | Berichte als JSON/XML/CSV | offiziell |
| REST-API (neuere Versionen, `/api/…`) | JSON-first-Alternative | offiziell (Version prüfen) |
| Webhooks | Plugin/Event-Mechanismen | Community |
| GraphQL | — | ❌ |

## Authentifizierung

- `token_auth=<32 Zeichen>` (persönlich, rollenwirksam) — niemals in öffentlichen Tracking-Codes!
- Public-Dashboards: `module=API&…&token_auth=anonymous&idSite=…` (wenn freigeschaltet)

## Kernmethoden

| Methode | Beschreibung |
|---------|--------------|
| `Actions.getActionUrls` | Top-Seiten |
| `VisitsSummary.get` | Besuche/Sessions je Tag |
| `CustomSegments.getSuggestedSegments` / eigene | Segmente |
| `Goals.getItems` / `EcommerceItems.getItems` | Conversions |
| Tracking-Parameter: `e_c/e_a/e_n` (Event), `ec_id…` (Shop) | Erfassung |

## Beispiel

Event melden (serverseitig):

```bash
curl "https://matomo.example.org/matomo.php?idsite=1&rec=1&apv=1\
&e_c=Formular&e_a=abschicken&e_n=Spende&url=https://org/spenden"
```

Bericht ziehen:

```http
GET /matomo.php?module=API&method=VisitsSummary.get&format=JSON
    &idSite=1&period=day&date=last30&token_auth=<token>
```

Response:

```json
{ "2026-10-01": { "nb_visits": 812, "nb_actions": 2411 },
  "2026-10-02": { "nb_visits": 903, "nb_actions": 2688 } }
```

## Rate Limits

Instanzseitig (`login`-Throttling; Tracking-Drosselung über Proxy).

## SDKs und Client-Bibliotheken

- offizielle Client-Libs (Python `matomo`, PHP, JS), `matomo-tag-manager`
- GA-Datenimport über Import-Plugin

## Skin-Hinweis

`idsite` = Property-Schlüssel in [modelle.md](../../../../data/modelle.md); Ereignisnamen als Vokabular in [felder.md](../../../../data/felder.md) zentral pflegen.
