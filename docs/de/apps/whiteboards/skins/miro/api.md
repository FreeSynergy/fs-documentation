# Miro - API Dokumentation

## Übersicht

Miro REST-API (`https://api.miro.com/v2/…`, JSON) mit OAuth2. Boards, Items (Sticky/Shapes/Frameworks), Frames, Karten, Mitglieder. Webhooks für Board-/Item-Änderungen. App-Kit für eigene Miro-Apps.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v2 Boards/Items | CRUD, Suche (`/boards/{id}/items`) | offiziell |
| Webhooks | `board.item.created/updated/deleted`, `board.member.*` | offiziell |
| App-Kit SDK (JS) | eigene Apps im Canvas | offiziell |
| GraphQL | Betas einzelner Produkte | ❌ allgemein |

## Authentifizierung

- OAuth2 **Authorization Code** (user) oder **Client Credentials** (Enterprise/M2M)
- Header `Authorization: Bearer <token>`; Scope z.B. `boards:read boards:write`

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v2/boards` | Boards auflisten |
| `POST` | `/v2/boards` | Board anlegen |
| `GET` | `/v2/boards/{id}/items` | Items (Filter `type=sticky_note`) |
| `POST` | `/v2/boards/{id}/stickies` | Sticky anlegen |
| `POST` | `/v2/boards/{id}/frames` | Frame anlegen |
| `PATCH` | `/v2/boards/{id}/items/{itemId}` | ändern (Inhalt, Position) |
| `DELETE` | `/v2/boards/{id}/items/{itemId}` | löschen |
| `GET` | `/v2/boards/{id}/members` | Teilnehmer |
| `POST` | `/v2/webhooks` | Webhook abonnieren |

## Beispiel

Request:

```http
POST /v2/boards/<board_id>/stickies HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "data": { "content": "Idee: Skin-Markt starten", "parent": null },
  "geometry": { "x": 120, "y": 340, "width": 220, "height": 220 },
  "style": { "fillColor": "#FFF2A8" } }
```

Response: `201` mit Item (`id`, `type:"sticky_note"`, `data`, `geometry`, `style`).

## Webhooks

`POST /v2/webhooks` mit `type:"board.item.updated"`, `board_id`, `callback_url`; Signatur-Header zur Verifikation; Retry-Mechanik vorhanden.

## Rate Limits

**~50 Requests/Sekunde pro Board; 1.000/min pro Nutzer** (Doku-Richtwerte; 429 + Retry-After).

## SDKs und Client-Bibliotheken

- App-Kit SDK (JS/TS) offiziell; REST-Beispiele in der Doku
- Zapier/Make-Konnektoren vorhanden

## Skin-Hinweis

Sticky/Frame/Connector entsprechen den Whiteboard-Bausteinen der Component-Doku; Item-JSON → [modelle.md](../../../../data/modelle.md) (Shape-Records analog tldraw).
