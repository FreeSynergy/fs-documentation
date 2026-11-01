# Damselfly - API Dokumentation

## Übersicht

Damselfly bietet eine JSON-API für Upload, Suche, Ordner und Verwaltung. Sie wird vom Web-Frontend genutzt und ist der einzige Weg für Automatisierung (Import-Skripte, Bulk-Upload).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON `/api/...` | Upload, Suche, Alben, Personen, Verwaltung | offiziell |
| Upload-Endpunkte (multipart) | Einzeln und als Bulk | offiziell |
| GraphQL / Webhooks | — | ❌ |

## Authentifizierung

- **Session-Cookie** nach Login
- **API-Token** für Skripte (Admin-Bereich erzeugbar), Header `Authorization: Bearer <token>`
- Reverse-Proxy-Auth (z. B. authelia) wird häufig vorgeschaltet

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/Upload` | Datei-Upload (multipart, Zielordner) |
| `POST` | `/api/Upload/Chunked` | großer Dateien in Blöcken |
| `GET` | `/api/Search` | Suche (`searchTerm`, `folderId`, `labels`, `dateFrom/To`) |
| `POST` | `/api/Search/Similar` | Ähnlichkeitssuche (`imageId`) |
| `GET` | `/api/Images/{id}` | Metadaten, Label, Personen |
| `PATCH` | `/api/Images/{id}` | Titel, Favorit, Label, Ordner |
| `DELETE` | `/api/Images/{id}` | Bild löschen |
| `GET/POST` | `/api/Albums` | Alben lesen/anlegen |
| `GET` | `/api/People` | Gesichts-Cluster, Benennen per `PATCH` |
| `POST` | `/api/Sync/Push` · `/api/Sync/Pull` | Ordner-Abgleich |
| `GET` | `/api/Index/Status` | ausstehende Index-Aufgaben |

## Beispiel

Request:

```http
POST /api/Search/Similar HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "imageId": 4711, "limit": 20 }
```

Response: `200 OK` mit `{ "results": [ { "id": 4802, "distance": 0.12 } ] }`.

## Rate Limits

Keine harten Limits; Upload-Größen und Worker-Anzahl konfigurieren den Durchsatz (`MAX_UPLOAD_SIZE`, Queue-Größe).

## SDKs und Client-Bibliotheken

- **offiziell**: keine SDKs; Import-Beispiele in den Release-Notes
- **Community**: Bash/PowerShell-Skripte für Bulk-Upload
- **Export**: Ordner-Export über Dateisystem, Metadaten als XMP-Sidecar

## Skin-Hinweis

Image/Album/Person/Label entsprechen dem Standardmodell ([modelle.md](../../../../data/modelle.md)); ID-Typ ist ganzzahlig.
