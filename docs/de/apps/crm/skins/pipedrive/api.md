# Pipedrive - API Dokumentation

## Übersicht

Pipedrive bietet eine **REST-API v1** mit JSON als Austauschformat. Sie ist die offizielle Schnittstelle für Integrationen und gut dokumentiert unter `developers.pipedrive.com`. Authentifiziert wird mit einem persönlichen API-Token oder über OAuth2. Ereignisse können per **Webhooks** nach außen gemeldet werden.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v1 (`https://api.pipedrive.com/v1/`) | Leads, Personen, Firmen, Deals, Aktivitäten, Produkte, Felder, Berichte-Hilfsdaten | Offiziell dokumentiert |
| OAuth2 (`https://oauth.pipedrive.com/`) | App-Zugriff im Namen eines Nutzers | Offiziell dokumentiert |
| Webhooks (`/v1/webhooks`) | Ereignisse an eigene Endpunkte senden | Offiziell dokumentiert |
| GraphQL | ❌ Nicht vorhanden | — |
| CalDAV / CardDAV | ❌ Nicht vorhanden | — |
| XML-RPC | ❌ Nicht vorhanden | — |

## Authentifizierung

- **Persönlicher API-Token**: im Avatar-Menü → Persönliche Einstellungen → "Personal access tokens" erzeugen. Übergabe wahlweise als Query-Parameter `api_token=...` oder als `Authorization: Bearer <token>` (Header-Variante versionsabhängig, in der API-Doku nachsehen).
- **OAuth2**: App im Pipedrive-Marketplace oder als interne App registrieren.
  - Autorisierung: `https://oauth.pipedrive.com/oauth/authorize`
  - Tausch des Codes: `POST https://oauth.pipedrive.com/oauth/token`
  - Refresh: erneuter Aufruf des Token-Endpunkts mit `refresh_token`
  - Scopes begrenzen den Zugriff (etwa `api:currentuser:read`, `files`, `activityTypes`; vollständige Liste in der API-Doku)

## Endpunkte

### Basis

```
https://api.pipedrive.com/v1/<ressource>
```

Lesende Aufrufe als `GET` mit Parametern (`start`, `limit`), schreibende als `POST`/`PUT` mit JSON-Body, Löschen als `DELETE`.

### Leads und Kontakte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v1/leads` | Leads auflisten (Filter, Paginierung) |
| `POST` | `/v1/leads` | Lead anlegen |
| `PUT` | `/v1/leads/{id}` | Lead ändern |
| `DELETE` | `/v1/leads/{id}` | Lead löschen |
| `GET` | `/v1/persons` | Kontakte auflisten |
| `POST` | `/v1/persons` | Kontakt anlegen |
| `PUT` | `/v1/persons/{id}` | Kontakt ändern |
| `DELETE` | `/v1/persons/{id}` | Kontakt löschen |

### Firmen und Deals

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v1/organizations` | Firmen auflisten |
| `POST` | `/v1/organizations` | Firma anlegen |
| `GET` | `/v1/deals` | Deals auflisten (nach Pipeline und Stage filterbar) |
| `POST` | `/v1/deals` | Deal anlegen |
| `PUT` | `/v1/deals/{id}` | Deal ändern (Stage, Betrag, Abschlussdatum) |
| `DELETE` | `/v1/deals/{id}` | Deal löschen |
| `GET` | `/v1/deals/{id}/products` | Produktzeilen eines Deals |
| `POST` | `/v1/deals/{id}/products` | Produktzeile zum Deal hinzufügen |
| `GET` | `/v1/dealFields` | Felddefinitionen der Deals |
| `GET` | `/v1/pipelines` | Pipelines auflisten |
| `GET` | `/v1/pipelines/{id}/stages` | Stages einer Pipeline |

### Aktivitäten und Kommunikation

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v1/activities` | Aktivitäten auflisten (Typ, Zeitraum, Bearbeiter) |
| `POST` | `/v1/activities` | Aktivität anlegen (Task, Call, Meeting) |
| `PUT` | `/v1/activities/{id}` | Aktivität ändern, etwa auf erledigt setzen |
| `GET` | `/v1/activities/{id}/participants` | Beteiligte Kontakte einer Aktivität |
| `POST` | `/v1/files` | Datei hochladen (multipart) und Objekt zuordnen |

