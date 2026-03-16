# Architektur-Übersicht

[← Zurück zum Index](../INDEX.md)

---

## Die Philosophie

FreeSynergy basiert auf drei Grundgedanken:

1. **Information vor Werkzeug.** Der Mensch braucht Antworten, nicht Programme. Ob eine Information aus einem Wiki, einem Messenger oder einer Datenbank kommt, ist für den Menschen irrelevant. Die Technik muss in den Hintergrund — was wichtig ist, muss nach vorne.

2. **Dezentral und freiwillig.** Kein Zentralserver, kein Zwang. Jeder Node ist souverän. Zusammenarbeit ist immer opt-in. Rechte können nur eingeschränkt, nie erweitert werden.

3. **Offene Standards.** WASM, OIDC, SCIM, ActivityPub, OCI, Automerge. Keine proprietären Protokolle. Jedes Teil ist austauschbar.

---

## Programm-Übersicht

```
┌─────────────────────────────────────────────────────────────┐
│                        Mensch                                │
│                          │                                   │
│                    ┌─────▼─────┐                            │
│                    │  Desktop  │  UI, Widgets, Lenses       │
│                    └─────┬─────┘                            │
│                          │ API                              │
│            ┌─────────────┼─────────────┐                    │
│            │             │             │                     │
│      ┌─────▼────┐  ┌────▼─────┐  ┌───▼────┐               │
│      │   Node   │  │Conductor │  │  Store  │               │
│      │Projekte, │  │Services, │  │Wissen,  │               │
│      │Hosts,    │  │Container,│  │Pakete,  │               │
│      │Föder.    │  │Variablen │  │Suche    │               │
│      └─────┬────┘  └────┬─────┘  └───┬────┘               │
│            │             │             │                     │
│      ┌─────▼─────────────▼─────────────▼────┐              │
│      │           Message Bus                 │              │
│      │    Events, Routing, Transformation    │              │
│      └─────┬──────────┬──────────┬──────────┘              │
│            │          │          │                           │
│      ┌─────▼───┐ ┌───▼────┐ ┌──▼──────┐                   │
│      │Services │ │  Bots  │ │ Search  │                    │
│      │Kanidm,  │ │Telegram│ │Lokal,   │                    │
│      │Forgejo, │ │Matrix, │ │Föder.   │                    │
│      │Outline  │ │Discord │ │         │                    │
│      └─────────┘ └────────┘ └─────────┘                    │
└─────────────────────────────────────────────────────────────┘
```

## Jedes Programm ist eigenständig

| Programm | Läuft alleine? | Braucht | Erweitert durch |
|---|---|---|---|
| [Node](../programme/node/README.md) | Ja | Nichts | Conductor, Store, Desktop |
| [Conductor](../programme/conductor/README.md) | Ja | Nur eine YAML-Datei | Store (optional), Node (optional) |
| [Desktop](../programme/desktop/README.md) | Ja (zeigt Offline-Daten) | Node-API für Live-Daten | Store, Lenses |
| [Store](../programme/store/README.md) | Ja | Nur ein Git-Repo oder URL | Node, Conductor, Desktop |
| [Lenses](../programme/lenses/README.md) | Nein | Desktop + mindestens 1 Service | Bus, Services |
| [Search](../programme/search/README.md) | Nein | Bus + mindestens 1 Service | Föderation |

Alle Programme kommunizieren über drei Wege:
1. **CLI** — Kommandozeile
2. **API** — REST/gRPC über Netzwerk
3. **UI** — Über Desktop (ruft API auf)

Die Business-Logik ist EINMAL implementiert. CLI, API und UI sind nur verschiedene Eingänge.

---

## Datenfluss

```
Mensch tippt "Meine Gruppe Köln" in Lenses
    │
    ▼
Lenses fragt den Bus: "Welche Services haben Daten über 'Helfa Köln'?"
    │
    ▼
Bus leitet an alle Services weiter:
    │
    ├── Wiki (Outline): "Ja, hier ist der Artikel 'Helfa Köln'"
    ├── Karte (uMap): "Ja, hier ist der Punkt auf der Karte"
    ├── Chat (Matrix): "Ja, hier sind die letzten 5 Nachrichten"
    ├── Tasks (Vikunja): "Ja, hier sind 3 offene Aufgaben"
    └── Git (Forgejo): "Ja, hier ist das Repository"
    │
    ▼
Lenses zeigt eine zusammengefasste Ansicht:
    - Artikel-Zusammenfassung (Link zum Wiki)
    - Kartenausschnitt (Link zur Karte)
    - Letzte Nachrichten (Link zum Chat)
    - Offene Aufgaben (Link zum PM)
    - Repository-Status (Link zu Git)
    │
    ▼
Mensch klickt auf "Offene Aufgaben" → wird zu Vikunja weitergeleitet
```

**Der Mensch muss NICHT wissen welches Programm was hat.** Er sucht nach "Helfa Köln" und bekommt alles.

---

Weiter: [Rollen-System](../konzepte/rollen.md) | [Programme](../programme/node/README.md)
