# Axelor - API Dokumentation

## Übersicht

Jedes freigegebene Modell bekommt **REST-Endpunkte unter `/ws/rest/<modell>`** (JSON): `fetch`, `search`, `create`, `update`, `delete`, plus Custom-Actions. Batch-Aufrufe gesammelt; Authentifizierung per Basic (Nutzer/Pass oder API-Nutzer) bzw. JWT bei Token-Flows.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/ws/rest/partner|saleOrder|invoice…` | CRUD + `search`-Query (JSON-Regeln) | offiziell (je Modell aktivierbar) |
| `/ws/rest/batch` | mehrere Operationen pro Request | offiziell |
| Action-Endpunkte (`/ws/rest/saleOrder/confirm` o.ä.) | Workflow-Aktionen | offiziell (Custom Actions) |
| Webhooks eingehend | nicht eingebaut (Batch/REST reaktiv nutzen) | ❌ |
| GraphQL | — | ❌ |

## Authentifizierung

- `Authorization: Basic base64(user:pass)` (einfacher Client-Standard)
- JWT nach Login-Endpunkt für Sitzungs-Clients

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/ws/rest/partner/{id}` | Datensatz |
| `POST` | `/ws/rest/partner` | anlegen |
| `PUT` | `/ws/rest/partner/{id}` | ändern |
| `POST` | `/ws/rest/saleOrder/search` | Suche (`{"domain":[["state","=","confirmed"]],"fields":[…]}`) |
| `POST` | `/ws/rest/saleOrder/confirm` | Modell-Action (Beispiel) |
| `DELETE` | `/ws/rest/invoice/{id}` | löschen |

## Beispiel

Request:

```http
POST /ws/rest/partner/search HTTP/1.1
Authorization: Basic <bot:pass>
Content-Type: application/json

{ "domain": [["isCustomer","=",true]], "fields": ["fullName","email"], "limit": 50 }
```

Response: `200`

```json
{ "data": [ { "id": 41, "fullName": "Muster AG", "email": "vertrieb@muster.de" } ],
  "_searchCount": true }
```

## Batch

```http
POST /ws/rest/batch
{ "data": [ { "action": "create", "model": "partner", "data": {…} } ] }
```

## Rate Limits

nicht eingebaut; Gateway-Limits empfohlen.

## SDKs und Client-Bibliotheken

- keine offiziellen SDKs; REST-Clients + Swagger-Export (OpenAPI je Version verfügbar machen)

## Skin-Hinweis

Modellname = Endpunkt: Skin-Mapping kann Modellkatalog aus Builder-Metadaten lesen (analog [felder.md](../../../../data/felder.md)).
