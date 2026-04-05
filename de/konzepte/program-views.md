# Program Views

[← Zurück zum Index](../INDEX.md)

---

## Grundidee

Jedes Programm ist mehr als nur ein Fenster. Es hat verschiedene **Perspektiven**:
Wie starte ich es? Was macht es gerade? Wie konfiguriere ich es? Wie verbinde ich es?

Diese Perspektiven heißen **Program Views**.

---

## ProgramViewProvider-Trait

Jedes Programm deklariert welche Views es anbietet:

```rust
pub trait ProgramViewProvider: Send + Sync {
    fn available_views(&self) -> Vec<ProgramView>;
    fn supports(&self, view: ProgramView) -> bool;  // Default-Impl enthalten
}
```

Die Titlebar zeigt entsprechende View-Buttons.
Nur deklarierte Views erscheinen — kein leerer Button für nicht-unterstützte Views.

**Implementiert in:**
- `fs-render/src/navigation.rs` — Trait + `ProgramView` Enum
- `fs-managers/{auth,mail,matrix,zentinel,forgejo,wiki}/src/view.rs` — je eine Impl
- `fs-desktop/crates/fs-gui-workspace/src/view.rs` — Desktop-Impl

---

## Die Views im Überblick

### Start

Das Programm starten / zur Haupt-UI wechseln.
Standard-View für die meisten Programme.

### Info

Alles über die laufende Instanz:

| Feld | Inhalt |
|------|--------|
| Titel | Anzeigename (caption) + Version |
| Beschreibung | Kurzbeschreibung aus package.toml |
| Laufzeit | Seit wann läuft die Instanz |
| PIDs | Prozess-IDs inkl. Unter-Prozesse |
| Aktionen | kill, restart, update, pause, ... |

**Berechtigungscheck für Aktionen:**
- Eigener Rechner/Mobil: alle Aktionen erlaubt
- Server: kritische Aktionen (kill, restart) nur mit Berechtigung
  (fs-auth Rights-Kaskade — wer keine Rechte hat, sieht die Aktion gar nicht)

### Manual

Scrollbare Hilfe-Dokumentation für das Programm.
Basis: `fs-help` HelpSystem — Topics + Volltextsuche.

Für externe Programme (Container-Apps): Links zu externer Doku.
Für FreeSynergy-Programme: integrierte FTL-basierte Hilfe.

Verschiedene Seiten navigierbar (Inhaltsverzeichnis + Breadcrumb).

### SettingsConfig

Sofortige Konfig-Änderungen — kein Neustart.
Das Settings-Config-Component passt sich dem aktuellen Programm an.

Typische Sektionen:
- **Ansicht** — Schriftgröße, Farbschema, Dichte
- **Sprache** — Sprachauswahl (via fs-manager-language)
- **Tastaturkürzel** — programm-spezifische Shortcuts
- **Sonstiges** — programm-spezifische Optionen

Desktop-spezifische Sektionen (nur im Desktop):
- **Icon-Größe** — Schieberegler
- **Menü-Stil** — Rund | Sidebar-Panel
- **Hintergrund** — Farbe oder Bild
- **Setup-Modus** — Widgets hinzufügen, Layout anpassen

### SettingsContainer

Pod-YAML-Konfig für Container-basierte Programme.
Änderungen erfordern einen Neustart des Containers — klarer Hinweis im UI.

Features:
- Alle konfigurierbaren Variablen aus `package.toml` werden angezeigt
- Secrets (Passwörter, API-Keys) werden maskiert
- **Instanz kopieren:** neue Instanz mit gleicher Konfig + neuem Namen erstellen
- Dann: neue Instanz starten, stoppen, löschen

Berechtigungscheck: nicht jeder darf Container konfigurieren.

### Binding *(G2)*

Workflow-Editor: Programm mit anderen Programmen verknüpfen.

Beispiel: "Beim Speichern einer Notiz → auch in Wiki speichern (bestimmte Seite)."

Bindings werden als Aktionen im Side-Menu angezeigt.
Der User kann Standard-Verknüpfungen konfigurieren.

---

## Beziehung zur Titlebar

```
[App-Icon] [Titel] [▶ Start][ℹ Info][📖 Manual][⚙ Config][🐳 Container] [Tiling][−][□][×]
```

