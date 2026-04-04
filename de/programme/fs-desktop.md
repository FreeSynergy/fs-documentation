# fs-desktop

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-desktop` · `/home/kal/Server/fs-desktop/`
**Typ:** Program (Workspace: 6 Crates)
**Capabilities:** `desktop.shell`, `desktop.window-manager`, `desktop.settings`, `desktop.profile`

---

## Was ist das?

`fs-desktop` ist die Wayland-Shell für FreeSynergy.
Sie verwaltet Fenster, Apps, Settings und Benutzerprofil.
Basiert auf `iced` via `libcosmic` (System76).

---

## Workspace-Struktur

```
fs-desktop/crates/
├── fs-gui-workspace  — Wayland-Compositor + Window-Manager (iced/libcosmic)
├── fs-app            — App-Launcher, App-Lifecycle-Management
├── fs-db-desktop     — SQLite-Datenbank für Desktop-State
├── fs-settings       — Settings-Verwaltung (Sprache, Theme, Tastatur)
├── fs-profile        — Benutzerprofil (Avatar, Name, Bio)
└── fs-showcase       — Komponenten-Demo / Design-System-Browser
```

---

## Design

```
DesktopShell (Facade)
    ├── ShellLayout           — Composite Pattern (ShellSection → SlotEntry)
    ├── AppLifecycleBus       — Observer Pattern (Opened/Closed/Pinned/Unpinned)
    ├── ComponentRegistry     — fs-render Phase-3 Komponenten-Registry
    ├── WindowManager         — Observer Pattern (SessionTracker → Fenster-Events)
    ├── AppLauncher           — Command Pattern
    ├── SettingsModule        — Strategy Pattern (LayoutSectionStrategy je Section)
    └── ProfileModule         — Repository Pattern
```

**Render-Engine:** `iced` via `fs-gui-engine-iced` → `libcosmic` (System76)
**Pattern:** Elm MVU — Message / Update / View

### Layout-System (Phase 4)

`ShellLayout` (Composite) verwaltet alle Shell-Sektionen:

| Sektion    | Standard           | Sichtbar |
|------------|--------------------|----------|
| Topbar          | `notification-bell` (top)                       | ja   |
| Sidebar (links) | `inventory-list` (fill), `pinned-apps` (bottom) | ja   |
| Main            | — (App-Content)                                 | ja   |
| Sidebar (rechts)| `help-panel` (fill)                             | ja   |
| Bottombar       | `system-info` (bottom)                          | nein |

Config-Datei: `~/.config/freesynergy/desktop/desktop-layout.toml`

### Sidebar State Machine (Phase 4B)

```
SidebarState:  Collapsed (48px Icon-Strip) | Expanding | Open (full width)
SidebarMode:   Auto (collapses on cursor leave) | Pinned (stays open)
SidebarSide:   Left | Right
```

**Transitions:**

| Von       | Trigger                     | Nach      |
|-----------|-----------------------------|-----------|
| Collapsed | Cursor ≤ Edge + 16px        | Expanding |
| Expanding | Cursor verbleibt in Zone    | Open      |
| Open      | Cursor > Full Width + 16px  | Collapsed |
| Any       | Pin-Button (Pinned Mode)    | stays Open|

**MouseProximityObserver** (`sidebar_state.rs`): prüft X-Koordinate gegen konfigurierten Schwellwert.

### Linke Sidebar — Taskbar

```
┌──────────────────────┐
│ ⊞ Launcher    📍     │  ← Launcher + Pin-Button (collapsed: nur ⊞)
├──────────────────────┤
│  INSTALLED           │  ← Section-Label (nur expanded)
│  🌐 Browser          │  ← alle installierten Apps
│  📦 Store            │
├──────────────────────┤
│  PINNED              │  ← Section-Label (nur expanded)
│  ⭐ Tasks            │  ← pinned Apps
├──────────────────────┤
│ ⚙ Settings           │  ← immer sichtbar, fixed bottom
└──────────────────────┘
```

### Rechte Sidebar — Help + AI

```
┌──────────────────────┐
│ Hilfe            📌  │  ← Titel + Pin-Button
├──────────────────────┤
│ [HelpContent]        │  ← LocalHelpTopicSource → AiHelpSource → NoHelpSource
│                      │    (Strategy Pattern, context-sensitiv)
├──────────────────────┤
│ KI fragen…  [Senden] │  ← AiInputBar (nur wenn AI-Capability vorhanden)
└──────────────────────┘
```

**HelpSource-Trait** (Strategy Pattern):
- `LocalHelpTopicSource` — fs-help HelpSystem (in-process)
- `AiHelpSource` — fs-ai gRPC (stub in Phase 4B, live ab Phase 6)
- `NoHelpSource` — Fallback

**CapabilityCheck**: prüft `FS_AI_ENDPOINT` env var oder Flag-Datei.

### SVG-Icons (Phase 4B)

`IcedLayoutInterpreter` lädt Icons in dieser Reihenfolge:
1. `~/.local/share/freesynergy/icons/{name}.svg` (User-Artifact)
2. `/var/lib/freesynergy/icons/{name}.svg` (System-Artifact)
3. `<binary-dir>/assets/icons/{name}.svg` (bundled)
4. Emoji-Fallback (z.B. `⚙` für `settings`, `●` für unbekannte Icons)

### App-Lifecycle-Bus (Phase 4)

```rust
lifecycle_bus.app_opened("fs-store");   // → AppOpenedPayload → tracing
lifecycle_bus.app_pinned("fs-store");   // → PinnedApps-Update → Sidebar
```

### Settings: Layout-Seite (Phase 4)

`LayoutSectionStrategy` (Strategy Pattern) rendert jede Shell-Sektion als Settings-Zeile.
Concrete Strategies: `TopbarStrategy`, `SidebarStrategy`, `BottombarStrategy`.

---

## Abhängigkeiten

| Crate                | Zweck                                        |
|----------------------|----------------------------------------------|
| `fs-session`         | Welche Apps sind offen? Session-Events       |
| `fs-render`          | GUI-Abstraktions-Traits                      |
| `fs-gui-engine-iced` | iced/libcosmic Render-Engine                 |
| `fs-settings`        | Settings persistieren                        |
| `fs-i18n`            | Lokalisierung aller UI-Texte                 |
| `fs-theme`           | Theme-Definitionen                           |
| `fs-help`            | Context-sensitive Help Topics                |

---

## Geplante Erweiterungen

| Phase | Inhalt                                                         |
|-------|----------------------------------------------------------------|
| 4B    | Sidebar Hot-Reload via inotify (Phase 3 HotReloadWatcher)      |
| 4B    | IcedLayoutInterpreter vollständig in Shell-View einbinden      |
| 5/6   | OIDC-Login-Flow in fs-settings konfigurierbar                  |
| 6     | SearchBar in Topbar (slot: fill)                               |
| 6     | AiHelpSource: echte gRPC-Anbindung an fs-ai                    |
