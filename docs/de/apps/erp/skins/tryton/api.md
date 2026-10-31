# Tryton - API Dokumentation

## Übersicht

Tryton-Server sprechen **XML-RPC oder JSON-RPC** unter `/rpc` (auch `/jsonrpc`). Muster: `common.login` → Session-ID; danach Modell-Methoden als RPC-Funktionsnamen `Model.<name>.execute_kw`. Feld-/Modell-Metadaten sind selbst RPC-objekte — Schema auslesbar.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| RPC `Model.x.read/create/write/unlink` | CRUD (execute/execute_kw) | offiziell (Kern) |
| `common.login`/`common.session_login` | Authentifizierung | offiziell |
| `ir.model*`-Modelle | Feldkatalog/Metadaten | offiziell |
| Webhooks | nicht eingebaut | ❌ |
| GraphQL | — | ❌ |

## Authentifizierung

```
common.login(database="firma", user="sync", password="…", context={})
→ { "session": "2c7d…", "user_id": 3 }
```

Jeder Modellaufruf trägt `session` + `context` (language, company IDs).

## Kernmethoden

| Methode (RPC-Name) | Beschreibung |
|--------------------|--------------|
| `Model.account.move.execute` | `read`/`create`/`write`-Wrapper via execute_kw |
| `Model.party.find_and_count(domain)` | Suche |
| `Model.sale.sale.action_confirm([ids])` | Workflow-Aktionen |
| `Model.ir.model_fields.read(...)` | Feldkatalog fürs Mapping |
| `common.set_metadata` / `common.message` | Client-Handling |

## Beispiel (JSON-RPC)

Request:

```json
{ "method": "call", "params": {
  "id": 1, "method": "Model.party.execute_kw",
  "args": ["2c7d…", {"language":"de_DE","tz":"Europe/Berlin"},
           [], "search_read", [[["name","like","%Muster%"]],
           ["name","email"]], {"limit": 20}] } }
```

Response: `result: [{ "id": 41, "name": "Muster AG", "email": "vertrieb@muster.de" }]`

## Workflow-Aktionen

`Model.sale.sale.action_confirm` / `action_process` — Zustandsübergänge explizit (state-Felder), genau wie im Client.

## Rate Limits

keine eingebauten; Server-/Proxy-Limits.

## SDKs und Client-Bibliotheken

- **offiziell**: `trytond`-Bibliothek (Client-Code nutzt dieselben Klassen), `proteus` (ORM-artiger Python-Client)
- JSON-RPC-Rezepte in Tryton-Wiki

## Skin-Hinweis

`context` ( Sprache/Firma/TZ) in Sync-Skins immer explizit setzen — häufigste Fehlerquelle; Metadaten via `ir.model.fields` → [felder.md](../../../../data/felder.md).
