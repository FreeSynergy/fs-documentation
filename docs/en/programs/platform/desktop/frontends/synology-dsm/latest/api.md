# Synology DSM - API Documentation

## Overview

DSM provides an **HTTP/JSON API** via a single entry point: `entry.cgi`. Each request describes the desired API, its version and the method:

```
GET/POST http://<nas>:5000/webapi/entry.cgi?api=SYNO.<Module>.<Name>&version=<n>&method=<name>
```

The API is documented in the **developer manuals of the packages** (FileStation, Download Station, Surveillance Station, WebStation …) and **is not promised as a stable product interface**: names and versions change between DSM major versions.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| `SYNO.*` APIs via `entry.cgi` | auth, system, users, shares, packages, FileStation | documented in developer manuals |
| `query.cgi` (`SYNO.API.Info`) | query available APIs and versions | documented |
| Package-specific endpoints | Drive, Chat, Surveillance, Container Manager | partly **not publicly documented** |
| Webhooks | ❌ Not available (event scripts instead) | — |

## Authentication

**`SYNO.API.Auth`** (versions 1–7, depending on DSM release) creates a session:

| Parameter | Description |
|-----------|--------------|
| `account` / `passwd` | user name and password (passed over HTTPS and URL-encoded) |
| `format` | `sid` (session ID in response body) or `cookie` (session via HTTP cookie) |
| `session` | name of the target area (e.g. `FileStation`), limits the session to this context |
| `expire` | session duration, `always` for unlimited (allowed depending on setting) |
| `otp_code` | 6-digit TOTP code if the account uses two-factor authentication |
| `enable_syno_token` | `yes` returns the anti-CSRF token (`SynoToken`) in the login result |

**Session handling**

- With `format=sid`, `sid` comes in the response body; each follow-up request passes it as `_sid=<value>`.
- With `format=cookie`, DSM sets an HttpOnly session cookie (in current versions `id`); the browser sends it automatically.
- **Write `POST` requests** additionally require the header **`SynoToken`** with the value of the cookie `_SynoToken`; if it is missing, the request is rejected.
- Sign out: `method=logout` with `session=<name>` (and `_sid` in SID mode). Sessions expire after a timeout; multiple sign-ins can end an older session (error `107`).

## Error codes

**General errors (across APIs)**

| Code | Meaning |
|------|-----------|
| 100 | unknown error |
| 101 | `api`, `version` or `method` missing |
| 102 | requested API does not exist |
| 105 | signed-in session has no permission |
| 106 | session timeout |

**`SYNO.API.Auth`**

| Code | Meaning |
|------|-----------|
| 400 | no such account or wrong password |
| 401 | account disabled |
| 402 | permission denied |
| 403 | two-factor code required |
| 404 | two-factor code rejected |
| 406–409 | extended protection cases (account or IP block after frequent failed attempts); **documented differently depending on DSM version** |

## Endpoints

