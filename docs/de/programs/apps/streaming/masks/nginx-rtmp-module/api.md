# nginx-rtmp-module - API Dokumentation

## Übersicht

Das Modul bietet **keine REST-API**. Die Schnittstellen sind: **HTTP-Hooks** (der Server ruft die eigene Anwendung auf), die **Statusseite** (`rtmp_stat`, XML) und **`exec`**-Kommandos. Wer automatisieren will, baut den HTTP-Endpunkt selbst.

## Authentifizierung

Zugangskontrolle existiert nur, wenn Hooks gesetzt sind:

```nginx
application live {
    live on;
    on_publish      http://127.0.0.1:9000/rtmp/publish;
    on_publish_done http://127.0.0.1:9000/rtmp/publish_done;
    on_play         http://127.0.0.1:9000/rtmp/play;
}
```

Der Hook erhält `name`, `app`, `type` (`live`/`record`), `addr` als Query-Parameter. Antwort-Logik:

| Antwort | Wirkung |
|---------|---------|
| `2xx` | Publish/Play erlaubt |
| `4xx`/`5xx` | Verbindung wird abgelehnt |
| JSON-Body (neuere Builds) | zusätzliche Params, z. B. `args` |

### Header (Hook-Eingang)

```
POST /rtmp/publish?name=test1&app=live&type=live&addr=10.0.0.5 HTTP/1.1
Host: 127.0.0.1:9000
```

## Hooks (Endpunkt-Referenz)

| Hook | Zeitpunkt | Verwendung |
|------|-----------|------------|
| `on_publish` | vor Publish | Stream-Key prüfen, Key ablehnen |
| `on_publish_done` | nach Publish-Ende | Aufräumen, Statistik |
| `on_play` | vor Play | Zuschauer-Zugriff prüfen |
| `on_play_done` | nach Play-Ende | Viewer-Zählung |
| `on_done` | Verbindungsende | generic |
| `on_update` | regelmäßig während des Streams | Heartbeat, Metriken |
| `on_record_done` | fertiges Recording | ffmpeg-Schnitt, Upload |
| `on_drop` | unplanned Abbruch eines Publishers | Alarm |
| `on_meta` | Metadaten des Streams | Titel/Description auswerten |
| `on_sei` | SEI-Nachrichten | timecode-Verarbeitung |

## Statusseite (maschinenlesbar)

```nginx
location /stat { rtmp_stat all; }        # XML
location /stat { rtmp_stat all; rtmp_stat_stylesheet stat.xsl; }  # HTML
```

```bash
curl -s http://localhost/stat | xmllint --format -
```

```xml
<streams>
  <publish>
    <publishing>false</publishing>
    <name>test1</name>
    <time>4512</time>
    <bw_in>1240000</bw_in>
    <bw_out>2480000</bw_out>
    <nclients>2</nclients>
    <clients><client><play>active</play><time>120</time></client></clients>
  </publish>
</streams>
```

## Beispiele

### Publish-Zulassung mit Stream-Key (Python/Flask)

```python
from flask import Flask, request, abort
app = Flask(__name__)
KEYS = {"geheim": "kirche"}

@app.post("/rtmp/publish")
def publish():
    name = request.args["name"]
    key = name.split("_")[-1]
    if KEYS.get(key) != "kirche":
        abort(403)
    return "", 200

app.run(port=9000)
```

### Recording nachbereiten (`on_record_done`)

```nginx
application live {
    live on;
    record all;
    record_path /var/records;
    record_unique on;
    on_record_done http://127.0.0.1:9000/rtmp/record_done;
}
```

```bash
# Hook-Empfänger startet z. B.:
ffmpeg -i "$path" -c:v libx264 -crf 23 "/var/processed/$(basename "$path")"
```

### `exec`-Transcoding (klassischer Weg)

```nginx
application live {
    live on;
    exec ffmpeg -i rtmp://127.0.0.1:1935/live_source/$(name) \
         -c:v libx264 -b:v 1200k -f flv rtmp://127.0.0.1:1935/hls/$(name);
}
```

## Rate Limits

- **keine Rate Limits im Modul**
- Schutz über nginx-Filter (`limit_req`, `limit_conn`) auf HLS/DASH, Firewall auf `1935`

## Webhooks

- der Hook-Mechanismus **ist** der Webhook-Mechanismus (Server → eigene Anwendung)
- Richtung „API → Server" gibt es nicht; Konfigurationsänderung = Datei + `nginx -s reload`

## SDKs und Client-Bibliotheken

- **keine SDKs** — Hooks sind Plain-HTTP, Status ist XML
- Wiedergabe: hls.js, video.js, VLC, ffmpeg
- Monitoring: Status-XML per Skript oder nginx-Exporter übersetzen

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
