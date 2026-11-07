# SuiteCRM - API Documentation

## Overview

SuiteCRM provides a **module-oriented REST interface (v8)** as well as an older **SOAP interface**. Both work with the instance's username and password, not with API keys. The official descriptions of methods and fields are in the developer handbook at `developers.suitecrm.com`; details and behavior are version-dependent.

**API types at a glance**

| Type | Usage | Status |
|-----|------------|--------|
| REST v8 (`/service/v8/rest.php`) | read, write, delete records of all modules; maintain relationships | Officially documented |
| SOAP (`/service/v4/soap.php`) | same methods as REST, XML-based | Deprecated, but available |
| New REST routes in SuiteCRM 8 | access via the 8.x shell | version-dependent, look up in the developer docs |
| Webhooks | ❌ Not available | — |
| GraphQL, OData, CalDAV, CardDAV | ❌ Not available | — |

## Authentication

- **No API key system**: there are no long-lived API tokens and (in 7.x) no OAuth2.
- **REST v8**: access either with the header `User-Auth: user::password` on each request, or via a session ID that was obtained beforehand with `login`.
- **Session ID**: the response of `login` contains a field `id`; this is passed as `session` in subsequent calls.
- **SOAP**: session ID as the first argument of every method.
- **Permissions**: all calls are subject to the account's roles and teams; an API call only sees data the account would be allowed to see in the interface.
- **OAuth/LDAP**: LDAP affects sign-in to the interface, not the API. External OAuth systems are only possible via extensions.

### Login flow (REST v8)

1. Call `login` with username and password
2. Store the returned session ID (`id`)
3. Run further methods with `session`
4. Call `logout` at the end

## Endpoints

### Base

```
GET/POST /service/v8/rest.php
```

Parameters are passed as form fields or query parameters: `method`, `input_type=JSON`, `response_type=JSON`, `session`, `module`, plus method-specific fields.

### Methods (REST v8)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `POST` | `/service/v8/rest.php?method=login` | Log in, returns session ID |
| `POST` | `/service/v8/rest.php?method=logout` | End session |
| `POST` | `/service/v8/rest.php?method=authenticate` | Check whether credentials are valid |
| `GET` | `/service/v8/rest.php?method=get_module_list` | List available modules |
| `GET` | `/service/v8/rest.php?method=get_metadata` | Field definitions and form layout of a module |
| `GET` | `/service/v8/rest.php?method=get_entry_list` | Records of a module with filter, sorting, pagination |
| `GET` | `/service/v8/rest.php?method=get_entry_count` | Number of hits for a filter |
| `GET` | `/service/v8/rest.php?method=get_entry` | Load a single record by ID |
| `POST` | `/service/v8/rest.php?method=set_entry` | Create or update a record |
| `POST` | `/service/v8/rest.php?method=set_entries` | Write several records in one call |
| `POST` | `/service/v8/rest.php?method=delete_entry` | Delete a record |
| `POST` | `/service/v8/rest.php?method=relationship_add` | Create a relationship between two records |
| `POST` | `/service/v8/rest.php?method=relationship_remove` | Remove a relationship |
| `GET` | `/service/v8/rest.php?method=get_related` | Load linked records (subpanel contents) |

### Modules in the CRM category

| Module | Meaning in the interface |
|-------|-----------------------------|
| `Leads` | Prospects (conversion to Contact/Account/Opportunity) |
| `Contacts` | Contacts |
| `Accounts` | Companies |
| `Opportunities` | Sales opportunities / deals |
| `Calls`, `Meetings`, `Tasks` | Activities |
| `Cases`, `Bugs` | Support cases |
| `Emails`, `Notes` | Communication |
| `Products`, `Quotes` | Product catalog and quotes |

### SOAP

```
POST /service/v4/soap.php
```

Method names correspond to the REST methods (`login`, `get_entry_list`, `set_entry`, ...); the first argument is always the session. The WSDL is served by the instance; exact path details are version-dependent.

## Examples

