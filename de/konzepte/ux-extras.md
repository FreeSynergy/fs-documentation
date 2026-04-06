# UX-Extras (G1.9)

[← Zurück zum Index](../INDEX.md)

---

## Übersicht

G1.9 erweitert das FreeSynergy Desktop um zwölf UX-Features.
Alle Typen sind engine-agnostisch in `fs-render/src/ux_extras.rs` definiert.
Komponenten-Implementierungen leben in `fs-components/src/ux_extras.rs`.
Shell-Integration liegt in `fs-gui-workspace/src/shell.rs`.

---

## Design Patterns

| Feature | Pattern |
|---|---|
| Status-Badges | Decorator (`BadgedIcon` wraps `CompositeIcon`) |
| Thumbnail-Preview | Observer (`ThumbnailSource` trait) |
| Focus Mode / Window Layout | State Machine (`WindowLayoutMode` enum) |
| Quick Switch Overlay | Command (`QuickSwitchCommand` trait) |
| Notification Center | Facade (`NotificationCenter` aggregiert Toasts + Bus) |
| Workspace Profiles | Strategy (`WorkspaceProfileManager` trait) |
| Touch Gestures | Observer (`TouchHandler` trait) |
| Pinboard Widget | Strategy (`PinboardStore` trait) |
| Auto Dark/Light | Strategy (`AutoThemeSchedule` + `ThemeScheduler`) |
| Breadcrumb in Titlebar | Observer (`BreadcrumbProvider` trait) |
| Global Clipboard History | Strategy (`ClipboardHistory` trait) |
| Window Snap | Strategy (`WindowSnapManager` trait) |

---

## 1. Status-Badges (`BadgeKind` + `BadgedIcon`)

```rust
pub enum BadgeKind {
    Unread(u32),       // rote Zahl — 0 = versteckt
    UpdateAvailable,   // Punkt
    Error,             // Ausrufezeichen
    Running,           // Kreis
}

pub struct BadgedIcon {
    pub icon: CompositeIcon,
    pub badges: Vec<BadgeKind>,
}
```

`BadgedIcon::plain(icon)` wraps a `CompositeIcon` ohne Badge.
`.with_badge(BadgeKind::Unread(3))` fügt Badges hinzu (Decorator).
Engines rendern Badges als Overlay in der Icon-Ecke.

---

## 2. Thumbnail-Preview (`ThumbnailSource`)

```rust
pub trait ThumbnailSource: Send + Sync {
    fn window_id(&self) -> &str;
    fn capture(&self, max_w: u32, max_h: u32) -> Option<ThumbnailData>;
}
```

Laufende Programme implementieren diesen Trait.
Die Engine ruft `capture()` beim Hover über Task-Ikons.
`ThumbnailData` enthält rohe RGBA-Bytes (width × height × 4).

---

## 3. Window Layout Mode (`WindowLayoutMode`)

```rust
pub enum WindowLayoutMode {
    Normal,     // Floating Windows
    Tiling,     // Automatisches Tiling
    FocusMode,  // Nur ein Fenster sichtbar
}
```

`mode.next()` zykliert: `Normal → Tiling → FocusMode → Normal`.
Der Titlebar-Button zeigt das aktuelle Symbol (⊡ / ⊞ / ⊟).
Im `FocusMode` rendert die Shell nur den Hauptinhalt ohne Chrome.

---

## 4. Quick Switch Overlay (`QuickSwitchCommand`)

```rust
pub trait QuickSwitchCommand: Send + Sync {
    fn open_windows(&self) -> Vec<QuickSwitchEntry>;
    fn activate(&self, window_id: &str);
    fn close(&self, window_id: &str);
}
```

Öffnet sich über `DesktopMessage::QuickSwitchToggle` (Alt+Tab-Ersatz).
`QuickSwitchEntry` enthält Fenster-ID, Titel, Icon-Key, optionales Thumbnail.
Tastaturnavigierbar; funktioniert in iced + bevy (nicht TUI).

---

## 5. Notification Center (`NotificationCenter`)

```rust
pub struct NotificationCenter { /* next_id, entries */ }

impl NotificationCenter {
    fn push(&mut self, level, title, body, timestamp) -> u64;
    fn mark_read(&mut self, id);
    fn mark_all_read(&mut self);
    fn dismiss(&mut self, id);
    fn all(&self) -> Vec<&NotificationEntry>;  // newest first
    fn unread_count(&self) -> u32;
}
```

Aggregiert alle Notifications dauerhaft (im Gegensatz zu Auto-expire-Toasts).
`NotificationCenterPanel`-Komponente zeigt die Liste + "Alle gelesen"-Button.
Öffnet sich über `DesktopMessage::NotificationCenterToggle`.

---

## 6. Workspace Profiles (`WorkspaceProfileManager`)

```rust
pub trait WorkspaceProfileManager: Send + Sync {
    fn profiles(&self) -> Vec<WorkspaceProfile>;
    fn active_profile(&self) -> Option<&WorkspaceProfile>;
    fn save(&mut self, profile: WorkspaceProfile);
    fn delete(&mut self, profile_id: &str);
    fn activate(&mut self, profile_id: &str);
}
```

