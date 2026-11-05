# Marketing — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Marketing` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Google Analytics](google-analytics/index.md) | [latest](google-analytics/latest/description.md) | Google Analytics (GA4, kommerziell) ist das Web-/App-Analyse-Standardwerk: ereignisbasierte Messung (Events + Parameter), Zielgruppen, Trichter, Attribution — verknüpft mit Google Ads/Search Console. |
| [Hotjar](hotjar/index.md) | [latest](hotjar/latest/description.md) | Hotjar (kommerziell) ergänzt Web-Analytik um das Wie: Heatmaps (Klicks/Scrolls/Moves), Session-Replays, Umfragen (Onsite-Surveys), Feedback-/Rage-Click-Erkennung und Funnel-Kopplung. |
| [Mailchimp](mailchimp/index.md) | [latest](mailchimp/latest/description.md) | Mailchimp (Intuit, kommerziell) ist die Newsletter-/Marketing-Automation-Plattform: Listen + Segmente, Kampagnen-Editor, E-Mail-Automatisierungen (Journeys), Landingpages, CRM-lite und Analytics. |
| [Matomo](matomo/index.md) | [latest](matomo/latest/description.md) | Matomo (GPL, ehem. |
| [Mautic](mautic/index.md) | [latest](mautic/latest/description.md) | Mautic (GPL, PHP/Symfony) ist quelloffene Marketing-Automation: Kontakte + Segmente, E-Mail-Kampagnen, Kampagnen-Baum (Trigger/Actions), Landingpages/Formulare, point scoring — self-hosted mit voll… |
| [Plausible](plausible/index.md) | [latest](plausible/latest/description.md) | Plausible (MIT/AGPL-Dual je Edition) ist minimalistische Web-Analyse: ein Skript, eine Zahlenansicht, cookieless & DSGVO-freundlich, self-hosted oder Cloud. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/marketing/frontends/<program>/
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
