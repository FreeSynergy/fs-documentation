# MistServer - Struktur & UI/UX

## Übersicht

MistServer hat eine schlanke Weboberfläche auf Port `4242`, die exakt die API abbildet. Diese Datei beschreibt die Seiten, die Prozessstruktur und die Portlandschaft.

## Fenster-Struktur

### Hauptbereiche

```
┌──────────────────────────── MistServer (Port 4242) ─────────────────────────┐
│ Login (bei Nicht-localhost; localhost wird automatisch autorisiert)        │
├──────────────┬──────────────────────────────────────────────────────────────┤
│ Navigation   │  Content (eine der drei Seiten)                            │
│              │                                                              │
│ Protocol     │  Tabelle der Connector + Spalten: Status, Port, Typ        │
│ Streams      │  Tabelle der Streams + Status, Rechtsklick-Menü            │
│ Push         │  Regeln pro Stream: Ziel, Trigger, Status                  │
│ API-Doku     │  eingebaute Referenz der JSON-Kommandos                    │
└──────────────┴──────────────────────────────────────────────────────────────┘
```

### Prozess- und Socket-Struktur

```
   MistController  ──unix sockets──►  MistIn_<typ>   (Eingang, Decoder)
        │                              MistOut_<typ>  (Ausgang, Muxer)
        │                              MistConnector_* (Protokolle)
        ▼
   config.json  /  /etc/mistserver.conf
```

### Protocol-Seite

- Liste aller aktiven Protokolle mit Port
- „Default protocols" setzt HTTP 8080, HTTPS 4433, RTMP 1935, RTSP 5554, SRT 8889 (udp), WebRTC 18203 (udp)
- Hinweis der Doku: Ports unter 1024 brauchen Admin-Rechte; für dedizierte Server werden 80/443/554 empfohlen

### Streams-Seite

- blaue Einträge = aktiv, aber nicht angelegt (Rechtsklick → anlegen)
- weiße Einträge = konfiguriert; Status zeigt live/verfügbar
- Source-Feld zeigt bei `push://` die konkreten Push-Zieladressen pro Protokoll

### Push-Seite

- zwei Modi: automatic (Regel) und single (einmalig)
- Ziel-Typen als Dropdown, inkl. Datei-Aufzeichnung

## UI/UX

### Design-Prinzipien

- **Tabellen statt Formulare**: alles ist Liste plus Detailseite
- **Rechtsklick statt Buttons**: Stream-Aktionen im Kontextmenü
- **API-Sichtbarkeit**: die API-Doku ist Teil der Oberfläche — Lernpfad vom Klick zum Kommando

### Farbschema

- Standard: dunkle Tabellen, Blau für aktive/blaue Streams, Grau für Inaktives
- Status farbig: live, verfügbar, Fehler

### Interaktionen

- Stream anlegen: Name + Source; Änderungen an Sources ersetzen die Quelle komplett
- Push löschen: entfernt nur die Regel, nicht den laufenden Push
- Stream-Keys: Feld unter den Push-Zielen, Token generieren/ersetzen

## Zugänglichkeit

- Oberfläche ist datenbankartig und tabellarisch → mit Screenreader als Tabelle lesbar
- keine Tastatur-Navigation über Standard hinaus, keine ARIA-Verbesserungen dokumentiert
- Media-Ausgabe (HLS/WebRTC) benötigt eigene Player-Accessibility

## Performance

- pro Protokoll ein eigener Prozess → Ausfall eines connectors betrifft nur diesen
- DVR-Puffer im RAM, Größe pro Stream konfigurierbar (Millisekunden)
- Tracks werden beim ersten Zuschauer dekodiert; VoD-Streams starten bei Bedarf
