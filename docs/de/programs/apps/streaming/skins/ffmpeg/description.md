# FFmpeg - Beschreibung

## Was das Programm macht

FFmpeg ist kein Fertiggerät, sondern der Motor: Es liest nahezu jedes Eingangsformat, decodiert es, schiebt es durch einen frei verdrahtbaren Filtergraphen und schreibt es in nahezu jedes Ausgangsformat — als Datei, als Segment-Stapel (HLS/DASH) oder als Stream zu einem Nachbarn (RTMP/SRT/UDP). `ffprobe` liefert dazu die strukturierte Diagnose, `ffplay` die Sofort-Wiedergabe. Alles ohne Oberfläche, dafür vollständig automatisierbar.

## Vorteile

- **Format-Universalität**: praktisch jede Codec-/Container-Kombination ein- und ausgehend
- **Volle Automatisierung**: ein Aufruf ist ein reproduzierbarer Arbeitsschritt — ideal für Batch und CI
- **Filtergraph als Schweizer Taschenmesser**: Skalieren, Overlay, Wasserzeichen, Loudness-Normalisierung in einem Durchlauf
- **Hardware-Anbindung**: nvenc/qsv/vaapi/videotoolbox machen Echtzeit-Encoding auf günstiger Hardware möglich
- **Überall eingebettet**: OBS, MediaMTX, Ant Media, Restreamer und dutzende Tools nutzen FFmpeg als Backend

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **OBS Studio** | interaktive Regie mit Szenen, Quellen und Mischer; FFmpeg kann nichts umschalten, sondern nur verarbeiten, was man ihm gibt (siehe [obs-studio](../obs-studio/index.md)) |
| **GStreamer** | gleiche Aufgabenklasse, aber als Pipeline-Bibliothek mit gst-Tooling und Graph-Modell; FFmpeg bleibt prozessbasiert mit Argument-Syntax (siehe [gstreamer](../gstreamer/index.md)) |
| **MediaMTX** | Protokoll-Server: nimmt Streams an und verteilt sie; FFmpeg ist dort oft nur das Backend für Relay/Aufnahme (siehe [mediamtx](../mediamtx/index.md)) |
| **Restreamer** | fertige Streaming-Box mit Weboberfläche; FFmpeg ist die darin eingesetzte Transcoding-Engine (siehe [restreamer](../restreamer/index.md)) |
| **Commercial Encoder (TMPGEnc, HandBrake)** | grafische Encode-Oberflächen; HandBrake und viele Converter bauen selbst auf FFmpeg/libav auf |

## Technische Details

- **Projektdach**: FFmpeg-Projekte (ffmpeg.org), Entwicklung über Mailinglisten, regelmäßige Release-Zweige (aktuell 6.x/7.x)
- **Bibliotheken**: libavformat, libavcodec, libavfilter, libswscale, libswresample, libavutil
- **Sprache**: C mit handoptimierten Assembler-Pfaden (x86/ARM)
- **Build-Optionen**: `--enable-gpl`, `--enable-libx264`, `--enable-libfdk-aac` u.v.m. bestimmen den Funktionsumfang
- **Lizenz**: LGPL für den Kern; GPL-Build mit `--enable-gpl`, faktisch GPL sobald GPL-Bibliotheken wie x264/x265 gelinkt werden
- **Plattformen**: Linux, macOS, Windows, BSD, Android/iOS-Ableger, Embedded

## Typische Einsatzmuster

| Muster | Kommando-Skizze |
|--------|-----------------|
| Archiv-Konvertierung | `ffmpeg -i vhs.mkv -c:v libx264 -crf 20 -c:a aac archiv.mp4` |
| HLS-Auslieferung | `ffmpeg -i live.mp4 -f hls -hls_time 6 -hls_playlist_type vod master.m3u8` |
| Lautheit normalisieren | `ffmpeg -i podcast.wav -af loudnorm out.wav` |
| Thumbnail | `ffmpeg -ss 5 -i video.mp4 -frames:v 1 vorschau.png` |
| Stream-Analyse | `ffprobe -of json -show_streams quelle.ts` |

## Charakter

FFmpeg ist bewusst werkzeughaft: kein Assistent, keine Defaults für Geschmacksfragen (Container-Wahl, CRF), keine Fehler-Umwege. Dafür ist jeder Arbeitsschritt exakt reproduzierbar, versionierbar und in Skripte gießbar — was FFmpeg zur Grundlage aller übrigen Streaming-Werkzeuge im Skin-Katalog macht.

## Grenzen im Team

| Punkt | Bedeutung |
|-------|-----------|
| Keine GUI | Einarbeitung für neue Teammitglieder nötig |
| Keine Projektdateien | Einstellungen stecken in jedem Aufruf — Wrapper-Skripte zentralisieren |
| Versionsabhängigkeit | Optionen und EncoderListen unterscheiden sich zwischen 6.x und 7.x |
| Lizenzfrage | LGPL-Bau vs. GPL-Bau (mit x264/x265) vor Weitergabe prüfen |

## Für wen geeignet

- Encoding-Betrieb, Batch-Konvertierung und Archivierung
- FreeSynergy-Skins, die FFmpeg als Verarbeitungs-Engine einbetten (Transcode, Thumbnail, Lautheit)
- Prototyping von Filterketten, bevor sie in OBS/GStreamer nachgebaut werden
- Weniger geeignet für Live-Regie ohne Vorkenntnisse — dafür sind OBS oder der Restreamer die Oberfläche, FFmpeg bleibt dahinter die Engine
