# Etsy - API Dokumentation

## Übersicht

**Open API v3** (`https://openapi.etsy.com/v3`, JSON). Lesezugriff mit API-Key, erweiterte Lese-/Schreiboperationen mit OAuth2-Access-Token (Scopes wie `listings_r`, `listings_w`, `receipts_r`, `shops_r`, `feedback_r`). App-Zulassung erforderlich.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v3 | shops, listings, receipts, reviews, taxonomy | offiziell (App-Akzeptanz) |
| OAuth2 Authorization Code + **PKCE** | Benutzerzugriff | offiziell |
| Webhooks | — | ❌ (polling) |
| GraphQL | — | ❌ |

## Authentifizierung

```
GET /v3/application/shops/{shopId}?api_key=<key>          (App-Ebene)
Authorization: Bearer <oauth-access-token>                (Nutzer-Ebene)
```

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v3/shops/{shop_id}/listings?limit=25&includes=Images` | Listings |
| `GET` | `/v3/shops/{shop_id}/receipts` | Bestellungen |
| `POST/PATCH` | `/v3/shops/{id}/listings` / `/v3/listings/{id}` | erstellen/ändern (Scopes `listings_*`) |
| `GET` | `/v3/ships-to-regions`, `/v3/taxonomy/…*` | Versand/Taxonomie-Helfer |
| `GET` | `/v3/listings/{id}/reviews` | Bewertungen |

## Beispiel

```http
GET /v3/shops/12345678/receipts?limit=50&sort_field=created&sort_order=desc
x-api-key: <api-key>
Authorization: Bearer <token-mit-receipts_r>
```

Response:

```json
{ "count": 50, "results": [
  { "receipt_id": 998877, "listing_id": 554433, "name": "Keramikset",
    "quantity": 1, "total_price": { "amount": 5240, "scale": 2, "currency_code": "EUR" },
    "shipping_address": { "name": "…", "country": "DE" }, "is_shipped": false } ] }
```

## Rate Limits

**~10.000 Requests/Tag pro App** (dokumentierte Vorgabe; 429 + Backoff, Header `X-Edg-Ratelimit-*`).

## SDKs und Client-Bibliotheken

- offiziell: OpenAPI-Spec + Beispielskripte; Community-Wrapper (Python/Node)

## Skin-Hinweis

`receipts`-Poll (5–15 min) ersetzt fehlende Webhooks; Feldnamen in [felder.md](../../../../data/felder.md) normieren (Beträge mit `scale`!).
