# OBS Studio - Beschreibung

## Was das Programm macht

OBS baut aus Quellen (Fenster, Kamera, Audio, Dateien) eine Szene, schaltet zwischen Szenen um und liefert das Ergebnis als Aufnahme oder Live-Stream zu einer Plattform. Es ist Regiepult und Encoder in einem.

## Vorteile

- **kostenlos und quelloffen** (GPLv2), Windows/macOS/Linux
- **extrem flexibel**: jede Quelle hat Filter, jede Szene Übergänge, jeder Kanal Filter
- **Steuerbar von außen** über obs-websocket — ideal für Automatisierung und Skin-Anbindung
- **riesige Community**: Anleitungen, Plugins, Szenen-Sammlungen

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Restreamer / MediaMTX / nginx-rtmp** | Serverseitige Aufnahme und Weitergabe; OBS ist die Client-Seite mit Bildmischung. |
| **Restream (SaaS)** | Multi-Streaming und Chat-Bündelung im Browser; OBS liefert den Ton/Bild, Restream verteilt. |
| **GStreamer / ffmpeg** | Programmier-Werkzeuge ohne Oberfläche; OBS ist die GUI darüber. |
| **vMix / StreamYard** | kommerziell; vMix nur Windows, StreamYard browserbasiert ohne lokale Aufnahmequalität. |

## Technische Details

- **Kern**: libobs (C/C++), Grafik via DirectX/OpenGL/Metal, Audio via PulseAudio/WASAPI/CoreAudio
- **Encoder**: x264, AV1 (SVT-AV1), NVENC, AMF, QSV, VideoToolbox
- **Profile/Szenen**: JSON-artige Sammlungen (`~/.config/obs-studio`), portabel
- **Fernsteuerung**: obs-websocket 5 (JSON über WebSocket, Auth mit Passwort)
- **Formate**: Ausgabe bis 4096×2160, 60 fps und höher, Mehrtonspuren
- **Lizenz**: GPLv2+

## Für wen geeignet

- Einzel-Produktion von Aufnahmen und Streams (Vortrag, Gaming, Schulung)
- FreeSynergy-Streaming-Skins mit Modell Szene / Quelle / Encoder / Ziel
- Automatisierte Aufnahme-Ketten über WebSocket (z. B. Start aus FreeSynergy-Kalender)
