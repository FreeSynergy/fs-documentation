# Manager

[← Zurück zum Index](../INDEX.md) | [Store](../programme/store/README.md) | [Inventory](inventory.md)

---

## Was ein Manager ist

Ein **Manager** ist das Bindeglied zwischen dem Store (was möglich ist), dem Inventory (was installiert ist) und den Programmen (was sie brauchen).

```
Store → Manager → Inventory ← Programme / UI
```

- Der Manager liest aus dem Store was verfügbar ist
- Der Manager führt Aktionen aus (installieren, starten, stoppen, entfernen)
- **Der Manager schreibt das Ergebnis ins Inventory** — das Inventory ist danach die einzige Wahrheit
- Das UI zeigt ausschließlich was im Inventory steht — nie direkt was im Store steht
- Settings ruft Manager auf — hat selbst keine Logik für diese Bereiche

**Wichtig:** Ein Paket ist installiert — egal wie. Ob via UI, CLI, API, oder direkt — der Manager schreibt den Eintrag ins Inventory. Das Inventory fragt nicht, wie es dorthin kam.

Siehe: [Die drei Ebenen (Inventory-Konzept)](inventory.md)

## Warum Manager?

Ohne Manager verwaltet jedes Programm seinen eigenen Zustand:
- Desktop hat eine eigene Sprachauswahl
- Node hat eine eigene Sprachauswahl
- Beide können auseinanderlaufen

Mit Manager:
- Einmal geändert → überall aktualisiert
- Kein Dropdown im UI — das Element gehört dem LanguageManager
- Konsistenz durch Ownership

## Kontext-Bewusstsein

Nicht jeder Manager macht überall Sinn. Bilder in einem Terminal ergeben keinen Sinn — Sprache schon. Jedes Programm bindet nur die Manager ein, die es wirklich braucht.

## Verfügbare Manager (Repos)

| Repo | Crate | Zuständigkeit |
|---|---|---|
| `fs-managers` | `fs-manager-language` | Aktive Sprache lesen, setzen, UI-Picker |
| `fs-managers` | `fs-manager-theme` | Aktives Theme lesen, setzen, UI-Picker |
| `fs-desktop` | `fs-container-app` | Container-Apps installieren, starten, stoppen, entfernen → [Container Manager](../programme/container/README.md) |
| `fs-icons` | `fs-manager-icons` | Icon-Sets verwalten, Repositories, Pfade auflösen, UI Icon-Picker → [Icon Manager](../programme/icons/README.md) |
| `fs-bots` | `fs-manager-bot` | Bots benutzen: Broadcasts senden, Subscriptions, Gatekeeper → [BotManager](../programme/botmanager/README.md) |

## Standardisiertes Manager-Layout (G5)

**Kein übergeordneter Master-Manager.** Jeder Manager ist ein eigenständiges Programm.
Aber alle Manager sehen fast gleich aus — dank `ManagerLayout`-Trait in `fs-render`.

### Layout-Prinzip

```
┌──────────────────────────────────────────────────────┐
│  Sidebar (Navigation)   │  Content-Area              │
│                         │                            │
│  [Manager-spezifische   │  [Manager-spezifischer     │
│   Navigationspunkte]    │   Inhalt]                  │
│                         │                            │
│  Gleiche Struktur bei   │  Unterschiedlich je        │
│  allen Managern         │  Manager-Aufgabe           │
└──────────────────────────────────────────────────────┘
```

Die Sidebar ist bei allen Managern strukturell gleich aufgebaut (Kategorien, Status-Punkte,
Drill-down-Navigation). Der Content-Bereich rechts variiert je nach Aufgabe des Managers.

### ManagerLayout-Trait

`ManagerLayout` ist in `fs-render/src/manager.rs` definiert und von jedem
Manager in seinem `view.rs`-Shim implementiert — dem einzigen File das `fs-render` importiert:

```rust
// In fs-render/src/manager.rs
pub struct ManagerSidebarItem {
    pub id: &'static str,
    pub label: String,
    pub icon: &'static str,
}

pub trait ManagerLayout {
    fn title(&self) -> &'static str;
    fn sidebar_items(&self) -> Vec<ManagerSidebarItem>;
    fn content_for(&self, item_id: &str) -> Box<dyn FsWidget>;
}

// Im Manager (language/src/view.rs — einziges Bindeglied zu fs-render)
impl ManagerLayout for LanguageManager {
    fn title(&self) -> &'static str { "Language Manager" }

    fn sidebar_items(&self) -> Vec<ManagerSidebarItem> {
        vec![
            ManagerSidebarItem { id: "list",     label: t("managers-language-section-list"), icon: "🌐" },
            ManagerSidebarItem { id: "active",   label: t("managers-language-section-active"), icon: "✓" },
            ManagerSidebarItem { id: "download", label: t("managers-language-section-download"), icon: "⬇" },
            ManagerSidebarItem { id: "preview",  label: t("managers-language-section-preview"), icon: "👁" },
        ]
    }

    fn content_for(&self, item_id: &str) -> Box<dyn FsWidget> {
        match item_id {
            "list"     => list::widget(self),
            "active"   => active::widget(self),
            "download" => download::widget(self),
            "preview"  => preview::widget(self),
            _          => fallback_widget(item_id),
        }
    }
}
```

Das Domain-Objekt (`LanguageManager`) importiert **kein** `fs-render` direkt.
Nur `view.rs` (das Bindeglied) importiert fs-render.

