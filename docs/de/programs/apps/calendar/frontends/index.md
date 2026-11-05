# Calendar — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Calendar` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [DAViCal](davical/index.md) | [latest](davical/latest/description.md) | DAViCal ist ein CalDAV-/CardDAV-Server in PHP auf PostgreSQL – ein schlanker, protokolltreuer Self-Hosted-Kalender-/Kontaktspeicher mit Web-Administration. |
| [Google Kalender](google-calendar/index.md) | [latest](google-calendar/latest/description.md) | Google Kalender (calendar.google.com) ist Googles Kalender-Dienst: Web-Oberfläche und Apps für Android, iOS, Wear OS und Apple Watch, gekoppelt mit Gmail, Meet, Tasks und (mit Premium-Abo) Gemini. |
| [Merkuro Calendar](merkuro/index.md) | [latest](merkuro/latest/description.md) | Merkuro Calendar ist der moderne Kalender-Client der KDE-Desktop-Umgebung (Qt 6/QML/Kirigami, konvergent auf Desktop und Plasma Mobile). |
| [Nextcloud Calendar](nextcloud-calendar/index.md) | [latest](nextcloud-calendar/latest/description.md) | Die Kalender-App des Nextcloud-Servers: eine Weboberfläche (Vue 3 + FullCalendar) über dem CalDAV-Backend (sabre/dav) des Nextcloud-Servers. |
| [Outlook-Kalender](outlook-calendar/index.md) | [latest](outlook-calendar/latest/description.md) | Kalenderkomponente der Microsoft-Outlook-Linie: Web-App (outlook.com / Outlook on the web), neues und klassisches Outlook für Windows, Outlook für Mac und iOS/Android – Daten im Postfach von Exchan… |
| [GNOME Planner](planner/index.md) | [latest](planner/latest/description.md) | Planner ist der Projektplaner unter GNOME (App-ID `app.drey.Planner`): Vorgänge mit Anfang/Ende, Aufwand, Kosten und Abhängigkeiten (FS/SS/FF/SF mit Lag), Ressourcen mit eigenen Arbeitskalendern, k… |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/calendar/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
