# Democracy — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Democracy` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Adhocracy4](adhocracy4/index.md) | [latest](adhocracy4/latest/description.md) | Adhocracy4 (AGPL, Python/Django) ist das Beteiligungs-Framework hinter vielen kommunalen Portalen (u.a. |
| [Circo](circo/index.md) | [latest](circo/latest/description.md) | Circo (Bürgerbeteiligungs-/Konsultations-Plattform, in DE/AT für Verbände und Parlamentsbeteiligung genutzt) verbindet Umfragen, Workshops und Online-Konsultationen mit Moderation und Ergebnisberic… |
| [Consul](consul/index.md) | [latest](consul/latest/description.md) | Consul („Decide Madrid“-Software, Apache-2.0, Ruby on Rails) ist die Beteiligungsplattform für Kommunen: Vorschläge, Beteiligungsprozesse, Bürgerhaushalte, Abstimmungen/Polls, Debatten, Gesetzgebun… |
| [Decidim](decidim/index.md) | [latest](decidim/latest/description.md) | Decidim (AGPL, Ruby on Rails) ist die Plattform für partizipative Demokratie: Prozesse (Bürgerhaushalt, Beteiligung, Planung), Vorschläge mit Kommentaren/Supports, Debatten, Treffen/Events, Abstimm… |
| [LiquidFeedback](liquid-feedback/index.md) | [latest](liquid-feedback/latest/description.md) | LiquidFeedback („LiQu“, PHP, frei) implementiert delegatives Votum (Liquid Democracy): Initiativen in Themenräumen, Delegationsketten für Stimmen, Argumente mit Pro/Contra, Abstimmungen mit Quoren. |
| [Pol.is](polis/index.md) | [latest](polis/latest/description.md) | Pol.is (kommerziell, gemeinnützige Wurzeln) ist die Deliberations-Skalierungsplattform: Alle Teilnehmenden schreiben Kommentare und bewerten andere („agree/disagree/pass“) — ein Algorithmus cluster… |

## Dateisatz pro Programm (ADR 0012)

```
programs/suites/democracy/frontends/<program>/
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