Nur die Views die das Programm anbietet erscheinen als Buttons.
View-Buttons sind beschriftet mit Icon + Label (oder nur Icon wenn Platz knapp).

---

## Desktop: keine Start-View

Der Desktop selbst hat keinen "Start"-Button.
Stattdessen: Tiling-Toggle (Fenster anordnen) als erstes Element.

```
[FS-Icon] [Desktop] [⊞ Tiling][⚙ Config] [−][□][×]
```

---

## Welche Programme bieten welche Views?

Implementiert via `ProgramViewProvider` trait — nur deklarierte Views erscheinen in der Titlebar.

| Programm | Start | Info | Manual | SettingsConfig | SettingsContainer | Binding |
|---------|-------|------|--------|---------------|------------------|---------|
| Desktop | — | — | — | ✓ | — | — |
| Kanidm | — | ✓ | ✓ | — | ✓ | G2 |
| Stalwart | — | ✓ | ✓ | — | ✓ | G2 |
| Tuwunel | — | ✓ | ✓ | — | ✓ | G2 |
| Zentinel | — | ✓ | ✓ | — | ✓ | G2 |
| Forgejo | — | ✓ | ✓ | — | ✓ | G2 |
| Outline / Wiki.js | — | ✓ | ✓ | — | ✓ | G2 |
| Alle Container-Apps | ✓ | ✓ | ✓ | — | ✓ | G2 |

> **Hinweis:** Container-Apps bekommen `Start` zusätzlich sobald `SettingsContainer` befüllt ist.
> Desktop hat bewusst kein `Start` (läuft immer) und kein `SettingsContainer` (kein Pod).

---

## caption — Anzeigename für Instanzen (G1.4)

Wenn mehrere Instanzen desselben Programms laufen (z.B. drei Wiki-Instanzen),
braucht jede einen eigenen Anzeigenamen:

```
InstalledResource.caption = Some("wiki.team-a")
```

- `caption` ist optional — ohne Caption wird die `id` angezeigt
- Gesetzt beim Installieren oder nachträglich per Inventory-API
- Auch in `PackageData.caption` (Store): der Store kann eine Empfehlung mitliefern

---

## ProgramGroup — mehrere Instanzen als Gruppe (G1.4)

Wenn `N` Instanzen desselben Programms laufen, bündelt die `ProgramGroup` sie:

```rust
pub struct ProgramGroup {
    pub parent_id: String,           // z.B. "wiki"
    pub instances: Vec<InstalledResource>,
    pub group_icon_key: String,      // z.B. "fs:apps/wiki"
}
```

Das Desktop-Menü zeigt ein Parent-Icon, darunter aufklappbar die Instanzen.
Jede Instanz hat ein `CompositeIcon` (primary = Programm-Icon, secondary = Badge).

---

## InfoViewScope — Berechtigungen im Info-Panel (G1.4)

Die Info-View prüft ob kritische Aktionen (kill, restart) erlaubt sind:

```rust
pub enum InfoViewScope {
    OwnMachine,    // alle Aktionen erlaubt
    RemoteServer,  // nur mit fs-auth Rights-Kaskade
}
```

- `OwnMachine`: eigener Rechner oder lokale VM → alle Aktionen sichtbar
- `RemoteServer`: Server → kritische Aktionen nur für Benutzer mit expliziter Berechtigung

Der Desktop bestimmt den Scope aus `fs-registry` (lokal vs. remote).

---

## i18n

View-Labels in `fs-i18n/locales/{lang}/navigation.ftl`:
```
nav-program-view-start              = Start
nav-program-view-info               = Info
nav-program-view-manual             = Handbuch
nav-program-view-settings-config    = Einstellungen
nav-program-view-settings-container = Container
nav-program-view-binding            = Verknüpfung
```

Caption/Gruppen-Labels in `fs-i18n/locales/{lang}/inventory.ftl`:
```
inventory-caption-label     = Anzeigename
inventory-group-label       = Programmgruppe
inventory-group-instances   = Instanzen
inventory-info-action-kill  = Beenden
inventory-info-action-restart = Neustart
inventory-info-critical-blocked = Diese Aktion erfordert Administratorrechte.
```
