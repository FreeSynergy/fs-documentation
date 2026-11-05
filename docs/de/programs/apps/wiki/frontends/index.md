# Wiki — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Wiki` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Confluence](confluence/index.md) | [latest](confluence/latest/description.md) | Confluence ist eine Enterprise-Wiki-Plattform von Atlassian für Team-Zusammenarbeit. |
| [MediaWiki](mediawiki/index.md) | [latest](mediawiki/latest/description.md) | MediaWiki ist die beliebteste Wiki-Software, die u.a. von Wikipedia verwendet wird. |
| [Notion](notion/index.md) | [latest](notion/latest/description.md) | Notion ist eine All-in-one-Plattform für Notizen, Dokumentation und Zusammenarbeit. |
| [Tango.io](tango.io/index.md) | [latest](tango.io/latest/description.md) | Tango.io ist eine moderne Wissensmanagement-Plattform, die sich auf Zusammenarbeit konzentriert. |
| [VSCodium](vscodium/index.md) | [latest](vscodium/latest/description.md) | VSCodium ist eine Open-Source-Version von Microsoft Visual Studio Code. |
| [Wiki.js](wikijs/index.md) | [latest](wikijs/latest/description.md) | Wiki.js ist ein moderner, leichtgewichtiger Wiki-System basierend auf Node.js. |
| [XWiki](xwiki/index.md) | [latest](xwiki/latest/description.md) | XWiki ist eine leistungsstarke Enterprise-Wiki-Plattform mit erweiterten Funktionen für Wissensmanagement. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/wiki/frontends/<program>/
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
