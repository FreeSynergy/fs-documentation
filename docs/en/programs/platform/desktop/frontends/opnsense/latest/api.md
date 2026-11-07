# OPNsense - API Documentation

## Overview

OPNsense is built API-first: the web UI is merely one MVC client; the same controllers serve the REST API. Calls follow the pattern

```
https://<host>/api/<module>/<controller>/<command>/[<param1>/[<param2>…]]
```

with two verbs: `GET` reads, `POST` writes or executes actions (JSON body/response). Official reference: developer documentation `docs.opnsense.org/development/api.html` (core and plugin APIs). Since ~99 % of the endpoints are used by the UI itself, the browser's network tab (filter `/api/`) is the most precise documentation of your own installation.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| MVC-REST `/api/<module>/<controller>/<command>` | configuration and actions | official, automatic for UI modules |
| Business Edition API (`OPNBECore`) | support/update automation | Business Edition only |
| Webhooks | — | ❌ Not available |

## Authentication

- **API key + secret**: created **per user** under **System ▸ Access ▸ Users** (edit user → generate API key; `apikey.txt` download possible).
- **Transport**: HTTP **Basic Auth** — `key` as user name, `secret` as password:

```bash
key='w86XNZob/8Oq8aC5r0kbNarNtdpoQU…'
secret='XeD26XVrJ5ilAc/EmglCRC+0j2…'
curl -k -u "$key:$secret" "https://opnsense.local/api/core/service/search" \
  -X POST -H 'Content-Type: application/json' \
  -d '{"current":1,"rowCount":7,"sort":{},"searchPhrase":""}'
```

- **ACLs**: the key inherits the group/resource rights of the user; "Effective Privileges" show which endpoints are allowed (resources correspond to the UI pages).
- **Separate API user** with minimum rights is best practice; GUI sessions (cookies) are unusual for scripts.

## Naming

The reference sometimes lists commands in snake_case (`add_rule`), the UI examples in camelCase (`addRule`). In practice the router largely accepts both forms; the safer choice is the spelling from the network trace of your own version.

## Endpoints (examples, module `firewall`)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/firewall/filter/searchRule?current=1&rowCount=25&searchPhrase=` | search rule grid |
| `POST` | `/api/firewall/filter/addRule` | create rule (body `{"rule": {…}}`) |
| `GET` | `/api/firewall/filter/getRule/<uuid>` | read single rule |
| `POST` | `/api/firewall/filter/setRule/<uuid>` | set rule |
| `POST` | `/api/firewall/filter/toggleRule/<uuid>/<0|1>` | enable/disable rule |
| `POST` | `/api/firewall/filter/delRule/<uuid>` | delete rule |
| `POST` | `/api/firewall/filter/apply` | activate rule set |
| `GET` | `/api/firewall/filter_util/rule_stats` | rule statistics |
| `GET,POST` | `/api/firewall/alias/search_item` | search aliases |
| `GET` | `/api/firewall/alias/get_item/<uuid>` | read alias |
| `POST` | `/api/firewall/alias/add_item` | create alias |
| `POST` | `/api/firewall/alias/set_item/<uuid>` | set alias |
| `POST` | `/api/firewall/alias/del_item/<uuid…>` | delete alias |
| `POST` | `/api/firewall/alias/reconfigure` | reload alias tables |
| `POST` | `/api/firewall/d_nat/searchRule` | search port forward rules |
| `POST` | `/api/firewall/source_nat/addRule` | create outbound rule |
| `POST` | `/api/core/service/search` | search services (System ▸ Diagnostics ▸ Services) |

Further modules: `core` (interfaces, firmware, settings …), `certificates`, `routes`, plus plugins (`wireguard`, `acmeclient`, `ids` …) – each plugin has its own controllers following the same pattern.

## Request/response basics

- **Base**: `https://<host>/api/…` – same port as the web UI (default 443, HTTP→HTTPS).
- **Content**: `Content-Type: application/json` for `POST`; some export commands (download/upload) work with file responses.
- **Parameters**: UUIDs as path segment (`/getRule/<uuid>`), optional flags likewise as segments (`/toggleRule/<uuid>/0`).
- **Errors**: validation and ACL errors come as a JSON message with text; status codes are not always unambiguous — check the message content.
- **Two-stage model**: write → `apply`/`reconfigure`; without the activation step the change remains inactive.

## Responses of grid endpoints

Search endpoints use uniform parameters (`current`, `rowCount`, `sort`, `searchPhrase`) and return:

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

## Examples

### Search for a rule and create it if needed (official pattern)

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

### Disable a rule and apply (curl)

```bash
UUID=0f4a…
curl -k -u "$key:$secret" -X POST \
  "https://opnsense.local/api/firewall/filter/toggleRule/$UUID/0"
curl -k -u "$key:$secret" -X POST \
  "https://opnsense.local/api/firewall/filter/apply"
```

Without `apply` the change remains active in the configuration file, but not in the running rule set – this two-step process is shared by API and UI.

## Rate limits and operational notes

- **No documented rate limit** for the API; protection via firewall rules on the UI interface and dedicated API users.
- Changes are staged: first `set/add`, then `apply`/`reconfigure`; scripts should never forget the apply action.
- Model defaults: almost all fields have default values – still set the relevant fields explicitly for robust scripts.
- Model types (boolean `y/n`, lists, UUID references) are defined in the XML models of the modules; incorrect types are answered by the API with validation messages.
- `verify=False`/`-k` only in the lab; in production, store the internal CA certificate (System ▸ Trust).

## Webhooks

- **Not available** — OPNsense offers no incoming or outgoing webhooks.
- Events can be reported externally via log/syslog export and plugins (Telegraf, Zabbix agent, CrowdSec); actions from outside remain API calls.

## SDKs and client libraries

- **No official SDK**; the API is plain REST, examples in the documentation use Python `requests`.
- **Community**: Terraform provider and Python wrappers exist, community-maintained, but not officially supported – evaluate depending on version.
- **Best reference per installation**: `docs.opnsense.org/development/api/<core|plugins>/…` plus network trace (`F12`) of your own version.
- **Test interface**: the menu *Firewall ▸ Automation* (core module "firewall") serves as a reference/test bed for API interaction.

## See also

- [index.md](../index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
