# Architektur-Übersicht

[← Zurück zum Index](../INDEX.md) | [Repository-Übersicht](repositories.md)

---

## Die Philosophie

FreeSynergy basiert auf drei Grundgedanken:

1. **Information vor Werkzeug.** Der Mensch braucht Antworten, nicht Programme.
   Ob eine Information aus einem Wiki, einem Messenger oder einer Datenbank kommt,
   ist für den Menschen irrelevant. Programme arbeiten im Hintergrund zusammen.
   Der Mensch sieht das Ergebnis. Wenn er tiefer eintauchen will, klickt er sich
   durch — aber erst dann.

2. **Dezentral und freiwillig.** Kein Zentralserver, kein Zwang. Jeder Node ist
   souverän. Zusammenarbeit ist immer opt-in. Rechte können nur eingeschränkt,
   nie erweitert werden.

3. **Offene Standards.** OIDC, SCIM, ActivityPub, OCI, S3, CalDAV, CardDAV.
   Keine proprietären Protokolle. Jede Komponente ist austauschbar.

---

## Architektur-Diagramm

```
┌──────────────────────────────────────────────────────────────────┐
│                           Mensch                                  │
│                             │                                     │
│                     ┌───────▼───────┐                            │
│                     │    Desktop    │  Fenster, Widgets, Lenses  │
│                     └───────┬───────┘                            │
│                             │                                     │
│          ┌──────────────────┼──────────────────┐                 │
│          │                  │                  │                  │
│    ┌─────▼─────┐    ┌───────▼──────┐   ┌──────▼──────┐         │
│    │  fs-node  │    │  fs-managers │   │  fs-store   │         │
│    │ Projekte  │    │ Konfig-Tools │   │ Pakete,     │         │
│    │ Hosts     │    │ (language,   │   │ Katalog,    │         │
│    │ S3-Server │    │  theme,      │   │ Download    │         │
│    │ Auth      │    │  container,  │   │             │         │
│    │ Federation│    │  bots, ai,…) │   └──────┬──────┘         │
│    └─────┬─────┘    └──────┬───────┘          │                  │
│          │                  │                  │                  │
│    ┌─────▼──────────────────▼──────────────────▼──────┐         │
│    │                   fs-bus                          │         │
│    │          Pub/Sub · Topic-Routing                  │         │
│    └─────┬─────────────────┬─────────────────┬─────────┘         │
│          │                 │                 │                    │
│   ┌──────▼──────┐  ┌───────▼──────┐  ┌──────▼──────┐           │
│   │ fs-registry │  │ fs-inventory │  │ fs-session  │           │
│   │ Was läuft?  │  │ Was ist      │  │ Wer ist     │           │
│   │ (Caps.)     │  │ installiert? │  │ eingeloggt? │           │
│   └──────┬──────┘  └──────────────┘  └─────────────┘           │
│          │                                                        │
│   ┌──────▼──────────────────────────────────────────────┐       │
│   │              Externe Services (via Adapter)          │       │
│   │   Kanidm (IAM) · Tuwunel (Matrix) · Stalwart (Mail) │       │
│   │   Forgejo (Git) · Outline (Wiki) · uMap (Karten)    │       │
│   └──────────────────────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────────────┘
```

---

## Programme

| Programm | Aufgabe | Repo |
|---|---|---|
| [Init](../programme/init/README.md) | Bootstrap: installiert den Store | `fs-init` |
| [Node](../programme/node/README.md) | Server: Projekte, Hosts, S3, Auth, Federation | `fs-node` |
| [Desktop](../programme/desktop/README.md) | Mensch-Maschine-Schnittstelle | `fs-desktop` |
| [Store](../programme/store/README.md) | Paketmanager: Katalog lesen, Pakete installieren | `fs-store` |
| [Browser](../programme/browser/README.md) | Eingebetteter Web-Browser | `fs-browser` |
| [Managers](../programme/container/README.md) | Konfig-Werkzeuge für alle Paket-Kategorien | `fs-managers` |
| [Bots](../programme/botmanager/README.md) | Bot-Runtime + Messenger-Adapter | `fs-bots` |
| [Icons](../programme/icons/README.md) | Icon-Sets verwalten | `fs-icons` |
| [Lenses](../programme/lenses/README.md) | Informations-Betrachter (Service-übergreifend) | `fs-lenses` |
| [Tasks](../programme/store/README.md) | Automatisierungs-Pipelines | `fs-tasks` |
| [AI](../programme/store/README.md) | LLM-Proxy und AI-Runtime | `fs-ai` |

