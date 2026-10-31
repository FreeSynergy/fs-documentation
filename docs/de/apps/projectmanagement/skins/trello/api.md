# Trello - API Dokumentation

## Übersicht

REST-API unter `https://api.trello.com/1/…` (JSON). Klassische Authentifizierung per `key`+`token` Query-Parameter; moderner OAuth2 für Power-Ups. Webhooks hängen an Objekten (Board/List/Card).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v1 | Boards, Lists, Cards, Actions, Members | offiziell |
| Webhooks (`/1/webhooks`) | Objektänderungen als POST | offiziell |
| REST 2-API (`api.trello.com/2`) | neue Endpunkte (Teams/Board-Felder) | offiziell (im Wachstum) |
| GraphQL | — | ❌ |

## Authentifizierung

- `?key=<app-key>&token=<member-token>` (persönlicher Token in den Konto-Einstellungen)
- OAuth2 (Power-Ups): `Authorization: OAuth oauth_token=…`
- Scoped Tokens für Power-Ups (nur eigene Rechte)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/1/boards/{id}/lists` | Listen eines Boards |
| `POST` | `/1/boards/{id}/lists` | Liste anlegen |
| `GET` | `/1/lists/{id}/cards` | Karten einer Liste |
| `POST` | `/1/cards` | Karte anlegen (`idList`, `name`, `due`, `desc`, `idMembers`, `labels`) |
| `PUT` | `/1/cards/{id}` | ändern (Position, Liste…) |
| `POST` | `/1/cards/{id}/actions/comments` | Kommentar |
| `GET` | `/1/boards/{id}/actions` | Aktivitäten-Feed |
| `POST` | `/1/webhooks` | Webhook auf Board/Card registrieren |

## Beispiel

Request:

```http
POST /1/cards?idList=62f…&key=KEY&token=TOKEN HTTP/1.1
Content-Type: application/json

{ "name": "Beitrag skizzieren", "desc": "Gliederung im Wiki",
  "due": "2026-11-04T17:00:00.000Z", "idMembers": ["5f…"] }
```

Response: `200` mit Kartenobjekt (`id`, `pos`, `due`, `dateLastEdit`).

## Webhooks

```json
{ "action": { "type": "createCard", "date": "…",
    "data": { "list": {"id": "62f…"}, "card": {"id": "…", "name": "…"} },
    "memberCreator": { "id": "…" } } }
```

Callback mit Retry; Modell „action-Events“ (auch `commentCard`, `updateCard`).

## Rate Limits

**~100 Requests/10 s pro Key und Member; 100/s pro Token**, plus Board-Actions-Limits — 429 mit `Retry-After`.

## SDKs und Client-Bibliotheken

- Community-SDKs: Python (`py-trello`), Node (`node-trello`), PHP; offizielle Referenz = API-Doku + Postman
- Power-Up-Framework: eigenes JS-SDK für In-Trello-Apps

## Skin-Hinweis

Board/List/Card/pos/labels sind das Referenz-Vokabular für Kanban-Skins ([modelle.md](../../../../data/modelle.md)); `pos`-Float entspricht der Sortierlogik in [felder.md](../../../../data/felder.md).
