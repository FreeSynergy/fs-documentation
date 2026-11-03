# OBS Studio - Funktionen

## Hauptfunktionen

### Szenen und Quellen
- unbegrenzt viele Szenen, in Ordnern gruppiert, mit Übergängen (Schnitt, Wischen, Fade, Eigenbau)
- Quellen: Fenster, Bildschirm, Browserquelle, Bild, Videodatei, Medienquelle, Text (GDI+/Freetype), Farbquelle, Folie, Kamera, Audio-Ein-/Ausgabe, virtuelle Kamera
- Gruppierung und Transformation (Position, Scale, Drehung, Rand, Zuschneiden), Animationen per Szenenwechsel

### Komposition und Filter
- pro Quelle: Scaling-Filter (Bikubisch, Lanczos, Bicubic), Farbkorrektur, Chroma-Key, Masken, Scrollen, Delay
- pro Szene: Audio-Filter, Übergangs-Filter
- Overlays, Lower Thirds, Browser-Overlays (Alerts, Chat), Green-Screen

### Audio
- mehrspuriger Mischer mit Kanälen, Noise-Gate, Rauschunterdrückung, Kompressor, Limiter, Delay
- Monitoring (Nur ausgehend / Nur beobachtet), Mehrspur-Aufnahme (bis 6 Spuren)

### Ausgabe
- Streaming: RTMP/RTMPS, SRT, RIST (je Version), mehrere Ziele über Multi-Encoder-Plugin
- Aufnahme: MKV/MP4/MOV, Container-Re-Mux, neue Aufnahme ohne Lücke („Reconnect“)
- Encoder: x264, NVENC, AMD AMF, QuickSync, Apple VideoToolbox

### Produktionshilfen
- Studio-Modus (Vorschau vs. Ausgang mit „Übergang ausführen“)
- Rekorde (Replay-Puffer), Untertitel, Szenenschnellwechsel per Hotkey
- Virtuelle Kamera (Ausgang als Webcam für Meetings)

## Was OBS Studio NICHT kann

- **Kein Videoschnitt / keine Nachbearbeitung** — Zeitachse, Tonspuren, Effekte nachträglich (❌)
- **Kein Multiview-Empfang fremder Streams** als Quelle ohne Browserquelle/Zusatz-Plugins (❌ nativ)
- **Kein plattformseitiges Transcoding/Restreaming** — OBS sendet an ein Ziel, Multipathing nur via Plugins/Restream-Dienst
- **Keine kollaborative Mehrpersonensteuerung** ohne obs-websocket-Skripte (❌ eingebaut)
- **Kein eingebautes Chat-/Stats-Dashboard** (❌, nur über Browserquelle)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| obs-websocket 5.x | eingebauter WebSocket-Server mit JSON-Protokoll |
| obs-ffmpeg-mux / FFMpeg-Video-Filter | offizielle Zusatzplugin-Sammlung |
| obs-multi-encoder (Community) | gleichzeitiges Streaming zu mehreren Zielen |
| obs-browser / obs-nvenc | Hardware-Encoding |
| Skripte | Python/Lua über obs-scripting |
| Virtuelle Kamera | offiziell (Windows/Linux/macOS) |