### Suche, Massenverarbeitung, Webhooks

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v1/searchResults` | Objekte übergreifend suchen (Suchbegriff, Objekttyp) |
| `POST` | `/v1/deals/bulk` | Mehrere Deals in einem Aufruf anlegen |
| `PUT` | `/v1/{objekt}/bulk` | Mehrere Datensätze gleichzeitig ändern |
| `DELETE` | `/v1/{objekt}/bulk?ids=...` | Mehrere Datensätze löschen |
| `GET` | `/v1/webhooks` | eingerichtete Webhooks auflisten |
| `POST` | `/v1/webhooks` | Webhook anlegen (`subscriber_url`, `model`, `subscription`) |
| `DELETE` | `/v1/webhooks/{id}` | Webhook löschen |


## Beispiele

### Deal anlegen (curl mit persönlichem Token)

```bash
curl -s -X POST "https://api.pipedrive.com/v1/deals?api_token=PERSOENLICHER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Website-Relaunch Meyer AG",
    "value": "24000",
    "currency": "EUR",
    "pipeline": 1,
    "stage": 3,
    "expected_close": "2026-12-15"
  }'
```

Antwort (gekürzt):

```json
{
  "success": true,
  "data": {
    "id": 148,
    "title": "Website-Relaunch Meyer AG",
    "value": "24000",
    "stage_id": 3,
    "status": "open",
    "add_time": "2026-10-31 12:00:00"
  }
}
```

### Deals gefiltert laden (curl)

```bash
curl -s "https://api.pipedrive.com/v1/deals?api_token=PERSOENLICHER_TOKEN&limit=50&status=open"
```

### Aktivität nachziehen (Python)

```python
import requests

BASE = "https://api.pipedrive.com/v1"
TOKEN = "PERSOENLICHER_TOKEN"

r = requests.get(f"{BASE}/activities", params={
    "api_token": TOKEN, "type": "task", "done": "0", "limit": 50,
})
for a in r.json()["data"]:
    print(a["id"], a["subject"], a["due_date"], a["person_name"])
```

### Webhook einrichten (curl)

```bash
curl -s -X POST "https://api.pipedrive.com/v1/webhooks?api_token=PERSOENLICHER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "subscriber_url": "https://example.com/pipedrive/webhook",
    "model": "deal",
    "subscription": {
      "deal.add": true,
      "deal.update": true,
      "deal.delete": true
    }
  }'
```

## Rate Limits

- Laut API-Doku gilt eine Begrenzung von **100 API-Anfragen pro Minute pro Firma** (rollierendes Fenster).
- Bei Überschreitung antwortet die API mit **HTTP 429**; Request danach mit Abstand wiederholen (Backoff).
- **Batch-Limit**: Massenaufrufe verarbeiten maximal 50 Ressourcen pro Anfrage; größere Mengen in Stapel aufteilen.
- Raten können sich je Plan und Release ändern — vor Produktivnutzung in der offiziellen API-Doku nachsehen.

## Webhooks

- **Modelle**: `deal`, `person`, `organization`, `activity`, `note`, `product` (Verfügbarkeit versionsabhängig).
- **Ereignisse** je Modell: `add`, `update`, `delete`, zusätzlich `deleted_permanently` und `duplicate_restore` beim Deal.
- **Payload**: JSON mit Modell, Objekt (`subject`), abonniertem Ereignis, `company_id` und `user_id`.
- **Zustellung**: einmal pro Ereignis; eigene Endpunkte sollten Idempotenz über die Objekt-ID sichern.

## SDKs und Client-Bibliotheken

- **Offiziell**: `pipedrive-api` für Node.js/JavaScript (deckt die REST-Endpunkte typisiert ab).
- **Inoffiziell**: Community-Clients für Python, PHP und andere Sprachen; Abdeckung und Pflege vor Einsatz prüfen.

## Hinweise für den Betrieb

- Persönliche Token an ein Dienstkonto mit minimalen Rechten binden und regelmäßig erneuern.
- HTTPS ausschließlich; Token nicht in Logs oder Client-seitigem Code ablegen.
- Eigene Felder haben interne Namen (oft mit Präfix); diese über `dealFields`, `personFields` und `orgFields` ermitteln, nicht raten.

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
