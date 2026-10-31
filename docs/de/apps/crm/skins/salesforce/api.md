# Salesforce - API Dokumentation

## Übersicht

Die Salesforce-API-Landschaft ist die Referenzklasse: REST (SObjects, SOQL), Bulk 2.0, Metadata, Tooling, Platform Events (Pub/Sub) und Change Data Capture. Authentifizierung ausschließlich OAuth2.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST API `/services/data/vXX.0/…` | SObject-CRUD, SOQL-Abfragen, Describe | offiziell |
| SOAP API | Enterprise-/Partner-WSDL | offiziell |
| Bulk API 2.0 | Massenimporte/-exports (CSV/JSON-Jobs) | offiziell |
| Metadata-/Tooling-API | Customizing-Deployment | offiziell |
| Platform Events / CDC | Event-Push (Webhook-Ersatz) | offiziell |
| GraphQL | Betas für Analysen | ❌ nicht allgemein |

## Authentifizierung (OAuth2)

- **JWT Bearer Flow** (serverseitig, mit Zertifikat) oder **Client Credentials** für Integration-User
- Access-Token als `Authorization: Bearer <token>`; Refresh wie OAuth2 üblich
- „Connected App“ definiert Scopes und Policies

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/services/data/v62.0/sobjects/Account/{id}` | Record lesen |
| `PATCH` | `/…/sobjects/Account/{id}` | ändern |
| `POST` | `/…/sobjects/Account` | anlegen (auch `AllFields`) |
| `GET` | `/…/query?q=SELECT Id,Name FROM Account WHERE Industry='IT'` | SOQL-Abfrage |
| `GET` | `/…/sobjects/Account/describe` | Feld-Metadaten |
| `POST` | `/…/jobs/ingest` (Bulk 2.0) | Job für Massenlast |
| `POST` | `/…/sobjects/Event_Name/` (Platform Events) | Event veröffentlichen |
| `GET` | `/…/event-relay` / empConnector | Streaming (Pub/Sub, Long Polling) |

## Beispiel

Request:

```http
GET /services/data/v62.0/query?q=SELECT+Id,Name,Industry+FROM+Account+WHERE+NumberOfEmployees>100 HTTP/1.1
Authorization: Bearer 00D…!AQw…
```

Response:

```json
{ "totalSize": 2, "done": true,
  "records": [{ "attributes": {"type":"Account","url":"/services/data/v62.0/sobjects/Account/001…"},
    "Id": "001…", "Name": "Beta GmbH", "Industry": "IT" }] }
```

## Limits

- API-Requests pro 24 h je Org skaliert nach Edition/Lizenzen (Standard: 15k–1m+);
- SOQL-Rows, Field-Lengths, Governor Limits (Apex-Transaktionen);
- Integrationen sollten aggregieren/cachen (und CDC statt Polling nutzen).

## SDKs und Client-Bibliotheken

- offizielle SDKs: Java, JS (jsforce in Community-Nähe), PHP (forcedotcom), Python (simple-salesforce, Community)
- **sf-CLI / SFDX** (Deployment + Apex), **Data Loader** (Bulk), **Postman**-Sammlungen offiziell

## Skin-Hinweis

Standard-Objektnamen (Account/Contact/Lead/Opportunity) als Glossar fürs [CRM-Modell](../../../../data/modelle.md) verwenden; Describe-Aufrufe liefern Feld-Mapping automatisch.
