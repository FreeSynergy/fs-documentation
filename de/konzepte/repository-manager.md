# Repository Manager — Repositories in jedem Programm

[← Zurück zum Index](../INDEX.md) | [Manager-Konzept](manager.md) | [Store](../programme/store/README.md) | [Icon Manager](../programme/icons/README.md)

---

## Das Problem

Store, Icon Manager und Bundle Manager verwalten alle Repositories — aber jedes hat seine eigenen Regeln:

| Programm | Regel |
|---|---|
| Store | Haupt-Repo (`freesynergy-main`) kann nicht gelöscht werden |
| Icon Manager | Haupt-Icons-Repo (`freesynergy-icons`) kann nicht gelöscht werden |
| Bundle Manager | Haupt-Bundle-Repo kann nicht gelöscht werden |

Ohne gemeinsame Abstraktion würde jedes Programm dieselbe Logik neu implementieren: Liste anzeigen, hinzufügen, aktivieren/deaktivieren, löschen (mit Schutz).

## Die Lösung: RepositoryManager

Ein einziges Objekt das diese Logik kapselt. Jedes Programm instanziiert es mit **seinen** Repositories und **seinen** Regeln — der Rest ist gleich.

```
RepositoryManager
  ├── list()               → alle Repositories
  ├── enabled()            → nur aktive
  ├── add(repo)            → hinzufügen
  ├── set_enabled(id, bool) → aktivieren / deaktivieren
  └── remove(id)           → entfernen (Err wenn builtin)
```

Die Regel "builtin kann nicht gelöscht werden" ist im `RepositoryManager` codiert — nicht im jeweiligen Programm. Programme müssen das nicht selbst prüfen.

---

## UI: Repository Manager in der Shell-Sidebar

Die **ManagersApp** (im Desktop-Repo, Crate `fsd-managers`) hat eine eigene Sidebar. Der unterste Eintrag ist immer **Einstellungen** (angepinnt).

In Einstellungen gibt es einen Bereich **Repositories** mit Tabs:

| Tab | Icon | Zuständigkeit |
|---|---|---|
| Store | Store-Icon | Store-Repositories |
| Icons | Icon-Manager-Icon | Icon-Set-Repositories |
| Bundles | Bundle-Manager-Icon | Bundle-Repositories |

Jeder Tab zeigt dieselbe UI:
- Liste aller Repositories (Name, URL, aktiv/inaktiv)
- Toggle: aktivieren / deaktivieren
- Button: hinzufügen (öffnet Dialog)
- Button: entfernen (fehlt bei Builtin-Repos)

Das Icon des jeweiligen Tabs ist das Icon des zugehörigen Managers — kein generisches Icon. So ist auf einen Blick klar welche Repositories für welches Programm gelten.

### Warum im Bundle Manager?

Der Bundle Manager ist der natürliche Ort: Er kennt alle Quell-Repositories für Pakete. Repositories für Store-Pakete, Icon-Sets und Bundles sind konzeptuell verwandt — alle sind "Quellen für installierbare Inhalte".

---

## Einträge — gleiche Struktur überall

Ein Repository-Eintrag sieht in jedem Programm gleich aus:

| Feld | Beschreibung |
|---|---|
| `id` | Eindeutige ID |
| `name` | Anzeigename |
| `url` | Remote-URL oder lokaler Pfad |
| `enabled` | Aktiv oder deaktiviert |
| `builtin` | Eingebaut — schreibgeschützt, nur deaktivierbar |

Diese Felder sind identisch ob es ein Store-Repo, ein Icon-Repo oder ein Bundle-Repo ist. Die UI ist damit vollständig wiederverwendbar.

---

## Implementierung

### Jetzt

Jeder Manager implementiert seinen eigenen `RepositoryManager` mit dem gleichen Interface — z.B. `fsn-manager-icons` hat `RepositoryManager` für `IconRepository`.

### Später (Lib)

Wenn das Muster in mehreren Crates stabil ist, zieht es nach `FreeSynergy.Lib` als generischer Typ:

```rust
// In FreeSynergy.Lib (geplant)
pub trait Repository {
    fn id(&self) -> &str;
    fn builtin(&self) -> bool;
    fn enabled(&self) -> bool;
    fn set_enabled(&mut self, enabled: bool);
}

pub struct RepositoryManager<R: Repository> {
    repositories: Vec<R>,
}

impl<R: Repository> RepositoryManager<R> {
    pub fn remove(&mut self, id: &str) -> Result<(), RepositoryError> {
        let pos = self.repositories.iter().position(|r| r.id() == id)
            .ok_or(RepositoryError::NotFound(id.into()))?;
        if self.repositories[pos].builtin() {
            return Err(RepositoryError::CannotRemoveBuiltin(id.into()));
        }
        self.repositories.remove(pos);
        Ok(())
    }
    // add(), list(), enabled(), set_enabled() …
}
```

Jedes Programm bringt nur noch seinen konkreten Repository-Typ mit — die gesamte Verwaltungslogik kommt aus Lib.

---

## Zusammenfassung

| Was | Wo |
|---|---|
| Repository-Logik (add/remove/enable) | `RepositoryManager` — ein Objekt, nicht drei |
| Builtin-Schutz-Regel | Im `RepositoryManager`, nicht im jeweiligen Programm |
| UI für Repository-Verwaltung | ManagersApp → Einstellungen → Repositories → Tabs |
| Tab-Icon | Icon des jeweiligen Managers (Store, Icons, Bundles) |
| Eintrags-Felder | Überall identisch (id, name, url, enabled, builtin) |

---

Weiter: [Manager-Konzept](manager.md) | [Icon Manager](../programme/icons/README.md) | [Store](../programme/store/README.md)
