# Owncast - Beschreibung

## Was das Programm macht
Owncast betreibt eine persönliche Live-Streaming-Seite. Die Streamerin oder der Streamer richtet die Sendesoftware (das README nennt OBS, Streamlabs und Restream als Beispiele) auf den Server; Zuschauende sehen im Browser zu und chatten. Ein Administrationsbereich konfiguriert den Server.

## Vorteile
- Selbst gehostet, MIT-Lizenz, ein Binär-Stack mit ffmpeg.
- Chat inklusive; kein separater Dienst.
- Optionales Folgen im Fediverse.

## Abgrenzung
| System | Unterschied |
|--------|-------------|
| PeerTube | Plattform für viele Nutzende mit Uploads und Föderation von Videos; Owncast ist ein Server für eine einzelne Person. |
| MediaMTX, nginx-rtmp-module | Medienrouter ohne Chat und ohne Zuschauerseite. |

## Technische Details
Backend in Go (das README verlangt eine aktuelle Go-Version, einen C-Compiler und ffmpeg); Frontend in React. Speicheroptionen: offen.