### Authentication and API overview

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET`/`POST` | `/webapi/entry.cgi?api=SYNO.API.Auth&version=6&method=login` | sign-in, returns `sid` and optionally `SynoToken` |
| `GET`/`POST` | `/webapi/entry.cgi?api=SYNO.API.Auth&version=6&method=logout` | end session |
| `GET` | `/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query&query=all` | query available APIs and versions |

### System, users, packages (`SYNO.Core.*`)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `api=SYNO.Core.System&version=1&method=info` | model, DSM version, uptime, drives |
| `GET` | `api=SYNO.Core.System.Utilization&version=1&method=get` | CPU, RAM, network and volume values |
| `GET` | `api=SYNO.Core.Share&version=1&method=list` | shared folders and settings |
| `GET` | `api=SYNO.Core.Package&version=1&method=load_all` | installed packages with status |
| `POST` | `api=SYNO.Core.Package.Control&version=1&method=start` / `stop` | start or stop package |
| `GET` | `api=SYNO.Storage.CGI.Storage&version=1&method=load_info` | pools, volumes, drives, warnings |

### File operations (`SYNO.FileStation.*`)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `POST` | `api=SYNO.FileStation.List&version=2&method=list` | contents of a folder |
| `POST` | `api=SYNO.FileStation.Download&method=download` | download file (`mode=open\|download`) |
| `POST` | `api=SYNO.FileStation.Upload&method=upload` | multipart upload (`path`, `overwrite`, `create_parents`) |
| `POST` | `api=SYNO.FileStation.CreateFolder&method=create` | create folder (task) |
| `POST` | `api=SYNO.FileStation.Delete&method=delete` | delete, returns `taskid` |
| `POST` | `api=SYNO.FileStation.CopyMove&method=start` / `status` / `stop` | copy or move |

## Examples

### Sign in (with OTP and SynoToken)

```bash
curl -s -k "https://nas.example.internal:5001/webapi/entry.cgi" \
  --data-urlencode "api=SYNO.API.Auth" --data-urlencode "version=6" \
  --data-urlencode "method=login" --data-urlencode "account=scripts" \
  --data-urlencode "passwd=geheim" --data-urlencode "format=sid" \
  --data-urlencode "session=FileStation" \
  --data-urlencode "enable_syno_token=yes" --data-urlencode "otp_code=123456"
```

Response:

```json
{
  "data": { "is_portal_port": false, "sid": "aG9tZXBhZ2U6MTcw…", "synotoken": "sFQ7m2YzQpXk…" },
  "success": true
}
```

### Query utilisation

```bash
curl -s -k "https://nas.example.internal:5001/webapi/entry.cgi?api=SYNO.Core.System.Utilization&version=1&method=get&_sid=$SID"
```

Response (shortened):

```json
{
  "success": true,
  "data": {
    "cpu": { "user_load": 8, "system_load": 3, "fg_cpu_load": 11 },
    "memory": { "total_real_ram": 17179869184, "actual_utilization": 42 },
    "volume": [ { "id": "/volume1", "size_free": 4123168604160, "size_total": 7988631699456 } ]
  }
}
```

### List folder contents and follow a task

```bash
curl -s -k "https://nas.example.internal:5001/webapi/entry.cgi" \
  -H "SynoToken: $SYNOTOKEN" \
  -d "api=SYNO.FileStation.List&version=2&method=list&folder_path=/video" \
  --data-urlencode "_sid=$SID"
```

Response (shortened):

```json
{
  "success": true,
  "data": {
    "offset": 0, "total": 1,
    "files": [ { "name": "Film.mkv", "path": "/video/Film.mkv", "isdir": false } ]
  }
}
```

```json
```

## Rate limits and limits

- **No publicly documented rate figures** for `entry.cgi`; in practice, CPU, I/O and the number of concurrent sessions limit requests.
- **Account protection**: after failed sign-ins, DSM blocks the source IP (control panel → security → protection); after failed OTP attempts the account is temporarily blocked.
- Recommendation: serialise requests, cache results, use task APIs (`taskid`) instead of many individual calls, end sessions cleanly.

## Events and webhooks

- **No webhooks**: DSM does not send HTTP events outwards.
- **Notifications**: email, push via Synology Notification, portal bell; configurable per event.
- **Task scheduler with custom events** (system start, shutdown, low storage space, SSD TRIM, USB device): these trigger Bash or PowerShell scripts, which in turn send a `curl` to an external system.

## SDKs and client libraries

- **No official SDK download**; the developer manuals (PDF per package) are the reference.
- **Community libraries** (selection, maintained outside Synology): `python-synology`/`SynoApi` (Python), `py-synologydsm-api` (Python), `synology-api` (Go), `Synology.Api.Client` (C#).
- **Integration help**: the Homepage library has a DSM handler for `SYNO.API.Auth` and `entry.cgi`, see [../gethomepage/structure.md](../../gethomepage/latest/layout.md).

## Operational notes

- **Use HTTPS on port 5001**; plaintext sign-ins over 5000 only in segmented networks.
- **Always send `SynoToken` with POST**, otherwise write calls fail.
- **End sessions** (`method=logout`) to avoid session collisions (error `107`).

## See also

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
