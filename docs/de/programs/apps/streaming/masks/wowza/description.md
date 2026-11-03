# Wowza Streaming Engine - Beschreibung

## Was das Programm macht

Wowza Streaming Engine ist ein professioneller Medienserver zum Selbstbetrieben: Er empängt Live-Streams von Encodern, verarbeitet sie (Transcoding, Aufzeichnung, Packaging) und liefert sie in allen gängigen Formaten an Browser, Apps und Endgeräte. Verwaltung, Überwachung und Automatisierung geschehen über Manager-Oberfläche, REST API und XML-Konfiguration.

## Vorteile

- **Protokoll-Breite**: ein Server für RTMP-Eingang und HLS/DASH/CMAF/Smooth-Ausgang
- **Produktionsreif**: nDVR, Time Shift, Live Repeater, Load Balancer, DRM —Features, die große Live-Übertragungen brauchen
- **Automatisierbar**: vollständige REST Server API v2 für Betriebsskripte
- **Kommerzieller Support**: dokumentierte Software mit Support-Kanal (keine Community-only-Basis)

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **nginx + nginx-rtmp-module** | kostenloser DIY-Baukasten ohne Manager, Transcoding und DRM. |
| **Restreamer** | fertig eingepackter Klein-Server für einen Stream; Wowza skaliert und differenziert pro Anwendung. |
| **MediaMTX** | schlanker Go-Router für Protokolle; ohne Transcoder-Workflows und DRM. |
| **MistServer** | deutlich leichter und ebenfalls kommerziell; Wowza hat das breitere Add-on-/Skalierungs-Ökosystem. |
| **Ant Media Server** | ähnlich professionell, stärker auf WebRTC/Cluster ausgerichtet; Wowza stärker bei klassischen Broadcast-Workflows. |
| **Restream (SaaS)** | fertiger Multistream-Dienst ohne eigene Server; Wowza ist die eigene Infrastruktur. |

## Technische Details

- **Basis**: Java-Prozess (JVM), Installationsverzeichnis `/usr/local/WowzaStreamingEngine` (Linux) bzw. Programmverzeichnis (Windows)
- **Ports (Voreinstellung)**: 1935 (RTMP), 8086 (HTTP-Streaming), 443 (HTTPS/RTMPS), 8087 (REST API), 8088 (Manager HTTP), 8090 (Manager HTTPS) — alle konfigurierbar
- **Konfiguration**: `conf/VHosts.xml`, je Virtual Host `VHost.xml`, je Anwendung `Application.xml` u. a.
- **Lizenz**: kostenpflichtige Instanzlizenz (Test-/Abomodelle des Herstellers)
- **Plattformen**: Linux und Windows, Docker-Images verfügbar

## Für wen geeignet

- Berufliche Veranstalter, Rundfunk-nahe Workflows und Video-Portale mit eigenen Servern
- FreeSynergy-Streaming-Skins, die professionelle Server-Modelle (Virtual Host → Anwendung → Stream) abbilden sollen
- Teams, die DRM, Multi-Bitrate und skalierbare Verteilung selbst betreiben wollen
