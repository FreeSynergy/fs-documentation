# FFmpeg - Tastatur-Shortcuts

FFmpeg ist primär ein CLI-Werkzeug: Es gibt keine Menü- oder Befehls-Shortcuts wie in einer GUI. Interaktiv wird nur während eines laufenden Prozesses oder in der Wiedergabe von `ffplay` gesteuert — die Tasten sind deshalb strikt nach Werkzeug getrennt.

## ffmpeg (während des Laufs)

| Taste | Wirkung |
|-------|---------|
| `q` / `ESC` | laufenden Vorgang abbrechen (Exit-Code ≠ 0) |
| `+` / `-` | Statistik-/Loglevel herauf-/heruntersetzen |
| `c` | frame-basierte Logausgabe wechseln |
| `v` | Verbosity-/Frame-Anzeige wechseln |

Hinweis: Es existieren **keine** belegten Tasten für Funktionen wie Pause, Seek oder Filterwechsel — alles davon wird vor dem Start als Argument übergeben. In Skripten (`-nostdin`, Pipe-Eingabe) ist auch die interaktive Abbruch-Taste wirkungslos.

## ffplay (SDL-Playerfenster)

| Taste | Wirkung |
|-------|---------|
| `Leertaste` / `p` | Wiedergabe pausieren/fortsetzen |
| `q` / `ESC` | Player beenden |
| `f` | Vollbild umschalten |
| `←` / `→` | 10 s zurück/vor (Suche) |
| `↑` / `↓` | 1 min zurück/vor |
| `PgUp` / `PgDn` | 10 min zurück/vor |
| `m` | stumm schalten |
| `+` / `-` | Lautstärke |
| `w` | Waveform-Anzeige |
| `s` | Audio-Frame-Statistik |
| `0`–`9` | Sprung auf Prozentmarke |
| `a` | Audio-Stream wechseln |
| `v` | Video-Stream wechseln |
| `r` | Untertitel-Stream wechseln |

## ffprobe

Keine interaktiven Tasten — Einmal-Aufruf, Ausgabe auf stdout, Ende mit Exit-Code.

## ffplay starten und einschränken

| Aufruf | Effekt |
|--------|--------|
| `ffplay datei.mkv` | Player-Fenster mit SDL-Steuerung |
| `ffplay -nodisp -autoexit datei.mp3` | ohne Fenster, endet am Dateiende |
| `ffplay -left / -right / -top / -bottom N` | Fensterposition |
| `ffplay rtsp://host/stream` | Netzwerkstreams direkt testen |

## Shortcuts nach Rolle

| Rolle | relevante Tasten |
|-------|------------------|
| Encoding-Betrieb | `q` (Abbruch), `+`/`-` (Logflut begrenzen) |
| Schnellprüfung | ffplay-Komplettsteuerung (Pause, Seek, Vollbild) |
| Automatisierung | keine — Aufrufparameter ersetzen jede Taste |

## Praxisnotiz

Wer von OBS oder anderen GUIs kommt, vermisst Shortcuts: FFmpeg verlagert jede „Tasten-Funktion“ in Optionen — Seek wird `-ss`, Pause gibt es nicht (Prozess stoppen), Lautstärke wird zum `volume`-Filter. Die vollständige Tastebelegung von ffplay ist bewusst minimalistisch und deckt nur Wiedergabesteuerung ab; Streamschnitte, Filter oder Encoder-Umschalten sind zur Laufzeit nicht möglich.

## Querverweise

- Interaktive Tasten- und Hotkey-Regie: [OBS Studio](../obs-studio/index.md)
- Server ohne Tastatur, rein Konfigurationsdatei: [MediaMTX](../mediamtx/index.md)
- Pipeline-Alternativen mit eigenem Tooling: [GStreamer](../gstreamer/index.md)
