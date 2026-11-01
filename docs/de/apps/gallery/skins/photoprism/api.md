# PhotoPrism - API Dokumentation

## Übersicht

PhotoPrism stellt eine JSON-REST-API unter `/api/v1` bereit (Dokumentation unter `/api` bzw. Swagger). Web-UI und CLI (`photoprism command`) nutzen dieselben Endpunkte.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON `/api/v1/...` | Photos, Alben, Ordner, Labels, Personen, Suche | offiziell |
| CLI-Kommandos | Index, Backup, Admin-Aufgaben | offiziell |
| Webhooks | Index-/Medien-Ereignisse | optional |
| GraphQL | — | ❌ |

## Authentifizierung

- **Basic**: `Authorization: Basic base64(user:pass)` für Kontozugriff
- **Bearer/Client**: `Authorization: Bearer <client-secret>` mit Scopes (`read`, `write`)
- **Session**: Cookie nach Login für die Web-UI

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/photos?q=<suche>&count=60` | Suche (Label, Person, Ort, Zeitraum) |
| `GET` | `/api/v1/photos/{uid}` | Detail mit EXIF und Labeln |
| `POST` | `/api/v1/photos` | Foto anlegen/Upload (`data`, `upload[]`) |
| `PUT` | `/api/v1/photos/{uid}` | Änderung (Titel, Label, Favorit, public) |
| `DELETE` | `/api/v1/photos/{uid}` | aus dem Index entfernen |
| `GET` | `/api/v1/albums` · `POST /api/v1/albums` | Alben lesen/anlegen |
| `GET` | `/api/v1/folders/{uid}` | Ordnerbaum |
| `GET/POST` | `/api/v1/batch` | Batch-Aktionen (Label, Album, public) |
| `GET` | `/api/v1/labels` · `POST /api/v1/labels` | Labels, KI-Vorschläge bestätigen |
| `GET` | `/api/v1/people` · `PUT /api/v1/people/{uid}` | Personen benennen, Gesicht zuschneiden |
| `POST` | `/api/v1/index` | Index-Neuberechnung anstoßen |
| `GET` | `/api/v1/file/{hash}` | Datei-/Vorschaustream in gewünschter Größe |
| `POST` | `/api/v1/share` | Freigabe-Link mit Ablauf und Passwort |

## Beispiel

Request:

```http
GET /api/v1/photos?q=label:beach+person:anna&count=10 HTTP/1.1
Authorization: Bearer <client-secret>
Accept: application/json
```

Response: `200 OK` mit `{ "data": [ { "id": "abc123", "title": "…", "labels": ["beach"] } ], "count": 10 }`.

## Rate Limits

Keine festen API-Quotas; konfigurierbare Limits über Reverse Proxy und `PHOTOPRISM_ADMIN_API_*`. Batch-Endpunkte bevorzugen, um Request-Stürme zu vermeiden.

## SDKs und Client-Bibliotheken

- **offiziell**: `photoprism-client` (Go), CLI als Referenzclient
- **Community**: Python- und Node-Clients, Beispiele in den API-Docs
- **Import/Export**: Ordner-Import, `photoprism export`, ExifTool-Sidecars

## Skin-Hinweis

Photo/Album/Label/Person entspricht dem Standardmodell ([modelle.md](../../../../data/modelle.md)); EXIF-Felder folgen [felder.md](../../../../data/felder.md).
