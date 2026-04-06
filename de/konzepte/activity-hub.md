# Activity Hub

[← Zurück zum Index](../INDEX.md)

---

## Grundidee

Klassische Desktops fragen: "Welches Programm willst du öffnen?"
Der Activity Hub fragt: "**Was willst du tun?**"

Statt Programme zu verwalten, verwaltet der Mensch **Absichten (Activities)**.
Das passende Programm im Hintergrund ist ein Implementierungsdetail.

---

## Was ist eine Activity?

Eine Activity ist eine Kategorie von Tätigkeiten, nicht ein konkretes Programm.

Beispiele:
- "Wiki" — Information nachschlagen oder bearbeiten (Outline, Wiki.js, ...)
- "Code" — Quellcode lesen oder schreiben (Forgejo, Editor, ...)
- "Chat" — Kommunikation (Tuwunel/Matrix, ...)
- "Office" — Bürodokumente (Write, Tabelle, Präsentation)

---

## Nesting: Activities in Activities

Activities können beliebig tief geschachtelt werden:

```
Office (Activity — container, kein eigenes Engine)
├── Write        (Activity → z.B. OnlyOffice Writer)
├── Tabelle      (Activity → z.B. OnlyOffice Calc)
└── Präsentation (Activity → z.B. OnlyOffice Impress)
```

"Office" ist selbst eine Activity mit eigenem Icon und eigenen Aktionen.
Container-Activities haben kein Engine — sie fassen Sub-Activities zusammen.
Die Unter-Activities erben die Kategorie des Parents.

---

## Activity-Views

Jede Activity bietet folgende Einsprungpunkte:

| View | FTL-Key | Beschreibung |
|------|---------|-------------|
| **Neu** | `activity-view-new` | Neues Dokument / Datei / Eintrag / Termin erstellen |
| **Zuletzt bearbeitet** | `activity-view-recent` | Die N zuletzt bearbeiteten Elemente anzeigen |
| **Programme** | `activity-view-programs` | 2. Ebene: welches konkrete Programm nutzen? |

"Programme" erlaubt die explizite Programm-Auswahl wenn man sie braucht —
aber normalerweise ist das Standard-Programm voreingestellt.

---

## Standard-Programm + Start-View

Pro Activity konfigurierbar:
- **Standard-Programm:** welches Programm für "Neu" / "Öffnen" genutzt wird
- **Start-View:** mit welcher View die Activity standardmäßig öffnet

Diese Einstellung ist pro Programm und pro Activity individuell.

---

## ActivityEngine-Trait

Ein Programm bietet Activities an, indem es den `ActivityEngine`-Trait implementiert
(via Adapter, in `fs-render/src/activity.rs`):

```rust
pub trait ActivityEngine: Send + Sync {
    fn activity_id(&self) -> &str;
    fn activity_name_key(&self) -> &str;
    fn supported_actions(&self) -> Vec<ActivityAction>;
    fn default_view(&self) -> ProgramView;
    fn category(&self) -> ActivityCategory;
    fn can_be_default(&self) -> bool { true }  // default impl
}
```

**ActivityAction:** `New | Open | Recent | Browse | Custom(String)`

**ActivityCategory:** `Document | Communication | Media | Data | Code | System | Custom(String)`

Jede Variante hat eine `label_key()`-Methode die den FTL-Key liefert.

---

## Activity-Struct

`Activity` (in `fs-components/src/activity_hub.rs`) hält Engine + Sub-Activities:

```rust
pub struct Activity {
    pub id: String,
    pub icon: CompositeIcon,
    pub name_key: String,
    pub category: ActivityCategory,
    pub engine: Option<Arc<dyn ActivityEngine>>,  // None für Container-Activities
    pub sub_activities: Vec<Activity>,
}
```

Konstruktoren:
- `Activity::new(...)` — Leaf mit Engine
- `Activity::container(...)` — Container ohne Engine
- `.with_sub_activities(...)` — Builder-Style

`Activity` implementiert `FsView` → liefert `ActivityWidget` (CSS-Klasse `fs-activity`).

