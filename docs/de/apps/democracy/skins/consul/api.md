# Consul - API Dokumentation

## Übersicht

Consul veröffentlicht **REST-JSON-Endpunkte** für Beteiligungsdaten (Vorschläge, Debatten, Polls, Haushalts-Elemente) plus OAuth2 für App-Zugriff. Die API ist primär lesend (Schreib-Endpunkte je Version/Installation — prüfen).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/v1/…` (z.B. proposals, polls, budgets) | öffentliche Inhalte | offiziell |
| OAuth2-Auth für private Inhalte/Apps | Zugriff | offiziell |
| Webhooks | je Version/Installation (ältere ohne) | eingeschränkt |
| GraphQL | — | ❌ |

## Authentifizierung

- öffentliche Endpunkte: keine
- Apps: OAuth2 (Client-Credentials/Authorization Code), Administrator gewährt

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/proposals.json` | Vorschläge (Pagination, `sort`) |
| `GET` | `/api/v1/proposals/{id}.json` | Detail |
| `GET` | `/api/v1/polls.json` | Abstimmungen |
| `GET` | `/api/v1/budgets.json` + `/budgets/{id}/investments` | Bürgerhaushalt |
| `GET` | `/api/v1/debates.json` | Debatten |

## Beispiel

Request:

```http
GET /api/v1/proposals.json?limit=20&sort=supports_count HTTP/1.1
Accept: application/json
```

Response:

```json
{ "data": [
  { "id": 903, "title": "Fahrradstraße Nord", "supports": 812,
    "theme": "Movilidad", "url": "https://consul.example/proposals/903" } ] }
```

## Rate Limits

instanzseitig (Stadtserver), üblich: großzügig für Lesezugriff.

## Skin-Hinweis

JSON-Feldnamen (supports_count, investments) direkt als [felder.md](../../../../data/modelle.md)-Referenz übernehmbar; für Live-Sync Export-Jobs statt Webhooks einplanen.
