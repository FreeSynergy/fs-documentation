# Lychee - API Dokumentation

## Übersicht

Lychee v5 spricht eine JSON-REST-API unter `/api`. Frontend und Mobile-Clients nutzen ausschließlich diese Endpunkte; die Referenz liegt im Repo (`openapi`-Zweige) und in den Controller-Quellen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON `/api/...` | Alben, Fotos, Freigaben, Nutzer, Einstellungen | offiziell |
| Share-Links `/public/…` | öffentlicher Zugriff auf Alben | offiziell |
| Webhooks / GraphQL | — | ❌ |

## Authentifizierung

- **Session**: Login `/api/Login` mit Benutzer/Passwort, Cookie-Session
- **API-Token**: `Authorization: Bearer <token>` (in Benutzer-Einstellungen erzeugbar)
- **OAuth2/OIDC**: Provider-Login, danach reguläre Session

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/Albums` · `GET /api/Root` | Wurzelbäume: Alben, Fotos, Tags |
| `GET` | `/api/Album?id=<id>` | Album mit Fotos und Vorschaustufen |
| `POST` | `/api/Album` | Album anlegen (`title`, `parent_id`) |
| `POST` | `/api/Album/{id}` | Album ändern |
| `DELETE` | `/api/Album/{id}` | Album löschen |
| `POST` | `/api/Photo` | Foto hochladen (multipart, `album_id`) |
| `GET` | `/api/Photo?id=<id>` | Foto-Details |
| `POST` | `/api/Photo/{id}` | Änderung (Titel, Beschreibung, Favorit, Rotation) |
| `DELETE` | `/api/Photo/{id}` | Foto löschen |
| `POST` | `/api/Share/Album` | Freigabe (`can_download`, `password`, `expires_at`) |
| `GET` | `/api/Share` | eigene Freigaben auflisten |
| `POST` | `/api/Search` | Suche nach Titel/Beschreibung/Album |
| `GET` | `/api/Instances` | Version, Einstellungen (Diagnose) |

## Beispiel

Request:

```http
POST /api/Album HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "title": "Sommer 2026", "parent_id": null, "sort": "date_desc" }
```

Response: `200 OK` mit `{ "data": { "id": "Abc123", "title": "Sommer 2026" } }`.

## Rate Limits

Keine API-Quotas eingebaut; empfohlen werden Limits im Webserver und Upload-Größen über `post_max_size`/`upload_max_filesize`.

## SDKs und Client-Bibliotheken

- **offiziell**: keine SDKs, aber vollständige API-Nutzung im React-Frontend als Referenz
- **Community**: Python/Node-Clients für Bulk-Upload
- **Import**: URL-Import, Lightroom-Export-Ordner

## Skin-Hinweis

Album/Photo/Share entsprechen dem Standardmodell ([modelle.md](../../../../data/modelle.md)); IDs sind Strings und müssen als solche behandelt werden.
