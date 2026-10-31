# Odoo - API Dokumentation

## Übersicht

Odoo-Instanzen sprechen standardmäßig **XML-RPC/JSON-RPC** gegen den ORM (`/XML-RPC/common`, `/jsonrpc`) — jedes Modell, jedes Feld ist damit erreichbar. Neuere Versionen ergänzen **REST-Module** (standardisierte REST-Endpunkte, je Version/Plan verfügbar — Stand prüfen) und Webhooks (Enterprise).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| XML-RPC/JSON-RPC (`execute_kw`) | Modell-CRUD, search/read/create/write/unlink | offiziell (Standard) |
| REST (`/api/…` via REST-Modul) | JSON-Endpunkte pro Modell/Endpoint | offiziell neu (Einzelfall prüfen) |
| Webhooks (ir.ql/Enterprise) | Datensatzänderungen → POST | offiziell (Enterprise-Features) |
| OAuth2/OIDC | API-Zugänge, Portal-Login | offiziell (neuere Versionen) |
| GraphQL | — | ❌ |

## Authentifizierung

- Session-basiert: `uid` + `password`/API-Key pro RPC-Aufruf (`database, uid, password, model, method, args`)
- API-Schlüssel für Nutzer (Einstellungen → Account), OAuth2 für neue REST-APIs

## Kernoperationen (RPC)

| Methode | Beschreibung |
|---------|--------------|
| `execute_kw(db, uid, pw, model, "search", [[domain]])` | IDs nach Filter |
| `…, "read", [[ids], [felder]]` | Datensätze lesen |
| `…, "create", [{felder}]` | anlegen |
| `…, "write", [[ids], {felder}]` | ändern |
| `…, "name_create" / "web_search_read"` | Komfortmethoden |
| Workflow-Methoden (`action_confirm`, `action_invoice_create`) | Zustandsübergänge |

## Beispiel

Request (JSON-RPC-Hülle gekürzt):

```json
{ "jsonrpc":"2.0", "method":"call", "params": {
  "service":"common","method":"authenticate","params":["demo","api_user","key"] }, "id":1 }
```

Datensatz:

```json
{ "service":"object","method":"execute_kw",
  "params":["demo", 2, "key", "res.partner", "create",
     [{"name":"Muster AG","email":"vertrieb@muster.de","phone":"+49 30 1234"}]] }
```

Response: `1234` (Datensatz-ID).

## Webhooks (Enterprise)

Einstellungen → Webhooks: Ereignis (create/update) + Secret; HMAC-signierte JSON-Payloads an Callback-URL.

## Rate Limits

keine eingebauten Limits (Instanz-/Worker-Grenzen); JSON-RPC über Reverse-Proxy drosseln.

## SDKs und Client-Bibliotheken

- `xmlrpc.client` (Stdlib), **`odoo` Python-Lib** / `odoorpc`, JS-RPC im Web-Framework
- `odoo-bin shell` für ORM-Interaktion von der Konsole

## Skin-Hinweis

Modell-/Feldkatalog per RPC (`ir.model.fields`) = perfekte Quelle für automatisches Mapping ([felder.md](../../../../data/felder.md)).
