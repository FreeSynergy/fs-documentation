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
    ├── WindowManager     — Observer Pattern (SessionTracker → Fenster-Events)
    ├── AppLauncher       — Command Pattern
    ├── SettingsModule    — Strategy Pattern (je Setting-Kategorie)
    └── ProfileModule     — Repository Pattern
```

**Render-Engine:** `iced` via `fs-gui-engine-iced` → `libcosmic` (System76)
**Pattern:** Elm MVU — Message / Update / View

---

## Abhängigkeiten

| Crate              | Zweck                                        |
|--------------------|----------------------------------------------|
| `fs-session`       | Welche Apps sind offen? Session-Events       |
| `fs-render`        | GUI-Abstraktions-Traits                      |
| `fs-gui-engine-iced` | iced/libcosmic Render-Engine              |
| `fs-settings`      | Settings persistieren                        |
| `fs-i18n`          | Lokalisierung aller UI-Texte                 |
| `fs-theme`         | Theme-Definitionen                           |

---

## Bekannte Build-Issues

- `libcosmic` (git dependency) hat Inkompatibilitäten mit `cosmic_text` bezüglich Argument-Änderungen in `buffer.set_size()`, `buffer.set_text()`, `buffer.set_metrics()`, `buffer.set_wrap()`.
- Dies ist ein **upstream Issue** in `libcosmic` — kein Code-Fehler in fs-desktop.
- Fix: libcosmic-Commit aktualisieren sobald upstream gepatcht.

---

## Geplante Erweiterungen (G1+)

| Phase | Inhalt                                               |
|-------|------------------------------------------------------|
| G1    | fs-render Traits vollständig implementiert           |
| G1    | libcosmic upstream Bug gefixt → Build wieder grün    |
| G2    | Dioxus vollständig entfernt, iced/libcosmic einzige Engine |
