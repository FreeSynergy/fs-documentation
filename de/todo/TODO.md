# FreeSynergy — Build Plan

[← Zurück zum Index](../INDEX.md)

---

## Regeln für Claude-Sessions

- TODO vollständig lesen zu Beginn jeder Session
- Erledigte Items löschen — kein [✓] behalten, spart Token
- Vor jeder Entscheidung fragen — nie eigenmächtig handeln
- Repo-Arbeit immer: erst lesen → dann planen → dann umsetzen

---

## Status-Markierungen

```
[ ]  Muss noch gemacht werden
[o]  Wird gerade bearbeitet
[~]  Muss noch getestet werden
```

---

## Architektur-Überblick (Stand 2026-04-02)

### Grundprinzipien

```
Standalone-First:
  Jedes Repo / jeder Container funktioniert unabhängig vom Rest.
  Integration über gRPC / REST / Bus — nie harte Runtime-Dependencies.

Everything through the Store:
  Was nicht im Store ist, existiert für das System nicht.
  Pakete, Engines, Themes, Sprachen, Adapter — alles ist ein Store-Artifact.

Engine-Auswahl zur Laufzeit:
  fs-info ermittelt Capabilities (display, terminal, headless).
  Die passende Render-Engine wird als Artifact geladen — nie hartgekodiert.
  display_server available → GUI (iced oder bevy)
  nur terminal             → TUI
  headless / SSH           → API + CLI

Adapter kommt immer mit:
  Jedes program-Paket hat einen adapter als Dependency.
  Store installiert beides zusammen.
  Adapter registriert Capability in fs-registry.

Deklarative UI-Abstraktion:
  Layout wird als Konfiguration beschrieben (engine-unabhängig).
  Jede Engine (iced, bevy, TUI, web) interpretiert sie eigenständig.
  Komponenten registrieren sich mit ComponentId.
  Neue Komponenten kommen als Store-Artifacts.
```

### Install-Kette

```
fs-init
  1. fs-info: ermittelt Capabilities (display? terminal? headless?)
  2. Zeigt minimale Bootstrap-UI (basierend auf Capability)
  3. Lädt Store-Service
  4. Store zeigt Bundles + Einzelpakete
  5. User wählt Install-Target: Container (bevorzugt) | rpm | deb | flatpak | AppImage
  6. fs-info schlägt passende Variante vor (OS-Detection)
  7. Adapter wird IMMER mitinstalliert (nicht optional)
  8. Manager übernimmt Konfiguration nach Install
```

### Package-Typen im Store

```
bundle   — Gruppe von Paketen (z.B. Workstation, Server, Minimal)
program  — Laufender Dienst (Container bevorzugt)
adapter  — Implementiert Trait, registriert Capability (kommt mit program)
artifact — Reine Daten (Sprachen, Themes, DB-Engines, Render-Engines, Bots)
fork     — 3rd-party Fork (Kanidm, Tuwunel, Stalwart, ...)
```

### Deklaratives Komponenten-System (fs-render)

```
Layout wird als Konfiguration beschrieben:
  Shells: Sidebar | Topbar | Bottombar | Main
  Jede Shell hat Slots: anchor = top | fill | bottom
  Komponenten deklarieren ihren bevorzugten Slot
  Mehrere top-Komponenten stacken automatisch
  fill-Komponenten teilen sich den Raum

Beispiel sidebar-layout:
  slot(top)  → InventoryList (installierte Programme)
  slot(fill) → AppSections (nach Kategorie)
  slot(bottom) → PinnedApps (angepinnte Programme)

Engine-Interpretation:
  iced  → native Widgets, Pixel-perfekt
  bevy  → 3D-Panels, gleiche Slot-Logik + Z-Achse
  TUI   → ASCII-Boxen, keine SVG/Animationen
  web   → HTML/CSS Grid

Komponenten kennen ihre Größe selbst (responsive).
Neue Komponenten kommen als Store-Artifacts.
```

