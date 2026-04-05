# fs-desktop

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-desktop` · `/home/kal/Server/fs-desktop/`
**Typ:** Program (Workspace: 6 Crates)
**Capabilities:** `desktop.shell`, `desktop.window-manager`, `desktop.settings`, `desktop.profile`

---

## Was ist das?

`fs-desktop` ist die GUI-Shell für FreeSynergy.
Sie verwaltet Fenster, Navigation, Activity Hub, Settings und Benutzerprofil.
Engine-agnostisch: läuft mit `iced` (Standard), `bevy` oder `TUI` — je nach Capabilities des Systems.

Das Desktop-Paradigma ist **absichts-zentrisch**:
Der Mensch denkt nicht in Programmen, sondern in dem, was er tun will.
Der Activity Hub stellt Kategorien bereit — das passende Programm kommt von selbst.

---

## Workspace-Struktur

```
fs-desktop/crates/
├── fs-gui-workspace  — Shell: Navigation, WindowManager, ActivityHub, AppLifecycle
├── fs-app            — Starter-Binary (Engine-Auswahl via Feature-Flags)
├── fs-db-desktop     — SQLite-Datenbank für Desktop-State
├── fs-settings       — Settings-Verwaltung: Ansicht, Sprache, Theme, Shortcuts
├── fs-profile        — Benutzerprofil (Avatar, Name, Bio, SSH-Keys)
└── fs-showcase       — Komponenten-Demo / Design-System-Browser (nur debug)
```

---

## Navigation: Corner Menus + Side Menus

Der Desktop nutzt **Corner Menus** (Viertelkreis-Indikator) und **Side Menus**
(Halbkreis-Indikator) statt klassischer Sidebars.
Alternativ: **Sidebar Panels** (Overlay, Bildschirm verschiebt sich nicht).
Umschaltbar in **Settings > Ansicht: Menü-Stil**.

### Default-Layout

```
┌──────────────────────────────────────────────────────────┐
│  ◔  [Titlebar: Icon | Titel | View-Buttons | Tiling | −□×]  ◕  │
│                                                          │
│                                                          │
│               [Fenster-Inhalt]                          │
│                                                          │
│                                                          │
│  ◔  [leer oder Notification Center]                   ◕  │
└──────────────────────────────────────────────────────────┘

Oben links  (◔): Task-Menü — alle installierten + laufenden Programme
Unten links (◔): Settings  — Desktop-Konfiguration (SettingsConfig)
Oben rechts (◕): Help      — General Help + Focus Help (kontext-sensitiv)
Unten rechts(◕): AI        — KI-Chat (nur wenn "ai.chat" Capability vorhanden)
```

Alle vier Corner Menus sind radiale Kreisbögen.
Der Viertelkreis-Indikator ist immer sichtbar — zeigt wo ein Menü wartet.
Icons vergrößern sich beim Hover (MacOS Dock-Stil, SVG-basiert → verlustfrei).

### Corner Menu — Verhalten

```
Hover → Indikator leuchtet auf
Klick → Menü öffnet (radiale Items auf Kreisbogen)
Item-Hover → Icon wächst (HoverMagnification), Nachbarn auch
Item-Klick → Aktion oder Sub-Menü (weitere Kreisebene)
Scroll-Fallback → wenn Items nicht reinpassen (Mobile / kleine Screens)
Icon-Hintergrund → immer transparent
```

### Side Menu — Verhalten (optional)

```
Halbkreis-Indikator an einer Seite (links/rechts/oben/unten)
Accordion-Animation: Items klappen von der Mitte nach oben+unten
Gleichmäßige Verteilung wenn wenige Items (muss Ränder nicht berühren)
Sub-Menüs: Item-Klick öffnet neue Accordion-Zeile
```

---

## Titlebar

Jedes Fenster hat eine einheitliche Titlebar:

```
[App-Icon] [Titel (zentriert)] [View-Buttons] [Tiling-Toggle] [−][□][×]
```

**View-Buttons:** wechseln zwischen den ProgramViews des aktiven Programms.
Welche Views ein Programm anbietet, deklariert es selbst via `ProgramViewProvider`-Trait.

**Tiling-Toggle:** drei Modi:
- **Manuell** — Fenster frei positionieren
- **Auto-Snap** — Fenster rasten in Raster ein (2er/3er/4er)
- **Focus Mode** — alles ausblenden, nur ein Fenster

---

## Program Views

Jedes Programm kann bis zu 6 Views anbieten (via `ProgramViewProvider`-Trait):

| View | Inhalt |
|------|--------|
| **Start** | Programm starten / Haupt-UI öffnen |
| **Info** | Titel, Beschreibung, Laufzeit, PIDs, Aktionen (kill/restart/update) |
| **Manual** | Scrollbare Hilfe-Dokumentation (fs-help HelpSystem) |
| **SettingsConfig** | Sofortige Konfig-Änderungen (Ansicht, Sprache, Schrift, ...) |
| **SettingsContainer** | Pod-YAML-Konfig (Restart erforderlich, Instanz kopieren) |
| **Binding** | Workflow-Editor: Programm mit anderen verknüpfen *(G2)* |

**Info-View: Berechtigungscheck**
- Eigener Rechner: alle Aktionen erlaubt
- Server: kritische Aktionen (kill, restart) nur mit Berechtigung (fs-auth Rights-Kaskade)

---

## Activity Hub

Statt "welches Programm?" fragt der Activity Hub: "was will ich tun?"

```
Activity Hub
├── Office (Activity)
│   ├── Write     (Activity → z.B. OnlyOffice oder Nextcloud Docs)
│   ├── Tabelle   (Activity → z.B. OnlyOffice Calc)
│   └── Präsentation (Activity → z.B. OnlyOffice Impress)
├── Wiki (Activity → Outline oder Wiki.js)
├── Code (Activity → Forgejo oder IDE)
├── Chat (Activity → Tuwunel Matrix)
└── ...
```

Activities sind beliebig schachtelbar.
Jede Activity bietet Aktionen: **Neu**, **Zuletzt bearbeitet**, **Programme** (2. Ebene).
Das Standard-Programm pro Activity ist konfigurierbar.
Ein Programm bietet Activities an via `ActivityEngine`-Trait + Adapter.

→ Konzept: [Activity Hub](../konzepte/activity-hub.md)

---

## Programm-Modell: Multi-Instance + Composite Icons

Mehrere Instanzen desselben Programms (z.B. drei Wiki.js-Instanzen) werden gruppiert:

```
wiki (ProgramGroup)
 ├── wiki.helfe.org     (caption: "Helfe-Wiki")
 ├── wiki.fpe.org       (caption: "FPE-Wiki")
 └── wiki.freesynergy.net (caption: "FS-Wiki")
