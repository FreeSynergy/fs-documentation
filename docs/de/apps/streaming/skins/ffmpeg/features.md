# FFmpeg - Funktionen

## Hauptfunktionen

- **Transcoding**: Dekodieren → Filtern → Enkodieren in einem Durchlauf; `-c copy` überschreibt nur den Container ohne Neukodierung
- **Muxing/Demuxing**: Container mp4, mkv/matroska, webm, ts, nut sowie HLS (`-f hls`) und DASH als Segment-Schreiber
- **Analyse mit `ffprobe`**: `-show_streams -show_format`, Ausgabe als json/csv/xml — die Maschinen-Auskunft über jede Datei
- **Filtergraph (libavfilter)**: `scale`, `overlay`, `concat`, `drawtext`, `crop`, `fps`, `volume`, `amix`, `loudnorm` (EBU R128); Verkettung mit `,`, Graphen mit `-filter_complex` und `-map`
- **Wiedergabe mit `ffplay`**: SDL-basierter Minimalplayer für Schnelltests
- **Selbsthilfe**: `ffmpeg -h`, `-h full`, themenbezogen `-h encoder|decoder|filter|muxer|protocol`

## Codecs

| Familie | Codec / Bibliothek |
|---------|--------------------|
| H.264 | `libx264`, `libx264`-Parameter `-crf`, `-preset`, `-tune` |
| H.265 | `libx265` |
| AV1 | `libaom`, `libsvtav1` (SVT-AV1) |
| VP9 / VP8 | `libvpx-vp9`, `libvpx` |
| Audio | `libopus`, `aac` (nativer Encoder), `libfdkAAC` (optional, Build-Flag), `libmp3lame` |
| Profi | `prores`, DNxHD |
| Bild | `png`, `mjpeg` |

## Hardware-Beschleunigung

| Backend | Encoder / Weg |
|---------|----------------|
| NVIDIA | `h264_nvenc`, `hevc_nvenc`, Dekodierung `-hwaccel cuda` |
| Intel | `qsv` (`h264_qsv`, `hevc_qsv`), `-hwaccel qsv` |
| Linux allg. | `vaapi`, `v4l2m2m` |
| Apple | `videotoolbox` (`h264_videotoolbox`) |

## Protokolle / IO

| Richtung | Protokolle |
|----------|------------|
| Eingang | RTMP, RTSP, SRT, HLS/DASH (Client), UDP/RTP, HTTP(S), `pipe:`, Geräte: `v4l2`, `alsa`, `dshow`, `avfoundation` |
| Ausgang | RTMP, SRT, UDP/RTP, HTTP(S), HLS/DASH-Segmente auf Dateisystem, `pipe:1` in andere Prozesse |

FFmpeg ist dabei **Client und Segment-Schreiber**, aber kein Server: HLS/DASH werden als Dateien geschrieben oder per Protokoll gepusht; Annehmen eingehender Streams übernimmt ein Server wie MediaMTX oder nginx-rtmp.

## Performance und Betrieb

- `-progress pipe:1` liefert maschinenlesbaren Fortschrittsstrom, `-stats` die Menschenanzeige
- `-f null -` erzwingt komplette Dekodierung ohne Ausgabe — Rechenlast-/Analyse-Benchmark
- CPU-Auslastung skalierbar per `-threads`; `-preset` steuert Geschwindigkeit/Kompression
- GPU-Encoder (nvenc/qsv/vaapi) entlasten die CPU bei Live-Ketten deutlich

## Was FFmpeg NICHT kann

- **Keine GUI** — kein Fenster, keine Mausbedienung, alles läuft über Kommandozeile (❌)
- **Keine Szenen- oder Bildmischer-Funktion** — kein interaktives Umschalten von Quellen wie in OBS (❌)
- **Kein Live-Streaming-Server** — nimmt keine eingehenden Publish-Ströme entgegen und verteilt sie nicht (❌)
- **Keine Timeline-/Schnitt-Oberfläche** — Schnitte entstehen nur durch Parameter wie `-ss`/`-t` (❌)
- **Keine Plattform-APIs** — kein OAuth, kein automatischer YouTube-Upload, kein Chat (❌)
- **Kein DRM und keine Lizenzprüfung-Auslieferung** — verschlüsselt nur, was der Container erlaubt (❌)

## Siehe auch

Streaming-Produktion erledigt [OBS Studio](../obs-studio/index.md); Stream-Annahme und Verteilung übernehmen [MediaMTX](../mediamtx/index.md) oder der [Restreamer](../restreamer/index.md); als Pipeline-Bibliothek mit eigener Bedienung alterniert [GStreamer](../gstreamer/index.md).
