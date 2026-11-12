# Tasks — Frontend-Dokumentation

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Tasks` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Linear](linear/index.md) | [latest](linear/latest/description.md) | Linear ist ein Issue-Tracker für Teams, auf Tempo gebaut: per Tastatur bedienbar, mit Cycles (zeitlich begrenzten Iterationen), Projekten, Initiativen und einem Triage-Eingang. |
| [OmniFocus](omnifocus/index.md) | [latest](omnifocus/latest/description.md) | OmniFocus ist ein Aufgabenmanager für Mac, iPhone, iPad, Apple Watch und Vision Pro, dazu OmniFocus im Web, ausgelegt auf langfristige Projekte und die wöchentliche Überprüfung. |
| [Taskwarrior](taskwarrior/index.md) | [latest](taskwarrior/latest/description.md) | Taskwarrior ist ein To-do-Manager für die Kommandozeile. |
| [Things 3](things-3/index.md) | [latest](things-3/latest/description.md) | Things 3 ist eine persönliche To-do-App für Mac, iPhone, iPad, Apple Watch und Vision Pro, aufgebaut um eine kleine Auswahl fester Listen und einen ruhigen, schnellen Erfassungsablauf. |
| [Todoist](todoist/index.md) | [latest](todoist/latest/description.md) | Todoist ist ein plattformübergreifender Aufgabenmanager mit Projekten, Abschnitten, Labels, Prioritäten und Datumsangaben in natürlicher Sprache. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/tasks/frontends/<program>/
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
