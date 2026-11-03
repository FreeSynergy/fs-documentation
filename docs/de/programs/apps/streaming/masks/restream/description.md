# Restream - Beschreibung

## Übersicht

Restream ist ein kommerzieller Multistreaming-Dienst: Er nimmt einen Stream an und verteilt ihn gleichzeitig an viele Plattformen. Dazu gibt es Browser-Studio, einheitlichen Chat, Event-Planung und Analyse — ohne eigene Infrastruktur.

## Was Restream macht

Ein Encoder (OBS, ffmpeg) oder das Restream Studio sendet einen Stream an die im Dashboard genannte Ingest-Adresse. Restream kopiert diesen Stream zu allen verbundenen Zielen, bündelt die Chats der Plattformen, zeichnet auf und misst Zuschauerzahlen. Der Dienst skaliert die Verteilung selbst.

## Vorteile

- **Sofort startklar**: keine Server, keine TLS-Zertifikate, keine Ports
- **Plattform-Kopplung per Login** statt Stream-Key-Raten
- **Studio im Browser** — Produktion ohne lokale Encoder-Hardware
- **Chat aus einer Hand** über alle Plattformen hinweg
- **Analytik inklusive** statt selbst gebaut

## Abgrenzung zu anderen Systemen

### Restream vs. Docker-Restreamer

- der Restreamer ist **selbst gehostet** (nginx-rtmp + Webui) und verteilt an eigene Ziele
- Restream ist SaaS: mehr Komfort, aber Datenhoheit und Konfigurationszugriff entfallen
- Kostenmodell: Abo-Pläne statt Infrastrukturkosten

### Restream vs. Wowza / Ant Media Server

- Wowza und AMS sind **Server-Software** (Plattform zum Selbstbetreiben, inkl. Transcoding und API)
- Restream bietet kein Transcoding-Setup und keinen Serverzugriff, dafür sofortige Plattformanbindung
- Wer White-Label oder eigene Infrastruktur braucht, wählt Wowza/AMS/MediaMTX

### Restream vs. direkte Plattform-Ingests

- statt getrennter Upstream-Keys pro Plattform nur **ein** Ingest
- dafür Abhängigkeit von einem Drittanbieter und dessen Verfügbarkeit
- Plattform-Features (z. B. Superchats) bleiben bei der Zielplattform

## Technische Details

- **Backend**: geschlossene SaaS-Infrastruktur des Anbieters
- **Database**: nicht einsehbar; Kontodaten, Ziele, Events im Konto
- **Frontend**: Web-Dashboard und Studio (Browser), eingebetteter Player
- **Authentication**: Konto-Login (E-Mail/Passwort, 2FA); APIs mit OAuth-Zugangs-Token
- **Hosting**: ausschließlich beim Anbieter — kein Selbstbetrieb möglich

## Für wen ist Restream geeignet?

- Creator und kleine Teams, die ohne Infrastruktur-Aufwand auf viele Plattformen gleichzeitig senden wollen
- Events mit Browser-Produktion und Gäste-Einladung
- Weniger geeignet für: datenschutzgetriebene Setups, White-Label-Produkte, Protokoll-/Port-Kontrolle oder sehr lange Streaming-Zeiten (Plan-Grenzen)
