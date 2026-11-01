# Ant Media Server - Beschreibung

## Übersicht

Der Ant Media Server ist eine ausgewachsene Streaming-Plattform: Java/Tomcat-Prozess mit RTMP-, RTSP-, SRT- und WebRTC-Empfang, eingebautem Transcoding und Multi-Bitrate-Packaging, Panel und REST-API. Freie Community- und kostenpflichtige Enterprise-Ausgabe.

## Was der Ant Media Server macht

Streams werden über Anwendungen (`live`, `WebRTCAppEE`, eigene) empfangen. Der Server transkodiert bei Bedarf in mehrere Stufen, verpackt in HLS/WebRTC/DASH, zeichnet auf und stellt Playlists bereit. Cluster-Knoten (Origin/Edge) skalieren Zuschauerlast. Alles, was das Panel zeigt, ist REST-aufrufbar.

## Vorteile

- **Alles aus einer Hand**: Ingest, Transcoding, Packaging, Aufnahme, Tokens, Cluster
- **Ultra-Low-Latency** via WebRTC mit SDKs für Web, Android, iOS
- **Automatisierbar**: vollständige REST-v2-Abdeckung (Broadcasts, VoD, Management, Cluster)
- **Produktionsreif**: Cloud-Images, Redis-Cluster, Monitoring, kommerzieller Support
- **Einstieg frei**: Community-Edition unter MIT-Lizenz

## Abgrenzung zu anderen Systemen

### Ant Media Server vs. Wowza Streaming Engine

- beide Plattformen mit Panel und Transcoding; Wowza kommerziell mit Lizenzkosten, AMS mit freier Basis
- Wowza punktet bei RIST, breiter DRM-Unterstützung und Addon-Ökosystem
- AMS punktet bei WebRTC-SDKs, Cloud-Skalierung und freier REST-API-Abdeckung

### Ant Media Server vs. MediaMTX

- MediaMTX ist bewusst schlank (Go, kein Transcoding, YAML, Control-API)
- AMS bringt Transcoding, Tokens, VoD-Bibliothek und Panel mit — deutlich mehr Komplexität und Ressourcenbedarf
- Für FreeSynergy-Skins: MediaMTX als simpler Knoten, AMS als Plattform-Vorlage

### Ant Media Server vs. MistServer

- MistServer ohne Transcoding, dafür winzig und komplett API-getrieben
- AMS ist schwerer (Java, Tomcat), dafür mit Adaptive Bitrate und Cluster
- Lizenzmodelle unterscheiden sich deutlich (GPL vs. MIT/Enterprise)

## Technische Details

- **Backend**: Java (Servlet-Container Tomcat), Ingest-Mediathek auf FFmpeg-Basis, In-Memory-Statistiken
- **Database**: Derby/PostgreSQL für App-Metadaten, Redis für Cluster-Zustand
- **Frontend**: Web-Panel (JavaScript) auf `5080`/`5443`
- **Authentication**: Panel-Login, REST über IP-Filter oder JWT, Medien über Publish-/Play-Token
- **Hosting**: Bare-Metal, Docker, VMs, AWS/Azure/GCP-Marktplatzimages, Kubernetes-tauglich

## Für wen ist der Ant Media Server geeignet?

- Teams, die eine **komplette Streaming-Plattform** (Transcoding + Packaging + Tokens + Cluster) selbst betreiben wollen
- WebRTC-Produkte mit sehr niedriger Latenz (Video-Apps, Events, Auktionen)
- FreeSynergy-Architekturen, die eine Referenz für „Streaming als Plattform" brauchen
- Weniger geeignet als Nebenkomponente auf kleiner Hardware — dafür MediaMTX/MistServer
