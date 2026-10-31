# Dolibarr - API Dokumentation

## Übersicht

**REST-API v3** unter `/api/index.php` (JSON), aktivierbar unter Start → Module → „API REST“. Objekte als Endpunkte (thirdparties, invoices, orders, products, projects, users, members…), CRUD + Filter. API-Keys je Benutzer. Webhooks über das Zusatzmodul „API REST hooks“; intern zusätzlich Trigger-/Hook-Klassen für PHP-Erweiterungen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v3 (`/api/index.php/<objekt>`) | CRUD, Listen (limit/sortfield/`sqlfilters`) | offiziell |
| API-Key (`Authorization: Bearer` / `?apikey=`) | Authentifizierung | offiziell |
| Webhooks (Modul) | Objekt-Ereignisse → POST | offiziell (Modul) |
| PHP-Triggers (`modXxx::…`) | serverseitige Hooks für Module | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

1. Admin → Benutzer → API-Keys erzeugen
2. `Authorization: Bearer <key>` (empfohlen) oder Session-Token nach Login

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/index.php/thirdparties?limit=10&sortfield=t.rowid&sortorder=DESC&sqlfilters=(t.nom:LK:%25GmbH%25)` | Dritte filtern |
| `GET/POST/PUT/DELETE` | `/api/index.php/thirdparties/{id}` | Detail/CRUD |
| `GET/POST` | `/api/index.php/invoices` | Kundenrechnungen (POST mit `lines`-Array) |
| `GET` | `/api/index.php/invoices/{id}` | inkl. Zeilen/Zahlungen |
| `POST` | `/api/index.php/orders` | Bestellungen |
| `GET/POST` | `/api/index.php/products` | Artikel |
| `GET/POST` | `/api/index.php/projects` | Projekte |

## Beispiel

Request:

```http
GET /api/index.php/thirdparties?sqlfilters=(t.client:=:2)&limit=50 HTTP/1.1
Authorization: Bearer <api-key>
Accept: application/json
```

Response: `200`

```json
{ "count": 2, "thirdparties": [
  { "id": 12, "nom": "Muster AG", "client": 1, "email": "vertrieb@muster.de",
    "code_client": "CLI-0012" } ] }
```

Rechnung anlegen: `POST /api/index.php/invoices` mit `{ "socid": 12, "type": 0, "lines": [{"product_id": 3, "qty": 2, "price": 120}] }`.

## Webhooks (Modul)

Modul aktivieren → Hooks definieren (Objekt + Ereignis wie `createInvoice`), Payload JSON an Ziel-URL; Signatur optional konfigurierbar.

## Rate Limits

keine internen Limits; Hosting-/Proxy-Ebene.

## SDKs und Client-Bibliotheken

- keine offiziellen SDKs; `curl`-Rezepte in der Online-Doku (dolibarr.org/wiki)
- Community-Bibliotheken (PHP/Node) für API v3

## Skin-Hinweis

`sqlfilters`-Syntax (t.feld:op:wert) in Sync-Skins sauber kapseln; Zahlenpräfix `CLI-…` wie in [felder.md](../../../../data/felder.md) dokumentieren.
