# Wekan - API Dokumentation

## Übersicht

REST-API mit **persönlichem Token** (Profil → Application Programming Interface). Endpunkte für Boards, Listen, Karten, Kommentare; zusätzlich **Invoke-Webhooks** (eingehende Hooks als Karten-Eingang) und **ausgehende Webhooks**.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/…` (JSON) | Boards/Listen/Karten CRUD | offiziell (dünn dokumentiert) |
| Invoke-Webhooks | POST von außen → Karte/Kommentar/Status | offiziell |
| Outgoing Webhooks | Board-Aktivität → HTTP-POST | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- Persönlicher Token: `Authorization: Bearer <token>` oder `?token=<token>`
- Token im Nutzerprofil erzeugbar (Scope: Konto des Erstellers)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/boards.json` | Boards des Tokens |
| `POST` | `/api/createBoard` | Board anlegen (`{"board":{title},"orgId":…}`) |
| `GET` | `/api/boards/{boardId}/lists` | Listen inkl. Swimlane-Referenz |
| `POST` | `/api/boards/{boardId}/lists/new` | Liste anlegen |
| `POST` | `/api/boards/{boardId}/lists/{listId}/cards/new` | Karte anlegen |
| `POST` | `/api/cards/{cardId}/comments/new` | Kommentar |
| `POST` | `/api/boards/{boardId}/lists/{listId}/cards/{cardId}/move` | Karte verschieben |
| `POST` | `/api/boards/{boardId}/archive` | Board archivieren |

## Beispiel

Request:

```http
POST /api/boards/abcd1234/lists/ef5678/cards/new HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "title": "Alert: Disk 91%", "description": "node-3 /var",
  "labelIds": ["red"], "customFields": { "host": "node-3" } }
```

Response: `200` → `{ "_id": "…", "title": "Alert: Disk 91%", "listId": "ef5678" }`

## Invoke-Webhooks (eingehend)

Board → Integrationen → „Invoke webhook“ anlegen; URL aufrufen:

```bash
curl -X POST "https://wekan.example.org/invite/hooks/<hook-id>?token=<token>" \
  -d "title=Neue Bestellung&comment=aus Shop-System"
```

## Webhooks (ausgehend)

JSON pro Ereignis (`activityType`: movedCard, addedCard, commented …) mit Board-/List-/Card-IDs; Secret-Header konfigurierbar.

## Rate Limits

Keine eingebauten; Instanz-Limits über Proxy.

## SDKs und Client-Bibliotheken

- keine offiziellen SDKs; curl/requests-Rezepte in Doku/Community
- Import-Skripte (Trello) als API-Referenz im Quellcode

## Skin-Hinweis

Swimlane-Ebene ergänzt das [Board-Modell](../../../../data/modelle.md) (Board → Swimlane → List → Card).
