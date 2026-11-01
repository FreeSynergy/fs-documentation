# MistServer - API Dokumentation

## Übersicht

MistServer hat genau **eine** Schnittstelle: ein JSON-API auf Port `4242`. Jeder Aufruf ist eine normale HTTP-GET-/POST-Anfrage mit dem Parameter `command`, der ein JSON-Objekt enthält. Die Weboberfläche ist nur ein JavaScript-Client dieser API.

## Authentifizierung

- Ohne Login antwortet der Server nur auf `authorize` (und auf localhost gar nicht erst abgefragt)
- HTTP ist nicht persistent → **Authorization muss bei jedem Request erneut gesendet werden**
- Passwort wird nie im Klartext übertragen: erst Challenge anfordern, dann `MD5(MD5(passwort) + challenge)` senden

### Ablauf

```
1) GET /api?command={"authorize":{"username":"admin","password":""}}
   → {"status":"CHALL","challenge":"abcdef1234567890"}

2) GET /api?command={"authorize":{"username":"admin","password":"<md5(md5(secret)+challenge)>"}}
   → {"status":"OK","challenge":"..."}
```

| Status | Bedeutung |
|--------|-----------|
| `OK` | angemeldet, alle Kommandos erlaubt |
| `CHALL` | nicht angemeldet, Challenge liegt bei |
| `NOACC` | kein Konto vorhanden (nur hier darf eines angelegt werden) |
| `ACC_MADE` | Konto wurde angelegt |

### URL-Format

```
http://<host>:4242/api?command=<URL-encodiertes JSON>
```

Der Pfad `/api` erzwingt eine JSON-Antwort; ohne ihn liefert der Server bei ungültigen Anfragen die HTML-Oberfläche. Mit `callback`/`jsonp` als zusätzlichem Parameter funktioniert JSONP.

## Kommandos (Auswahl)

| Kommando | Richtung | Beschreibung |
|----------|----------|--------------|
| `authorize` | lesen/schreiben | Login, Challenge, Konto anlegen |
| `config` | lesen/schreiben | Controller-Port, aktivierte Protokolle, `serverid`; Antwort mit `version`, `time`, `online` |
| `streams` | **deklarativ** | sendet den **vollständigen** Stream-Plan; fehlt ein Stream, wird er gelöscht |
| `active_streams` | lesen | Liste aktuell aktiver Stream-Namen |
| `stats_streams` | lesen | Statistiken; Array-Request z. B. `["clients","lastms"]` |
| `clients` | lesen | Zuschauer- und Push-Verbindungen |
| `capabilities` | lesen | installierte Connector/Codecs, CPU, RAM, Load |
| `update` / `checkupdate` | lesen | Versionsvergleich (LTS-Ausgabe) |

> Achtung: `streams` ist kein Lese-Endpunkt im Sinne von „zeigen", sondern ein Sichern des gesendeten Zustands. Für reine Abfragen `active_streams`, `stats_streams` oder `config` verwenden.

## Beispiele

### Aktive Streams und Zuschauerzahlen

```bash
curl -s 'http://localhost:4242/api?command=%7B%22active_streams%22%3A%5B%5D%7D'
# → ["kirche","test1"]

curl -s 'http://localhost:4242/api?command=%7B%22stats_streams%22%3A%5B%22clients%22%5D%7D'
# → {"kirche":[12],"test1":[0]}
```

### Stream deklarativ anlegen

```bash
curl -s -X POST http://localhost:4242/api \
  --data-urlencode 'command={"streams":{"kirche":{"source":"push://","DVR":30000}}}'
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

# 1) Challenge holen, 2) hashen, 3) autorisieren
ch = call({"authorize": {"username": "admin", "password": ""}})["challenge"]
pw = hashlib.md5((hashlib.md5(b"secret").hexdigest() + ch).encode()).hexdigest()
call({"authorize": {"username": "admin", "password": pw}})

print(call({"active_streams": []}))
```

## Rate Limits

- **keine dokumentierten Rate Limits**
- Der Server ist single-process mit Connector-Prozessen; häufiges Pollen von `clients` kostet CPU → Intervall bewusst wählen
- Schutz: Port `4242` nicht öffentlich exponieren, nur localhost/Management-Netz

## Webhooks

- **keine Webhooks**; Ereignisse (Stream online/offline, Zuschauerzahlen) werden über `active_streams`/`stats_streams` abgefragt
- Weiterleitungen und Aufnahme laufen als **Automatic push**-Regeln, nicht als Callbacks

## SDKs und Client-Bibliotheken

- **keine offiziellen SDKs** — die API ist bewusst „HTTP + JSON"
- Referenz-Client: die mitgelieferte HTML-Oberfläche (`http://host:4242`)
- Doxygen-Referenz aller Kommandos: `mistserver.org/doxygen/api.html`
- Docker-Images und systemd-Units für den Betrieb

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
