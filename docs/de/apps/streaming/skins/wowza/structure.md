# Wowza Streaming Engine - Struktur und UI/UX

## Übersicht

Wowza besteht aus Medienprozess und Manager-Webapp. Diese Datei beschreibt das Manager-Layout, die Konfigurationshierarchie und die Portstruktur.

## Fenster-Struktur (Manager)

### Hauptbereiche

```
┌──────────────────────────────── Wowza Streaming Engine Manager ─────────────────────┐
│ Wowza-Logo │ Instanzname │ Lizenzhinweis                    angemeldet │ Logout      │
├──────────────────┬──────────────────────────────────────────────────────────────────┤
│ Menü             │  Content (gewählte Ebene)                                        │
│                  │                                                                  │
│ Applications     │  Applications: Tabelle der Apps (Name, Typ, Status, Neustart)    │
│  Add Application │  Streaming Publishers: aktive Einspeiser + [Block]               │
│ Streaming        │  Connections: Zuschauer (IP, Stream, Dauer) + [Disconnect]       │
│  Publishers      │  Connections: Portliste (RTMP 1935, HTTP 8086 …)                 │
│ Connections      │  Application-Detail: Reiter Playback Options / Properties /      │
│ Restart          │                  Security / Stream Targets / Restart Application │
│ Log Viewer       │  Log Viewer: rollendes Log-Fenster                               │
└──────────────────┴──────────────────────────────────────────────────────────────────┘
```

### Konfigurationshierarchie

```
Instanz (WowzaStreamingEngine-<version>)
 ├── conf/VHosts.xml                      Virtual Hosts registrieren
 ├── [vhost]/VHost.xml                    Ports, Handler, Limits
 │    └── [app]/Application.xml           Verhalten je Anwendung (DVR, Sicherheit…)
 │         └── [stream]/Stream.xml        einzelne Streams (laufzeitgeneriert)
 ├── TranscoderTemplates.xml              Bitrate-Leitern
 └── logs/                                access-/error-Logs
```

### Portstruktur (Voreinstellung)

```
Medien   RTMP/RTMPS   :1935 / :443
         HTTP-Play    :8086   HTTPS-Play :443
Verwaltung Manager     :8088   Manager HTTPS :8090
         REST API      :8087
```

## UI/UX

- Manager ist funktional und textlastig; Tabellen + Formulare, keine Dashboards/Diagramme
- Standard-Klassisches Layout, helle Oberfläche
- Gefährliche Aktionen (Restart, Block) als bestätigungsbehaftete Buttons

## Interaktionen

- Application anlegen über Assistent (Name, Typ) — danach sofort playback-fähig
- Properties-Maske schreibt beim Speichern direkt in `Application.xml`
- „Playback Options“ zeigt alle Wiedergabe-URLs des Streams zum Kopieren

## Responsive Design

| Plattform | Verhalten |
|-----------|-----------|
| Desktop-Browser | volles Layout |
| Mobil-Browser | Manager skaliert einfach (Tabellen schmal), ❌ kein dediziertes Mobil-Layout |
| native Apps | ❌ keine |

## Accessibility

- Einfache HTML-Tabellen/-Formulare; Tab-Reihenfolge gegeben, aber nicht auditiert (⚠)
- Status textlich (running/not started) und farbig
- Log Viewer als reiner Textbereich (gut screenreader-tauglich)

## Performance

- JVM-Heap über Startskripte einstellbar; Transcoding skaliert mit CPU-Kernen
- Origin/Edge-Trennung (Live Repeater) hält Zuschauerlast von Einspeisung/Transcoding getrennt
- Log Viewer zeigt nur Ausschnitt — lange Historie bleibt in Logdateien