### API-Standard

```
gRPC (tonic):   primär — intern + extern, type-safe
REST (axum):    zusätzlich — universell, Browser-kompatibel
OpenAPI (utoipa): auto-generiert
NIE direkte Calls über Repo-Grenzen — immer über gRPC/REST
```

### OOP-Grundregeln

```
Design Pattern ZUERST festlegen
Traits + Structs definieren — erst dann Impl schreiben
Traits statt match-Blöcke, Objekte statt Daten
Immer gegen Interface (Trait) — nie gegen konkrete Impl
Domain-Objekte importieren KEIN fs-render
view.rs ist das einzige Bindeglied zwischen Domain + fs-render
```

### i18n-Grundregeln

```
Jeder user-facing Text braucht FTL — egal ob UI, CLI, Fehler, Log
"Sieht ein Mensch den Text?" → FTL. Interner Code → kein FTL nötig
Fallback: en (immer eingebaut), weitere Sprachen als Artifacts
```

### DB-Grundregeln

```
Immer über fs-db Repository<T> + Filter<T>
Konkrete Engine kommt als Artifact (fs-db-engine-sqlite default)
DbEngine-Trait + direktes SeaORM/sqlx nur in Adapter-Repos
```

---

## Offene Konzept-Entscheidungen (vor Umsetzung klären)

### O1 — Bootstrap ohne Render-Engine

Wie sieht die allererste Ausgabe von fs-init aus, BEVOR eine Engine geladen ist?
Optionen: reiner Terminaltext (println!) | minimales TUI (ratatui hardcoded) | beides je nach Capability

```
[ ] Entscheidung: Was zeigt fs-init vor dem ersten Engine-Download?
```

### O2 — LayoutDescriptor-Format

Wie wird das deklarative Layout beschrieben?
- TOML (einfach, lesbar, bereits in fs-config)
- eigenes Rust-DSL (typsicher, aber kein Hot-Reload)
- JSON (universell, aber verbose)
Anforderung: Hot-Reload via inotify (wie FTL), Engine-unabhängig, erweiterbar

```
[ ] Entscheidung: Format für LayoutDescriptor
[ ] Entscheidung: Wie registriert eine Komponente ihre ComponentId im Store?
[ ] Entscheidung: Wie lädt fs-render eine Komponente zur Laufzeit (dynamic dispatch vs. static)?
```

### O3 — Bundle-Definitionen

Welche Standard-Bundles gibt es?
- Minimal: fs-init + fs-store + fs-registry + fs-inventory
- Server: Minimal + fs-auth (Kanidm) + fs-node + Zentinel + Stalwart
- Workstation: Server + fs-desktop + fs-gui-engine-iced + fs-managers + fs-apps
- Developer: Workstation + Forgejo + fs-builder-integration

```
[ ] Entscheidung: Bundles definieren und in Store/ Katalog eintragen
[ ] Entscheidung: Welche Engine ist Standard für Workstation? (iced empfohlen)
```

### O4 — Wiki: Wiki.js oder Outline?

Beide haben ähnliche APIs. Outline: modernere REST-API, bessere SSO-Integration.
Wiki.js: etablierter, mehr Features, aber schwerer.

```
[ ] Entscheidung: Outline als Standard, Wiki.js als Alternative? Oder beide im Store?
```

### O5 — fs-builder Status

fs-builder-Funktionalität ist bereits in fs-managers integriert.
fs-builder Repo ist strukturell fertig (Pipeline Pattern, 9 Tests grün).

```
[ ] Entscheidung: fs-builder archivieren (wie fs-apps)? Oder als Standalone behalten für CLI-Build-Pipelines?
```

---

---

# Phase 1 — Bootstrap

> Ziel: System kann sich selbst initialisieren und den Store laden.
> Jedes Teilsystem muss standalone funktionieren.

---

## 1.1 — fs-init: Capability-Detection

