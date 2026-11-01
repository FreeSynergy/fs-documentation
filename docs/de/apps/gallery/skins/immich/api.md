# Immich - API Dokumentation

## Übersicht

Immich ist REST-basiert unter `/api` (OpenAPI/Swagger unter `/api/docs`). Alle Clients (Web, Mobile, CLI) nutzen dieselben Endpunkte. Dazu kommen interne Job-Warteschlangen (BullMQ) und Webhooks.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON `/api/...` | Assets, Alben, Personen, Suche, Teilen, Verwaltung | offiziell |
| Swagger-UI `/api/docs` | interaktive Referenz | offiziell |
| Webhooks | Ereignisse (asset.create …) → HTTP-POST | offiziell |
| GraphQL | — | ❌ |
| WebSocket | Upload-/Job-Fortschritt (intern) | inoffiziell |

## Authentifizierung

- **API-Key**: Header `x-api-key: <key>` (pro Benutzer, Scopes read/admin)
- **JWT-Session**: `Authorization: Bearer <jwt>` nach Login, Refresh über Cookie
- **OAuth2/OIDC**: Externer Provider konfigurierbar (Authentik, Keycloak, Google …)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/albums` | Alben des Kontos |
| `POST` | `/api/albums` | Album anlegen (`albumName`, `assetIds`) |
| `POST` | `/api/albums/{id}/assets` | Aufnahmen hinzufügen |
| `POST` | `/api/albums/{id}/sharing` | Freigabe an Benutzer |
| `GET` | `/api/assets` | Assets mit Filtern (`userId`, `isFavorite`, `takenAfter`) |
| `GET` | `/api/assets/{id}` | Detail inkl. EXIF |
| `GET` | `/api/assets/{id}/original` | Original herunterladen |
| `POST` | `/api/assets` | Metadaten-Eintrag vor Upload (`deviceAssetId`, `checksum`) |
| `PUT` | `/api/asset-status` | Batch: Favorit, Archive, Trash, Duplicate-Markierung |
| `POST` | `/api/search/metadata` | Suche nach EXIF/Ort/Person/Datum |
| `POST` | `/api/search/smart` | semantische CLIP-Suche (`{ "q": "hund am see" }`) |
| `GET` | `/api/people` | erkannte Personen, `updatePerson` zum Benennen |
| `POST` | `/api/share` | öffentlicher Link (`expiresAt`, `password`, `allowDownload`) |
| `POST` | `/api/jobs/{name}` | Job-Typ neu anstoßen (`THUMBNAIL`, `FACIAL_RECOGNITION`) |
| `GET/POST` | `/api/admin/users` | Benutzerverwaltung (nur Admin) |

## Beispiel

Request:

```http
POST /api/search/smart HTTP/1.1
x-api-key: <key>
Content-Type: application/json

{ "q": "Fahrrad in der Stadt", "size": 20 }
```

Response: `200 OK` mit `{ "assets": { "items": [ { "id": "…", "originalFileName": "IMG_1.jpg" } ], "count": 20 } }`.

## Rate Limits

Keine harte API-Begrenzung eingebaut; empfohlen werden Limits im Reverse Proxy sowie Job-Drossel (`IMMICH_MACHINE_LEARNING_QUEUE_CONCURRENCY`).

## SDKs und Client-Bibliotheken

- **offiziell**: `@immich/sdk` (TypeScript, aus OpenAPI generiert), offizielle CLI für Upload/Import
- **Community**: Python `immich-api-client`, Go- und Rust-Clients
- **Importe**: Google-Photos-Import, ExifTool-basierte Metadatenübernahme

## Skin-Hinweis

Asset/Album/Share entspricht dem Standardmodell ([modelle.md](../../../../data/modelle.md)); EXIF-Felder folgen [felder.md](../../../../data/felder.md).
