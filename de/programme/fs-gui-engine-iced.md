# fs-gui-engine-iced

**iced / libcosmic Render-Engine für FreeSynergy**

Implementiert alle `fs-render`-Traits auf Basis der
[iced](https://iced.rs/) 0.13 GUI-Bibliothek.  Consumer-Code importiert **nur**
`fs-render` — niemals dieses Crate direkt.

---

## Architektur

```
fs-render (Traits — keine Engine-Abhängigkeit)
    └── fs-gui-engine-iced
            IcedEngine  → implementiert RenderEngine
            IcedWindow  → implementiert FsWindow
            IcedWidget  → implementiert FsWidget
            IcedTheme   → implementiert FsTheme
            mvu         → Elm-Muster (Model–View–Update)
            capability  → "render.engine.iced" für fs-registry
```

**Adapter Pattern**: `IcedEngine` adaptiert die iced-API an die
`RenderEngine`-Schnittstelle.  Der Desktop-Shell kennt nur `RenderEngine` —
die konkrete Engine wird über Cargo-Feature-Flags gewählt.

---

## Module

### `IcedEngine` — `RenderEngine`-Implementierung

Einstiegspunkt für alle FreeSynergy-Applikationen, die das iced-Backend nutzen.

| Methode | Beschreibung |
|---|---|
| `new()` | Erstellt Engine mit FreeSynergy-Default-Theme |
| `create_window(cfg)` | Erstellt einen `IcedWindow`-Deskriptor |
| `apply_theme(theme)` | Speichert das aktive Theme für den nächsten Render-Tick |
| `set_context(ctx)` | Aktualisiert Locale, Theme-Name, Feature-Flags |
| `app_context()` | Liest den aktuellen `AppContext`-Snapshot |
| `dispatch_event(evt)` | Leitet ein `FsEvent` in die iced-Event-Schleife |
| `run()` | Lifecycle-Hook (no-op; Start via `run_app`) |
| `shutdown()` | Sendet Abbruch-Signal an iced |
| `run_app(title, update, view)` | Startet die typisierte iced-Event-Schleife |

### `IcedWindow` — `FsWindow`-Implementierung

Hält den Fensterzustand zwischen Render-Ticks.  Mutationen werden als
`FsEvent`-Liste gepuffert und von der iced-`update`-Funktion geleert.

```rust
let mut win = IcedWindow::new("Meine App");
win.minimize();
let events = win.drain_events(); // enthält FsEvent::Window(Minimized)
```

### `IcedWidget` — `FsWidget`-Implementierung

Widget-Deskriptor: ID + enabled-Flag.  Die iced-View-Funktion liest den
Deskriptor und baut das konkrete `iced::Element`.

### `IcedTheme` — `FsTheme`-Implementierung

Wrapper um `iced::Theme`.  Alle `FsTheme`-Abfragen leiten ihre Werte aus
der iced-Palette ab — beide bleiben so automatisch synchron.

```rust
let theme = IcedTheme::fs_default();   // FreeSynergy Default (Dark, Cyan)
let bg = theme.background_color();     // Color::rgb(0.08, 0.08, 0.12)
```

---

## MVU-Muster (`mvu`-Modul)

Das Elm-Pattern trennt drei Belange sauber:

| Schicht | Typ | Beschreibung |
|---|---|---|
| **Model** | `S: Default` | Unveränderlicher Applikationszustand |
| **Update** | `fn(&mut S, M) -> Task<M>` | Reine Zustandsübergangs-Funktion |
| **View** | `fn(&S) -> Element<M>` | Reine Render-Funktion |

```rust
use fs_gui_engine_iced::mvu::MvuApp;

MvuApp::new("Titel", update_fn, view_fn).run().unwrap();
```

`MvuApp::run` delegiert intern an `iced::application(…).run()`.
Consumer-Crates brauchen kein `iced` in ihrem `Cargo.toml`.

---

## Capability-Registrierung

Beim Start registriert die Engine die Capability **`render.engine.iced`** in
`fs-registry`, damit Shell und App-Launcher wissen, welche Render-Engines
verfügbar sind.

```rust
use fs_gui_engine_iced::{IcedCapability, CAPABILITY_ID};

let cap = IcedCapability::descriptor();
assert_eq!(cap.id, "render.engine.iced");
```

---

## i18n

Alle Strings sind als FTL-Keys in `fs-i18n` hinterlegt:

- `fs-i18n/locales/en/gui-engine-iced.ftl`
- `fs-i18n/locales/de/gui-engine-iced.ftl`

Schlüssel-Präfix: `gui-iced-`

---

## libcosmic-Integration (G2.8)

Der aktuelle Build nutzt vanilla **iced 0.13**.  Eine vollständige
[libcosmic](https://github.com/pop-os/libcosmic)-Integration
(Pop!_OS COSMIC Design System, System-Palette, Portal-Support) ist für Phase
**G2.8** geplant, wenn `fs-desktop` über Feature-Flag auf diese Engine
wechselt.

---

## Qualitäts-Gates

```
cargo clippy --all-targets -- -D warnings   → 0 Fehler
cargo fmt --check                           → sauber
cargo test                                  → alle grün
cargo build --release                       → fehlerfrei
```

---

## Abhängigkeiten

| Crate | Rolle |
|---|---|
| `fs-render` | Trait-Definitionen (RenderEngine, FsWidget, …) |
| `iced 0.13` | GUI-Framework (features: tokio) |

---

Siehe auch: `fs-render` (Trait-Definitionen) · `fs-gui-engine-bevy` (Bevy-Implementierung)
