# Whiteboards — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Whiteboards` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [draw.io](drawio/index.md) | [latest](drawio/latest/description.md) | draw.io (diagrams.net) ist ein freies Diagramm-Werkzeug für Flussdiagramme, Netzwerkpläne, UML und BPMN. |
| [Excalidraw](excalidraw/index.md) | [latest](excalidraw/latest/description.md) | Excalidraw ist ein freies, quelloffenes kollaboratives Whiteboard im handgezeichneten Stil. |
| [Miro](miro/index.md) | [latest](miro/latest/description.md) | Miro ist das kommerzielle Online-Whiteboard (SaaS) für Visual Collaboration: Infinite Canvas, Shapes/Sticky Notes, Frames, Vorlagen-Bibliothek (Retros, Workshops, Customer Journeys), Voting/Timer u… |
| [Mural](mural/index.md) | [latest](mural/latest/description.md) | Mural ist die Workshop-Whiteboard-Suite (SaaS) mit starker Facilitation: Canvas mit Formen/Notizen, „Facilitation Sequence“ (Moderationsabläufe), Teilnahmesteuerung und Vorlagen. |
| [OpenBoard](openboard/index.md) | [latest](openboard/latest/description.md) | OpenBoard ist ein freies Interactive-Whiteboard-Tool (C++, Qt) für Unterricht und Präsentationen: mehrseitige „Tableaus“, Stifte/Text/Bilder, integrierte Browser-, Dokument- und Notiz-Werkzeuge, Of… |
| [tldraw](tldraw/index.md) | [latest](tldraw/latest/description.md) | tldraw ist eine quelloffene Infinite-Canvas-Whiteboard-Bibliothek und App in TypeScript: einsatzbereit auf tldraw.com und als React-SDK (`tldraw`) für eigene Canvas-Anwendungen. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/whiteboard/frontends/<program>/
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
