# LibrePhotos - API Dokumentation

## Übersicht

Django-REST-Endpunkte unter `/api/`, von Web-UI und Apps genutzt. Die API ist funktional vollständig, aber nicht versioniert und ohne offizielle OpenAPI-Referenz.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON `/api/...` | Photos, Alben, Personen, Suche, Upload | offiziell (undokumentiert stabil) |
| Django-Admin | Verwaltung | nur Web |
| Celery-Jobs | Scan, ML | intern |
| GraphQL / Webhooks | — | ❌ |

## Authentifizierung

- **Token**: `Authorization: Token <token>` (Login-Endpunkt liefert Token)
- **Session-Cookie** im Browser
- Zwei-Faktor optional für Konten

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/auth/token/` | Login, liefert Token |
| `GET` | `/api/photos` | Auflistung mit Filtern (`user`, `album`, `date`) |
| `GET` | `/api/photos/{id}` | Detail inkl. EXIF und Faces |
| `POST` | `/api/photos/upload/` | Upload (multipart) |
| `GET` | `/api/search` | Volltext und semantisch (`search_text`, `time`) |
| `GET/POST` | `/api/albums` | Alben lesen/anlegen |
| `POST` | `/api/albums/{id}/photos` | Aufnahmen hinzufügen |
| `GET` | `/api/people` | Personen und Gesichter |
| `POST` | `/api/people/{id}/merge` | Personen zusammenführen |
| `POST` | `/api/share` | Album-Freigabe (Link/Benutzer) |
| `POST` | `/api/tasks/scan` | Scan-Aufgabe anstoßen |

## Beispiel

Request:

```http
POST /api/search HTTP/1.1
Authorization: Token <token>
Content-Type: application/json

{ "search_text": "Hund im Garten", "user": 3, "time": "all" }
```

Response: `200 OK` mit `{ "results": [ { "id": 812, "image": "/media/samples/…jpg" } ] }`.

## Rate Limits

Keine API-Limits vorkonfiguriert; Django-Caching und Reverse-Proxy-Limits empfohlen.

## SDKs und Client-Bibliotheken

- **offiziell**: keine SDKs; Referenz sind die API-Aufrufe des React-Clients
- **Community**: Python-Skripte für Import/Export in Repositanhängen
- **Export**: Ordner-Export über Admin-Kommando `manage.py export`

## Skin-Hinweis

Modell Photo/Album/Person entspricht [modelle.md](../../../../data/modelle.md); wegen fehlender Versionierung sollten Feldänderungen bei Upgrades geprüft werden.
