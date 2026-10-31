# OPNsense - API Dokumentation

## Übersicht

OPNsense ist API-first gebaut: Die Web-UI ist nur ein MVC-Client, dieselben Controller dienen der REST-API. Aufrufe folgen dem Muster

```
https://<host>/api/<modul>/<controller>/<command>/[<param1>/[<param2>…]]
```

mit zwei Verben: `GET` liest, `POST` schreibt oder führt Aktionen aus (JSON-Body/-Antwort). Offizielle Referenz: Entwickler-Doku `docs.opnsense.org/development/api.html` (Core- und Plugin-APIs). Da ~99 % der Endpunkte von der UI selbst genutzt werden, ist der Netzwerk-Tab des Browsers (Filter `/api/`) die präziseste Doku der eigenen Installation.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| MVC-REST `/api/<modul>/<controller>/<command>` | Konfiguration und Aktionen | Offiziell, automatisch für UI-Module |
| Business-Edition-API (`OPNBECore`) | Support-/Update-Automation | Nur Business Edition |
| Webhooks | — | ❌ Nicht vorhanden |

## Authentifizierung

- **API-Key + Secret**: wird **pro Benutzer** erzeugt unter **System ▸ Access ▸ Users** (Benutzer bearbeiten → API-Schlüssel generieren, `apikey.txt`-Download möglich).
- **Transport**: HTTP **Basic Auth** — `key` als Benutzername, `secret` als Passwort:

```bash
key='w86XNZob/8Oq8aC5r0kbNarNtdpoQU…'
secret='XeD26XVrJ5ilAc/EmglCRC+0j2…'
curl -k -u "$key:$secret" "https://opnsense.local/api/core/service/search" \
  -X POST -H 'Content-Type: application/json' \
  -d '{"current":1,"rowCount":7,"sort":{},"searchPhrase":""}'
```

- **ACLs**: Der Key erbt die Gruppen-/Ressourcenrechte des Benutzers; „Effective Privileges“ zeigen, welche Endpunkte erlaubt sind (Ressourcen entsprechen den UI-Seiten).
- **Getrennter API-Benutzer** mit Minimalrechten ist Best Practice; GUI-Sessions (Cookies) sind für Skripte unüblich.

## Benennung

Die Referenz listet Kommandos teils snake_case (`add_rule`), die UI-Beispiele camelCase (`addRule`). In der Praxis akzeptiert der Router beide Formen weitgehend; sicherer ist die Schreibweise aus dem Netzwerk-Trace der eigenen Version.

## Endpunkte (Beispiele, Modul `firewall`)

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/firewall/filter/searchRule?current=1&rowCount=25&searchPhrase=` | Regelgrid durchsuchen |
| `POST` | `/api/firewall/filter/addRule` | Regel anlegen (Body `{"rule": {…}}`) |
| `GET` | `/api/firewall/filter/getRule/<uuid>` | Einzelregel lesen |
| `POST` | `/api/firewall/filter/setRule/<uuid>` | Regel setzen |
| `POST` | `/api/firewall/filter/toggleRule/<uuid>/<0|1>` | Regel aktivieren/deaktivieren |
| `POST` | `/api/firewall/filter/delRule/<uuid>` | Regel löschen |
| `POST` | `/api/firewall/filter/apply` | Regelwerk aktivieren |
| `GET` | `/api/firewall/filter_util/rule_stats` | Regelstatistiken |
| `GET,POST` | `/api/firewall/alias/search_item` | Aliases durchsuchen |
| `GET` | `/api/firewall/alias/get_item/<uuid>` | Alias lesen |
| `POST` | `/api/firewall/alias/add_item` | Alias anlegen |
| `POST` | `/api/firewall/alias/set_item/<uuid>` | Alias setzen |
| `POST` | `/api/firewall/alias/del_item/<uuid…>` | Alias löschen |
| `POST` | `/api/firewall/alias/reconfigure` | Alias-Tabellen neu laden |
| `POST` | `/api/firewall/d_nat/searchRule` | Port-Forward-Regeln durchsuchen |
| `POST` | `/api/firewall/source_nat/addRule` | Outbound-Regel anlegen |
| `POST` | `/api/core/service/search` | Dienste durchsuchen (System ▸ Diagnostics ▸ Services) |

Weitere Module: `core` (interfaces, firmware, settings …), `certificates`, `routes`, plus Plugins (`wireguard`, `acmeclient`, `ids` …) — je Plugin eigene Controller mit demselben Muster.

## Request/Response-Grundlagen

- **Basis**: `https://<host>/api/…` — gleicher Port wie die Web-UI (Standard 443, HTTP→HTTPS).
- **Inhalt**: `Content-Type: application/json` für `POST`; einige Export-Kommandos (download/upload) arbeiten mit Datei-Antworten.
- **Parameter**: UUIDs als Pfadsegment (`/getRule/<uuid>`), optionale Flags ebenfalls als Segmente (`/toggleRule/<uuid>/0`).
- **Fehler**: Validierungs- und ACL-Fehler kommen als JSON-Meldung mit Text; Statuscodes sind nicht immer trennscharf — auf Meldeinhalt prüfen.
- **Zwei-Stufen-Modell**: schreiben → `apply`/`reconfigure`; ohne Aktivierungsschritt bleibt die Änderung inaktiv.

