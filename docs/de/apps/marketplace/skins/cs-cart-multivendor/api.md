# CS-Cart Multi-Vendor - API Dokumentation

## Übersicht

CS-Cart exponiert eine **REST-API (`/api`)** für Kernobjekte: products, orders, categories, customers, shipments. Multivendor-Felder (vendor_id, fees) sind integriert. Authentifizierung per API-Schlüssel (Scope admin/seller/customer).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/products|orders|…` | CRUD mit JSON | offiziell |
| API-Keys (je Rolle) | Authentifizierung | offiziell |
| Webhooks (Add-on/Core je Version) | Bestell-/Produkt-Events | prüfen (Version) |
| GraphQL | — | ❌ |

## Authentifizierung

- API-Schlüssel im Backend erzeugen; Request-Header `Authorization: <key>` (Schema je Version in der Knowledgebase)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET/POST` | `/api/products` | Produkte (filterbar nach `vendor_id`) |
| `GET/PUT` | `/api/products/{id}` | Detail/Ändern |
| `GET` | `/api/orders?status=open` | Bestellungen |
| `PUT` | `/api/orders/{id}` | Statusupdates (Vendor-Sicht) |
| `GET/POST` | `/api/categories`, `/api/products/{id}/images` | Katalogteile |

## Beispiel

Request:

```http
GET /api/products?fields=product_id,product,vendors,price&limit=50 HTTP/1.1
Authorization: <api-key>
```

Response (Auszug):

```json
{ "products": [ { "product_id": 1042, "product": "Keramikset",
  "price": "48.00", "vendors": [{ "vendor_id": 3, "company": "Töpferei Nord" } ] } ] }
```

## Rate Limits

nicht hart eingebaut; Hosting-Limits + Drosselung empfohlen.

## Skin-Hinweis

`vendor_id`-Beziehung ist das Marktplatz-Merkmal im Datenmodell → [modelle.md](../../../../data/modelle.md) (Angebot↔Anbieter); Sync-Felder in [felder.md](../../../../data/felder.md) normieren.
