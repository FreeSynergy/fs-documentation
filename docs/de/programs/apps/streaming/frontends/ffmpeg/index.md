# FFmpeg Dokumentation

> Kategorie: [streaming](../../index.md)

## Übersicht

FFmpeg ist die Kommandozeilen-Werkzeugsammlung der FFmpeg-Projekte: `ffmpeg` transcodiert, muxed/demuxed und filtert Medien, `ffprobe` analysiert Dateien maschinenlesbar, `ffplay` spielt sie als einfacher SDL-Player ab. Der Technik-Stack ist reines C (libavformat, libavcodec, libavfilter, libswscale, libswresample) mit Build-Optionen für x264/x265, AV1, Opus und Hardware-Beschleunigung (NVENC, QSV, VAAPI, VideoToolbox). FFmpeg ist primär eine CLI — es gibt keine grafische Oberfläche; Bedienung, Automatisierung und Integration laufen über Argumente, Exit-Codes und Statusströme. Lizenziert ist der Kern unter LGPL, mit GPL-Baubarkeit (und de-facto GPL, wenn GPL-Code wie x264 einkompiliert wird). Aktuelle Standlinien sind die 6.x- und 7.x-Reihen (ffmpeg.org).

## Bemerkenswerte Ideen

_Zu tun: Was kann dieses Programm, das andere nicht können? Warum ist es hier dokumentiert (ADR 0013)?_

## Dokumentierte Versionen

<!-- gen:versions (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 0/7 |

### latest

| Datei | Inhalt |
|------|----------|

⚠️ Fehlende Pflichtdateien: `description.md`, `features.md`, `layout.md`, `menus.md`, `shortcuts.md`, `api.md`, `themes/index.md`
<!-- /gen:versions -->

## Einordnung im System

FFmpeg ist die darunterliegende Engine vieler anderer Werkzeuge: [OBS Studio](../obs-studio/index.md) nutzt es für Aufnahmen, [MediaMTX](../mediamtx/index.md) und Ant Media Server setzen es als Backend für ffmpeg-basierte Pfade ein, der [Restreamer](../restreamer/index.md) transkodiert damit auf Wunsch, und [GStreamer](../gstreamer/index.md) ist die grafisch-orientierte Pipeline-Alternative mit eigener API.

| Merkmal | Wert |
|---------|------|
| Projekt | FFmpeg-Projekte, ffmpeg.org |
| Sprache | C (Assembler-Optimierungen für gängige Architekturen) |
| Werkzeuge | `ffmpeg`, `ffprobe`, `ffplay` (`ffserver` eingestellt/entfernt) |
| Versionen aktuell | 6.x / 7.x |
| Lizenz | LGPL (Kern), GPL-möglicher Build, GPL faktisch mit x264/x265 |
| Plattform | Linux, macOS, Windows, BSD, eingebettete Systeme |