---

## Activity als eigenständiges Programm

Eine Activity kann verschieden implementiert sein:

| Art | Beschreibung |
|-----|-------------|
| **Eingebettet** | Kein eigener Container, Adapter läuft im Host-Prozess |
| **Container + Adapter** | Eigener Container, Adapter implementiert `ActivityEngine` |
| **Mit GUI** | Eigene GUI via `FsView`-Trait (optional) |
| **Im Store** | Als `program`-Paket mit `ActivityEngine`-Capability veröffentlicht |

Der Activity Hub fragt nur den Trait — die Implementierung dahinter ist egal.

---

## ActivityHub Registry

`ActivityHub` (in `fs-components/src/activity_hub.rs`):

```
ActivityHub
├── register(activity)            — Activity anmelden (Duplikat-ID wird ersetzt)
├── all() -> &[Activity]          — alle registrierten Activities
├── by_category(cat)              — nach ActivityCategory filtern
├── search(query)                 — Volltextsuche (id + name_key)
├── to_menu_items()               — MenuItemDescriptors für Corner/Side Menu
├── len() / is_empty()            — Anzahl
└── view_mode: ActivityHubView    — CornerMenuEntry | DesktopWidget | Both
```

Nur installierte Activities werden angezeigt (fs-inventory gRPC — in Produktion).
Der Store kann weitere Activities anbieten (dann: "installieren" Hinweis).

`ActivityHub` implementiert `FsView` → liefert `ActivityHubWidget` (CSS-Klasse `fs-activity-hub`).

---

## ActivityHubView

```rust
pub enum ActivityHubView {
    CornerMenuEntry,  // als Eintrag in einem Corner Menu
    DesktopWidget,    // als eigenständiges Widget auf dem Desktop-Hintergrund
    Both,             // beides gleichzeitig aktiv
}
```

Konfigurierbar in Settings > Ansicht.

---

## Navigation-Integration

`Activity::to_menu_item()` konvertiert eine Activity (inkl. Sub-Activities) in
einen `MenuItemDescriptor` — kompatibel mit G1.1/G1.2/G1.3 Corner/Side Menus.

Action-String: `"activity:open:{id}"` — wird vom Desktop-Shell-Dispatcher verarbeitet.

---

## Im Store

Activities sind Store-Artifacts:
- Im Store als `program`-Paket mit Capability `activity.engine.<id>`
- Adapter wird automatisch mitinstalliert
- Adapter registriert Capability in fs-registry
- Activity Hub liest fs-registry → weiß was verfügbar ist

---

## Beziehung zum Program-Modell

Activities sind **unabhängig** von Programmen, aber verbunden:

```
InstalledResource (fs-inventory)
  └── ProgramGroup (mehrere Instanzen)
        └── caption: "Wiki.js — helfe.org"

Activity "Wiki"
  └── engine: WikiJsActivityEngine (Adapter)
        └── wraps: WikiJsAdapter
              └── connected to: InstalledResource "wikijs"
```

Ein Programm kann mehrere Activities anbieten.
Eine Activity kann von mehreren Programmen angeboten werden (Auswahl in "Programme"-View).

---

## i18n

Alle Texte in `fs-i18n/locales/{lang}/activity-hub.ftl`.
Keys in `fs-components` direkt als String-Literale (kein separates keys.rs nötig —
die FTL-Keys sind in der FTL-Datei und im Code konsistent benannt).

---

## Implementierungsstand (G1.6)

| Komponente | Status |
|-----------|--------|
| `ActivityAction` + `ActivityCategory` + `ActivityEngine` trait | ✅ fs-render |
| `Activity` + `ActivityHub` + Widget-Typen | ✅ fs-components |
| i18n: `activity-hub.ftl` (en + de) | ✅ fs-i18n |
| Anbindung an Corner Menu (G1.5) | ⏳ G1.5 |
| fs-inventory gRPC Filter | ⏳ nach G1.4 |
| Adapter-Impls (Wiki, Chat, Code, ...) | ⏳ nach G1.4 |
