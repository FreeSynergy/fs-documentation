# Synology DSM Dokumentation

## Übersicht

Synology DiskStation Manager (DSM) ist das proprietäre Betriebssystem der Synology-NAS mit einem vollständigen **Desktop-Portal im Browser**: Hauptmenü, Fenster-Verwaltung, App-Leiste, Desktop-Widgets, Paketzentrum und Systemsteuerung. Der Verwaltungs-API-Zugang läuft über `GET/POST /webapi/entry.cgi` mit `SYNO.*`-APIs; Standardports sind **5000 (HTTP)** und **5001 (HTTPS)**.

## Dateistruktur

- [menu.md](menu.md) - Hauptmenü, App-Leiste, Paketzentrum, Rollenmenüs
- [features.md](features.md) - Pakete, Dienste, Rechte, Sicherung, Überwachung
- [description.md](description.md) - Beschreibung und Abgrenzung zu Homarr, Heimdall, Homer, Dashy
- [structure.md](structure.md) - Desktop-Portal, Fenster, Widgets, Themes
- [shortcuts.md](shortcuts.md) - Tasten im Portal und klar als fehlend markierte Kombinationen
- [api.md](api.md) - `entry.cgi`, `SYNO.API.Auth` mit OTP, `SYNO.Core.*`, Session-Handling