```
[ ] fs-info einbinden: display_server / terminal / headless ermitteln
[ ] Bootstrap-Modus wählen: GUI | TUI | CLI-only
[ ] Minimal-UI vor Engine-Download (O1 muss entschieden sein)
[ ] Engine als Artifact aus Store laden (nach O1-Entscheidung)
```

## 1.2 — fs-init: Install-Wizard

```
[ ] Wizard-Schritte: Welcome → Capability-Info → Engine-Wahl → Bundle-Wahl → Bestätigung → Progress
[ ] Bundle-Auswahl anzeigen (aus Store/ Katalog)
[ ] Einzelpaket-Auswahl (falls kein Bundle)
[ ] Install-Target pro Paket: Container | rpm | deb | flatpak | AppImage
[ ] fs-info: OS-Detection → passende Variante vorschlagen
[ ] Adapter immer mitinstallieren (nicht optional)
[ ] Nach Install: Manager startet Konfiguration
```

## 1.3 — fs-init: Standalone-Test

```
[ ] fs-init ohne jedes andere FS-Service startbar
[ ] Nur fs-info als Dependency (Compile-Time)
[ ] Store-Download funktioniert ohne laufenden fs-store-Container
```

---

---

# Phase 2 — Store

> Ziel: Alles installierbar machen. Store ist Single Source of Truth.
> fs-store läuft als eigenständiger Container.

---

## 2.1 — Store/ Katalog: Pakete vervollständigen

```
[ ] Alle bestehenden Repos auf einheitliches package.toml-Format migrieren
[ ] Bundles definieren: Minimal | Server | Workstation | Developer (O3)
[ ] Für jedes program-Paket: artifact-Einträge für container, rpm, deb, flatpak
[ ] Adapter-Dependencies in package.toml eintragen
[ ] Fork-Pakete: Kanidm, Tuwunel, Stalwart, Zentinel, Zentinel-Plane
[ ] Neue Pakete: Outline (oder Wiki.js), Forgejo, Bulwark Mail
```

## 2.2 — fs-store: Install-Pipeline

```
[ ] InstallRequest: Paket + Target (Container/rpm/deb/flatpak) + Variante
[ ] Download: aus Store-Katalog → URL ermitteln → Artifact holen
[ ] Adapter-Auto-Install: wenn program installiert → zugehöriger Adapter auch
[ ] fs-inventory: nach Install updaten (upsert_resource)
[ ] fs-registry: nach Install registrieren (Register Capability)
[ ] Bus: install::completed publishen
```

## 2.3 — fs-store: UI + CLI

```
[ ] Store-UI: Paket-Liste, Suche, Detail, Install-Wizard (SelectStep → ConfirmStep → ProgressStep → DoneStep)
[ ] Store-CLI: search / install / remove / list-installed / update
[ ] Install-Target wählbar (Container bevorzugt, OS-passende Alternative vorgeschlagen)
[ ] Bundle-Install: alle Pakete des Bundles auf einmal
```

## 2.4 — fs-store: Standalone-Test

```
[ ] fs-store ohne fs-desktop startbar (CLI reicht)
[ ] fs-store ohne laufenden fs-node startbar
```

---

---

# Phase 3 — fs-render: Component System

> Ziel: Engine-unabhängiges deklaratives Layout.
> Komponenten beschreiben WHAT, Engines rendern HOW.

---

## 3.1 — LayoutDescriptor (O2 muss entschieden sein)

```
[ ] LayoutDescriptor-Format definieren (TOML bevorzugt)
[ ] Shell-Typen: Sidebar | Topbar | Bottombar | Main
[ ] Slot-Typen: top | fill | bottom
[ ] ComponentId-Registry: Komponente meldet sich an
[ ] Hot-Reload via inotify (wie FTL in fs-i18n)
```

## 3.2 — Komponenten-System

```
[ ] ComponentTrait: render(engine, slot_size) → Element
[ ] Slot-Layout-Algorithmus: top stacken, fill teilt Raum, bottom stacken
[ ] Responsive: Komponente kennt ihre Mindest-/Maxgröße
[ ] Engines: iced-Impl + TUI-Impl (bevy später)
```

