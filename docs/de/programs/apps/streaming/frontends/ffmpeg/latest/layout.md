# FFmpeg - Struktur & UI/UX

## „UI“ ist die Kommandozeile

Es gibt keine Fenster, Dialoge oder Menüs. Die gesamte Benutzeroberfläche besteht aus Aufrufzeile, Fortschrittsanzeige und Exit-Code. Das Verständnis dieser Struktur ersetzt die Bedienoberfläche.

## Pipeline-Struktur (inneres Modell)

```
Eingabe (Demuxer) → Decoder → Filtergraph (libavfilter) → Encoder → Muxer → Ausgabe
```

| Stufe | Was passiert | typische Optionen |
|-------|--------------|-------------------|
| Demuxer | Container lesen (mp4, mkv, ts, HLS) | `-f`, `-i` |
| Decoder | Rohbild/-ton erzeugen | `-hwaccel`, `-c:v` (Eingang) |
| Filtergraph | Umformen, Mischen, Zeichnen | `-vf`, `-af`, `-filter_complex` |
| Encoder | neu kodieren | `-c:v libx264`, `-crf`, `-preset` |
| Muxer | in Zielcontainer schreiben | `-f mp4|mkv|webm|ts|hls|dash|nut` |

Mehrere `-i`-Eingaben werden über `-map 0:v -map 1:a`-artige Ausdrücke den Ausgaben zugeordnet; Pads im Graphen erhalten Namen wie `[0:v][1:v]overlay[v]`.

## CLI-Struktur (äußeres Modell)

| Element | Konvention |
|---------|------------|
| Reihenfolge | Optionen gelten für die **folgende** Datei; `-ss` vor `-i` ist schnell, nach `-i` genau |
| Overrides | letzte Angabe gewinnt; `-y` überschreibt vorhandene Ausgaben |
| Spezialpfade | `pipe:0`/`pipe:1` für Stdio, `:0`/`:1` als Stream-Auswahl |
| Selbsthilfe | `-h`, `-h full`, `-h filter overlay`, `-h encoder h264_nvenc` |

## Anzeige während des Laufs

| Anzeige | Inhalt |
|---------|--------|
| Banner | Version, eingebaute Codecs (unterdrückbar mit `-hide_banner`) |
| `-stats` | Zeit, Frame-Zahl, Geschwindigkeit, Bitrate, q-Index |
| Loglevel | `-loglevel error|warning|info|verbose|debug` |
| `-progress pipe:1` | derselbe Status als `key=value`-Zeilen für Maschinen |

## Filtergraph-Notation

- Verkettung: `scale=1280:-2,fps=30`
- Mehrere Quellen: `[0:v][1:v]overlay=x=10:y=10[out]`, Ansprechen mit `-map "[out]"`
- Pro Filter eigene Optionen (`flag=value`-Paare); Optionenliste per `-h filter NAME`

## Struktur der Projektbausteine

| Baustein | Rolle |
|----------|-------|
| `ffmpeg` / `ffprobe` / `ffplay` | CLI-Werkzeuge über denselben Bibliotheken |
| libavformat / libavcodec / libavfilter | Mux/Demux, Codec-API, Filtergraph |
| libswscale / libswresample | Bildskalierung, Audio-Resampling |
| Testsuite (`fate`) | Referenztests für Decoder/Filter |

## UX-Bewertung

| Aspekt | Bewertung |
|--------|-----------|
| Einarbeitung | steil — Syntax und Optionsreihenfolge wollen gelernt sein |
| Wiederholbarkeit | hervorragend — Aufrufe sind Skripte |
| Fehlerkultur | klare Fehlermeldungen pro Stufe, Exit-Code ≠ 0 bei Fehlern |
| Barrierefreiheit | Text-basiert, dadurch gut für Logs und Automatisierung |
