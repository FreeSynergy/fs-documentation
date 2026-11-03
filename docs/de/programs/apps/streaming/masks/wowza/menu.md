# Wowza Streaming Engine - Menüpunkte

## Übersicht

Alle Bedienung läuft über den **Wowza Streaming Engine Manager** (`http://<host>:8088`, HTTPS `:8090`). Der Manager ist eine schlanke Web-App: Server-Menü links, Detailseiten rechts. Die darunterliegende Konfiguration liegt in XML-Dateien; Manager-Seiten sind meist direkte Masken darauf.

## Server-Menü (linker Bereich)

| Menüpunkt | Beschreibung |
|-----------|--------------|
| Login | Benutzername/Passwort (Konten in `managernames.properties`) |
| Applications | Liste aller Anwendungen einer Virtual Host; Auswahl öffnet die Application-Seite |
| Add Application | Assistent: Name + Typ (z. B. Live, Live and VOD, VOD) |
| Streaming Publishers | aktive Einspeiser; Publisher sperren/freigeben (Publisher Control) |
| Connections | aktive Zuschauer-/Playerverbindungen mit IP, Stream, Dauer |
| Restart | Server oder einzelne Anwendung neu starten |
| Log Viewer | Live-Ausschnitt aus `wowzastreamingengine_error.log` |
| Server-Name/Logout | oben: Instanzname, Lizenzstatus, Abmelden |

## Je Anwendung (Reiter auf der Application-Seite)

| Reiter | Beschreibung |
|--------|--------------|
| Playback Options | fertige Wiedergabe-URLs (HLS, DASH, Smooth, RTMP, CMAF) zum Kopieren |
| Properties | formularbasierte Bearbeitung der `Application.xml` (Aufzeichnung, DVR, Timing …) |
| Security | Hash-Key-/Token-Prüfungen für Play und Publish konfigurieren |
| Stream Targets | Weiterleitung des Eingangs an externe RTMP-Ziele (Name + URL/Schlüssel) |
| Restart Application | nur diese Anwendung neu starten |

## Kontext-Menüs

- ❌ keine Rechtsklick-Kontextmenüs — alle Aktionen sind Buttons/Links in Tabellen (⚠ Manager ist bewusst einfach)
- Stream-/Verbindungszeilen enthalten direkt ihre Aktionen (z. B. Blockieren bei Publishern)

## Menüs nach Benutzerrolle

| Rolle | sichtbar |
|-------|----------|
| Manager-Konto (admin) | alle Menüs |
| weitere Konten | gleicher Funktionsumfang wie das admin-Konto; fein granulare Rollen ❌ |
| REST-API-Nutzer | kein Menü — gleiche Konten wie Manager, Zugriff nur auf API |

## Hinweis

Die genauen Menü-/Reiternamen variieren leicht mit der Engine-Version (4.x); maßgeblich ist die installierte Version.
