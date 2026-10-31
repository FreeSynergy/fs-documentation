# Request Tracker - API Dokumentation

## Übersicht

RT hat zwei offizielle APIs: die klassische **REST 1.0** (show/create/edit/correspond, text/plain + XML/JSON) und die modernere **JSON-RPC 2.0** (`/REST/2.0`). Zusätzlich existiert das vollmächtige CLI `rt`.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST 1.0 (`/REST/1.0/...`) | show/create/edit/correspond/comment | offiziell |
| REST 2.0 JSON-RPC (`/REST/2.0`) | strukturierte Objekte, bulk | offiziell (seit RT 4.4) |
| CLI `rt` | alles, auch Cron-Automation | offiziell |
| Webhooks | — | ❌ (Extensions/Trigger statt Webhooks) |

## Authentifizierung

- **Basic-Auth** oder `user=…&pass=…` (REST 1.0)
- **REST 2.0**: HTTP-Header `X-Rest-Protocol: JSON`, Basic oder Session-Cookie
- API-User mit reduziertem Rights-Set anlegen (Best-Practice)

## REST 1.0

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/REST/1.0/show/ticket/4711` | Ticket als Textobjekt |
| `GET` | `/REST/1.0/search/tickets?query=…` | Query-Ergebnis |
| `POST` | `/REST/1.0/new/ticket` | anlegen (Form: `Queue`, `Requestor`, `Subject`, `Text`) |
| `POST` | `/REST/1.0/edit/ticket/4711` | Felder ändern |
| `POST` | `/REST/1.0/comment/ticket/4711` | interne Notiz |
| `POST` | `/REST/1.0/correspond/ticket/4711` | Antwort an Kunden |

`?format=xml`/`out=json` optional.

## REST 2.0 (JSON-RPC)

```json
{
  "jsonrpc": "2.0",
  "method": "edit",
  "params": {
    "type": "ticket",
    "objects": ["4711"],
    "data": { "Status": "resolved" }
  },
  "id": 3
}
```

Response:

```json
{
  "jsonrpc": "2.0",
  "result": { "action": "set", "tickets": [{ "id": "4711", "Status": "resolved", "LastUpdated": "2026-10-31T14:00:00Z" }] },
  "id": 3
}
```

Wichtige Methoden: `create`, `edit`, `show`, `lookup`, `search`, `correspond`, `comment`, `user_tickets`, `tickets_who_have_queue`.

## Beispiel (curl, REST 2.0)

```bash
curl -u svc-bot:secret -H 'X-Rest-Protocol: JSON' -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"search","params":{"type":"ticket","queue":"hw","query":"Status = new"},"id":1}' \
  https://rt.example.org/REST/2.0
```

## Rate Limits

Keine eingebauten; Best-Practices: eigene API-User, Proxy-Limits, Transaktionsflut über Scrips vermeiden.

## SDKs und Client-Bibliotheken

- Perl-API (`RT->API`) als Referenz im Kern
- Community: Python `rtrest`, Node `rt-client`; REST 2.0 ist für jede Sprache trivial

## Skin-Hinweis

Transaktionsmodell (Ticket = Kopf, Transactions = Events) ist Vorbild für das [Comment-/Event-Modell](../../../../data/modelle.md).