```

**Composite Icon:** Stamm-Icon + Instanz-Icon leicht überlappend.
Beide sind immer sichtbar — man erkennt was es ist (Stamm) und welche Instanz (Badge).
Konfigurierbar in `package.toml`: `primary_icon`, `secondary_icon`, `overlap_factor`.

---

## Content-Komponenten

| Komponente | Zweck | Repo |
|-----------|-------|------|
| `InventoryComponent` | Alle installierten Programme (mit Gruppen) | fs-render |
| `GeneralHelpComponent` | Was kann ich hier tun? | fs-help |
| `FocusHelpComponent` | Was ist dieses Element? (fokussiertes Input-Feld etc.) | fs-help |
| `SettingsConfigComponent` | Sofortige Konfig-Änderungen | fs-settings |
| `SettingsContainerComponent` | Pod-YAML-Konfig, Instanzen | fs-container-app |
| `SearchComponent` | Schnellsuche + erweiterter Modus | fs-desktop |
| `AiComponent` | KI-Chat Textbox | **fs-ai** (nicht allgemein) |

---

## Design

```
DesktopShell (Facade)
├── CornerMenuRegistry    — Composite (4 Ecken × N Items × Sub-Items)
├── SideMenuRegistry      — Composite (4 Seiten × N Items × Sub-Items)
├── ActivityHub           — Registry Pattern (Activities per Store + fs-inventory)
├── WindowManager         — Observer Pattern (SessionTracker → Fenster-Events)
├── AppLifecycleBus       — Observer Pattern (Opened/Closed/Pinned/Unpinned)
├── ComponentRegistry     — fs-render Komponenten-Registry
├── CapabilityObserver    — prüft fs-registry auf "ai.chat" u.a.
├── SettingsModule        — Strategy Pattern (SettingsSection je Programm)
└── ProfileModule         — Repository Pattern
```

**Render-Engine:** Engine-agnostisch via `fs-render` Traits.
- Standard: `iced` via `fs-gui-engine-iced`
- Optional: `bevy` (3D-fähig)
- Fallback: TUI via `fs-gui-engine-tui` (wenn kein Display-Server)

**Pattern:** Elm MVU — Message / Update / View

---

## Settings: Ansicht

Konfigurierbar unter **Settings > Ansicht**:

| Einstellung | Typ | Standard |
|-------------|-----|---------|
| Icon-Größe | Schieberegler (16–64px) | 32px |
| Menü-Stil | Rund (Corner/Side) \| Sidebar-Panel | Rund |
| Hintergrund | Farbe oder Bild-Pfad | dunkel (Primärfarbe) |
| Auto Dark/Light | Zeitfenster konfigurierbar | aus |
| Schriftart | kommt in G2 | System-Standard |

---

## Abhängigkeiten

| Crate | Zweck |
|-------|-------|
| `fs-render` | GUI-Abstraktions-Traits |
| `fs-gui-engine-iced` | iced Render-Engine (Standard) |
| `fs-session` | Welche Apps sind offen? |
| `fs-inventory` | Was ist installiert? (via gRPC) |
| `fs-registry` | Welche Capabilities laufen? (via gRPC) |
| `fs-settings` | Settings persistieren |
| `fs-i18n` | Lokalisierung aller UI-Texte |
| `fs-theme` | Theme-Definitionen |
| `fs-help` | Context-sensitive Help Topics |
| `fs-components` | CornerMenu, SideMenu, ActivityHub, ... |

---

## Geplante Erweiterungen

→ Alle offenen Punkte: [TODO G1](../todo/TODO.md)

Wichtigste nächste Schritte:

| Phase | Inhalt |
|-------|--------|
| G1.1 | Navigations-Traits in fs-render |
| G1.2 | iced-Implementierung der neuen Navigation |
| G1.3 | Navigations-Komponenten in fs-components |
| G1.5 | Desktop-Shell-Refactor (Corner Menus statt Sidebars) |
| G1.6 | Activity Hub |
| G2 | TUI + bevy Navigation-Impls |
| G2 | libcosmic vollständige Integration |
