# MistServer - Beschreibung

## Übersicht

MistServer ist ein C++-Streaming-Server, der ohne Datenbanken und ohne Transcoding auskommt: Quellen werden als Streams angemeldet und über aktivierte Protokoll-Connector ausgeteilt. Alles — Oberfläche eingeschlossen — läuft über eine JSON-API.

## Was MistServer macht

MistServer verwaltet benannte Streams mit je einer Quelle (Live-Push, Datei, Ordner, Pull-URL, MPEG-TS/UDP). Aktivierte Connector erzeugen die Ausgangsseite (HTTP, HLS, DASH, WebRTC, RTMP, RTSP, SRT). Automatic-push-Regeln zeichnen auf oder geben an andere Server/Plattformen weiter.

## Vorteile

- **Winziger Footprint**: ein Prozess, keine Laufzeit-Abhängigkeiten, läuft auf schwacher Hardware
- **Alles über eine API**: Interface, Automatisierung und Konfiguration nutzen dieselbe Schnittstelle
- **DVR ab Werk**: Puffer pro Stream, ohne Zusatz-Addon
- **Push als Kernkonzept**: Weiterleitung und Aufnahme folgen demselben Mechanismus
- **Vorhersagbar**: keine versteckten Defaults — wer einen Stream löscht, muss ihn komplett neu melden

## Abgrenzung zu anderen Systemen

### MistServer vs. MediaMTX

- beide ohne Transcoding; MistServer konfiguriert über JSON-API/Oberfläche, MediaMTX über YAML
- MistServer bietet DVR und Automatic-push-Regeln; MediaMTX bietet MoQ, JWT/HTTP-Auth und Prometheus
- MediaMTX ist Single-File-Binary, MistServer hat Connector-Prozesse und Unix-Sockets

### MistServer vs. nginx-rtmp-module

- nginx-rtmp hängt an nginx und braucht ffmpeg-Skripte für alles Weitere; MistServer ist eigenständig
- MistServer kann WebRTC und SRT, nginx-rtmp nicht; nginx-rtmp kann DASH ohne Zusatztool
- Wartungslage: nginx-rtmp seit Jahren ohne wesentliche Entwicklung, MistServer aktiv

### MistServer vs. Ant Media Server

- Ant Media ist eine Plattform (Java/Tomcat) mit Transcoding, Tokens, Cluster und Panel
- MistServer bleibt absichtlich klein: keine Renditions, kein Panel-Komfort, kein Cluster
- Für FreeSynergy-Skins ist MistServer die einfachste Vorlage, Ant Media die funktionsreichste

## Technische Details

- **Backend**: C++, Controller-Prozess plus Connector-Prozesse (HTTP, RTMP, …) über Unix-Sockets
- **Konfiguration**: `config.json` neben dem Binary oder `/etc/mistserver.conf` als Dienst
- **Frontend**: ausgelieferte Single-Page-Oberfläche auf Port `4242`
- **Authentication**: Login mit Challenge-Hash (`MD5(MD5(passwort) + challenge)`); localhost ohne Login
- **Hosting**: Bare-Metal, Docker, VMs; Ports frei wählbar (unter 1024 nur mit Rechten)

## Für wen ist MistServer geeignet?

- kleine bis mittlere eigene Streaming-Instanzen (Verein, Campus, Event)
- Teams, die Konfiguration komplett automatisieren wollen (eine API, keine GUI-Logik)
- Low-Latency-Zuschauerzugriff über WebRTC/HLS ohne Lizenzkosten der Community-Ausgabe
- Nicht geeignet, wenn Transcoding, Multi-Bitrate-Renditions oder DRM gebraucht werden
