# eBay - API Dokumentation

## Übersicht

Moderne **Sell/Browse-Familie** (JSON, REST): `Inventory API` (Artikel), `Listing API` (Angebote), `Sell Feed API` (Bulk), `Fulfillment API` (Bestellungen), `Browse API` (Katalog/Suche). Dazu die klassische Trading-API (XML). Alles OAuth2.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `https://api.ebay.com/sell/inventory/v1/…` | Lagerartikel | offiziell |
| REST `/sell/listing/v1/inventory_listing/` | Listings erstellen/ändern | offiziell |
| REST `/sell/fulfillment/v1/order/…` | Bestellungen, Versandstatus | offiziell |
| REST `/buy/browse/v1/item/search` | Suchen (Marktforschung) | offiziell |
| Trading XML (`verifyAddItem` etc.) | Legacy | offiziell |
| Push-Events | nicht frei; Polling/Feed-Status | eingeschränkt |

## Authentifizierung

1. App im Developer-Portal (Auth-Scopes beantragen)
2. Application Token: `POST /identity/v1/oauth2/client_token` (client_credentials)
3. User-Token: Authorization-Code-Flow → Access+Refresh; `Authorization: Bearer`

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `PUT` | `/sell/inventory/v1/inventory_item/{sku}` | Artikel anlegen/aktualisieren |
| `POST` | `/sell/inventory/v1/inventory_item/{sku}/offer` | Marketplace-Angebot (price, marketplace_id EBAY_DE) |
| `POST` | `/sell/listing/v1/inventory_listing/` | Listing publizieren (auction/FixedPrice) |
| `GET` | `/sell/fulfillment/v1/order?orderStatus=INTEGRATION_PENDING` | Bestellungen |
| `POST` | `/sell/fulfillment/v1/order/{id}/shipping_fulfillment` | Versand melden (tracking) |
| `GET` | `/buy/browse/v1/item/search?q=…&fieldgroups=…` | Markt-Suche |

## Beispiel

```http
POST /sell/listing/v1/inventory_listing/ HTTP/1.1
Authorization: Bearer <user-access-token>
Content-Type: application/json

{ "sku": "KER-004", "marketplaceId": "EBAY_DE", "format": "FIXED_PRICE",
  "availableForCheckout": true,
  "listingPolicyId": "5000123", "fulfillmentPolicyId": "5000234" }
```

Response: `{ "listingId": "…", "sku": "KER-004", "status": "PUBLISHED" }`

## Rate Limits

pro API/Operation dokumentiert (z.B. mehrere hundert Requests/min + Tageskontingente je Seller-Level); Fehler `429` + `X-ebay-*`-Header.

## SDKs und Client-Bibliotheken

- offizielle SDKs (Node/Java), Postman-Sammlungen; Trading-SDK historisch

## Skin-Hinweis

Bestell-/Listing-Reader für Dashboard-Skins; Gebühren-/Feldnamen in [felder.md](../../../../data/felder.md) normieren, Policies der API-Nutzung einhalten (Compliance-Skin!).
