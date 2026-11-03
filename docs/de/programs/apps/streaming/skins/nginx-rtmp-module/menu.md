# nginx-rtmp-module - Menüpunkte

## Übersicht

Es gibt **keine Oberfläche**. „Menüpunkte" sind die Konfigurationsblöcke in `nginx.conf` und die Statusseite. alles andere erledigen Hooks und `exec`-Kommandos.

## Konfigurationsblöcke

| Block | Inhalt |
|-------|--------|
| `rtmp { server { … } }` | RTMP-Server, `listen 1935`, Timeouts, `chunk_size` |
| `application <name> { … }` | eine „App" = ein Stream-Raum (`live`, `stream`, …) |
| `live on` | Live-Modus: durchreichen statt Datei ausspielen |
| `hls on` + `hls_path` | HLS-Ausgabe (Segmente + Playlist ins Verzeichnis) |
| `dash on` + `dash_path` | MPEG-DASH-Ausgabe |
| `record all\|video\|audio` | Aufzeichnung, `record_path`, `record_unique` |
| `exec` / `exec_async` | externes Kommandos (meist ffmpeg) pro Publish starten |
| `pull rtmp://…` | Relay: Stream von anderer Instanz ziehen |
| `on_publish` / `on_play` | HTTP-Hooks für Zugangskontrolle |
| `http { … rtmp_stat all; }` | Statusseite als XML, optional mit `stat.xsl` |

## Wichtige Direktiven (Auswahl)

| Direktive | Default | Bedeutung |
|-----------|---------|-----------|
| `listen` | `1935` | RTMP-Port |
| `timeout` | `180s` | Inaktivitäts-Timeout |
| `drop_idle_publisher` | `10s` | verwirft Publisher, die nicht senden |
| `ping_interval` / `ping_timeout` | `8s` / `8s` | Keepalive zum Client |
| `chunk_size` | `4096` | RTMP-Chunk-Größe |
| `interleave` | `on` | Audio/Video in einem Kanal mischen |
| `wait_key` / `wait_video` | `on` / `on` | erst ab Keyframe senden |
| `idle_streams` | `on` | Streams ohne Zuschauer weiterführen |
| `publish_notify` | `off` | Client-Notifications bei Statuswechsel |
| `hls_fragment` / `hls_playlist_length` | `5s` / `30s` | HLS-Segmentierung |
| `hls_nested` | `off` | eigener Unterordner pro Stream |
| `record_append` / `record_unique` | `off` / `off` | Verhalten der Aufzeichnung |

## Statusseite

```nginx
http {
    server {
        location /stat  { rtmp_stat all; rtmp_stat_stylesheet stat.xsl; }
        location /      { root /var/www/hls; }   # HLS/DASH-Auslieferung
    }
}
```

## Menüs nach Rolle

| Rolle | Zugriff |
|-------|---------|
| Publisher | `rtmp://host/live/<streamname>` — Zugang nur über `on_publish` absicherbar |
| Zuschauer | HLS/DASH über nginx (`/live.m3u8`) oder RTMP-Play |
| Betreiber | `nginx.conf`, `nginx -t`, `nginx -s reload` |
| Automatisierung | HTTP-Hooks und `exec`-Skripte |