## Antworten der Grid-Endpunkte

Such-Endpunkte nutzen einheitliche Parameter (`current`, `rowCount`, `sort`, `searchPhrase`) und liefern:

```json
{
  "total": 10,
  "rowCount": 7,
  "current": 1,
  "rows": [
    { "id": "configd", "locked": 1, "running": 1,
      "description": "System Configuration Daemon", "name": "configd" }
  ]
}
```

## Beispiele

### Regel suchen und bei Bedarf anlegen (offizielles Muster)

```python
import requests, json
uri = "https://192.168.1.1"
auth = (api_key, api_secret)

r = requests.get(f"{uri}/api/firewall/filter/searchRule"
                 "?current=1&rowCount=7&searchPhrase=testrule_1",
                 auth=auth, verify=False)
rows = json.loads(r.text)["rows"]
if not rows:
    data = {"rule": {"description": "testrule_1",
                     "source_net": "192.168.0.0/24",
                     "protocol": "TCP",
                     "destination_net": "10.0.0.0/24"}}
    r = requests.post(f"{uri}/api/firewall/filter/addRule",
                      auth=auth, verify=False, json=data)
    print("created:", json.loads(r.text)["uuid"])
```

### Regel deaktivieren und anwenden (curl)

```bash
UUID=0f4a…
curl -k -u "$key:$secret" -X POST \
  "https://opnsense.local/api/firewall/filter/toggleRule/$UUID/0"
curl -k -u "$key:$secret" -X POST \
  "https://opnsense.local/api/firewall/filter/apply"
```

Ohne `apply` bleibt die Änderung in der Konfigurationsdatei aktiv, aber nicht im laufenden Regelsatz — dieser Zwei-Schritt ist API und UI gemeinsam.

## Rate Limits und Betriebshinweise

- **Keine dokumentierte Ratenbegrenzung** der API; Schutz über Firewall-Regeln auf das UI-Interface und dedizierte API-Benutzer.
- Änderungen staged: erst `set/add`, dann `apply`/`reconfigure`; Skripte sollten die Apply-Aktion nie vergessen.
- Modell-Defaults: fast alle Felder haben Defaultwerte — für robuste Skripte relevante Felder trotzdem explizit setzen.
- Model-Typen (Boolean `y/n`, Listen, UUID-Referenzen) stehen in den XML-Modellen der Module; fehlerhafte Typen quittiert die API mit Validierungs-Meldungen.
- `verify=False`/`-k` nur im Labor; produktiv internes CA-Zertifikat hinterlegen (System ▸ Trust).

## Webhooks

- **Nicht vorhanden** — OPNsense bietet keine ein-/ausgehenden Webhooks.
- Ereignisse lassen sich über Log-/Syslog-Export und Plugins (Telegraf, Zabbix-Agent, CrowdSec) nach außen melden; Aktionen von außen bleiben API-Calls.

## SDKs und Client-Bibliotheken

- **Kein offizielles SDK**; die API ist schlicht REST, Beispiele in der Doku nutzen Python-`requests`.
- **Community**: Terraform-Provider und Python-Wrapper existieren gemeindegetragen, sind aber nicht offiziell gepflegt — versionsabhängig evaluieren.
- **Beste Referenz je Installation**: `docs.opnsense.org/development/api/<core|plugins>/…` plus Netzwerk-Trace (`F12`) der eigenen Version.
- **Testoberfläche**: Das Menü *Firewall ▸ Automation* (Core-Modul „firewall“) dient als Referenz-/Testbett für API-Interaktionen.

## Siehe auch

- [index.md](index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
