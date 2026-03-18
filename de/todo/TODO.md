# TODO-Liste

[← Zurück zum Index](../INDEX.md) | [Bugs](BUGS.md)

**Regeln:**
- Jeder Punkt wird KOMPLETT umgesetzt. Keine Stubs.
- IMMER `cargo build` vor und nach jeder Änderung.
- Altes das nicht passt → LÖSCHEN und neu machen.
- Kein Menüpunkt ohne Funktion. Kein Button der nichts tut.
- Begriffe: **App** (nicht Programm), **Container-App** (nicht Container-Service), **Bundle** (nicht Gruppe), **Ressource** (alles im Store)

---

## Phase A–F: ✅ ERLEDIGT

Siehe Git-History. Fundament, Themes, Store, S3, Widgets, Conductor — alles implementiert.

---

## Phase G: Ressourcen-System & Inventory ✅

```
G1. [x] ResourceMeta Struct (fsn-types/resources/meta.rs)
    - ResourceType enum (16 Varianten: App, ContainerApp, Bundle, Widget, Bot, Bridge,
      Task, Language, ColorScheme, Style, FontSet, CursorSet, IconSet, ButtonStyle,
      WindowChrome, AnimationSet)
    - ValidationStatus (Ok, Incomplete, Broken) mit badge() ✅⚠️❌
    - Dependency struct (required/optional, version_req)
    - Role newtype wrapper

G2. [x] Typ-spezifische Structs (fsn-types/resources/)
    - AppResource (platforms, binary_name, locales, cli_commands, api_endpoints,
      roles_provided, roles_required)
    - ContainerAppResource (compose_yaml, services[], variables[], networks, volumes,
      apis, roles_provided, roles_required)
      inkl. ContainerVariable (VarType, AutoSource: InternalService/RoleVariable)
    - WidgetResource (required_roles mit ANY/ALL Modus, data_sources, sizes)
    - BotResource (channels, commands, triggers, tokens_required)
    - BridgeResource (target_role, target_service, methods[] mit FieldMapping)
    - BundleResource (packages[], theme mit ThemeBundleRefs)
    - ColorScheme, FontSet, CursorSet, IconSet, ButtonStyle, WindowChrome, AnimationSet

G3. [x] Style als standardisierte Ressource (StyleResource)
    - Striktes Schema: 19 Pflichtfelder (radius, spacing, shadows, borders,
      scrollbar, sidebar, transitions)
    - Validator: Alle Felder müssen vorhanden sein → sonst Broken
    - StyleTokens::default_tokens() liefert FreeSynergy-Standardwerte
    - Im Store einzeln ladbar

G4. [x] fsn-inventory Crate (eigene SQLite: fsn-inventory.db)
    - InstalledResource (resource_type, version, channel, status, config_path,
      data_path, validation)
    - ServiceInstance (instance_name, roles_provided, roles_required, bridges,
      variables, network, port, s3_paths)
    - BridgeInstance (role, service_instance, api_base_url, status)
    - Sea-ORM Entities + Migrations im SCHEMA const
    - Inventory::services_with_role(role) / bridges_for_role(role)

G5. [x] Validate trait für alle Ressource-Typen (fsn-types/resources/validator.rs)
    - Einheitliches Validate trait mit validate() → meta.status wird gesetzt
    - required_methods_for_role(role) definiert Minimal-API für iam/wiki/git/chat/
      database/cache/smtp/llm/map/tasks/monitoring
    - Bridge: alle Pflicht-Methoden gemappt → sonst Incomplete
    - Bundle: mindestens eine Referenz → sonst Broken
    - Container-App: YAML + Services + Healthcheck + Variablen-Beschreibungen
    - 61 Unit-Tests grün
```

## Phase H: Bridges & Rollen-APIs ✅

```
H1. [x] Rollen-API-Definitionen (fsn-types/resources/role_api.rs)
    - Typed request/response structs für alle 11 Rollen
    - IamUser*, WikiPage*, GitRepo*, ChatChannel*, DbQuery*, Cache*, Mail*, Llm*, Map*, Task*, Alert*

H2. [x] Bridge-Framework (fsn-bridge Crate in FreeSynergy.Lib)
    - BridgeExecutor: nimmt BridgeResource + base_url, führt HTTP-Calls aus
    - FieldMapping wird auf Request + Response angewendet
    - BridgeError Enum

H3. [x] Erste Bridges implementiert (fsn-bridge/src/catalog.rs)
    - kanidm_iam_bridge() → BridgeResource mit allen 8 IAM-Methoden
    - outline_wiki_bridge() → BridgeResource mit allen 4 Wiki-Methoden
    - forgejo_git_bridge() → BridgeResource mit allen 4 Git-Methoden
    - Alle validieren als ✅ Ok (Tests grün)

H4. [x] BridgeDispatcher (Inventory ↔ Bridge Integration)
    - BridgeDispatcher::execute(role, method, params) → Value
    - Sucht aktive BridgeInstance im Inventory für gegebene Rolle
    - Lädt BridgeResource aus Katalog, delegiert an BridgeExecutor
    - Bus-Integration folgt in Phase J
```

## Phase I: Resource Builder ✅

