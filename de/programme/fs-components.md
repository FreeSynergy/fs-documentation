# fs-components

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-components` · `/home/kal/Server/fs-components/`
**Typ:** Library (kein Container)
**Capabilities:** keine (reine App-Komponenten-Library)

---

## Was ist das?

`fs-components` enthält wiederverwendbare App-Level-Komponenten — eine Ebene höher als `fs-render`.
Während `fs-render` die engine-agnostischen Traits und Primitives definiert, bietet `fs-components`
fertige, konkrete Bausteine für typische App-Bereiche: Navigation, Activity Hub, UX-Extras.

**Kein Dioxus.** Alle Komponenten basieren auf dem `FsView`-Pattern und `LayoutElement`-Bäumen
aus `fs-render` — engine-unabhängig.

---

## Architektur

```
fs-render (Traits, Primitives)
    └── fs-components
            navigation_menu.rs  — CornerMenu, SideMenu, SidebarPanel  (G1.3)
            activity_hub.rs     — Activity, ActivityHub, ActivityHubView  (G1.6)
            ux_extras.rs        — UX-Extra-Komponenten (Badges, Overlays, …)  (G1.9)
            toast_bus.rs        — Async Broadcast-Channel für Toast-Nachrichten
            [weitere UI-Module: button, card, chat, form, input, modal, …]
```

Design Patterns:
- **Composite** (MenuTree via `MenuItemDescriptor`-Nesting)
- **Registry** (ActivityHub: `register`, `by_category`, `search`)
- **Strategy** (ActivityEngine pro Programm)
- **Decorator** (BadgedIconWidget: Icon + Badges)
- **Command** (QuickSwitchOverlay → QuickSwitchCommand)
- **Facade** (NotificationCenterPanel)

---

## Navigation-Komponenten (G1.3)

Modul `navigation_menu.rs` — implementiert `CornerMenuDescriptor` / `SideMenuDescriptor`
aus `fs-render` und liefert domain-typische Konfigurationen.

### `CornerMenu`

Radiales Ecken-Menü mit Viertelkreis-Indikator.

```
CornerMenuConfig: base_size, max_size, spread, scroll_fallback
CornerMenu: id, corner: Corner, items: Vec<MenuItemDescriptor>, config: CornerMenuConfig
  → impl CornerMenuDescriptor
  → impl HoverMagnification
  → impl FsView  (produziert Widget-Descriptor)
CornerMenuWidget: FsWidget-Impl
```

### `SideMenu`

Accordion-Seitenmenü mit Halbkreis-Indikator.

```
SideMenuConfig: base_size, max_size, spread, distribution: Distribution, scroll_fallback
SideMenu: id, side: Side, items: Vec<MenuItemDescriptor>, config: SideMenuConfig
  → impl SideMenuDescriptor
  → impl HoverMagnification
  → impl FsView
SideMenuWidget: FsWidget-Impl
```

### `SidebarPanel`

Overlay-Sidebar: kommt über den Content-Bereich, verschiebt ihn **nicht**.
Geeignet für Help-, AI- und Notification-Seitenfenster.

```
SidebarPanelConfig: side: Side, width_px: u32, scroll_fallback
SidebarPanel: id, side, title_key, items: Vec<MenuItemDescriptor>, config
  → impl FsView
SidebarPanelWidget: FsWidget-Impl
```

---

## Activity Hub (G1.6)

Modul `activity_hub.rs` — absichts-zentrische Navigation. Registriert alle
verfügbaren Activities; Engine-Wechsel ändert keinen App-Code.

### `Activity`

```
Activity {
    id:             String,            // z.B. "wiki", "office.write"
    icon:           CompositeIcon,
    name_key:       String,            // FTL-Key
    category:       ActivityCategory,
    engine:         Option<Arc<dyn ActivityEngine>>,
    sub_activities: Vec<Activity>,     // Composite: beliebig tief
}

Konstruktoren:
  Activity::new(id, icon, name_key, category, engine)        — Blatt-Activity
  Activity::container(id, icon, name_key, category, subs)    — Container ohne Engine
  activity.with_sub_activities(subs)                         — Builder
```

### `ActivityHub` (Registry)

```
ActivityHub {
    activities:  Vec<Activity>,
    view_mode:   ActivityHubView,    // CornerMenuEntry | DesktopWidget | Both
}

Methoden:
  register(activity)              — Activity hinzufügen
  all()                           — alle Activities
  by_category(cat)                — gefiltert nach ActivityCategory
  search(query)                   — Volltextsuche über id + name_key
  to_menu_items()                 → Vec<MenuItemDescriptor>  — für CornerMenu-Integration
```

```
ActivityHubView:
  CornerMenuEntry   — nur im Corner-Menü (TL/TR)
  DesktopWidget     — als eigenständiges Desktop-Widget
  Both              — beides gleichzeitig
```

### Widgets

```
ActivityWidget     — CSS-Klasse "fs-activity",     FsView auf Activity
ActivityHubWidget  — CSS-Klasse "fs-activity-hub", FsView auf ActivityHub
```

---

## UX-Extra-Komponenten (G1.9)

Modul `ux_extras.rs` — alle Komponenten nutzen `LayoutElement`-Bäume, kein Dioxus.

| Komponente | Pattern | Beschreibung |
|---|---|---|
| `BadgedIconWidget` | Decorator | Rendert `BadgedIcon` mit Status-Overlays (Unread, Error, Running, Update) |
| `QuickSwitchOverlay` | Command | Alt+Tab-Ersatz: listet offene Fenster, ruft `QuickSwitchCommand::activate()` auf |
| `NotificationCenterPanel` | Facade | Zeigt `NotificationEntry`-History mit Dismiss-Button |
| `WorkspaceProfilePanel` | Strategy | Profil-Liste + Aktivierungs-Button via `WorkspaceProfileManager` |
| `ClipboardHistoryPanel` | Strategy | Clipboard-Einträge (Text/Image/File) via `ClipboardHistory` |
| `PinboardPanel` | Strategy | Notiz-Pins via `PinboardStore` |
| `WindowSnapPanel` | Strategy | Snap-Zonen-Picker via `WindowSnapManager` |
| `AutoThemePanel` | Observer | Zeitplan-Einstellungen via `AutoThemeManager` |
| `BreadcrumbBar` | Strategy | Navigationspfad via `BreadcrumbProvider` |
| `TouchOverlay` | Observer | Touch-Gesten weiterleiten an `TouchHandler` |

---

## Toast Bus (`toast_bus.rs`)

Immer kompiliert (kein Feature-Flag nötig). Async Broadcast-Channel für
Toast-Nachrichten — entkoppelt Sender von der Toast-UI.

```rust
let (tx, rx) = ToastBus::channel();
tx.send(ToastMessage::info("Gespeichert")).await?;
// ToastWidget konsumiert rx und rendert die Nachrichten
```

---

## i18n

Alle Keys in `fs-i18n/locales/{lang}/navigation.ftl` und
`fs-i18n/locales/{lang}/activity-hub.ftl`.

---

## Abhängigkeiten

| Crate | Rolle |
|---|---|
| `fs-render` | Traits + Primitives (FsView, FsWidget, LayoutElement, …) |
| `fs-theme` | Farben + CSS-Variablen |
| `fs-i18n` | Übersetzungen |

---

Siehe auch:
[fs-render](fs-render.md) ·
[konzepte/navigation-menus.md](../konzepte/navigation-menus.md) ·
[konzepte/activity-hub.md](../konzepte/activity-hub.md) ·
[konzepte/ux-extras.md](../konzepte/ux-extras.md)
