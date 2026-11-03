# nginx-rtmp-module - Beschreibung

## Übersicht

Das nginx-rtmp-module ist die klassische Open-Source-Basis für eigene Streaming-Server: Ein nginx-Prozess empfängt RTMP und liefert HLS/DASH aus. Es ist bewusst ein Modul, keine Plattform.

## Was das nginx-rtmp-module macht

nginx erhält einen zusätzlichen RTMP-Listener. Publisher senden an eine `application`, das Modul muxed mit und schreibt HLS-/DASH-Dateien ins Dateisystem. nginx selbst liefert diese Dateien an Browser aus. Everything else — Transcoding, Auth, Upload — geschieht über Hooks und `exec`.

## Vorteile

- **Ein Prozess, eine Konfigurationsdatei**: keine zweite Runtime, keine Datenbank
- **Vertraute Betriebstechnik**: nginx-Logik (TLS, Vhosts, Rate-Filter, Caching) gilt automatisch
- **Vorhersagbar**: Streams sind Verzeichnisse auf der Platte, prüfbar mit `ls`
- **Seit Jahren im Einsatz**: sehr gut dokumentiert, unzählige Beispiele
- **Lizenz**: BSD, frei kombinierbar

## Abgrenzung zu anderen Systemen

### nginx-rtmp vs. MediaMTX

- MediaMTX ist ein eigener Server mit YAML, Control-API, WebRTC/SRT/MoQ und Prometheus
- nginx-rtmp ist älter, kleiner im Funktionsumfang, aber mitten in der nginx-Welt
- MediaMTX kann moderne Protokolle ohne Zusatztools; nginx-rtmp braucht ffmpeg und eigene Skripte

### nginx-rtmp vs. MistServer

- MistServer konfiguriert über JSON-API und hat DVR und Push-Regeln
- nginx-rtmp konfiguriert nur über Dateien; dafür ist jede Datei eine normale nginx-Direktive
- MistServer bringt WebRTC mit, nginx-rtmp nicht

### nginx-rtmp vs. Restreamer

- der Restreamer **ist** nginx + nginx-rtmp-module plus Webui und ffmpeg-Integration
- wer die Webui nicht braucht, fährt mit dem nackten Modul schlanker und versionierbarer

## Technische Details

- **Backend**: C-Modul für nginx 1.18+ (Build mit `--add-module`)
- **Database**: keine — Konfiguration in `nginx.conf`, Zustand im Prozess
- **Frontend**: Statusseite `rtmp_stat` (XML, optional XSL-Stylesheet)
- **Authentication**: nur über HTTP-Hooks (`on_publish`, `on_play`)
- **Hosting**: überall, wo nginx läuft; Docker-Images vorhanden (inoffiziell)

## Für wen ist das Modul geeignet?

- Teams mit bestehender nginx-Infrastruktur und einfachen RTMP→HLS-Anforderungen
- Lern- und Referenzprojekte, bei denen jede Zeile Konfiguration/versionierbar sein muss
- als Basis des Docker-Restreamers
- **nicht** geeignet, wenn WebRTC, SRT, RTMPS oder Multi-Bitrate-Renditions benötigt werden — hier MediaMTX/Ant Media/Wowza wählen
