# Redmine - API Dokumentation

## Übersicht

Redmine enthält eine **REST-API** im Kern: jede Sammlungs- oder Detailressource ist unter ihrem Pfad mit Endung `.xml` oder `.json` erreichbar (JSON ist seit Redmine 4.0 offiziell vollständig unterstützt). Zusätzlich liefert Redmine **Atom-Feeds** (`.atom`) und **ICS-Kalenderfeeds**. GraphQL, WebSocket-API oder Webhooks gibt es im Kern nicht.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST (`/issues.json` u. a.) | Issues, Projekte, Benutzer, Zeiterfassung, Stammdaten | Offiziell (XML/JSON) |
| Atom-Feeds (`.atom`) | Issues, Aktivitäten, Aktivitäten-Feed des Kontos | Offiziell |
| ICS-Feeds | Kalenderabo (URL mit Token) | Offiziell (Pfad versionsabhängig) |
| Webhooks | ❌ Nicht im Kern - nur Plugins | - |
| GraphQL / WebSocket | ❌ Nicht vorhanden | - |

## Authentifizierung

- **API-Key**: in „Mein Konto" erzeugbar; Übergabe als `?key=<apikey>` oder Header `X-Auth-Token: <apikey>`
- **Basic Auth**: Benutzername/Passwort im Authorization-Header
- **Session-Cookie**: API-Aufrufe aus der Browser-Sitzung heraus
- Der API-Key ist personengebunden; Rechte entsprechen den Projektrollen des Kontos

## Endpunkte

Alle Pfade relativ zur Instanz-URL, z. B. `https://redmine.example.org/issues.json`. Nicht alle Module haben Endpunkte - **Wiki-Seiten** besitzen im Kern keine REST-Endpunkte (Workarounds: Plugin oder Browser-Automation).

### Issues

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/issues.(xml\|json)` | Issues auflisten; Filter: `project_id`, `tracker_id`, `status_id`, `assigned_to_id`, `created_on`, `limit`, `offset` |
| `GET` | `/issues/{id}.(xml\|json)` | Detail; `?include=children,journals,attachments,relations,watchers,changesets,allowed_statuses` |
| `POST` | `/issues.(xml\|json)` | Issue anlegen (Projekt per Name oder ID) |
| `PUT` | `/issues/{id}.(xml\|json)` | Felder ändern, Notiz anhängen, Status wechseln |
| `DELETE` | `/issues/{id}.(xml\|json)` | Issue löschen |
| `GET` | `/issues/{id}/children.(xml\|json)` | Unter-Issues |
| `PUT`/`DELETE` | `/issues/{id}/watchers.(xml\|json)` | Beobachter hinzufügen/entfernen (User-ID im Body) |

### Projekte, Benutzer, Zeiterfassung

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/projects.(xml\|json)` | Projekte auflisten |
| `GET` | `/projects/{id}.(xml\|json)` | Projektdetails (`?include=trackers,issue_categories,versions,members`) |
| `POST`/`PUT`/`DELETE` | `/projects.(xml\|json)` | Projekte verwalten (Admin) |
| `GET` | `/projects/{id}/issue_categories.(xml\|json)` | Kategorien eines Projekts |
| `GET` | `/projects/{id}/memberships.(xml\|json)` | Mitgliedschaften und Rollen |
| `GET` | `/users.(xml\|json)` | Benutzer auflisten (Admin) |
| `GET` | `/users/current.(xml\|json)` | Angemeldetes Konto |
| `GET` | `/time_entries.(xml\|json)` | Zeiterfassungen mit Filtern |
| `POST`/`PUT`/`DELETE` | `/time_entries/{id}.(xml\|json)` | Zeiterfassung anlegen/ändern/löschen |