**Implementiert von (G5 ✅):** LanguageManager, CursorManager, ThemeManager, IconManager, ContainerManager

### Standard-Sidebar-Elemente

Jeder Manager hat diese Sidebar-Bereiche (in dieser Reihenfolge):

1. **Liste** — das primäre Objekt (Sprachen, Themes, Icon-Sets, …)
2. **Aktiv** — was gerade aktiv ist (hervorgehoben)
3. **Aktionen** — installieren, entfernen, aktualisieren
4. **Info** — über den Manager selbst (Version, Backend)

Unterschiede zwischen Managern nur dort wo fachlich nötig — sonst identisch.

### Kein Master-Manager

Es gibt **keinen** übergeordneten Manager der alle anderen wrapping. Jeder Manager:
- ist ein eigenständiges Programm (eigenes Fenster)
- teilt das gleiche Layout via `ManagerLayout`-Trait
- wird direkt aus der Shell-Sidebar geöffnet

Die einheitliche Optik entsteht durch den gemeinsamen Trait — nicht durch Aggregation.

### Das Paket liefert das WAS — der Manager das WIE

Der Manager fragt das Paket via `Manageable`-Trait (siehe [Pakete → Manageable-Trait](pakete.md#manageable-trait)):
- `config_fields()` → welche Felder gibt es, welche Typen, welche Werte
- `check_health()` → sind alle Abhängigkeiten erfüllt
- `instances()` → gibt es Sub-Instanzen (für Bot/Container)

Der Manager rendert daraus eine fertige Oberfläche. Das Paket hat keinen UI-Code.

### ManagerViewModel

`ManagerViewModel::from_manageable()` extrahiert alle Anzeige-Daten in ein reines
Daten-Struct. Die View (`view.rs`) arbeitet ausschließlich mit dem ViewModel —
nie mit dem Trait-Objekt direkt.

## Settings Manager (`PackageSettingsView`)

Der **Settings Manager** aggregiert die `config_fields()` aller installierten Pakete in einer einzigen Ansicht:

```
Settings → Packages
  ├ kanidm     → Felder: Port, Secret, OIDC-URL, …
  ├ forgejo    → Felder: Admin-User, Port, …
  └ stalwart   → Felder: Domain, DKIM-Key, …
```

- Linke Sidebar: Paketliste mit Suchfilter
- Rechter Panel: Felder des gewählten Pakets (mit Hilfe-Text, Restart-Warnung)
- Felder ohne Hilfe-Text werden mit Warnung markiert (Doku-Pflicht)
- Eingabe: sofort on blur gespeichert

Die Komponente `PackageSettingsView` (in `fs-desktop/crates/fs-settings`) erhält eine `Vec<PackageSettingsEntry>` vom Desktop. Der Desktop erstellt die Einträge via `PackageSettingsEntry::from_manageable()`.

## Verwendung (Beispiel LanguageManager)

```rust
use fs_manager_language::LanguageManager;

let mgr = LanguageManager::new();
let lang = mgr.active();       // aktuelle Sprache
let all  = mgr.available();    // alle Sprachen
mgr.set_active("de")?;         // Sprache wechseln → schreibt in den Store
```

Der Manager liefert immer ein konsistentes Ergebnis — unabhängig davon wo er aufgerufen wird.

## UI-Integration

### Shell-Sidebar

In der System-Sektion der Shell-Sidebar gibt es einen **Managers**-Ordner mit Sub-Items (Language, Theme, Icons, Containers, Bots). Ein Klick öffnet die Sub-Ebene (Slide-Animation). Ein Pfeil-Button oben links führt zurück zur Haupt-Ebene.

```rust
FsSidebarItem::folder("Managers", "📦", vec![
    FsSidebarItem::new("language", "🌐", "Language"),
    FsSidebarItem::new("theme",    "🎨", "Theme"),
    // ...
])
```

### fs-managers Crate

Das Crate `fs-managers` (in `fs-desktop/crates/`) stellt die standardisierte `ManagerView`-Komponente bereit. Sie wird vom Desktop direkt mit einem `PackageViewModel` aufgerufen — kein separates App-Binary nötig.

## Berechtigungen

Manager können nur dann in den Store schreiben, wenn sie die entsprechende Berechtigung haben. Die Rechte-Kaskade gilt wie überall: Schreib-Rechte können nur vom Node-Owner vergeben werden.

Siehe: [Rechte-Kaskade](rechte.md)

## Icon Manager und Icon-Sets

Der Icon Manager liest das `manifest.toml` aus **fs-icons**, kennt alle installierten Sets (Name, Pfad, Icon-Anzahl) und stellt einen wiederverwendbaren Icon-Picker bereit. Er unterstützt mehrere Quell-Repositories analog zum Store.

Neue Icon-Sets werden in `fs-icons` als eigener Ordner hinzugefügt (z.B. `homarrlabs/`, `simpleicons/`). Der Icon Manager erkennt sie automatisch über das Manifest.

Siehe: [Icon Manager](../programme/icons/README.md) | [Repository Manager](repository-manager.md)

---

Weiter: [Store](../programme/store/README.md) | [Pakete → Manageable](pakete.md#manageable-trait) | [Icon Manager](../programme/icons/README.md) | [Repository Manager](repository-manager.md) | [Rechte-Kaskade](rechte.md) | [Themes](themes.md) | [BotManager](../programme/botmanager/README.md) | [Container Manager](../programme/container/README.md)
