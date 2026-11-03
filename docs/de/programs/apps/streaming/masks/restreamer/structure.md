# Restreamer - Struktur und UI/UX

## Übersicht

Der Restreamer besteht aus drei Prozessen in einem Docker-Container (nginx mit nginx-rtmp-module, Node.js-Webui, ffmpeg) und einer einzigen Weboberfläche. Diese Datei beschreibt Webui-Masken, Player-Einbettung und Prozess-/Portstruktur.

## Webui (Standard-Layout)

```
┌────────────────────────────────────────────────────────────────────┐
│ Restreamer                                    [language] [logout]  │
├───────────────┬────────────────────────────────────────────────────┤
│ Menü          │  Inhalt der gewählten Maske                        │
│ ▸ Start       │   Start: Status-Banner (Stream offline/online),    │
│   Push Key    │   Player-Vorschau, Statistik (Zuschauer, Bitrate), │
│   Player      │   Kurzbefehle für Push-/Play-URLs                  │
│   Settings    │   Push Key: Schlüssel anzeigen/kopieren/neu        │
│   Advanced    │   Player: Vorschauspieler, Direktlinks,            │
│   Logs        │            Einbettungs-Snippet                     │
│               │   Settings / Advanced: Formulare (siehe menu.md)   │
└───────────────┴────────────────────────────────────────────────────┘
```

- Masken sind einfache Formulare bzw. Info-Panels; Aktionen immer als Buttons in der Maske
- Status (laufender Stream ja/nein) oben auf der Start-Maske, zusätzlich farbig (grün = live)

## Prozess- und Portstruktur

```
Docker-Container "restreamer"
 ├── nginx + nginx-rtmp-module   RTMP-Empfang :1935, HLS-Auslieferung :8080
 ├── Node.js-Webui               Admin-Oberfläche + interne API :8080/:8081
 └── ffmpeg                      Transcoding und Segment-Aufzeichnung (on_demand)
```

- Persistenz über Volumes: `/opt/restreamer/var/media` (Segmente), `/var/statistics`
- HTTPS (Port 8081) mit selbst erzeugtem Zertifikat, abschaltbar

## Player-Einbettung

- Die Player-Maske zeigt ein fertiges `<iframe>`-Snippet (HLS-Player) zum Kopieren; Größe per Attribute anpassbar
- Alternativ Direktdirektlinks: HLS-Playlist (`…/hls/stream.m3u8`) und MP4-Segmente zum Download
- Einbettung funktioniert in jeder Webseite/FreeSynergy-Gallery-Maske, da nur HTTP benötigt wird

## UI/UX

- Schlichtes Hell-Dunkel-Layout ohne Theme-Optionen; die Webui ist funktional, nicht gestaltbar
- Jede Maske enthält Erklärtexte direkt über den Feldern (Self-Service ohne Doku-Studium)
- Gefahrlose Aktionen (Push Key neu generieren) mit Sicherheitsabfrage

## Interaktionen

- Konfiguration fast ausschließlich über Formulare; Speichern wirkt nach Neustart des Containers
- Logs einsehbar, aber ohne Live-Streaming der Logs in der UI (Download/Support-Paket)

## Responsive Design

| Plattform | Verhalten |
|-----------|-----------|
| Desktop-Browser | volles Layout mit festem Seitenmenü |
| Mobil-Browser | Menü einklappbar, Formulare einspaltig |
| native Apps | ❌ keine (Zugriff nur per Browser) |

## Accessibility

- Einfache HTML-Formulare, Tab-Reihenfolge gegeben; Screenreader-getestet nur eingeschränkt (⚠)
- Status nicht nur farbig, sondern auch als Text ("online"/"offline")
- Keine offiziellen Shortcuts (siehe [shortcuts.md](shortcuts.md))

## Performance

- Eine Push-Quelle, beliebig viele HLS-Leser; Skalierung über nginx-Worker und CDN vor dem Player
- Transcoding optional — ohne ffmpeg-Profil läuft der Stream mit Minimal-CPU
