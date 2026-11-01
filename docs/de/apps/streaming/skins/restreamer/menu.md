# Restreamer - Menüpunkte

## Webui-Bereiche (linkes Menü)

| Bereich | Beschreibung |
|---------|--------------|
| Start / Dashboard | Status: laufende Push-Streams, Player-Vorschau, Statistik |
| Push Key | geheimer Schlüssel für den Eingang (`?key=<pushKey>`), neu generieren |
| Player | eingebetteter HLS-/HTTP-Player, Direktlinks, Einbettungscode |
| Settings | Grundeinstellungen, Ports, Authentifizierung, Speicherort |
| Advanced Settings | nginx-rtmp-Direktiven, Transcoding, WebRTC, Aufzeichnungsintervall |
| Multi-Target (RTMP-Restream) | Ziele mit Name und RTMP-URL, aktivieren/deaktivieren |
| Logs / Diagnostics | nginx-, Node- und ffmpeg-Logs, Support-Paket |

## Settings (Auswahl)

| Feld | Inhalt |
|------|--------|
| HTTP-Port / HTTPS-Port | Weboberfläche und Stream-Auslieferung |
| RTMP-Port | Standardeingang 1935 |
| Webui-Passwort | Zugriffsschutz der Oberfläche |
| Aufzeichnung | Intervall (Segment-Größe), Ordner, Aufbewahrung |
| Transcoding | ffmpeg-Profile, Auflösung/FPS, Audio-Codec |
| WebRTC / Low-Latency | optional aktivierbar |
| Auto-Start | Stream bei Containerstart beginnen |

## Menüs nach Rolle

| Rolle | Sichtbar |
|-------|----------|
| anonym | Player und Stream-URLs (wenn erlaubt) |
| Webui-Benutzer | alle Bereiche nach Passworteingabe |
| Admin (Container) | Umgebungsvariablen, Volumes, Neustart über Docker |
