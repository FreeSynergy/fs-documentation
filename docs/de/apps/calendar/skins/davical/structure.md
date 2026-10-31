# Baïkal/Davical - Struktur und UI/UX

## Systemstruktur

```
Client (Thunderbird/Kalendar/iOS)
        │  HTTPS (Basic-Auth)
        ▼
Reverse Proxy (TLS)
        │
┌───────┴─────────────────────────┐
│ PHP-Anwendung                   │
│ ├── /  → DAV-Endpunkt (dav.php)│   PROPFIND/REPORT/PUT/DELETE
│ ├── /admin/ → Web-Administration│   Benutzer, Kalender, Settings
│ └── Settings/ (config, SQLite)  │
└───────┬─────────────────────────┘
        ▼
MySQL/MariaDB oder SQLite
```

## Admin-Web-UI

```
┌────────────────────────────────────────────────┐
│ Baïkal                      [admin] [logout]   │
├──────────┬─────────────────────────────────────┤
│ Users    │  Benutzerliste (Tabelle)            │
│ Calendars│  ┌────────────────────────────────┐ │
│ Addr-Books│ │ anna   admin ▢  aktiv ✔  [edit]│ │
│ Shares   │ │ ben    admin ▢  aktiv ✔  [edit]│ │
│ Settings │  └────────────────────────────────┘ │
│          │  [+ Add User]                       │
└──────────┴─────────────────────────────────────┘
```

- Schlichte Tabellen-UI, kein Responsive-Layout im Detail — auf Mobilgeräten gut nutzbar, aber nicht optimiert
- Standard-Sprache Englisch; deutsch nicht offiziell übersetzt

## Request-/Speicherstruktur

- Jeder Kalender ist ein DAV-„Collection"-Objekt; jedes Ereignis eine eigene Zeile mit `caldav_data` (ICS-Fragment) + ETag + Sync-Token-Historie
- Änderungen laufen über `PUT`/`DELETE` pro UID — atomare Einzeloperationen

## Deployment-Formen

| Form | Beschreibung |
|------|--------------|
| Klassisch | Apache/nginx + PHP-FPM, Composer-Installation |
| Docker | `ckulka/baikal:nginx` (TLS am Proxy) |
| Shared Hosting | funktioniert wegen reiner PHP-Ausführung oft ohne Shell |

## Accessibility

- Admin-UI: einfache HTML-Tabellen und Formulare, bildschirmleser-tauglich; Kontrast Standard-Bootstrap-artig
- Der Endnutzer-Alltag läuft über Clients — Accessibility hängt dort am jeweiligen Client

## Performance

- `REPORT`-Abfragen mit kleinem Zeitraum bleiben schnell (Index auf Kalender/Zeiten)
- Sehr große Kalender (> 50 MB ICS) bremsen `GET` des Gesamtordners — inkrementelle Sync Token nutzen
