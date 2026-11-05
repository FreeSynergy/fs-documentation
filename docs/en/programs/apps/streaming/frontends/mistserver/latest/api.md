# MistServer - API documentation

## Overview

MistServer has exactly **one** interface: a JSON API on port `4242`. Every call is a normal HTTP GET/POST request with the parameter `command`, which contains a JSON object. The web interface is only a JavaScript client of this API.

## Authentication

- Without a login the server only answers `authorize` (and on localhost it is not even asked for one)
- HTTP is not persistent → **authorization has to be sent again with every request**
- The password is never transmitted in clear text: first request a challenge, then send `MD5(MD5(password) + challenge)`

### Sequence

```
1) GET /api?command={"authorize":{"username":"admin","password":""}}
   → {"status":"CHALL","challenge":"abcdef1234567890"}

2) GET /api?command={"authorize":{"username":"admin","password":"<md5(md5(secret)+challenge)>"}}
   → {"status":"OK","challenge":"..."}
```

| Status | Meaning |
|--------|---------|
| `OK` | signed in, all commands allowed |
| `CHALL` | not signed in, a challenge is attached |
| `NOACC` | no account exists (only here may one be created) |
| `ACC_MADE` | the account was created |

### URL format

```
http://<host>:4242/api?command=<URL-encoded JSON>
```

The path `/api` forces a JSON answer; without it the server returns the HTML interface on invalid requests. With `callback`/`jsonp` as an additional parameter, JSONP works.

## Commands (a selection)

| Command | Direction | Description |
|---------|-----------|-------------|
| `authorize` | read/write | login, challenge, create an account |
| `config` | read/write | controller port, activated protocols, `serverid`; answer with `version`, `time`, `online` |
| `streams` | **declarative** | sends the **complete** stream plan; if a stream is missing it is deleted |
| `active_streams` | read | list of currently active stream names |
| `stats_streams` | read | statistics; array request e.g. `["clients","lastms"]` |
| `clients` | read | viewer and push connections |
| `capabilities` | read | installed connectors/codecs, CPU, RAM, load |
| `update` / `checkupdate` | read | version comparison (the LTS edition) |

> Careful: `streams` is not a read endpoint in the sense of "show", but a saving of the state you send. For pure queries use `active_streams`, `stats_streams` or `config`.

## Examples

### The active streams and their viewer counts

```bash
curl -s 'http://localhost:4242/api?command=%7B%22active_streams%22%3A%5B%5D%7D'
# → ["church","test1"]

curl -s 'http://localhost:4242/api?command=%7B%22stats_streams%22%3A%5B%22clients%22%5D%7D'
# → {"church":[12],"test1":[0]}
```

### Create a stream declaratively

```bash
curl -s -X POST http://localhost:4242/api \
  --data-urlencode 'command={"streams":{"church":{"source":"push://","DVR":30000}}}'
```

### Python

```python
import hashlib
import json
import requests

BASE = "http://localhost:4242/api"

def call(payload: dict) -> dict:
    r = requests.get(BASE, params={"command": json.dumps(payload)})
    return r.json()

# 1) get the challenge, 2) hash, 3) authorise
ch = call({"authorize": {"username": "admin", "password": ""}})["challenge"]
pw = hashlib.md5((hashlib.md5(b"secret").hexdigest() + ch).encode()).hexdigest()
call({"authorize": {"username": "admin", "password": pw}})

print(call({"active_streams": []}))
```

## Rate limits

- **no documented rate limits**
- the server is single-process with connector processes; polling `clients` frequently costs CPU → choose the interval deliberately
- protection: do not expose port `4242` publicly, only localhost/the management network

## Webhooks

- **no webhooks**; events (stream online/offline, viewer counts) are queried through `active_streams`/`stats_streams`
- forwarding and recording run as **automatic push** rules, not as callbacks

## SDKs and client libraries

- **no official SDKs** — the API is deliberately "HTTP + JSON"
- reference client: the shipped HTML interface (`http://host:4242`)
- Doxygen reference of all commands: `mistserver.org/doxygen/api.html`
- Docker images and systemd units for operation

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
