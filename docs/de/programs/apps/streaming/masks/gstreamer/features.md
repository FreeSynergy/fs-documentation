# GStreamer - Funktionen

## Übersicht

GStreamer ist ein Baukasten: Fast alles — Aufnahme, Transcoding, Streaming, Abspielen, Aufzeichnung — entsteht aus kombinierbaren Elementen. Es liefert keine fertige Anwendung, sondern die Laufzeit und die Bausteine dafür.

## Hauptfunktionen

### 1. Pipeline-Aufbau

- **Elemente und Pads**: Quellen, Filter, Kodierer und Senken werden über Pads mit ausgehandelten Capabilities (`Caps`) verbunden
- **Bins und `decodebin3`**: automatisches Erkennen von Demuxer/Decoder-Ketten
- **Bus und Nachrichten**: `EOS`, Fehler, Zustandswechsel, Latenz- und Tag-Messages
- **Zustandsmodell**: `NULL` → `READY` → `PAUSED` → `PLAYING` für kontrollierten Start

### 2. Live-Streaming und niedrige Latenz

- **WebRTC**: `webrtcbin` mit ICE/DTLS/SRTP, WHIP-ähnliche Integration über eigene Handler
- **SRT/RTMP/RTSP/MPEG-TS**: `srtsrc`/`srtsink`, `rtmp2src`/`rtmp2sink`, `rtspsrc`/`rtspclientsink`, `mpegtsmux`, `udpsrc`/`udpsink`
- **HLS/DASH schreiben und lesen**: `hlssink`, `dashdemux`/`hlssink`-Kombinationen, `hlsdemux`
- **`tune=zerolatency`** bei Encodern, `sync=false` für Vorführzweige

### 3. Bild und Ton bearbeiten

- **Compositing**: `compositor`, `glvideomixerelement`, Overlays, Greenscreen (`gscreenseg`)
- **Skalierung/Farben**: `scale`, `videoconvert`, `videoflip`, `videobox`, Farbmetadaten
- **Audio**: `audioconvert`, `mixer`, `volume`, `audiofx`-Elemente, Loudness-Ketten
- **Text/Untertitel**: `subtitleoverlay`, `rsvgoverlay`, `textoverlay`

### 4. Hardware und Performance

- **GPU/Codec-Beschleunigung**: `vaapi*`, `nvcodec` (NVEnc/NVDec), `qsv`, `v4l2*` (Embedded), `vulkan`, `glupload`
- **Parallelität**: Bins, Queues und Threads pro Element; `GST_DEBUG=*:5` für Laufzeitanalyse
- **Speicherkontrolle**: Buffer-Pools, `leaky`-Queues, `max-size-buffers`

## Editoren und Begleitwerkzeuge

| Werkzeug | Zweck |
|----------|-------|
| `gst-launch-1.0` | Pipelines interaktiv testen |
| `gst-inspect-1.0` | Dokumentation aller Elemente und Eigenschaften |
| `gst-discoverer-1.0` | Medien-Analyse im Terminal |
| `gst-validate-1.0` | Qualitätsprüfung von Pipelines |
| GST Editing Services (GES) | Timeline-/Schnitt-Bibliothek für eigene Editoren |

## Vergleich der Zugänge

| Zugang | Stärke | Schwäche |
|--------|--------|----------|
| `gst-launch-1.0` | schnellste Pipeline, kein Code | keine dynamische Steuerung |
| C-API | volle Kontrolle, Probes, Signale | Aufwand, GObject-Typwissen nötig |
| `appsrc`/`appsink` | eigene Frames ein-/ausspeisen | Kopien und Zeitsteuerung selbst behandeln |
| GES | Timeline, Clips, Schnitte | eigene Oberfläche nötig |

## Was GStreamer NICHT kann

- **Keine fertige GUI** — ohne eigene oder fremde App gibt es kein Fenster (❌)
- **Kein Streaming-Server out of the box** — `gst-rtsp-server` ist eine Bibliothek, kein Dienst (❌)
- **Kein Multi-Bitrate-Packaging** mit Master-Playlist aus einer Quelle (❌)
- **Kein Szenen-Mischer wie OBS** — Compositing muss selbst verdrahtet werden (❌)
- **Kein DRM** und keine Lizenzserver-Integration (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Plugins (base/good/bad/ugly) | C-Module, zur Laufzeit erkannt |
| `appsrc`/`appsink` | Anbindung an eigene Programme (libgstapp) |
| gst-rtsp-server | RTSP-Endpunkte als Mount-Points |
| gst-python (PyGObject), gstreamer-rs | Skripting und moderne Sprachbindung |
| OBS-Studio, Pitivi, Totem | Anwendungen auf GStreamer-Basis |
