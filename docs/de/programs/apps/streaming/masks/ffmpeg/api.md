# FFmpeg - API Dokumentation

## Keine REST-API

FFmpeg bietet **keine** HTTP-/REST-Schnittstelle, keine Endpunkte, keine Authentifizierung, keine Rate Limits und keine Webhooks — und kann das auch nicht, weil es kein Daemon und kein Server ist, sondern ein Prozess, den man startet, beobachtet und der mit einem Exit-Code endet. `ffserver` (der einstige HTTP-Stream-Server) wurde eingestellt und aus den Builds entfernt. „Integration“ bedeutet daher: Prozess steuern, Statusströme lesen, Bibliotheken einbinden.

## Integrationsfläche 1: Prozess-Aufruf

| Fläche | Detail |
|--------|--------|
| Aufruf | `ffmpeg [Optionen] -i EIN [Optionen] OUT` |
| Exit-Code | `0` Erfolg, `≠ 0` Fehler (z. B. 1 allgemeiner Fehler, 69 etc. je nach Build) |
| stdout/stderr | Menschen-Statistik auf stderr; für Maschinen `-progress` nutzen |
| Signale | `SIGINT`/`q` brechen ab, SIGPIPE bei Pipe-Ende |
| stdin sperren | `-nostdin` verhindert Tastatur-Eingriff in Pipelines |

## Integrationsfläche 2: `-progress pipe:1` (Statusstrom)

```
ffmpeg -nostdin -progress pipe:1 -i in.mp4 -c:v libx264 out.mp4
```

| Feld (Beispiel) | Bedeutung |
|-----------------|-----------|
| `frame=`, `fps=`, `bitrate=` | Encode-Fortschritt |
| `out_time_us=`, `out_time_ms=` | verarbeitete Zeit (Mikrosekunden) |
| `progress=` | `continue` bis `end` |

Eine Zeile pro Update, `key=value` — die de-facto „Streaming-API“ für Fortschritt in Weboberflächen und Workern.

## Integrationsfläche 3: `ffprobe -of json` (Maschinen-API)

```
ffprobe -v quiet -print_format json -show_streams -show_format datei.mkv
```

| Bereich | zurückgegeben |
|---------|---------------|
| `streams[]` | Codec, Auflösung, Framerate, Kanalzahl, Timeline |
| `format` | Container, Dauer, Bitrate, Tags |
| Formate | json, csv, xml, ini (`-of`/`-print_format`) |

Damit ist ffprobe die vollständige Lese-API ohne Bibliotheksbindung — ideal für Skin- und Weboberflächen-Tools, die Metadaten anzeigen.

## Integrationsfläche 4: libav\*-Bibliotheken (C)

| Bibliothek | Aufgabe |
|------------|---------|
| libavformat | Muxer/Demuxer, Protokolle |
| libavcodec | Encode/Decode |
| libavfilter | Filtergraph programmatisch |
| libswscale / libswresample | Skalierung, Audio-Konvertierung |
| libavutil | Puffer, Zeitbasis, Hashing |

Bindung über `pkg-config libavformat libavcodec libavfilter`; Versions-/API-Garantien folgen den Release-Zweigen (6.x/7.x).

## Sprachbindungen und Wrapper

| Sprachbindung | Ansatz |
|---------------|--------|
| ffmpeg-python | Python-Command-Builder um `ffmpeg`/`ffprobe` |
| Python `subprocess` | Direktaufruf + `-progress`-Parsing (Standardweg) |
| fluent-ffmpeg / ffmpeg-static | Node.js-Builder bzw. gebündelte Binaries |
| JavaCV / JavaCPP (bytedeco) | Java-Binding der libav\*-C-API |
| MediaMTX, Ant Media Server | nutzen FFmpeg als Prozess-Backend (Remux/Aufnahme) |

| Eigenschaft | FFmpeg-Prozess-API |
|-------------|--------------------|
| Rate Limits | keine — lokal begrenzt durch CPU/GPU |
| Webhooks | keine — Ersetzen durch Exit-Code und `-progress end` |
| Auth | keine — Dateisystem-/Prozessberechtigungen genügen |
| Parallelität | so viele Prozesse, wie Hardware zulässt |

## Command-Builder-Muster

```python
cmd = ["ffmpeg", "-nostdin", "-hide_banner",
       "-ss", "00:01:00", "-t", "60",
       "-i", src, "-vf", "scale=1280:-2",
       "-c:v", "libx264", "-crf", "23", dst]
```

Regel: Argumente als Liste übergeben (kein Shell-String), `-progress pipe:1` anzapfen, Exit-Code auswerten — das ist die komplette „API“ von FFmpeg.

## Siehe auch

- [index.md](index.md) - Übersicht und Dateistruktur
- [menu.md](menu.md) - Werkzeuge, Optionen, Filter-Kommandos
- [features.md](features.md) - Funktionen und Grenzen
- [description.md](description.md) - Einordnung und Abgrenzung
- [structure.md](structure.md) - Pipeline- und CLI-Struktur
- [shortcuts.md](shortcuts.md) - Tastatursteuerung von ffmpeg und ffplay