## 3.3 — Standard-Komponenten (für Desktop)

```
[ ] InventoryListComponent: zeigt installierte Programme (aus fs-inventory)
[ ] PinnedAppsComponent: angepinnte Programme (aus fs-session)
[ ] AppSectionsComponent: Programme nach Kategorie
[ ] SystemInfoComponent: CPU/RAM/Disk (aus fs-info)
[ ] NotificationBellComponent: Bus-Events
[ ] SearchBarComponent: global search (Phase 5)
```

---

---

# Phase 4 — Desktop

> Ziel: Vollständige Desktop-Shell mit konfigurierbarem Layout.
> Läuft auf fs-render + fs-gui-engine-iced.

---

## 4.1 — Desktop-Shell: Layout-System

```
[ ] ShellLayout: Sidebar | Topbar | Bottombar | Main (alle optional)
[ ] Slot-basierte Konfiguration (aus Phase 3)
[ ] Layout-Konfiguration in TOML (hotpluggable)
[ ] Default-Layout: Topbar(brand + breadcrumbs + avatar) + Sidebar(inventory + pinned) + Main
```

## 4.2 — Desktop-Shell: Komponenten einbinden

```
[ ] InventoryList in Sidebar (slot: fill)
[ ] PinnedApps in Sidebar (slot: bottom)
[ ] SystemInfo in Topbar oder Bottombar (slot: bottom)
[ ] NotificationBell in Topbar (slot: top)
[ ] SearchBar in Topbar (slot: fill)
```

## 4.3 — Desktop-Shell: App-Management

```
[ ] App starten: aus Inventory oder Pinned → Fenster öffnen
[ ] App-Fenster: FsWindow-Trait (fs-render)
[ ] fs-session: geöffnete Apps tracken (app::opened / app::closed)
[ ] Mehrfenster: Fenster-Liste in Taskbar
[ ] App anpinnen / lösen (persist in fs-session)
```

## 4.4 — Desktop: Settings

```
[ ] Appearance (Theme-Wahl)
[ ] Language (Sprache global + per App)
[ ] Desktop-Layout konfigurieren (welche Komponenten wo)
[ ] Service Roles (welcher Service übernimmt welche Funktion)
[ ] Accounts (IAM via Kanidm)
[ ] Shortcuts
[ ] Packages (Store-View)
```

## 4.5 — Desktop: i18n vollständig

```
[ ] Alle UI-Texte in .ftl migrieren (derzeit noch einige hardcoded)
[ ] fs-theme-app: FTL-Keys migrieren
[ ] fs-container-app: FTL-Keys migrieren
[ ] fs-builder: FTL-Keys migrieren (falls nicht archiviert)
```

## 4.6 — Desktop: Langfristige Polish

```
[ ] Action Registry + konfigurierbare Shortcuts (Q1-Q2)
[ ] Menü: jeder Punkt ruft echte Aktion auf (Q3)
[ ] Context-Menüs (Q6)
[ ] Animationen konfigurierbar (AnimationSet aus Store) (Q7)
[ ] Alle Stubs / toten Code entfernen (Q8)
```

---

---

# Phase 5 — Ecosystem Services

> Ziel: Kritische Dienste installierbar, konfigurierbar, laufend.
> Jeder Dienst standalone — Integration über Adapter + Bus.

---

## 5.1 — Kanidm (Auth-Grundlage)

```
[ ] Store-Eintrag: kanidm als fork-Paket (Container + fs-auth-Adapter)
[ ] Nach Install: Konfigurationsassistent (Admin-Account, Domain, OIDC-Clients)
[ ] fs-auth: Kanidm-Impl vollständig (OAuthProvider + ScimProvider + SsoProvider + PamProvider)
[ ] Desktop: Login via Kanidm (fs-profile → IAM)
[ ] API-Clients (alle Services): OIDC-Login über Kanidm
[ ] Test: Kanidm standalone startbar (ohne fs-desktop)
```

