# Surveys — Frontend-Dokumentation

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Surveys` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Consul Democracy](consul/index.md) | [latest](consul/latest/description.md) | Consul Democracy ist Open-Source-Software für die Bürgerbeteiligung durch Regierungen und Organisationen: Debatten, Vorschläge, Abstimmungen, Bürgerhaushalt, gemeinsame Gesetzgebung und Umfragen. |
| [Decidim](decidim/index.md) | [latest](decidim/latest/description.md) | Decidim ist eine Plattform für partizipative Demokratie, gestartet vom Rathaus Barcelona. |
| [LiquidFeedback](liquidfeedback/index.md) | [latest](liquidfeedback/latest/description.md) | LiquidFeedback ist Open-Source-Software für die Entwicklung von Vorschlägen und die Entscheidung online, herausgegeben von der Public Software Group (Berlin) unter der MIT-Lizenz. |
| [Loomio](loomio/index.md) | [latest](loomio/latest/description.md) | Loomio ist Open-Source-Software für gemeinsame Entscheidungen in Gruppen: Kontext teilen, diskutieren, Rückmeldungen sammeln, abstimmen und das Ergebnis festhalten. |
| [Polis](polis/index.md) | [latest](polis/latest/description.md) | Polis ist eine Open-Source-Plattform, um bei großen Gruppen die Stimmung zu offenen Fragen zu erfassen. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/surveys/frontends/<program>/
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
</content>
