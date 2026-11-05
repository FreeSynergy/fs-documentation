# Messenger — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Messenger` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Discord](discord/index.md) | [latest](discord/latest/description.md) | Discord ist eine proprietäre Communication-Plattform für Gaming-Communities, mit Voice/Video und Server-Struktur. |
| [Element](element/index.md) | [latest](element/latest/description.md) | Element ist der Open-Source-Messenger für das Matrix-Protokoll, mit dezentraler Architektur und End-to-End-Verschlüsselung. |
| [Kontact](kontact/index.md) | [latest](kontact/latest/description.md) | Kontact ist die integrierte PIM-Anwendung für KDE, die E-Mail, Kalender, Kontakte, Aufgaben und Notzen in einer einzigen Anwendung vereint. |
| [Mastodon](mastodon/index.md) | [latest](mastodon/latest/description.md) | Mastodon ist ein Open-Source-Mikroblogging-Netzwerk, das auf ActivityPub-Protokoll basiert und dezentral ist. |
| [Outlook](outlook/index.md) | [latest](outlook/latest/description.md) | Outlook ist der beliebteste E-Mail-Client von Microsoft, Teil von Microsoft 365. |
| [Telegram](telegram/index.md) | [latest](telegram/latest/description.md) | Telegram ist ein cloud-basierter Messenger mit Fokus auf Geschwindigkeit, große Gruppen/Kanäle und Verschlüsselung. |
| [Thunderbird](thunderbird/index.md) | [latest](thunderbird/latest/description.md) | Thunderbird ist der quelloffene E-Mail-Client von Mozilla, plattformunabhängig und E-Mail-Fokus. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/messenger/frontends/<program>/
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