`WorkspaceProfile` enthält ID, Name-Key, `WindowLayoutMode`, Icon-Key, Default-Apps.
`WorkspaceProfilePanel`-Komponente listet Profile und bietet Aktivieren + Speichern.
Konfigurierbar in Settings > Ansicht (via G1.8 Settings-Seiten).

---

## 7. Touch Gestures (`TouchHandler`)

```rust
pub enum TouchGesture {
    Swipe { zone: SwipeZone },
    Pinch { scale: f32 },
    Rotate { angle_radians: f32 },
}

pub trait TouchHandler: Send + Sync {
    fn on_gesture(&self, gesture: TouchGesture);
}
```

`SwipeZone` deckt alle 4 Kanten + 4 Ecken ab.
Swipe von Ecke → Corner Menu öffnen.
Swipe von Kante → Side Menu öffnen.
Pinch → Desktop-Zoom (Engine-abhängig).

---

## 8. Pinboard Widget (`PinboardStore`)

```rust
pub struct PinboardNote {
    pub id: String,
    pub content: String,
    pub x: f32,   // normalisiert [0.0, 1.0]
    pub y: f32,
    pub color_key: Option<String>,
}
```

Notizen werden auf dem Desktop-Hintergrund platziert.
`PinboardStore` trait: `notes()`, `add()`, `update()`, `remove()`.
`InMemoryPinboard` als Test-/Headless-Impl vorhanden.

---

## 9. Auto Dark/Light (`AutoThemeSchedule`)

```rust
pub struct AutoThemeSchedule {
    pub light_from: TimeOfDay,   // default: 07:00
    pub dark_from: TimeOfDay,    // default: 20:00
}

impl AutoThemeSchedule {
    pub fn is_light_at(&self, current: TimeOfDay) -> bool { ... }
}
```

Der `ClockTick`-Handler (alle 30 s) prüft `is_light_at(now)` und
schaltet `dark_mode` automatisch um, wenn konfiguriert.
Konfigurierbar in Settings > Ansicht (Zeitfenster).

---

## 10. Breadcrumb in Titlebar (`BreadcrumbProvider`)

```rust
pub trait BreadcrumbProvider: Send + Sync {
    fn breadcrumbs(&self) -> Vec<BreadcrumbItem>;
}
```

`BreadcrumbItem` hat Label, optionalen Icon-Key, optionales `target_id` für Rücknavigation.
Bereits existierendes `header.rs::Breadcrumb` ist engine-seitig kompatibel.
Programme mit hierarchischer Navigation (Browser, Store, Docs) implementieren diesen Trait.

---

## 11. Global Clipboard History (`ClipboardHistory`)

```rust
pub trait ClipboardHistory: Send + Sync {
    fn entries(&self) -> Vec<&ClipboardEntry>;
    fn push(&mut self, content: ClipboardContent, timestamp: u64);
    fn set_pinned(&mut self, id: u64, pinned: bool);
    fn remove(&mut self, id: u64);
    fn search(&self, query: &str) -> Vec<&ClipboardEntry>;
    fn capacity(&self) -> usize;
}
```

`ClipboardContent`: `Text(String)` | `ImagePath(String)` | `Uri(String)`.
Auto-Truncation auf `capacity` (default: 50) unpinned Einträge.
Pinned Einträge überleben Truncation.
Über Search-Komponente abrufbar (Kategorie "Clipboard").
Lokaler Store — kein Cloud-Sync; Verschlüsselung in Produktions-Impl.

---

## 12. Window Snap (`WindowSnapManager`)

```rust
pub trait WindowSnapManager: Send + Sync {
    fn config(&self) -> &SnapConfig;
    fn set_config(&mut self, config: SnapConfig);
    fn snap_rect(&self, zone: SnapZone, screen_w: u32, screen_h: u32) -> (u32, u32, u32, u32);
    fn auto_arrange(&self, window_ids: &[String], screen_w: u32, screen_h: u32)
        -> Vec<(String, u32, u32, u32, u32)>;
}
```

`SnapZone`: Left, Right, Top, Bottom, TopLeft, TopRight, BottomLeft, BottomRight, Center.
`SnapConfig`: columns (2|3|4), rows (1|2), gap, enabled.
`auto_arrange()` ordnet alle offenen Fenster im konfigurierten Raster an.
`WindowSnapStatusWidget` zeigt Status + Toggle in der Shell-Komponente.

---

## Dateien

| Datei | Inhalt |
|---|---|
| `fs-render/src/ux_extras.rs` | Alle Traits + Datentypen + In-memory Impls |
| `fs-render/src/lib.rs` | Re-exports |
| `fs-components/src/ux_extras.rs` | 6 Komponenten (ComponentTrait) |
| `fs-components/src/lib.rs` | Re-exports |
| `fs-gui-workspace/src/shell.rs` | Shell-Integration (State + Messages + View) |
| `fs-i18n/locales/{en,de}/desktop.ftl` | 40 neue FTL-Keys |

---

## Abhängigkeiten

```
fs-render ← fs-components ← fs-gui-workspace
                               ↑ nutzt: WindowLayoutMode, InMemorySnapManager,
                                        AutoThemeSchedule, NotificationCenter
```
