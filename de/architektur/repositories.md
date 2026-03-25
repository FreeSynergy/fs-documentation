# Repository-Übersicht

[← Zurück zum Index](../INDEX.md) | [Gesamtübersicht](uebersicht.md)

---

## Prinzip

FreeSynergy ist eine Betriebssystem-artige Plattform. Jede Komponente hat eine
klar definierte Verantwortlichkeit — kein Repo macht mehrere Dinge gleichzeitig.

**Grundregel:** Ein Repository = eine klare Antwort auf eine klare Frage.

**Jedes Programm-Repo** hat:
- Eigenen Release-Zyklus und eigene Versionierung
- Eigene `rustfmt.toml`, `deny.toml`, `LICENSE`, `README.md`, `CLAUDE.md`
- `#![deny(clippy::all, clippy::pedantic, warnings)]` in jeder `lib.rs` / `main.rs`
- `assets/icon.svg` (auch als Platzhalter)
- Unit-Tests pro Modul

---

## Start-Schicht

```
fs-init
  └─ bootet das System, lädt nur den Store
       └─ fs-store installiert alles weitere
```

### fs-init
**Frage:** "Was muss beim ersten Start passieren?"
- Einmaliger Bootstrap — lädt den Store-Katalog und installiert `fs-store`
- Danach übernimmt der Store
- GitHub: `FreeSynergy/fs-init` | Lokal: `/home/kal/Server/fs-init/`

---

## Platform-Services (eigenständige Repos)

Diese Services laufen als Hintergrund-Dienste. Jeder hat sein eigenes Repo,
weil sie unabhängig voneinander versioniert und deployed werden.

### fs-bus
**Frage:** "Wie kommunizieren Programme miteinander?"
- Async Event-Bus mit Topic-Routing (Pub/Sub)
- Keine direkte Kopplung zwischen Programmen — nur über Topics
- Library: wird in jeden Prozess eingebettet, kein separater Daemon
- GitHub: `FreeSynergy/fs-bus` | Lokal: `/home/kal/Server/fs-bus/`

### fs-config
**Frage:** "Wie liest und schreibt ein Programm seine Konfiguration?"
- TOML-Loader mit Validierung, Schema und Auto-Repair
- Live-Updates laufen über Bus-Events (`config::changed::*`)
- GitHub: `FreeSynergy/fs-config` | Lokal: `/home/kal/Server/fs-config/`

### fs-db
**Frage:** "Wie redet ein Programm mit seiner Datenbank?"
- SQLite-Abstraktion auf Basis von sea-orm
- Gemeinsam genutzt von allen Programmen die SQLite brauchen
- Schema-Migration via sea-orm-migration
- GitHub: `FreeSynergy/fs-db` | Lokal: `/home/kal/Server/fs-db/` *(wird angelegt)*

### fs-inventory
**Frage:** "Was ist auf diesem Node installiert?"
- SQLite: installierte Ressourcen + laufende Service-Instanzen + Ports + Rollen
- Einzige Wahrheitsquelle — kein anderes Programm darf eine eigene Liste führen
- Nur Manager schreiben rein; alle anderen lesen nur
- GitHub: `FreeSynergy/fs-inventory` | Lokal: `/home/kal/Server/fs-inventory/`

### fs-session
**Frage:** "Wer ist eingeloggt und welche Programme sind offen?"
- Aktiver User + Liste offener Programme mit Window-State
- Löst das Minimize-Problem: minimiertes Programm ist `Minimized`, nicht beendet
- Restore öffnet das bestehende Fenster, startet kein zweites
- GitHub: `FreeSynergy/fs-session` | Lokal: `/home/kal/Server/fs-session/`

### fs-registry
**Frage:** "Welche Capabilities laufen gerade auf diesem Node?"
- Dienste registrieren sich beim Start (z.B. `"iam"`, `"mail"`, `"storage"`)
- Der Bus fragt die Registry: "Wer kann Capability X?" → bekommt Endpoint
- Ersetzt das alte Bridge-Konzept vollständig (siehe [Adapter-Pattern](../konzepte/adapter.md))
- GitHub: `FreeSynergy/fs-registry` | Lokal: `/home/kal/Server/fs-registry/`

---

## Primitives (fs-libs Monorepo — bewusst klein gehalten)

`FreeSynergy/fs-libs` enthält **nur** universelle Primitives — Dinge die
buchstäblich jedes Programm braucht und die keine Domain-Logik enthalten.

