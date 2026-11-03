# nginx-rtmp-module - Struktur & UI/UX

## Übersicht

Bedienobjekte sind die `nginx.conf` und das Ausgabeverzeichnis. Diese Datei beschreibt, wie Eingänge, Pfade und Auslieferungswege zusammenspielen — die Vorlage für eine Skin-Oberfläche.

## Prozess- und Konfigstruktur

### Hauptbereiche

```
                    nginx (ein Master, mehrere Worker)
┌───────────────────────────────────────────────────────────────────┐
│  rtmp { }            http { }                                      │
│  ─────────           ──────────                                    │
│  listen 1935         listen 80/443  (TLS, CORS, Cache)             │
│   application live    location /live/  → /var/www/hls/live/        │
│     live on           location /stat   → rtmp_stat all             │
│     hls on            location /dash/  → /var/www/dash/live/       │
│     hls_path /var/www/hls                                                            │
└───────────────────────────────────────────────────────────────────┘
        ▲                                        │
        │ rtmp publish                           ▼ m3u8/TS-Dateien
   OBS / ffmpeg                              Browser (hls.js)
```

### Eingangsseite

- `application live` ist der Raum: Stream-Name ergibt `rtmp://host/live/<name>`
- `on_publish`-Hook kann vor Verbindungsaufbau ablehnen
- `exec`-Kommandos laufen als Kindprozess pro Stream

### Ausgangsseite

- HLS: `/var/www/hls/<name>/index.m3u8` plus `indexN.ts` (mit `hls_nested` ein Ordner pro Stream)
- DASH: `/var/www/dash/<name>/index.mpd`
- Auslieferung, Caching, CORS und TLS sind ganz normale nginx-Einstellungen

### Konfigurationsschichten

| Ebene | Datei/Weg |
|-------|-----------|
| Haupt | `nginx.conf` (`rtmp`- und `http`-Blöcke) |
| Include | `include /etc/nginx/apps/*.conf;` pro application sinnvoll |
| Hooks | `on_publish http://127.0.0.1:9000/rtmp/publish` |

## UI/UX (Übertragung auf eine Skin-Oberfläche)

### Design-Prinzipien

- **Konfiguration als primäre Oberfläche**: Ansicht zeigt application-Blöcke und ihre Direktiven
- **Dateisystem sichtbar machen**: HLS-/DASH-Pfade und Segmentalter sind direkt einsehbar
- **Status als XML-Ansicht**: `rtmp_stat` ist die Referenz für Live-Ansichten

### Farbschema und Typografie

- keine eigene Oberfläche; für eine Skin: Konfig-Blöcke in Monospace, Statuswerte tabellarisch
- Empfehlung: application = Akzentfarbe, Direktiven = neutral, Fehler (Timeouts) = rot

### Interaktionen

- Reload ohne Unterbrechung: `nginx -t && nginx -s reload` (Streams können dabei neu gestartet werden)
- Hook-Antworten sind der einzige „Button" zur Laufzeit (Zugriff erlauben/ablehnen)

## Zugänglichkeit

- Konfiguration ist Text → versionierbar, vorlesbar, diffbar
- Statusseite: XML ohne Stylesheet ist Screenreader-freundlicher als die XSL-HTML-Version
- Browser-Wiedergabe braucht eigene Accessibility im Player (Untertitel, Tastatur)

## Performance

- HLS-Segmentierung (`hls_fragment`) bestimmt Latenz; kleine Segmente erhöhen Request-Last
- `out_queue`/`max_message` begrenzen langsame Zuschauer
- `idle_streams on` kostet weiter CPU/Bandbreite — für teure Quellen auf `off` setzen
- Viele parallele Publisher skalieren über mehrere nginx-Instanzen (Relay per `pull`)
