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

## Verfügbare Manager

Alle Manager leben im Repo **FreeSynergy.Managers** (`git@github.com:FreeSynergy/Managers.git`).

| Unterordner | Crate | Zuständigkeit |
|---|---|---|
| `language/` | `fsn-manager-language` | Aktive Sprache lesen, setzen, UI-Picker |
| `theme/` | `fsn-manager-theme` | Aktives Theme lesen, setzen, UI-Picker |
| `container_app/` | `fsn-manager-container-app` | Container-Apps installieren, starten, stoppen, entfernen → [Container App Manager](../programme/container_app/README.md) |
| `icons/` | `fsn-manager-icons` | Icon-Sets verwalten, Repositories, Pfade auflösen, UI Icon-Picker → [Icon Manager](../programme/icons/README.md) |
| `bots/` | `fsn-manager-bot` | Bots benutzen: Broadcasts senden, Subscriptions, Gatekeeper → [BotManager](../programme/botmanager/README.md) |

## Verwendung

```rust
use fsn_manager_language::LanguageManager;

let mgr = LanguageManager::new();
let lang = mgr.active();       // aktuelle Sprache
let all  = mgr.available();    // alle Sprachen
mgr.set_active("de")?;         // Sprache wechseln → schreibt in den Store
```

Der Manager liefert immer ein konsistentes Ergebnis — unabhängig davon wo er aufgerufen wird.

## UI-Integration

### Shell-Sidebar

In der System-Sektion der Shell-Sidebar gibt es einen **Managers**-Ordner mit fünf Sub-Items: Language, Theme, Icons, Container Apps, Bots. Ein Klick auf den Ordner öffnet die Sub-Ebene (Slide-Animation). Ein Pfeil-Button oben links führt zurück zur Haupt-Ebene.

Die Folder-Navigation basiert auf `FsnSidebarItem::folder()` aus `FreeSynergy.Lib.UI`:

```rust
FsnSidebarItem::folder("Managers", Icon::Folder, vec![
    FsnSidebarItem::new("Language", Icon::Language, AppTarget::Managers),
    FsnSidebarItem::new("Theme",    Icon::Theme,    AppTarget::Managers),
    // ...
])
```

Items mit nicht-leerem `children`-Feld sind Folder-Items. Klick → Drill-down, kein App-Start.

### fsd-managers App

Das Crate `fsd-managers` (im Desktop-Repo) stellt die `ManagersApp` bereit — eine eigenständige App im LayoutB-Stil mit eigener Sidebar. Alle fünf Manager (Language, Theme, Icons, Container Apps, Bots) sind als Panels integriert. Die App wird über den App-Key `"app-managers"` registriert und von allen Sidebar-Sub-Items geöffnet.

## Berechtigungen

Manager können nur dann in den Store schreiben, wenn sie die entsprechende Berechtigung haben. Die Rechte-Kaskade gilt wie überall: Schreib-Rechte können nur vom Node-Owner vergeben werden.

Siehe: [Rechte-Kaskade](rechte.md)

## Icon Manager und Icon-Sets

Der Icon Manager liest das `manifest.toml` aus **FreeSynergy.Icons**, kennt alle installierten Sets (Name, Pfad, Icon-Anzahl) und stellt einen wiederverwendbaren Icon-Picker bereit. Er unterstützt mehrere Quell-Repositories analog zum Store.

Neue Icon-Sets werden in FreeSynergy.Icons als eigener Ordner hinzugefügt (z.B. `homarrlabs/`, `simpleicons/`). Der Icon Manager erkennt sie automatisch über das Manifest.

Siehe: [Icon Manager](../programme/icons/README.md) | [Repository Manager](repository-manager.md)

---

Weiter: [Store](../programme/store/README.md) | [Icon Manager](../programme/icons/README.md) | [Repository Manager](repository-manager.md) | [Rechte-Kaskade](rechte.md) | [Themes](themes.md) | [BotManager](../programme/botmanager/README.md) | [Container App Manager](../programme/container_app/README.md)
