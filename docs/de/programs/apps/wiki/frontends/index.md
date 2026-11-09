# Wiki — Frontends

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weithin bekannt ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm für diese Kategorie ist `FreeSynergy.Wiki` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [Anforderungen](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Confluence](confluence/index.md) | [latest](confluence/latest/description.md) | Confluence ist eine Team-Wiki- und Kollaborationsplattform von Atlassian. |
| [MediaWiki](mediawiki/index.md) | [1.46](mediawiki/1.46/description.md), [latest](mediawiki/latest/description.md) | MediaWiki ist die Wiki-Engine hinter Wikipedia und den anderen Wikimedia-Projekten. |
| [Notion](notion/index.md) | [2026-11-07](notion/2026-11-07/description.md), [latest](notion/latest/description.md) | Notion ist ein gehosteter All-in-one-Arbeitsbereich für Notizen, Dokumente und Datenbanken, aufgebaut aus typisierten Blöcken. |
| [Tango](tango/index.md) | [latest](tango/latest/description.md) | Tango macht aus aufgezeichneten Klicks Schritt-für-Schritt-Anleitungen; kein Wiki, dokumentiert wegen der Idee von der Aufzeichnung zur Anleitung. |
| [Tango.io](tango.io/index.md) | [latest](tango.io/latest/description.md) | Tango.io ist eine moderne Wissensmanagement-Plattform mit Schwerpunkt auf Zusammenarbeit. |
| [VSCodium](vscodium/index.md) | [latest](vscodium/latest/description.md) | VSCodium ist eine Open-Source-Version von Microsoft Visual Studio Code. |
| [Wiki.js](wikijs/index.md) | [3.1.1](wikijs/3.1.1/description.md), [latest](wikijs/latest/description.md) | Wiki.js ist eine Open-Source-Wiki-Engine zum Selbsthosten. |
| [XWiki](xwiki/index.md) | [latest](xwiki/latest/description.md) | XWiki ist eine leistungsstarke Enterprise-Wiki-Plattform mit erweiterten Funktionen für Wissensmanagement. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/wiki/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es geeignet ist
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastenkürzel
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie sind unter [data](../../../../data/standards.md) beschrieben.