| Crate | Frage |
|---|---|
| `fs-types` | Welche Basis-Typen teilen alle? (`FsValue`, `SemVer`, `FsUrl`, `LanguageCode`, ...) |
| `fs-error` | Wie behandeln wir Fehler einheitlich? (`Repairable`, `Validation`) |
| `fs-crypto` | Wie verschlüsseln und signieren wir? (age, JWT, Signing) |
| `fs-health` | Wie prüft ein Service ob er gesund ist? (Health-Check-Trait) |
| `fs-i18n` | Wie übersetzen wir? (Mozilla Fluent, Fluent-Bundles) |

**Was NICHT in fs-libs gehört:**
- `fs-bus`, `fs-config`, `fs-db` → eigene Repos (oben gelistet)
- Domain-Logik (Auth, Federation, LLM, Bot, Container, UI) → ins jeweilige Programm-Repo
- Alles was nur ein einziges Programm braucht → dort hin

GitHub: `FreeSynergy/fs-libs` | Lokal: `/home/kal/Server/fs-libs/`

---

## Programme (jedes hat sein eigenes Repo)

### fs-node
**Frage:** "Was verwaltet der Server?"
- Projekte, Hosts, Netzwerke, Föderationen, externer Zugriff (Desktop auf Mobilgeräten etc.)
- S3-Server (Datei-Storage für alle Programme auf diesem Node)
- Authentifizierung (Kanidm-Integration), Rechte-Kaskade
- Enthält: `fs-auth`, `fs-federation`, `fs-sysinfo` (nur dieser Repo braucht sie)
- GitHub: `FreeSynergy/fs-node` | Lokal: `/home/kal/Server/fs-node/`

### fs-desktop
**Frage:** "Wie sieht und bedient der Benutzer das System?"
- Desktop-Shell, Fenster-Management, Widgets, Lenses-Oberfläche
- Enthält eigene UI-Crates (`fs-ui`, `fs-components`, `fs-render`, `fs-theme`)
  denn UI-Primitives gehören zum Desktop, nicht zu den Shared-Libs
- Workspace-Crates: `fs-app` (Shell), `fs-db-desktop`, `fs-gui-workspace`,
  `fs-settings`, `fs-profile`
- GitHub: `FreeSynergy/fs-desktop` | Lokal: `/home/kal/Server/fs-desktop/`

### fs-store
**Frage:** "Wo findet und installiert man Pakete?"
- Liest TOML-Kataloge aus dem `Store/`-Repo (StoreReader)
- Verwaltet Install-Records lokal (`records.toml`)
- Download + SHA256-Verifikation von Binaries (via GitHub Releases)
- Workspace-Crates: `fs-store` (Library), `fs-store-app` (GUI), `fs-store-cli`
- GitHub: `FreeSynergy/fs-store` | Lokal: `/home/kal/Server/fs-store/`

### fs-browser
**Frage:** "Wie öffnet der Benutzer Webseiten?"
- Eingebetteter Web-Browser (eigenständig, keine Node-Abhängigkeit)
- GitHub: `FreeSynergy/fs-browser` | Lokal: `/home/kal/Server/fs-browser/`

### fs-managers
**Frage:** "Wie konfiguriert man installierte Pakete?"
- Workspace mit 7 Managern — alle folgen demselben Muster:
  *Paket installieren → verbinden/konfigurieren → fertig*
- Manager sind Konfigurationswerkzeuge, keine Runtimes

| Sub-Crate | Was er konfiguriert |
|---|---|
| `language` | Sprache, Region, Formate, Übersetzungs-Editor |
| `theme` | Farben, Typografie, Fenster-Stil, Dark/Light |
| `icons` | Icon-Sets, Icon-Picker, SVG-Upload |
| `cursor` | Mauszeiger-Sets, Animationen |
| `container` | Container-Apps: installieren, starten, stoppen, Variablen setzen |
| `bots` | Bots mit Messengern verbinden (Token, Kanal, Gruppen), Status überwachen |
| `ai` | LLM auswählen, Konfig aufbauen, mehrere Instanzen verwalten |

- GitHub: `FreeSynergy/fs-managers` | Lokal: `/home/kal/Server/fs-managers/`

### fs-bots
**Frage:** "Wie laufen Bots?"
- Runtime und Workspace für alle Messenger-Adapter
- Jeder Messenger-Typ = eigene Binary (mehrere Binaries in einem Release)
- Enthält: `fs-bot` (Framework), `fs-channel` (Adapter)

```
fs-bots/
  broadcast-bot/   → Binary für Broadcast-Funktionalität
  menu-bot/        → Binary für interaktive Menüs
  calendar-bot/    → Binary für Kalender-Integration
  ...              → ein Crate pro Bot-Typ
```

- GitHub: `FreeSynergy/fs-bots` | Lokal: `/home/kal/Server/fs-bots/`

