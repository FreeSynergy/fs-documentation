# OpenProject - API Dokumentation

## Übersicht

OpenProject stellt eine offene **REST-API v3** unter `/api/v3` bereit. Antworten sind HAL+JSON (hypermediale Links auf verwandte Ressourcen). Zur Instanz gehört ein interaktiver **API-Browser** unter `/api/docs`, der alle je Version verfügbaren Ressourcen zeigt. Ergänzende Maschinenschnittstellen: Webhooks (ausgehend), iCal-Kalenderfeeds.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v3 (`/api/v3/...`) | Arbeitspakete, Projekte, Benutzer, Abfragen, Stammdaten | Offiziell, HAL+JSON |
| API-Browser (`/api/docs`) | Selbstbeschreibung der eigenen Instanz | Offiziell |
| Webhooks | Arbeitspaket-Ereignisse nach außen | Offiziell (Modul) |
| GraphQL | ❌ Nicht vorhanden | - |
| iCal-Feeds | Kalenderabo "Meine Arbeiten"/Aktivitäten | Offiziell |

## Authentifizierung

- **Persönlicher API-Token**: in den Kontoeinstellungen erzeugbar; Nutzung als `Authorization: Bearer <token>`
- **OAuth 2.0**: Autorisierungscode-Flow und Client-Credentials für Apps (registrierte OAuth-Anwendung)
- **Session-Cookie**: funktioniert in derselben Browser-Sitzung (CSRF-Schutz beachten)
- **Basic Auth**: mit Benutzername und API-Token möglich, je nach Instanz deaktiviert (versionsabhängig)
- **Rechte**: die API erzwingt dieselben Projektberechtigungen wie die Oberfläche

## Endpunkte

Alle Pfade relativ zur Instanz-URL, z. B. `https://op.example.org/api/v3/work_packages`. Die vollständige Liste je Version liefert `/api/docs`; nicht alle Module besitzen in jeder Version Ressourcen (z. B. Zeitwirtschaft - im API-Browser prüfen, versionsabhängig).

### Arbeitspakete

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v3/work_packages` | Arbeitspakete Auflisten (Filter, Sortierung, Pagination) |
| `POST` | `/api/v3/work_packages` | Arbeitspaket anlegen |
| `GET` | `/api/v3/work_packages/{id}` | Einzelnes Arbeitspaket laden |
| `PATCH` | `/api/v3/work_packages/{id}` | Felder ändern, Statusübergang (`_links/status`) |
| `DELETE` | `/api/v3/work_packages/{id}` | Arbeitspaket löschen |
| `POST` | `/api/v3/work_packages/filter` | Komplexe Filter-Operatoren (AND/OR, Menge, Datum) |
| `GET` | `/api/v3/work_packages/{id}/activities` | Kommentierter Aktivitätenstrom (Pagination) |
| `POST`/`DELETE` | `/api/v3/work_packages/{id}/watchers...` | Beobachter hinzufügen/entfernen (Form versionsabhängig) |
| `POST` | `/api/v3/work_packages/{id}/attachments` | Anhang hochladen (multipart) |

### Projekte, Benutzer, Abfragen

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v3/projects` | Projekte auflisten |
| `POST` | `/api/v3/projects` | Projekt anlegen (Admin-Recht) |
| `PATCH` | `/api/v3/projects/{id}` | Projekteinstellungen ändern |
| `GET` | `/api/v3/memberships` | Projektmitgliedschaften (Formate je Version) |
| `GET` | `/api/v3/users` | Benutzer auflisten |
| `GET` | `/api/v3/users/{id}` | Benutzerprofil |
| `GET` | `/api/v3/queries` | Gespeicherte Abfragen laden |