### Stammdaten, Anhänge, Sonstiges

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/enumerations.(xml\|json)` | Status, Prioritäten, Aktivitäten, Dokumenten-Kategorien |
| `GET` | `/trackers.(xml\|json)` | Tracker |
| `GET` | `/issues/{id}/attachments/{attachment_id}` | Anhang herunterladen |
| `DELETE` | `/attachments/{id}.(xml\|json)` | Anhang löschen |
| `POST` | `/uploads.(xml\|json)?filename=NAME` | Datei hochladen, liefert Token für Issue-Anhänge |
| `GET` | `/queries.(xml\|json)` | Öffentliche Abfragen |
| `GET` | `/news.(xml\|json)` | Projekt-News (Filter `project_id`) |
| `GET` | `/projects/{id}/versions.(xml\|json)` | Meilensteine/Versionen |

## Pagination

- Parameter `limit` (maximal **100**) und `offset`
- Antwort-Attribute: `total_count`, `limit`, `offset` (JSON: `limit`/`offset`/`total_count` auf oberster Ebene, XML: Attribute des Wurzelelements)

## Beispiele

### Issues abrufen

```bash
curl -s -H "X-Auth-Token: <apikey>" \
  "https://redmine.example.org/issues.json?project_id=kern&status_id=open&limit=2"
```

Antwort (gekürzt):

```json
{
  "issues": [
    {
      "id": 1234,
      "project": { "id": 5, "name": "Kern" },
      "tracker": { "id": 1, "name": "Fehler" },
      "status": { "id": 1, "name": "Neu" },
      "priority": { "id": 2, "name": "Normal" },
      "subject": "Login bricht ab",
      "author": { "id": 7, "name": "Anna Berg" },
      "created_on": "2026-10-30T09:12:00Z",
      "spent_on": null
    }
  ],
  "total_count": 87,
  "limit": 2,
  "offset": 0
}
```

### Issue anlegen

```bash
curl -s -X POST \
  -H "X-Auth-Token: <apikey>" \
  -H "Content-Type: application/json" \
  -d '{
    "issue": {
      "project_id": "kern",
      "tracker_id": 1,
      "subject": "API-Anbindung dokumentieren",
      "priority_id": 2,
      "description": "curl-Beispiele sammeln",
      "assigned_to_id": 7,
      "notes": "per API angelegt"
    }
  }' \
  "https://redmine.example.org/issues.json"
```

Erfolg: HTTP 201, Antwort enthält das vollständige Issue-Objekt.

### Anhang hochladen (Zwei-Schritt)

```bash
# 1. Datei hochladen -> Token
curl -s -X POST --data-binary "@bericht.pdf" \
  -H "X-Auth-Token: <apikey>" \
  "https://redmine.example.org/uploads.json?filename=bericht.pdf"

# 2. Token beim Issue-Anlegen mitgeben
curl -s -X POST -H "X-Auth-Token: <apikey>" \
  -H "Content-Type: application/json" \
  -d '{"issue":{"project_id":"kern","tracker_id":1,"subject":"Anhang",
       "uploads":[{"token":"<token>","filename":"bericht.pdf","content_type":"application/pdf"}]}}' \
  "https://redmine.example.org/issues.json"
```

## Rate Limits

- Redmine bringt **keine eingebaute Ratenbegrenzung** mit
- Drosselung über Webserver/Proxy (nginx `limit_req`, Apache `mod_ratelimit`) empfohlen
- Schwere Listenabfragen ohne `limit` bremsen die Instanz statt den Client - immer `limit`/`offset` nutzen

## Webhooks

- **Nicht im Kern**: ausgehende Webhooks nur als Plugin (z. B. „redmine_webhook"-artige Erweiterungen; Verfügbarkeit und Eventumfang versionsabhängig)
- **Eingehend**: Repositorium-Post-Receive-URL (`/repositories/{identifier}/fetch_changesets?key=...`) aktualisiert Changesets; Issue-Kommentare per E-Mail-Migration sind ebenfalls möglich (Setup-Aufwand)

## SDKs und Client-Bibliotheken

- **Python**: `redminelib` (verbreiteter Community-Client)
- **Ruby/PHP/JavaScript**: Community-Clients unterschiedlicher Pflege, ohne offizielle Bindung
- **Offiziell**: keine SDKs - REST mit `curl`, `requests` oder `httpx` ist der Standardweg
- **CLI-Alternative**: `rails runner`-Skripte auf dem Server für Massennebenläufiges (Administration, kein Public-API-Ersatz)

## Betriebshinweise

- API-Key rotieren, wenn Automationskonten kompromittiert wirken (Einstellungen im Benutzerkonto)
- `.xml`/`.json` ist Teil des Pfads - Content-Negotiation über `Accept` funktioniert nicht als Ersatz

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