## 5.2 — Zentinel + Zentinel Control Plane (Reverse-Proxy)

```
[ ] Store-Eintrag: zentinel + zentinel-plane als fork-Pakete
[ ] S3-Integration: Zentinel nutzt fs-s3 / opendal für Konfigurationsspeicher
[ ] Control Plane: Routen-Konfiguration (welcher Service hinter welchem Pfad)
[ ] Manager: ZentinelManager (konfiguriert Routen nach Service-Install)
[ ] fs-registry: neu registrierte Services → Zentinel-Route automatisch
[ ] Test: Zentinel standalone (ohne fs-desktop, ohne Kanidm)
```

## 5.3 — Stalwart + Bulwark Mail (E-Mail)

```
[ ] Store-Eintrag: stalwart (fork) + bulwark-mail (webmail frontend)
[ ] Nach Install: Domain-Konfiguration, IAM-Integration (Kanidm via OIDC/LDAP)
[ ] Adapter: smtp + imap → fs-registry (Service Roles: mail)
[ ] Domain-Konfiguration pro Node (fs-node Integration)
[ ] Test: Stalwart standalone (ohne fs-desktop)
```

## 5.4 — Tuwunel (Matrix-Messenger)

```
[ ] Store-Eintrag: tuwunel (fork) als Container
[ ] fs-channel-matrix: MatrixAdapter vollständig
[ ] IAM: Matrix-Accounts via Kanidm (OIDC)
[ ] Bots: fs-bots → Tuwunel als Backend (via fs-channel-matrix)
[ ] Test: Tuwunel standalone
```

## 5.5 — Telegram (externer Kanal)

```
[ ] fs-channel-telegram: TelegramAdapter vollständig
[ ] fs-bots: Telegram als Bot-Backend (via fs-channel-telegram)
[ ] Store-Eintrag: fs-channel-telegram als adapter-Paket
[ ] Konfiguration: Bot-Token via fs-config / Manager
```

## 5.6 — Outline (Wiki / Dokumentation)

```
[ ] Store-Eintrag: outline als Container-Paket
[ ] IAM: SSO via Kanidm (OIDC)
[ ] S3: Datei-Storage via opendal
[ ] Adapter: outline-adapter → fs-registry (Service Role: wiki)
[ ] Alternative: Wiki.js als zweites Store-Paket (beide unterstützen)
[ ] Test: Outline standalone
```

## 5.7 — Forgejo (Git-Server, Self-Hosted)

```
[ ] Store-Eintrag: forgejo als Container-Paket
[ ] IAM: Kanidm OIDC
[ ] S3: Repository-Storage via opendal
[ ] Adapter: forgejo-adapter → fs-registry (Service Role: git)
[ ] Test: Forgejo standalone
```

---

---

# Phase 6 — Apps & Search

> Alle Apps: UI (FsView-Trait) + CLI + API (gRPC + REST)
> Standalone: jede App läuft ohne den Rest

---

## 6.1 — Apps: Langfristige Open Items

```
fs-db: CrudRepo → Repository<T> migrieren (low priority)
fs-db: Filter<T> → SQL übersetzen in Adapter-Repos (nach G8)
fs-bots: bot-db/src/lib.rs aufteilen (735 Zeilen) → conversation/user/state/command_log
fs-bots: DB nur über fs-db DbEngine-Trait
fs-ai: Konversationshistorie über fs-db DbEngine-Trait
fs-tasks: TaskStore über fs-db DbEngine-Trait
fs-lenses: LensRegistry vollständig (Strategy Pattern)
fs-manager-language: gix-API (pre-0.65) migrieren (bekannter Bug)
matrix-sdk: PostgreSQL State Store (wartet auf rustc recursion-overflow Fix upstream)
```

## 6.2 — Search (Phase M)

