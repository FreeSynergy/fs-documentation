# Planka - API Dokumentation

## Übersicht

Planka (Node.js + React, Sequelize) hat eine stabile interne **REST-API**, die das Frontend selbst nutzt — sie ist damit der dokumentierbare Schnitt für Skin-Integrationen. Echtzeitänderungen laufen über einen **Socket.io**-Kanal.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/all`, `/api/...` | Vollzugriff auf Projekte, Boards, Listen, Karten, Nutzer | offiziell-intern, stabil |
| Socket.io (`/socket.io`) | Live-Updates (Karte bewegt, Kommentar) | offiziell-intern |
| Webhooks | — | ❌ Nicht vorhanden |
| GraphQL | — | ❌ Nicht vorhanden |

## Authentifizierung

- **Session-Cookie** (`sess`) nach Login; HTTP-only
- Alternative: **Bearer-Token** (API-Token pro Nutzer unter Konto →-API)
- Login: `POST /api/accessTokens` mit E-Mail/Passwort; 2FA optional (TOTP)

## Wichtigste Endpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/all` | gesamter Zustand (Projekte, Boards, Listen, Karten, Nutzer) in einem Rutsch |
| `POST` | `/api/accessTokens` | Login, setzt Cookie |
| `POST` | `/api/projects` | Projekt anlegen |
| `PATCH` | `/api/projects/{id}` | Projekt ändern |
| `DELETE` | `/api/projects/{id}` | Projekt löschen |
| `POST` | `/api/boards/{boardId}/lists` | Liste/Spalte anlegen |
| `POST` | `/api/lists/{listId}/cards` | Karte anlegen |
| `PATCH` | `/api/cards/{id}` | Karte ändern (Titel, Beschreibung, Fälligkeit, ListId) |
| `DELETE` | `/api/cards/{id}` | Karte löschen |
| `POST` | `/api/cards/{id}/comments` | Kommentar |
| `POST` | `/api/cards/{id}/checklistItems` | Unteraufgabe |
| `POST` | `/api/projects/{projectId}/users` | Mitglied hinzufügen |

## Beispiel

Request:

```http
POST /api/lists/42/cards HTTP/1.1
Authorization: Bearer <api-token>
Content-Type: application/json

{
  "name": "Skin-API mappen",
  "description": "Felder auf data/modelle.md",
  "dueDate": "2026-11-05T10:00:00.000Z",
  "labelIds": ["640f..."],
  "memberIds": ["641a..."]
}
```

Response: `201 Created` mit Kartenobjekt (`id`, `createdBy`, `listId`, `type: "tasks"`, `position`).

## Socket.io-Events (Auszug)

| Event | Richtung | Beschreibung |
|-------|----------|--------------|
| `card create/update/delete` | Server → Client | Live-Boardänderungen |
| `card move` | beidseitig | Position/Liste geändert |
| `comment create` | Server → Client | neuer Kommentar |

## Rate Limits

Eingebaute Limits: ❌ (nur Node-Standard); für Production Proxy-Limits empfohlen.

## SDKs und Client-Bibliotheken

- Offizielle SDKs: ❌
- Community: REST mit jedem HTTP-Client; `fetch`-Beispiele im Planka-Frontend-Quellcode (maßgebliche Referenz)

## Skin-Hinweis

Planka-Kartenmappern auf das Task-Modell ([modelle.md](../../../../data/modelle.md)); `position`-Feld entspricht der Listen-Sortierlogik ([felder.md](../../../../data/felder.md)).