### Stammdaten

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v3/statuses` | Arbeitspaket-Status |
| `GET` | `/api/v3/priorities` | Prioritäten |
| `GET` | `/api/v3/versions` | Versionen/Meilensteine |
| `GET` | `/api/v3/activities` | Projekt-Aktivitäten (Feed) |

## Pagination und Filter

- **Offset-Pagination**: `?offset=1&pageSize=25`; Antwort enthält `total`, `count`, `pageSize`, `offset` in `_embedded`
- **Cursor-Pagination**: `?startAfter=<id>` für große Listen (versionsabhängig)
- **Elemente** stehen in `_embedded.elements`; jedes Element trägt `_links` (self, status, project, ...)

## Beispiele

### Arbeitspakete auflisten (persönlicher Token)

```bash
curl -s -H "Authorization: Bearer <api-token>" \
  "https://op.example.org/api/v3/work_packages?pageSize=2&offset=1"
```

Antwort (gekürzt, HAL+JSON):

```json
{
  "_type": "Collection",
  "total": 137,
  "count": 2,
  "pageSize": 2,
  "offset": 1,
  "_embedded": {
    "elements": [
      {
        "_type": "WorkPackage",
        "id": 421,
        "subject": "Login-Maske testen",
        "_links": {
          "self": { "href": "/api/v3/work_packages/421" },
          "status": { "href": "/api/v3/statuses/1", "title": "Neu" },
          "assignee": { "href": "/api/v3/users/7", "title": "anna" }
        }
      }
    ]
  }
}
```

### Arbeitspaket anlegen

```bash
curl -s -X POST \
  -H "Authorization: Bearer <api-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "API-Daendone",
    "_links": {
      "type": { "href": "/api/v3/types/1" },
      "project": { "href": "/api/v3/projects/5" },
      "status": { "href": "/api/v3/statuses/1" },
      "priority": { "href": "/api/v3/priorities/2" }
    }
  }' \
  "https://op.example.org/api/v3/work_packages"
```

### Filtern mit Operatoren

```bash
curl -s -X POST \
  -H "Authorization: Bearer <api-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "filters": [
      { "status": { "operator": "o", "values": [] } },
      { "project": { "operator": "=", "values": ["/api/v3/projects/5"] } }
    ],
    "sortBy": [{ "id": "updatedAt", "sort": "desc" }]
  }' \
  "https://op.example.org/api/v3/work_packages/filter"
```

## Rate Limits

- OpenProject publiziert **keine zentralen festen Zahlenwerte**; die Instanz kann Limitierungen über den Reverse Proxy (nginx/Traefik) erhalten
- Schwere `filter`-Abfragen sind teurer als einfache `GET`-Listen - für Skripte schlanke Filter und Pagination nutzen
- Fehlerfall: HTTP 429 bei externer Drosselung; `Retry-After` auswerten, falls vorhanden

## Webhooks

Das Webhook-Modul (Administration) sendet JSON an konfigurierte HTTPS-Endpunkte:

| Ereignis | Ausloesung |
|----------|------------|
| `openproject::work_package::created` | Arbeitspaket angelegt |
| `openproject::work_package::updated` | Arbeitspaket geändert (Feld-/Statuswechsel) |

Payload enthält das Arbeitspaket als `data`-Objekt (HAL-Struktur). Gültigkeit und zusätzliche Ereignisse: versionsabhängig, im Administration-Menue "Webhooks" sichtbar.

## SDKs und Client-Bibliotheken

- **Kein offizielles SDK**; die API ist bewusst normales REST/HAL
- **Community-Clients** existieren für Python und JavaScript (je nach Pflegezustand, ohne Gewaehr; ueber die REST-Doku direkt bleiben Skripte versionsstabiler)
- **Codegenerierung**: HAL ist nicht OpenAPI - Werkzeuge lesen die Beispiele im API-Browser `/api/docs`
- **Import-Skripte**: fuer Migrationen (z. B. aus Redmine) existieren Community-Skripte; offiziell sind Import-Assistenten je Version unterschiedlich

## Betriebshinweise

- API-Token sind personengebunden: Automatisierung über Dienstkonto mit minimalen Rechten betreiben
- `/api/docs` ist öffentlich erreichbar, wenn die Instanz es nicht deaktiviert - Zugang mitbedenken

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