### fs-icons
**Frage:** "Wie werden Icon-Sets verwaltet?"
- Icon-Repository-Verwaltung, SVG-Validierung, Icon-Picker
- GitHub: `FreeSynergy/fs-icons` | Lokal: `/home/kal/Server/fs-icons/`

### fs-lenses
**Frage:** "Wie betrachtet der Benutzer Informationen über Programme hinweg?"
- Aggregiert Daten aus verschiedenen Services via Bus
- GitHub: `FreeSynergy/fs-lenses` | Lokal: `/home/kal/Server/fs-lenses/` *(wird angelegt)*

### fs-tasks
**Frage:** "Wie automatisiert man Abläufe?"
- Automatisierungs-Pipelines, Task-Templates, Data Offers/Accepts
- GitHub: `FreeSynergy/fs-tasks` | Lokal: `/home/kal/Server/fs-tasks/`

### fs-container-app
**Frage:** "Wie sieht die Container-App-Verwaltung aus?"
- UI für Container-Apps (installieren, konfigurieren, starten, stoppen)
- GitHub: `FreeSynergy/fs-container-app` | Lokal: `/home/kal/Server/fs-container-app/` *(wird angelegt)*

### fs-ai
**Frage:** "Wie redet das System mit KI-Modellen?"
- AI-Runtime und Proxy zwischen FreeSynergy und lokalen LLMs (fs-mistral)
- Enthält: `fs-llm` (LLM-Abstraktion, Ollama/OpenAI-kompatibel)
- GitHub: `FreeSynergy/fs-ai` | Lokal: `/home/kal/Server/fs-ai/` *(wird angelegt)*

---

## Daten-Repos (kein Rust-Code)

### Store/
**Frage:** "Was gibt es im Store?"
- TOML-Kataloge aller verfügbaren Pakete
- Beschreibungen, i18n-Snippets, Icon-Referenzen
- Wird von `fs-store` (StoreReader) gelesen
- Binaries liegen **nicht** hier — nur Referenzen (URLs + SHA256)
- GitHub: `FreeSynergy/Store` | Lokal: `/home/kal/Server/Store/`

### fs-documentation
- Diese Dokumentation
- GitHub: `FreeSynergy/fs-documentation` | Lokal: `/home/kal/Server/fs-documentation/`

---

## Drittanbieter-Forks (nur kompilieren, nicht ändern)

| Repo | Zweck | Original |
|---|---|---|
| `fs-kanidm` | Identity / IAM | `kanidm/kanidm` |
| `fs-tuwunel` | Matrix-Server | `matrix-construct/tuwunel` |
| `fs-zentinel` | Reverse Proxy | `zentinelproxy/zentinel` |
| `fs-zentinel-plane` | Proxy Control Plane | `zentinelproxy/zentinel-control-plane` |
| `fs-stalwart` | Mail-Server | `stalwartlabs/stalwart` |
| `fs-mistral` | LLM-Inferenz | `EricLBuehler/mistral.rs` |

Forks werden **nicht geändert**. Upstream-Patches werden via GitHub Actions
automatisch eingepflegt. Jeder Fork wird als App-Paket in den Store gebracht.

---

## Adapter-Pattern (ersetzt Bridge vollständig)

Kein Bridge-Executor, keine Bridge-Library. Stattdessen implementiert jeder
externe Dienst einen Standard-Trait und registriert sich in der Registry:

```rust
// Adapter für Kanidm — implementiert unseren Auth-Trait
struct KanidmAdapter { base_url: String }
impl AuthService for KanidmAdapter { ... }

// Beim Start: Adapter registriert sich
registry.register(ServiceEntry::new("kanidm", "iam", "http://kanidm:8443")).await?;
```

Der Bus fragt die Registry — bekommt den Endpoint — routet direkt.
Der Compiler prüft den Kontrakt. Tests nutzen Mock-Adapter.

---

## Binary-Distribution

```
Programm-Repo (z.B. fs-browser/)
  └── git tag v1.0.0 && git push --tags
        └── GitHub Actions: Build → GitHub Release
              └── Artifacts: fs-browser-linux-x86_64, SHA256

Store/-Katalog (packages/apps/browser/1.0.0.toml)
  └── [[binaries]]
        url    = "https://github.com/FreeSynergy/fs-browser/releases/..."
        sha256 = "abc123..."

fs-store (StoreReader)
  └── liest Katalog → lädt Binary → verifiziert Hash
        └── schreibt InstallRecord + fs-inventory-Eintrag
```

Für Pakete mit mehreren Binaries (z.B. Bots): mehrere `[[binaries]]`-Einträge,
ein GitHub-Release mit mehreren Artifacts.

---

Weiter: [Gesamtübersicht](uebersicht.md) | [Adapter-Pattern](../konzepte/adapter.md) | [Pakete](../konzepte/pakete.md)