### Search leads (curl)

```bash
curl -s -X POST "https://crm.example.com/service/v8/rest.php" \
  -d "method=get_entry_list" \
  -d "input_type=JSON" \
  -d "response_type=JSON" \
  -H "User-Auth: api_user::secret" \
  -d "module=Leads" \
  -d "query=last_name LIKE '%Meyer%'" \
  -d "max_num=10" \
  -d "order_by=date_modified DESC" \
  -d "offset=0"
```

Response (abridged):

```json
{
  "module_list": [
    { "Leads": { "id": "5f1a...", "first_name": "Anna", "last_name": "Meyer", "status": "New" } }
  ],
  "result_count": 1,
  "current_entry": 0
}
```

### Create lead (curl)

```bash
curl -s -X POST "https://crm.example.com/service/v8/rest.php" \
  -d "method=set_entry" \
  -d "input_type=JSON" \
  -d "response_type=JSON" \
  -H "User-Auth: api_user::secret" \
  -d "module=Leads" \
  --data-urlencode 'name_value_list=[{"name":"first_name","value":"Anna"},{"name":"last_name","value":"Meyer"},{"name":"status","value":"New"},{"name":"account_name","value":"Meyer AG"}]'
```

### Opportunity with session (Python)

```python
import requests

BASE = "https://crm.example.com/service/v8/rest.php"

# 1. Login
r = requests.post(BASE, data={
    "method": "login", "input_type": "JSON", "response_type": "JSON",
    "user_auth": "api_user::secret",
})
session_id = r.json()["id"]

# 2. Load open deals
r = requests.get(BASE, params={
    "method": "get_entry_list", "input_type": "JSON", "response_type": "JSON",
    "session": session_id, "module": "Opportunities",
    "query": "sales_stage NOT IN ('Closed Won','Closed Lost')",
    "max_num": 50, "order_by": "date_expected_close ASC",
})
for row in r.json()["module_list"]:
    print(list(row.values())[0]["name"], list(row.values())[0]["amount"])

# 3. Logout
requests.post(BASE, data={"method": "logout", "session": session_id,
                          "input_type": "JSON", "response_type": "JSON"})
```

## Rate limits

- SuiteCRM ships **no built-in rate limiting** for REST or SOAP.
- Protection via the web server or reverse proxy is recommended: nginx `limit_req`, Apache `mod_ratelimit`, Fail2ban on error messages.
- PHP settings (`max_execution_time`, `memory_limit`, `post_max_size`) and database performance also act as limits; large `set_entries` calls and broad `get_entry_list` queries are the usual bottlenecks.
- Recommended approach: few, bundled calls per minute instead of many single queries; always use `max_num` and `offset`.

## Webhooks and automation

- **No webhooks**: SuiteCRM does not send events to external systems.
- **Own automation**: the workflow module (triggers, conditions, actions) and the scheduler (`cron.php`) run within the instance.
- **Logic hooks**: PHP functions on model events (`before_save`, `after_save`, `after_delete`) are the usual way to call an external system via HTTP on changes.
- **Workaround for outgoing events**: a cron script that determines changed records via the field history and reports them to a target system via REST.

## SDKs and client libraries

- **No official SDK** from SuiteCRM for programming languages.
- REST v8 is plain HTTP with form parameters, so `curl`, `requests` (Python), `axios`/`fetch` (JavaScript) and Guzzle (PHP) are sufficient.
- SOAP clients (SoapClient in PHP, suds/zeep in Python) work against the SOAP interface.
- Community libraries for SuiteCRM/SugarCRM exist but are not officially maintained; check version and coverage before use.

## Operational notes

- Create an API account with its own rights and restrict it to the required modules.
- Enforce HTTPS; otherwise the `User-Auth` header contains plaintext passwords.
- After updates, clear the metadata cache; otherwise `get_metadata` returns outdated field definitions.
- Custom fields are named in the API as Studio creates them (read the field name from `get_metadata`, do not guess).

## See also

- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
