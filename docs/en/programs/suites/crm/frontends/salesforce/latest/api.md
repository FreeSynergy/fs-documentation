# Salesforce - API Documentation

## Overview

The Salesforce API landscape is the reference class: REST (SObjects, SOQL), Bulk 2.0, Metadata, Tooling, Platform Events (Pub/Sub) and Change Data Capture. Authentication is exclusively OAuth2.

**API types at a glance**

| Type | Usage | Status |
|-----|------------|--------|
| REST API `/services/data/vXX.0/…` | SObject CRUD, SOQL queries, describe | official |
| SOAP API | Enterprise/partner WSDL | official |
| Bulk API 2.0 | mass imports/exports (CSV/JSON jobs) | official |
| Metadata/Tooling API | customization deployment | official |
| Platform Events / CDC | event push (webhook replacement) | official |
| GraphQL | betas for analytics | ❌ not generally available |

## Authentication (OAuth2)

- **JWT Bearer flow** (server-side, with certificate) or **client credentials** for integration users
- Access token as `Authorization: Bearer <token>`; refresh as usual for OAuth2
- A "Connected App" defines scopes and policies

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/services/data/v62.0/sobjects/Account/{id}` | read record |
| `PATCH` | `/…/sobjects/Account/{id}` | update |
| `POST` | `/…/sobjects/Account` | create (also `AllFields`) |
| `GET` | `/…/query?q=SELECT Id,Name FROM Account WHERE Industry='IT'` | SOQL query |
| `GET` | `/…/sobjects/Account/describe` | field metadata |
| `POST` | `/…/jobs/ingest` (Bulk 2.0) | job for bulk load |
| `POST` | `/…/sobjects/Event_Name/` (Platform Events) | publish event |
| `GET` | `/…/event-relay` / empConnector | streaming (Pub/Sub, long polling) |

## Example

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

- API requests per 24 h per org scale by edition/licenses (standard: 15k–1m+);
- SOQL rows, field lengths, governor limits (Apex transactions);
- Integrations should aggregate/cache (and use CDC instead of polling).

## SDKs and client libraries

- Official SDKs: Java, JS (jsforce, close to the community), PHP (forcedotcom), Python (simple-salesforce, community)
- **sf CLI / SFDX** (deployment + Apex), **Data Loader** (bulk), **Postman** collections officially provided

## Skin note

Use the standard object names (Account/Contact/Lead/Opportunity) as a glossary for the [CRM model](../../../../../../data/models.md); describe calls deliver the field mapping automatically.