```
[ ] Search-View (Suchfeld, gruppierte Ergebnisse, Preview)
[ ] Service-Suche (lokal, fs-registry)
[ ] Host-Suche (Bus-aggregiert)
[ ] Föderale Suche
```

## 6.3 — libcosmic Integration (langfristig, G2.8)

```
[ ] fs-gui-engine-iced: libcosmic vollständige Integration
    (vanilla iced 0.13 als Basis, libcosmic als Theme-Layer)
```

---

---

# Phase 7 — Federation & Infrastruktur

---

## 7.1 — Federation

```
[ ] Federation-Grundstruktur (ActivityPub)
[ ] Rechte-Kaskade + Audit-Log
[ ] Föderaler Bus
[ ] WireGuard (nach Federation)
[ ] Hickory DNS (nach Federation)
```

## 7.2 — Infrastruktur

```
[ ] Vaultwarden (Passwort-Manager)
[ ] Ntfy / UnifiedPush (Push-Benachrichtigungen)
[ ] Element Call + coturn (WebRTC für Matrix-Calls)
```

---

## Archiviert / Erledigt (Referenz)

```
fs-apps: archiviert 2026-04-01 (alle Apps in eigene Repos migriert)
fs-builder: Entscheidung ausstehend (O5) — Funktionalität in fs-managers integriert
fs-bootc: ✅ 2026-03-31 (GitHub Actions + Butane/Ignition)
fs-libs (5 Primitives): ✅ 2026-03-26
fs-bus: ✅ 2026-03-31
fs-config: ✅ 2026-03-30
fs-db: ✅ 2026-03-31 (Repository<T> Basis)
fs-i18n: ✅ 2026-03-30
fs-theme: ✅ 2026-03-30
fs-render: ✅ 2026-04-02 (Traits; Component System kommt in Phase 3)
fs-gui-engine-iced: ✅ 2026-03-29
fs-gui-engine-bevy: ✅ 2026-03-30
fs-web-engine + servo: ✅ 2026-03-30
fs-auth: ✅ 2026-03-30 (Traits; Kanidm-Impl vollständig in Phase 5.1)
fs-registry: ✅ 2026-03-31
fs-inventory: ✅ 2026-03-31
fs-session: ✅ 2026-03-31
fs-info: ✅ 2026-03-31
fs-container: ✅ 2026-03-30
fs-browser: ✅ 2026-04-01
fs-theme-app: ✅ 2026-04-01 (FTL-Migration offen, Phase 4.5)
fs-lenses: ✅ 2026-04-01
fs-ai: ✅ 2026-04-01
fs-container-app: ✅ 2026-04-01
fs-tasks: ✅ 2026-04-01
fs-bots: ✅ 2026-04-01
fs-builder: ✅ 2026-04-01 (Pipeline Pattern — Archivierung O5)
fs-store (Wizard): ✅ 2026-04-02 (H9a-H9d)
fs-managers: ✅ 2026-04-01
Store/ Katalog: ✅ 2026-03-31 (Vervollständigung Phase 2.1)
fs-documentation: ✅ 2026-03-30
fs-ci + GitHub Actions: ✅ 2026-03-31
Fork-Repos (CI): ✅ 2026-03-31
```

---

## Reihenfolge (aktuell)

```
1. Offene Konzept-Entscheidungen klären (O1-O5)
2. Phase 1: Bootstrap (fs-init Wizard + Capability-Detection)
3. Phase 2: Store (Install-Pipeline + Bundle-Katalog)
4. Phase 5.1: Kanidm (Auth-Grundlage, Blocker für alle anderen Services)
5. Phase 5.2: Zentinel (Proxy, Grundlage für Service-Routing)
6. Phase 3: fs-render Component System (Layout-Abstraktion)
7. Phase 4: Desktop (Shell + Komponenten)
8. Phase 5.3-5.7: weitere Ecosystem-Services
9. Phase 6: Apps & Search
10. Phase 7: Federation & Infrastruktur
```
