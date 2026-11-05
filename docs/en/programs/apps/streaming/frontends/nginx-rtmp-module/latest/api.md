# nginx-rtmp-module - API documentation

## Overview

The module offers **no REST API**. The interfaces are: the **HTTP hooks** (the server calls your own application), the **status page** (`rtmp_stat`, XML) and the **`exec`** commands. Anyone who wants to automate builds the HTTP endpoint themselves.

## Authentication

Access control only exists when hooks are set:

```nginx
application live {
    live on;
    on_publish      http://127.0.0.1:9000/rtmp/publish;
    on_publish_done http://127.0.0.1:9000/rtmp/publish_done;
    on_play         http://127.0.0.1:9000/rtmp/play;
}
```

The hook receives `name`, `app`, `type` (`live`/`record`) and `addr` as query parameters. Answer logic:

| Answer | Effect |
|--------|--------|
| `2xx` | publish/play allowed |
| `4xx`/`5xx` | the connection is refused |
| JSON body (newer builds) | additional params, e.g. `args` |

### Header (hook input)

```
POST /rtmp/publish?name=test1&app=live&type=live&addr=10.0.0.5 HTTP/1.1
Host: 127.0.0.1:9000
```

## Hooks (endpoint reference)

| Hook | Moment | Use |
|------|--------|-----|
| `on_publish` | before publishing | check the stream key, reject a key |
| `on_publish_done` | after the end of publishing | clean up, statistics |
| `on_play` | before playing | check viewer access |
| `on_play_done` | after the end of playing | viewer counting |
| `on_done` | end of connection | generic |
| `on_update` | repeatedly during the stream | heartbeat, metrics |
| `on_record_done` | finished recording | ffmpeg cutting, upload |
| `on_drop` | an unplanned abort by a publisher | alarm |
| `on_meta` | the stream's metadata | evaluate title/description |
| `on_sei` | SEI messages | timecode processing |

## Status page (machine-readable)

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

## Examples

### Publish admission with a stream key (Python/Flask)

```python
from flask import Flask, request, abort
app = Flask(__name__)
KEYS = {"secret": "church"}

@app.post("/rtmp/publish")
def publish():
    name = request.args["name"]
    key = name.split("_")[-1]
    if KEYS.get(key) != "church":
        abort(403)
    return "", 200

app.run(port=9000)
```

### Post-processing a recording (`on_record_done`)

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
# the hook receiver then starts, for example:
ffmpeg -i "$path" -c:v libx264 -crf 23 "/var/processed/$(basename "$path")"
```

### `exec` transcoding (the classic route)

```nginx
application live {
    live on;
    exec ffmpeg -i rtmp://127.0.0.1:1935/live_source/$(name) \
         -c:v libx264 -b:v 1200k -f flv rtmp://127.0.0.1:1935/hls/$(name);
}
```

## Rate limits

- **no rate limits in the module**
- protection through nginx filters (`limit_req`, `limit_conn`) on HLS/DASH, a firewall on `1935`

## Webhooks

- the hook mechanism **is** the webhook mechanism (server → your own application)
- the direction "API → server" does not exist; changing the configuration = file + `nginx -s reload`

## SDKs and client libraries

- **no SDKs** — the hooks are plain HTTP, the status is XML
- playback: hls.js, video.js, VLC, ffmpeg
- monitoring: translate the status XML with a script or the nginx exporter

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