**Jedes Programm** hat ein eigenes Repository mit eigenem Release-Zyklus.
`fs-apps` existiert nicht mehr — jede App ist eigenständig.

---

## Die vier Ebenen

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  STORE         Das Mögliche    — Katalog aller verfügbaren      │
│                Pakete. Nur TOML-Daten + Binary-URLs. Kein Zustand│
│                                                                  │
│  INVENTORY     Der Jetzt-Zustand — Was ist installiert, welche  │
│                Versionen, welche Service-Instanzen laufen.       │
│                Einzige Wahrheitsquelle. Nur Manager schreiben.   │
│                                                                  │
│  REGISTRY      Was läuft gerade — Welche Capabilities sind       │
│                aktiv, auf welchem Endpoint. Services registrieren│
│                sich beim Start, deregistrieren beim Stop.        │
│                                                                  │
│  MANAGERS      Das Wie — Konfigurationswerkzeuge. Sie führen     │
│                Aktionen aus und schreiben das Ergebnis ins        │
│                Inventory. Runtime läuft getrennt.               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

- **Store** fragt: "Was gibt es?" → liest `Store/`-Repo
- **Inventory** fragt: "Was habe ich?" → schreibt und liest `fs-inventory`
- **Registry** fragt: "Was läuft?" → schreibt und liest `fs-registry`
- **Manager** fragt: "Wie mache ich es?" → schreibt in Inventory + Registry

Alles was im UI angezeigt wird, kommt aus Inventory oder Registry.
Nie direkt aus dem Store-Katalog.

---

## CLI = API = Objekt-Methoden

Jede Aktion ist genau einmal implementiert — drei Zugangswege, eine Logik:

```
fs store install kanidm
       ↕  identisch mit
POST /api/store/install  { "id": "kanidm" }
       ↕  identisch mit
Store::install("kanidm")  ← Rust-Methode
```

Die CLI ist ein dünner Wrapper (clap) über die Rust-Methode.
Die API (axum) ruft dieselbe Rust-Methode auf.
Business-Logik genau einmal — kein doppelter Code.

---

## Datenfluss — Beispiel Lenses

```
Benutzer tippt "Helfa Köln" in Lenses
  │
  ▼
Lenses fragt den Bus:
  "Welche Services haben Daten über 'Helfa Köln'?"
  │
  ▼
Bus fragt die Registry:
  "Wer hat Capability 'wiki'? Wer hat 'map'? Wer hat 'chat'?"
  │
  ▼
Registry antwortet mit Endpoints
Bus leitet Suchanfrage an gefundene Services weiter
  │
  ├── Capability 'wiki'  (Outline): Artikel-Zusammenfassung + Link
  ├── Capability 'map'   (uMap): Kartenausschnitt + Link
  ├── Capability 'chat'  (Matrix/Tuwunel): Letzte Nachrichten + Link
  ├── Capability 'tasks' (Vikunja): Offene Aufgaben + Link
  └── Capability 'git'   (Forgejo): Repository-Status + Link
  │
  ▼
Lenses zeigt zusammengefasste Ansicht
Benutzer klickt auf "Offene Aufgaben" → Weiterleitung zu Vikunja
```

Der Benutzer muss nicht wissen, welches Programm welche Daten hat.
Er fragt — das System antwortet.

---

## Start-Reihenfolge

```
1. fs-init          → prüft ob Store vorhanden, lädt ihn wenn nötig
2. fs-bus           → startet zuerst (alle anderen brauchen ihn)
3. fs-registry      → registriert sich im Bus
4. fs-inventory     → lädt installierten Zustand
5. fs-node          → Auth, S3, Federation starten
6. fs-session       → lädt letzte Sitzung
7. fs-desktop       → öffnet UI, stellt Sitzung wieder her
8. Programme        → starten bei Bedarf, registrieren sich in Registry
```

---

## SysInfo

FreeSynergy kennt das System auf dem es läuft (`fs-sysinfo`, Teil von `fs-node`):

- **Statisch (gecacht):** OS, Architektur, verfügbare Features (systemd, Podman, Git, ...)
- **Dynamisch (auf Anfrage):** Festplattenbelegung, RAM, CPU-Temperatur
- **Alerting (Bus-Events):** Konfigurierbare Schwellenwerte → `sysinfo.alert.*`

Pakete deklarieren Platform-Anforderungen (`requires:systemd`, `platform:linux`).
Der Store kombiniert sie mit SysInfo und zeigt nur was installierbar ist.

---

Weiter: [Repository-Übersicht](repositories.md) | [Inventory](../konzepte/inventory.md) | [Adapter-Pattern](../konzepte/adapter.md)
