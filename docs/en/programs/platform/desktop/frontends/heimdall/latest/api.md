# Heimdall - API Documentation

## Overview

Heimdall has **no officially documented API**. The project is aimed at people who maintain their dashboard in the user interface and deliberately forgoes automation interfaces. Existing HTTP routes are the internal Laravel routes of the frontend; they are not versioned and may change without notice.

**Interfaces at a glance**

| Type | Use | Status |
|-----|------------|--------|
| Laravel routes (web/JSON) | manage apps, panels, layout, accounts | Internal, undocumented |
| External service APIs | called by enhanced apps (Pi-hole, Sonarr, Emby, Portainer …) | API of the respective service |
| Server statistics | read locally on the Heimdall machine | No network endpoint |
| Webhooks | ❌ Not available | — |
| API key for Heimdall itself | ❌ Not available | — |

## Authentication

- **Session (session cookie)**: after sign-in, Laravel sets a session cookie (`LaravelApplicationCookie` or similar). All internal routes require a valid session.
- **CSRF protection**: write requests require the CSRF token stored in the HTML (meta tag or form field) plus the header `X-CSRF-TOKEN`. Without this token, Heimdall responds with HTTP 419.
- **Roles**: administrative routes are reserved for administrators (role-dependent, version-dependent).
- **Disabled sign-in**: if sign-in is switched off, the routes are reachable by anyone who can reach the page — protection then relies solely on the proxy or network.
- **Encrypted service keys**: API keys of the enhanced apps are stored encrypted in the database and protected with `APP_KEY`.

## Internal routes (not officially documented)

The following table shows typical routes of the frontend. **Prerequisites**: valid session, CSRF token, correct `APP_URL`. The names are an aid to understanding the frontend, not a guaranteed interface.

### Apps

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/` | Start page, renders panels and apps |
| `GET` | `/apps` | List the apps of the account (view/JSON depending on version) |
| `POST` | `/apps` | Create app (title, URL, icon, colour) |
| `GET` | `/apps/{id}` | Load a single app |
| `PUT` | `/apps/{id}` | Change app |
| `DELETE` | `/apps/{id}` | Delete app |
| `POST` | `/apps/{id}/icon` | Upload icon file |

### Layout and panels

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/layout` | Currently saved layout of the account |
| `POST` | `/layout` | Save layout (order and panel assignment) |
| `POST` | `/layout/reset` | Reset layout to the default |

### Account and users

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/login` | Sign-in form |
| `POST` | `/login` | Sign in (email, password) |
| `POST` | `/logout` | Sign out |
| `GET` | `/settings` | Settings overview |
| `POST` | `/settings/account` | Change own credentials |
| `GET` | `/settings/users` | User list (newer versions, admin) |
| `POST` | `/settings/users` | Create user (admin) |
| `DELETE` | `/settings/users/{id}` | Delete user (admin) |

## Example: internal route with session and CSRF

```bash
# 1. Load the sign-in page, note the CSRF token and cookie
curl -s -c cookies.txt https://heimdall.example/login \
  | grep -o 'name="_token" value="[^"]*"'

# 2. Sign in
curl -s -b cookies.txt -c cookies.txt -X POST https://heimdall.example/login \
  -d "email=admin@example.com" \
  -d "password=secret" \
  -d "_token=<token>"

# 3. Create app (CSRF token from a loaded page)
curl -s -b cookies.txt -X POST https://heimdall.example/apps \
  -H "X-CSRF-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"Grafana","url":"https://grafana.local","colour":"#4a90d9"}'
```

Possible response (not guaranteed, since undocumented):

```json
{
  "success": true,
  "app": {
    "id": 12,
    "title": "Grafana",
    "url": "https://grafana.local",
    "colour": "#4a90d9"
  }
}
```

## Example: using the API key of an enhanced app

Enhanced apps call the **API of the connected service**, not a Heimdall API. The stored key is used server-side. Example Pi-hole:

```bash
# Check whether the stored data works (Pi-hole v6 API)
curl -s "http://pihole.local/api.php" \
  -d "token=<api-key>&num=10"
```

Expected values (simplified) and their use in the tile:

```json
{
  "status": "enabled",
  "ads_blocked_today": 1284,
  "dns_queries_today": 21450
}
```

**Important**: if the request fails, the tile shows an error state; Heimdall itself does not log webhooks or events.

## Configuration as "interface"

The most reliable automation runs via files and environment variables, not via HTTP.

### `.env` (selection)

| Variable | Description |
|----------|--------------|
| `APP_KEY` | Key for encrypting the service keys; **must not change**, otherwise all keys become unusable |
| `APP_URL` | Public address, important for icons and redirects |
| `APP_DEBUG` | Error output; leave at `false` in operation |
| `DB_CONNECTION` | `sqlite` (default), `mysql`, `pgsql` |
| `DB_DATABASE` | Path to the SQLite file or name of the external database |
| `TZ` | Time zone, affects date information in calendars and statistics |
| Auth switch | Sign-in on/off (variant name version-dependent, e.g. `AUTH_ENABLED=false`) |

### Persistent data

| Path | Content |
|------|--------|
| SQLite file in the data directory | apps, panels, layouts, accounts, encrypted keys |
| `app/public/uploads` | uploaded icons |
| Custom CSS/theme files | visual customizations |

A backup consists of the database file plus uploads. After replacing the file, containers must be restarted and migrations run.

## Rate limits

- Heimdall ships **with no built-in rate limit**.
- The load arises mainly from server-side queries of the enhanced apps when the page is loaded.
- Protection via the reverse proxy is recommended (nginx `limit_req`, Traefik middleware, Fail2ban for sign-in attempts).
- Recommendation: keep the number of enhanced apps small and do not integrate slow services into the dashboard.

## Webhooks and internal eventing

- **No webhooks**, no event output, no notifications.
- **Internal eventing**: the frontend updates statistics values and tiles by querying again when the page is loaded; layout changes are saved to the database immediately.
- **Workaround for automation**: external scripts write changes indirectly via the database (risky, not recommended) or replace the entire instance from a backed-up volume.

## SDKs and client libraries

- **No SDK** for Heimdall.
- Anyone who wants to extend Heimdall writes an **enhanced-app package** (Laravel class, service provider, Blade template) and uses the SDKs of the respective service.
- For automation, address the APIs of the connected services directly instead of involving Heimdall.

## See also

- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
