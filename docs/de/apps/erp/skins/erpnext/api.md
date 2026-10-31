# ERPNext - API Dokumentation

## Übersicht

Frappe liefert eine **generische JSON-REST-API für alle DocTypes**: `/api/resource/<DocType>`. Schema (Feldtypen, Links, Pflichtfelder) ist über die API selbst auslesbar — ideal für Skin-Mapping. Webhooks für Änderungen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/resource/<DocType>` | CRUD + Listen (Filter/Sort/Pagination) | offiziell |
| `/api/method/<pfad>` | whitelisted Python-Funktionen (Workflow-Aktionen, Reports) | offiziell |
| DocType-Metadaten (`/api/v2/doctype/<name>`) | Feldkatalog | offiziell |
| Webhooks | DocType-Ereignis → POST (Secret-Signatur) | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- API-Key/Secret des Users: `Authorization: token <api_key>:<api_secret>`
- OAuth2/OIDC (Provider wie Server), Cookie-Session für UI-Clients

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/resource/Customer?filters=[["mobile_no","like","%1234"]]` | Liste |
| `POST` | `/api/resource/Customer` | anlegen |
| `GET/PUT/DELETE` | `/api/resource/Customer/CUST-00042` | Detail (namentliche IDs!) |
| `POST` | `/api/method/frappe.client.insert` | generischer Insert |
| `GET` | `/api/v2/doctype/Sales Invoice/` | Metadaten-Feldliste |
| `POST` | `/api/method/erpnext.controllers.website_list_for_contact…` | Modul-Methoden |

## Beispiel

Request:

```http
POST /api/resource/Sales Invoice HTTP/1.1
Authorization: token abc123:def456
Content-Type: application/json

{ "customer": "Kunde X", "due_date": "2026-11-15",
  "items": [{ "item_code": "BERATUNG-TAG", "qty": 3, "rate": 850 }] }
```

Response: `200` → Dokument-JSON (`name`: `ACC-SINV-2026-00117`, `rounded_total`: 2550, Links, `doctype`).

## Webhooks

DocType + Event (after_insert/on_submit…), Callback + Signing-Secret; Payload enthält Doc-JSON + `request_id`.

## Rate Limits

keine eingebauten Standardlimits; Frappe Cloud/Proxy setzen Kontingente.

## SDKs und Client-Bibliotheken

- `frappe` Python-Bibliothek (offiziell, serverseitig + Client-Nutzung), Community-SDKs (Node/PHP)
- Postman-Sammlung in Frappe-Doku

## Skin-Hinweis

DocType-Metadaten → automatisches [Mapping](../../../../data/felder.md); namentliche Dokument-IDs (`CUST-…`) bei Verbundmodellen beachten.
