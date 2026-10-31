# GLPI - API Dokumentation

## Übersicht

GLPI bietet eine offizielle **REST-API** (`/apirest.php`) mit Session-basierter Authentifizierung: init → Session-Token → CRUD- Aufrufe. Sie deckt praktisch alle Objekttypen generisch ab (`Ticket`, `Computer`, `User`, …).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/apirest.php` | CRUD + Suche für alle Kernobjekte | offiziell |
| XML-RPC (alt) | Legacy-Integration | veraltet |
| Plugin-APIs | z.B. Webhooks, Inventory | pluginabhängig |
| GraphQL | — | ❌ |

## Authentifizierung

1. `POST /apirest.php/initSession` mit Header `Session-Token: leer` und Credentials
   - `Authorization: Basic …` oder `Login+Password`
   - oder API-Token (`App-Token`) + user/key für service accounts
2. Antwort liefert `session_token`; alle Folgerequests mit Header `Session-Token: <t>`
3. `killSession` zum Beenden

## Endpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/salut.php` | Health-Check |
| `POST` | `/apirest.php/initSession` | Session starten |
| `POST` | `/apirest.php/{Objekt}` | anlegen (`input={…}`) |
| `GET` | `/apirest.php/{Objekt}/{id}` | lesen |
| `GET` | `/apirest.php/{Objekt}` (mit `range`, `order`) | Liste |
| `POST` | `/apirest.php/{Objekt}/{id}` | ändern (`input={…}`) |
| `DELETE` | `/apirest.php/{Objekt}/{id}` | löschen |
| `GET` | `/apirest.php/{Objekt}/search?criteria=[…]` | Suche mit Filterkriterien |
| `GET` | `/apirest.php/Ticket/{id}/getFollowups` | Subobjekte (Followups, Tasks, Documents) |
| `POST` | `/apirest.php/Entity/{id}/changeActiveEntity` | Mandant/Mandant wechseln |

## Beispiel

Request:

```http
POST /apirest.php/HTTP/1.1
Host: glpi.example.org
Session-Token: abc123
Content-Type: application/json

{ "input": {
    "name": "VPN bricht ab",
    "content": "seit 08:40 mehrfach",
    "categories_id": 12,
    "entities_id": 0,
    "users_id_recipient": 5 } }
```

Response:

```json
{ "id": 9982 }
```

## Rate Limits

Keine eingebauten; Session-Timeout (Standard 30 min) und `App-Token`-Rotation adminseitig.

## SDKs und Client-Bibliotheken

- **offiziell**: PHP-Bibliotheken (glpi-project); REST mit jedem HTTP-Client
- **Community**: Python-Wrapper (`pyglpi`), Node-Beispiele
- **CLI**: `glpi:crm:*`-Konsolenbefehle für Wartung

## Skin-Hinweis

Ticket↔Asset-Verknüpfung ist das GLPI-Besondere — FreeSynergy-Skins mappen es auf Relationen im [Modell-Set](../../../../data/modelle.md) (`ticket.related = [file, device]`).
