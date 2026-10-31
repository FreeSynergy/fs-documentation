# osTicket - API Dokumentation

## Übersicht

osTicket v1 hat eine schlanke **REST-API** (JSON, auch XML) mit API-Key. Sie deckt Tickets und Benutzerprofile; tieferes Customizing läuft über die Datenbank direkt (nicht unterstützt).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `/api/v1/tickets.json` … | Tickets erstellen/lesen, Anhängen, Zuweisen | offiziell |
| E-Mail-Ingest (Subjekt-Header) | Ticket-/Threadsteuerung per Mail | offiziell |
| XML-Variante `.xml` | alternativ | offiziell |
| Webhooks | — | ❌ |

## Authentifizierung

- **API-Key** aus Admin → API Settings, Header `X-API-Key: <key>` oder Query `api=`
- alternativ Ticket-„user key“ (Link-Token) für read-only-Ticketzugriff

## Endpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/v1/tickets.json` | Ticket erstellen |
| `GET` | `/api/v1/tickets.json?ticket=#4711&key=…` | Ticket lesen (mit user-key oder Key+Q) |
| `POST` | `/api/v1/tickets/answer.json` | Antwort anhängen |
| `POST` | `/api/v1/tickets/note.json` | interne Notiz |
| `POST` | `/api/v1/tickets/claim.json` | zuweisen |
| `POST` | `/api/v1/tickets/close.json` | schließen |
| `POST` | `/api/v1/users.json` | Kundenprofil erstellen/aktualisieren |
| `GET` | `/api/v1/users.json?q=b@example.org` | Profil suchen |

## Beispiel

Request:

```http
POST /api/v1/tickets.json HTTP/1.1
X-API-Key: <api-key>
Content-Type: multipart/form-data; charset=utf-8

name=Ben Klein&email=b@example.org&subject=Drucker offline&topic=hardware&message=Seit 9 Uhr...
```

Response:

```json
{ "data": { "number": "XRT-4712", "status": "open", "url": "https://help.example.org/?a=tickets&t=XRT-4712&key=..." } }
```

## E-Mail-Steuerung

Im Betreff: Antwort auf Ticketreferenz `Re: [#XRT-4712 …]` erhält den Thread; `#topic-slug`, `#status-open`, `#pri-high` setzen Felder beim Ingest.

## Rate Limits

Keine eingebauten; über Webserver/Anti-Spam (Flood-Schwellen in den Ticket-Einstellungen) begrenzen.

## SDKs und Client-Bibliotheken

- offizielle SDKs: ❌ (curl/`requests`-Rezepte in der API-Doku)
- CLI: eigene Skripte gegen API; Import-Wizard für Alt-Tickets (CSV)

## Skin-Hinweis

Statusmodell new/open/pending/closed → Standard-Ticket-Statusliste ([modelle.md](../../../../data/modelle.md)); API-Feldnamen entsprechen [felder.md](../../../../data/felder.md).
