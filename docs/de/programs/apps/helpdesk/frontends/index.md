# Helpdesk — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Helpdesk` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Freshdesk](freshdesk/index.md) | [latest](freshdesk/latest/description.md) | Freshdesk (Freshworks) ist ein SaaS-Helpdesk mit Tickets, Knowledge Base, SLAs, Omnichannel-E-Mail/Telefon/Chat und Freddy-KI. |
| [GLPI](glpi/index.md) | [latest](glpi/latest/description.md) | GLPI ist ein französisch geprägtes Open-Source-ITSM: Helpdesk-Tickets plus vollständige IT-Asset-Verwaltung (Rechner, Software, Verträge, Netzwerk), projekt- und budgetfähige Reportings. |
| [Helodesk](helodesk/index.md) | [latest](helodesk/latest/description.md) | Helodesk ist eine französische SaaS-Kundenservice-Suite (Kontaktcenter): Telefonie/Softphone, E-Mail, Chat, SMS und Callback in einer Oberfläche, dazu Cases (Tickets), Wissensdatenbank, IVR und Rep… |
| [Help Scout](helpscout/index.md) | [latest](helpscout/latest/description.md) | Help Scout ist Support als gemeinsames Postfach: Kunden schreiben an eine E-Mail-Adresse („Conversations“), das Team antwortet wie aus einer persönlichen Mail — ohne Ticketnummern-Gefühl. |
| [osTicket](osticket/index.md) | [latest](osticket/latest/description.md) | osTicket ist der Klassiker unter den Open-Source-Helpdesks: PHP/MySQL, E-Mail-Ingest, Help Topics, Filterregeln und ein schlichtes Agenten- bzw. |
| [Request Tracker (RT)](request-tracker/index.md) | [latest](request-tracker/latest/description.md) | Request Tracker von Best Practical ist der Veteran der Ticketsysteme: Perl-basiert, extrem regexp-/skriptgetrieben, mit REST 1.0 und JSON-RPC 2.0 API. |
| [Zammad](zammad/index.md) | [latest](zammad/latest/description.md) | Zammad ist ein moderner, quelloffener Helpdesk: Tickets aus E-Mail, Web-Formular, Chat, Telefon und Telegram laufen in einer Oberfläche zusammen, mit SLAs, Textbausteinen, Wissensdatenbank und eine… |
| [Zendesk](zendesk/index.md) | [latest](zendesk/latest/description.md) | Zendesk ist die kommerzielle Support-Plattform (SaaS) mit Tickets, Help Center, Chat/Messaging, Voice und Analytics. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/helpdesk/frontends/<program>/
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
