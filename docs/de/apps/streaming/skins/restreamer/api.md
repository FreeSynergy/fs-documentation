# Restreamer - API Dokumentation

## Übersicht

Der Restreamer hat keine formale öffentliche API. Zugangsweg ist das Zusammenspiel aus **RTMP-Eingang**, **HTTP-/HLS-Ausgang**, **Hooks** (nginx-rtmp-Ereignisse an Scripte/HTTP) sowie **`restreamer-cli`** und der Config-Datei für Konfiguration von außen. Die JSON-Endpunkte der Webui sind inoffiziell und können sich ändern.

**Zugangswege im Überblick**

| Weg | Verwendung | Status |
|-----|------------|--------|
| RTMP(S)-Push | Stream-Eingang | offiziell |
| HLS/MP4-URLs | Wiedergabe und Download | offiziell |
| Hooks (`on_publish` …) | eigene Logik bei Ereignissen | offiziell (nginx-rtmp) |
| `restreamer-cli` | Settings ohne Webui | offiziell |
| `/opt/restreamer/config.json` | deklarativen Zustand setzen | offiziell |
| Webui-JSON-Endpunkte | interne UI-Aufrufe | ⚠ inoffiziell, versionsabhängig |

## Eingang und Ausgang

| Zweck | Adresse (Standard) |
|-------|--------------------|
| Push (von OBS/ffmpeg) | `rtmp://<host>:1935/live/stream?key=<pushKey>` |
| HLS-Playlist (Player) | `http://<host>:8080/hls/stream.m3u8` |
| HLS-Segmentliste/Dateien | `http://<host>:8080/hls/…` |
| Aufgezeichnete Segmente | `http://<host>:8080/media/…` (Volume `var/media`) |
| Weboberfläche | `http://<host>:8080`, `https://<host>:8081` |

Der Push-Key ist das einzige Geheimnis des Eingangs; er wird im Query-Parameter `key` mitgeführt und lässt sich in der Webui rotieren.

## Authentifizierung

- **Eingang**: Push-Key pro Stream (`?key=…`), optional IP-Beschränkung über nginx-Direktiven
- **Webui**: ein Passwort (Session-Cookie), kein Benutzerkonzept
- **Ausgang**: ❌ keine Token-geschützte HLS-Auslieferung (❌, Schutz nur vorgelagert)

## Hooks (Ereignisse)

nginx-rtmp-Hooks sind als Umgebungsvariablen oder Direktiven konfigurierbar und rufen Scripte oder HTTP-Endpunkte auf:

| Hook | Zeitpunkt |
|------|-----------|
| `on_publish` | Push beginnt (hier kann man ablehnen: HTTP != 200) |
| `on_publish_done` | Push endet |
| `on_record_done` | ein Aufzeichnungs-Segment ist fertig |
| `on_dvr` | Segment für die Aufzeichnung geschrieben |

### Hook-Beispiel (HTTP)

```
on_publish http://hooks.example.com/restreamer/publish
```

Der Aufruf ist ein `POST` mit nginx-rtmp-Formulardaten (`callid`, `streamid`, `remote_addr` …); Antwortstatus 200 erlaubt, alles andere lehnt ab.

## Konfiguration von außen

```bash
# Einstellung lesen/setzen (Syntax je Version, Hilfe anzeigen lassen)
docker exec restreamer /opt/restreamer/bin/restreamer-cli help
docker exec restreamer /opt/restreamer/bin/restreamer-cli config set \
  --key webui_password --value 's3cret'

# deklarativer Ansatz: Config-Datei bearbeiten und Container neu starten
docker cp restreamer:/opt/restreamer/config.json ./config.json
# … editieren …
docker cp ./config.json restreamer:/opt/restreamer/config.json
docker restart restreamer
```

## Beispiel: Stream-Test von außen

```bash
# 10 Sekunden Test-Push mit ffmpeg
ffmpeg -re -f lavfi -i testsrc=size=1280x720:rate=30 \
  -f lavfi -i sine -t 10 \
  -c:v libx264 -preset veryfast -c:a aac \
  -f flv "rtmp://localhost:1935/live/stream?key=PUSHKEY"

# HLS prüfen
curl -s http://localhost:8080/hls/stream.m3u8 | head -5
```

## Rate Limits

Keine dokumentierten Kontingente (Selbstbetrieb). Praktische Grenzen: nginx-Worker, Bandbreite und optional vorgelagerter Reverse-Proxy (`limit_req`).

## SDKs und Client-Bibliotheken

- ❌ kein offizielles SDK (❌)
- Ökosystem: nginx-rtmp-Direktiven, ffmpeg/OBS als Push-Clients, jeder HTTP-Client für Hooks
- `restreamer-cli` ist die einzige mitgelieferte Automatisierungsschnittstelle

## Skin-Hinweis

Eingang/Ziel/Segment entsprechen dem Standardmodell ([modelle.md](../../../../data/modelle.md)); URL- und Schlüsselfelder folgen [felder.md](../../../../data/felder.md).
