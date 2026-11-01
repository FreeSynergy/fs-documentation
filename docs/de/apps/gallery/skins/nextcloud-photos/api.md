# Nextcloud Photos - API Dokumentation

## Übersicht

Die Galerie nutzt die Plattform-APIs: **WebDAV** für Dateien, **OCS** für Alben und Sharing, zusätzliche Photos-Endpunkte unter `/apps/photos/api`. Alle Zugriffe sind nutzerbezogen und folgen den Rechten der Files-App.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| WebDAV `/remote.php/dav/files/<user>/` | Dateien, Metadaten, Ordner | offizieller Standard |
| OCS `/ocs/v2.php/...` | Alben, Teilen, Navigation, Preview | offiziell |
| Photos-Endpunkte `/index.php/apps/photos/api/v1/…` | Chronologie, Ordnerauswahl | offiziell (app-intern) |
| GraphQL / Webhooks | — (Webhooks nur als App) | ❌ |

## Authentifizierung

- **Basic mit App-Passwort** für WebDAV: `Authorization: Basic …`
- **OCS**: dasselbe Prinzip, Header `OCS-APIRequest: true`
- **Session-Cookie** in der Web-UI
- SSO (SAML/OIDC) liefert Nextcloud-Sitzungen; API-Passwörter bleiben nötig für Clients

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `PROPFIND` | `/remote.php/dav/files/<user>/` | Ordnerinhalte inkl. `_displayname`, `getlastmodified` |
| `GET` | `/remote.php/dav/files/<user>/Fotos/IMG.jpg` | Dateiinhalt |
| `PUT` | `/remote.php/dav/files/<user>/Fotos/IMG.jpg` | Upload |
| `GET` | `/index.php/core/preview?fileId=<id>&x=512&y=512` | generierte Vorschau |
| `GET` | `/index.php/apps/photos/api/v1/preview/<fileId>` | Vorschau in Galerie-Auflösung |
| `GET` | `/ocs/v2.php/apps/photos/folders` | für die Galerie gewählte Ordner |
| `GET/POST` | `/ocs/v2.php/apps/files_sharing/api/v1/shares` | Freigaben (Link/Benutzer/Gruppe) |
| `GET/POST/DELETE` | `/index.php/apps/files_sharing/publiclink/...` | öffentliche Links |
| `GET` | `/ocs/v2.php/privatedata` | Favoriten und Album-Metadaten (KVI) |

## Beispiel

Request:

```http
PROPFIND /remote.php/dav/files/kal/Fotos/ HTTP/1.1
Authorization: Basic <user:app-password>
Depth: 1
OCS-APIRequest: true
```

Response: `207 Multi-Status` mit DAV-XML; pro Bild `getcontenttype`, `creationdate` (EXIF-Aufnahme), `fileid`.

## Rate Limits

Keine API-Quotas; Bremsen kommen von PHP-Worker-Limits, `throttling`-App (Login) und Reverse-Proxy-Konfiguration.

## SDKs und Client-Bibliotheken

- **offiziell**: WebDAV-Clients (ncdu, rclone, Cyberduck), Client-Apps iOS/Android
- **Community**: Python `nextcloud-api-wrapper`, Node `nextcloud-node-client`
- **Export**: WebDAV-Rsync, Occ-Kommandos für Metadaten-Scan

## Skin-Hinweis

Datei-/Freigabeobjekte entsprechen dem Standardmodell ([modelle.md](../../../../data/modelle.md)); Preview-URLs verhalten sich wie [felder.md](../../../../data/felder.md) (`fileId` als Referenz).
