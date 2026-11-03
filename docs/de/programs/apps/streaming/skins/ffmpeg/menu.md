# FFmpeg - Menüpunkte

FFmpeg hat keine Menüs — es ist eine reine Kommandozeilensammlung. Statt Menüleiste und Dialogen gibt es Werkzeuge, Options-Schalter und Filter-Kommandos. „Menüpunkte“ sind hier also die Aufrufvarianten.

## Werkzeuge (statt Anwendungsmenü)

| Werkzeug | Zweck |
|----------|-------|
| `ffmpeg` | Transcoding, Muxing/Demuxing, Filtern, Stream-Auswahl |
| `ffprobe` | Analyse von Streams/Formaten, Ausgabe als json/csv/xml |
| `ffplay` | einfacher SDL-Player für Schnellchecks |
| `ffserver` | Stream-Server — eingestellt und aus den Builds entfernt |
| `ffmpeg -h` / `-help` | eingebaute Selbsthilfe nach Themen (`-h encoder`, `-h filter`, `-h muxer`) |

## Aufrufstruktur

```
ffmpeg [globale Optionen] [Input-Optionen] -i EINGABE ... [Output-Optionen] AUSGABE
```

| Bereich | typische Optionen |
|---------|-------------------|
| Global | `-hide_banner`, `-loglevel`, `-y`/`-n`, `-stats`, `-progress` |
| Input | `-ss` (Seek), `-t`/`-to` (Dauer), `-f` (Format erzwingen), `-i` |
| Stream-Auswahl | `-map`, `-vn`, `-an`, `-sn`, `-map_metadata` |
| Codec | `-c copy`, `-c:v libx264`, `-c:a aac`, `-b:a 128k` |
| Qualität | `-crf`, `-b:v`, `-preset`, `-tune`, `-pix_fmt` |

## Optionsthemen (statt Untermenüs)

| Themenblock | Beispiele |
|-------------|-----------|
| Video | `-vf`, `-r`, `-s WxH`, `-g`, `-profile`, `-level` |
| Audio | `-af`, `-ar`, `-ac`, `-channel_layout` |
| Muxer/Container | `-f mp4|mkv|webm|ts|hls|dash|nut`, `-movflags` |
| Netzwerk | `-rtsp_transport`, timeout-Optionen, SRT-Parameter |
| Hardware | `-hwaccel`, `-hwaccel_output_format`, Encoder wie `h264_nvenc` |

## Filter-Kommandos (libavfilter)

Der Filtergraph ist das eigentliche „Bedienmenü“ von FFmpeg — Kurzkommandos, per `,` verkettet und über `-filter_complex` mit benannten Pads verdrahtet.

| Filter | Aufgabe |
|--------|---------|
| `scale` | Skalieren, Aspect-Handling |
| `crop` / `pad` | Beschneiden, Ränder ansetzen |
| `overlay` | Bild-im-Bild, Wasserzeichen |
| `drawtext` | eingebrannter Text (Libfreetype) |
| `concat` | Aneinanderfügen von Quellen |
| `fps` | Framerate-Konvertierung |
| `volume` / `amix` | Lautstärke, Mehrkanal-Mischung |
| `loudnorm` | Audio-Normalisierung nach EBU R128 |

Beispiel:

```
ffmpeg -i in.mp4 -i logo.png -filter_complex "[0:v][1:v]overlay=W-w-10:10" out.mp4
```

## Menüs nach Rolle

FFmpeg kennt keine Rollen und keine Benutzeroberfläche — Bedienbarkeit entsteht allein durch Argumente, Shell-Skripte und Wrapper. Team-Rollen (Schnitt, Encoding-Betrieb, Automatisierung) nutzen dieselben Kommandos; Berechtigungen sind Dateisystem-Berechtigungen.