```
I1. [x] Builder-CLI (cli/crates/fsn-builder/)
    - fsn-builder analyze <compose.yml> → ContainerAppResource (TOML/JSON)
    - fsn-builder validate <dir> → ✅⚠️❌ mit Message
    - fsn-builder publish <dir> → signieren + git clone/push zum Store

I2. [x] Container-App-Analyse-Pipeline (fsn-builder/src/analyze.rs)
    - Docker Compose YAML → ContainerAppResource (vollständig typisiert)
    - Primary-Service-Erkennung (Infra vs. App)
    - Variablen-Analyse: Typ (Secret/Url/Hostname/Port/…) + Rolle + Konfidenz
    - AutoSource: InternalService (Sibling) oder RoleVariable (Inventory)
    - Netzwerk auto-generieren ({servicename}-backend)
    - Volumes → S3-Pfade vorschlagen
    - 5 Unit-Tests grün

I3. [x] Builder-UI im Desktop (fsd-studio → fsd-builder umbenannt)
    - Tab "Container App": YAML-Paste → ContainerAppResource, Variablen-Tabelle
      mit Typ + Rolle + Pflicht-Badge, Validierungs-Anzeige ✅⚠️❌
    - Tab "Bridge": BridgeBuilder — Rolle wählen, Methoden-Checkliste, validieren
    - "Save Locally" + "Publish to Store" Buttons (publish via CLI)
    - i18n Editor + Resource Browser bleiben erhalten
    - AI Assist (Ollama) für Metadaten-Anreicherung
```

## Phase J: Message Bus

```
J1. [ ] Bus-Grundstruktur (Pub/Sub + Direct Messages)
J2. [ ] Rollen-basierte Adressierung (nie direkt an Service)
J3. [ ] Subscription-Manager (Rolle + Topic + Instanz-Tag Filter)
J4. [ ] Nachrichtentypen (Fire&Forget, Guaranteed, Standing Order)
J5. [ ] Speicherungs-Layer (NoStore, UntilAck, Persistent)
J6. [ ] Konfigurierbare Default-Zuordnung (regelbasiert, TOML)
J7. [ ] Standing Orders Engine
J8. [ ] Bridges (Bus-zu-Bus, Rechte-Kaskade, doppelter Checkpoint)
J9. [ ] Bus-API (CLI, REST, WebSocket)
```

## Phase K: Browser

```
K1. [ ] Browser-View im Desktop
    - URL-Leiste
    - WebView-Rendering (Dioxus WebView)
    - Tabs für mehrere Seiten

K2. [ ] Download-Handler
    - Downloads abfangen → S3 /shared/downloads/

K3. [ ] Service-Integration
    - Klick auf Service im Conductor → öffnet dessen Web-UI im Browser
    - Auto-Auth: IAM-Token mitschicken

K4. [ ] Lesezeichen + History (SQLite)
```

## Phase L: Lenses

```
L1. [ ] Lens-Datenmodell (SQLite)
L2. [ ] Lens-View (gruppiert nach Rolle, Summary + Link → öffnet im Browser)
L3. [ ] Lens als Desktop-Icon
```

## Phase M: Search

```
M1. [ ] Search-View (Suchfeld, gruppierte Ergebnisse, Preview + Link)
M2. [ ] Service-Suche (Ebene 1)
M3. [ ] Host-Suche (Ebene 2, Bus-aggregiert)
M4. [ ] Föderale Suche (Ebene 3-4, nur mit search-Recht)
```

## Phase N: Bots

```
N1. [ ] Bot-Framework
N2. [ ] Broadcast-Bot (Telegram)
N3. [ ] Gatekeeper-Bot
```

## Phase O: Tasks

```
O1. [ ] Data Offers/Accepts
O2. [ ] Task Builder UI
O3. [ ] Task-Templates aus Store
```

## Phase P: Node (Invite, Federation)

```
P1. [ ] Invite-System (Token, verschlüsselte TOML, Port pro Einladung)
P2. [ ] Federation-Grundstruktur (Domain-Pflicht, Auth-Broker)
P3. [ ] Rechte-Kaskade (read/write/execute/search, Audit-Log)
P4. [ ] Föderaler Bus (Bridge-Konfiguration)
```

## Phase Q: Shortcuts, Menü, Profil, Polish

```
Q1. [ ] Action Registry + konfigurierbare Shortcuts
Q2. [ ] Hilfe: Auto-generierte Shortcut-Referenz
Q3. [ ] Menü: JEDER Punkt ruft echte Aktion auf
Q4. [ ] Profil: IAM + editierbar + Account-Linking + S3-Visitenkarte
Q5. [ ] Notification Bell
Q6. [ ] Context-Menüs
Q7. [ ] Animationen konfigurierbar
Q8. [ ] Alle Stubs/toten Code entfernen
```

---

## Reihenfolge

```
✅ Erledigt: A-F  (Fundament, Themes, Store, S3, Widgets, Conductor)
✅ Erledigt: G    (Ressourcen-System & Inventory)
✅ Erledigt: H    (Bridges & Rollen-APIs)
✅ Erledigt: I    (Resource Builder — Builder-UI, CLI, Analyse-Pipeline)

Prio 1:  J1-J9      Message Bus
Prio 2:  K1-K4      Browser
Prio 3:  L1-L3      Lenses
Prio 4:  M1-M4      Search
Prio 5:  N1-N3      Bots
Prio 6:  O1-O3      Tasks
Prio 7:  P1-P4      Node (Invite + Federation)
Prio 8:  Q1-Q8      Polish
Prio 4:  J1-J9      Message Bus
Prio 5:  K1-K4      Browser
Prio 6:  L1-L3      Lenses
Prio 7:  M1-M4      Search
Prio 8:  N1-N3      Bots
Prio 9:  O1-O3      Tasks
Prio 10: P1-P4      Node (Invite + Federation)
Prio 11: Q1-Q8      Polish
```
