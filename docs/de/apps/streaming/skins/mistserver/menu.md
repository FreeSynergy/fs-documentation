# MistServer - Menüpunkte

## Übersicht

MistServer wird über eine eingebaute Weboberfläche auf Port `4242` bedient; diese ist nur ein Client derselben JSON-API. Die Oberfläche hat drei Kernseiten.

## Protocol-Seite

| Element | Inhalt |
|---------|--------|
| Default-Protokolle aktivieren | HTTP, HTTPS, RTMP, RTSP, SRT, WebRTC auf Standard-Ports setzen |
| Connector hinzufügen | Protokoll/Port wählen (HTTP 8080, HTTPS 4433, RTMP 1935, RTSP 5554, SRT 8889/udp, WebRTC 18203/udp) |
| Connector entfernen | Listener deaktivieren |
| Stream-Keys | Token pro Stream statt Streamname im Push-Pfad |

## Streams-Seite

| Element | Inhalt |
|---------|--------|
| Streams-Liste | blau = aktiv aber nicht angelegt, weiß = konfiguriert |
| Rechtsklick auf Stream | Stream-Seite öffnen, löschen, anlegen |
| Neuen Stream anlegen | `Stream name` + `Source` (Datei, Ordner, `push://`, `srt://:port`, `tsudp://ip:port`, `http://…m3u8`) |
| Push-Protokolle anzeigen | unter dem Source-Feld: RTMP-, SRT-, RTSP-, WebRTC- und WHIP-Zieladresse |
| Tracks | Video-/Audio-/Daten-Spuren eines Streams einsehen |

## Push-Seite

| Element | Inhalt |
|---------|--------|
| Automatic push | Regel: bei Stream-Aktivität (oder Zeit/Variable) automatisch pushen/aufzeichnen |
| Single push | einmaligen Push sofort starten |
| Target-Typ | RTMP, SRT, RTSP, WebRTC oder lokale Datei (Aufzeichnung) |
| Track-Auswahl | welche Video-/Audio-Spur gepusht wird (Standard: letzte kompatible) |
| Variablen | Ersetzungen für Streamname, Zeit, Datum im Ziel |

## Menüs nach Rolle

| Rolle | Zugriff |
|-------|---------|
| localhost | ohne Login vollen Zugriff (Automatik-Erkennung) |
| Admin (Benutzer) | nach Login alle drei Seiten, alle API-Kommandos |
| Erststart ohne Konto | `NOACC`-Zustand: lokales Konto über API/Oberfläche anlegen |
| Zuschauer | nur Media-Ports (nicht 4242) |
