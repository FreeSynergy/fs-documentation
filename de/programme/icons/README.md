# Icon Manager — Icon-Sets & Picker

> Lebt in **FreeSynergy.Managers** (`icons/`, Crate: `fsn-manager-icons`).

[← Zurück zum Index](../../INDEX.md) | [Manager-Konzept](../../konzepte/manager.md) | [Repository Manager](../../konzepte/repository-manager.md) | [Theme Manager](../theme/README.md)

---

## Was der Icon Manager ist

Der Icon Manager kennt alle installierten Icon-Sets, löst Icon-Namen zu Dateipfaden auf und stellt einen **wiederverwendbaren Icon-Picker** bereit — für jedes Programm das Icons braucht.

Kein Programm baut einen eigenen Icon-Browser. Stattdessen ruft es den Icon Manager auf.

---

## Icon-Sets

Ein Icon-Set ist ein Ordner mit SVG-Dateien. Optionale Dark-Varianten folgen dem Schema `name-dark.svg`.

Jedes Set hat folgende Metadaten:

| Feld | Beschreibung |
|---|---|
| `id` | Eindeutige ID (= Ordnername, z.B. `homarrlabs`) |
| `name` | Anzeigename (`Homarr Labs Icons`) |
| `description` | Kurzbeschreibung |
| `path` | Absoluter Pfad auf Disk |
| `icon_count` | Anzahl Icons (nur Light-Varianten gezählt) |
| `has_dark_variants` | Hat das Set Dark-Varianten? |
| `source_repo_id` | Von welchem Repository kommt das Set |
| `builtin` | Eingebaut — kann nicht entfernt werden |

Die Sets werden aus `manifest.toml` in `FreeSynergy.Icons` gelesen.

---

## Repository-Verwaltung

Der Icon Manager unterstützt mehrere Quell-Repositories — analog zum Store.

```
Quell-Repositories → installierte Icon-Sets → Picker → andere Programme
```

### Regeln

| Aktion | Regel |
|---|---|
| Hinzufügen | Immer erlaubt |
| Aktivieren / Deaktivieren | Immer erlaubt |
| Entfernen | Nur erlaubt wenn **nicht builtin** |

Das Haupt-Repository (`freesynergy-icons`) ist `builtin = true` und kann nur deaktiviert, aber **nie gelöscht** werden.

### Verwaltung in der UI

Der unterste Eintrag in der Sidebar des Icon Managers ist **Einstellungen** (angepinnt). Dort:

- Alle Repositories aufgelistet
- Jedes Repository aktivier-/deaktivierbar
- Repositories hinzufügen / entfernen
- Builtin-Repositories: kein Löschen-Button

Das ist dasselbe Muster wie im Store und im Bundle Manager. Intern verwendet alle drei den gleichen `RepositoryManager`-Mechanismus — siehe [Repository Manager](../../konzepte/repository-manager.md).

---

## Icon-Picker

Der Icon-Picker ist eine wiederverwendbare Komponente. Jedes Programm das Icons braucht, ruft ihn auf:

- **Theme Manager** — Icons der einzelnen Programme ändern
- **Store / Package-Editor** — Icon für ein Paket auswählen
- **Container App Manager** — Icon eines Services anpassen
- **Desktop** — Widget-Icons, Shortcut-Icons
- **Überall sonst** — wo der Nutzer ein Icon wählen soll

### Filter

```rust
IconPickerFilter {
    set_id: Some("homarrlabs"),  // nur aus diesem Set (None = alle)
    search: Some("kanidm"),       // Suchtext (case-insensitive)
    prefer_dark: true,            // Dark-Variante bevorzugen wenn vorhanden
}
```

### Ergebnis: `PickedIcon`

Ein `PickedIcon` enthält den aufgelösten `Icon` (mit Pfad). Der Aufrufer kann es:
- **Direkt anzeigen** — Pfad an die UI übergeben
- **Kopieren** — `picked.copy_to(target_path)` → kopiert die SVG-Datei ans Ziel

### Kopieren — warum?

Wenn ein anderes Programm ein Icon dauerhaft übernehmen möchte (z.B. Theme Manager ändert das Icon eines Programms), wird die SVG-Datei in den Zielordner kopiert. Das Icon ist dann unabhängig davon ob das Quell-Set später entfernt wird.

---

## API

```rust
use fsn_manager_icons::{IconManager, IconRepository, IconPickerFilter};

// Manager erzeugen
let mgr = IconManager::new(
    "/opt/freesynergy/icons",
    vec![
        IconRepository {
            id:      "freesynergy-icons".into(),
            name:    "FreeSynergy Icons".into(),
            url:     "https://github.com/FreeSynergy/Icons".into(),
            enabled: true,
            builtin: true,
        },
    ],
);

// Alle installierten Sets (mit Pfad + Anzahl)
let sets = mgr.sets();
for set in &sets {
    println!("{}: {} icons at {:?}", set.name, set.icon_count, set.path);
}

// Einzelnes Icon auflösen
let icon = mgr.resolve("homarrlabs", "kanidm", false);

// Picker — alle Icons die "kanidm" im Namen haben
let results = mgr.pick(&IconPickerFilter {
    search: Some("kanidm".into()),
    ..Default::default()
});

// Icon in anderen Ordner kopieren
if let Some(picked) = results.first() {
    picked.copy_to("/opt/freesynergy/themes/my-theme/icons/kanidm.svg".as_ref())?;
}

// Repository hinzufügen
mgr.repositories.add(IconRepository {
    id: "community-icons".into(),
    name: "Community Icons".into(),
    url: "https://example.com/icons".into(),
    enabled: true,
    builtin: false,
});

// Repository deaktivieren (geht immer)
mgr.repositories.set_enabled("community-icons", false)?;

// Repository entfernen (schlägt fehl wenn builtin)
mgr.repositories.remove("community-icons")?;       // ok
mgr.repositories.remove("freesynergy-icons")?;     // Err(CannotRemoveBuiltin)
```

---

## manifest.toml — Format

```toml
[[set]]
id              = "homarrlabs"
name            = "Homarr Labs Icons"
description     = "Icons from the Homarr community"
has_dark_variants = true
source_repo_id  = "freesynergy-icons"
builtin         = true

[[set]]
id              = "simpleicons"
name            = "Simple Icons"
description     = "Free SVG icons for popular brands"
has_dark_variants = false
source_repo_id  = "freesynergy-icons"
builtin         = true
```

---

## Verzeichnisstruktur

```
FreeSynergy.Icons/
├── manifest.toml           ← Alle Sets + Metadaten
├── homarrlabs/
│   ├── kanidm.svg
│   ├── kanidm-dark.svg
│   ├── forgejo.svg
│   └── ...
├── simpleicons/
│   ├── github.svg
│   └── ...
└── ...
```

---

Weiter: [Repository Manager](../../konzepte/repository-manager.md) | [Theme Manager](../theme/README.md) | [Store](../store/README.md) | [Manager-Konzept](../../konzepte/manager.md)
