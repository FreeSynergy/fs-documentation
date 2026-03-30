# fs-help

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-help` · `/home/kal/Server/fs-help/`
**Typ:** Library-Crate (kein laufender Prozess)
**Capabilities:** `help.system`, `help.topics`

---

## Was ist das?

`fs-help` ist das kontext-sensitive Hilfesystem für FreeSynergy.
Es bietet `HelpSystem`, `HelpTopic`, `HelpKind` (Strategy Pattern) und Volltextsuche.
Genutzt von `fs-desktop` (Help-Panel) und `fs-node` / CLI für Hilfe-Anzeigen.

---

## Design

```
HelpSystem         — Registry aller Topics, querybar per Context oder Suche
HelpTopic          — Einzelnes Topic mit i18n-Keys, Links, Related-Topics
HelpKind (Trait)   — Strategy: ExternalHelp (3rd-party) / InternalHelp (FreeSynergy)
HelpLoader         — Topics aus TOML-Dateien laden
HelpSearch         — Volltextsuche über alle Topics
HelpContext        — Context-Lookup (spezifischstes → Root-Fallback)
```

**Pattern:** Composite (`HelpSystem` besitzt Topics), Strategy (`HelpKind` je Topic)

---

## HelpSystem

```rust
let mut h = HelpSystem::new();

// Topics registrieren
h.add_topic(
    HelpTopic::new("project.create", "help.project.create.title", "help.project.create.body")
        .related(["project"])
        .keywords(["create", "new", "project"])
);

// Context-Lookup (spezifischstes → Root-Fallback)
let topic = h.help_for_context("project.create.host")?;
// → gibt "project.create" zurück (parent-fallback)

// Volltextsuche
let results: Vec<&HelpTopic> = h.search("create");

// Related Topics
let related: Vec<&HelpTopic> = h.related_for("project.create");

// Alle Topics sortiert
let all: Vec<&HelpTopic> = h.all_topics();
```

---

## Context-Lookup-Strategie

| Anfrage                  | Gefunden       | Warum                          |
|--------------------------|----------------|--------------------------------|
| `"project.create"`       | `project.create` | Exact match                  |
| `"project.create.host"`  | `project.create` | Parent-Fallback              |
| `"project.delete"`       | `project`        | Root-Fallback                |
| `"unknown.foo"`          | `None`           | Kein Ancestor registriert    |

---

## HelpTopic

```rust
HelpTopic::new("id", "i18n.title.key", "i18n.body.key")
    .keywords(["keyword1", "keyword2"])   // Suchwörter (lowercase gespeichert)
    .related(["other.topic.id"])          // Verwandte Topics
    .with_kind(external(ExternalHelp::new()
        .with_links(vec![HelpLink::docs("https://docs.example.com")])
        .with_search("tutorial query")
    ))
```

| Feld          | Typ            | Beschreibung                              |
|---------------|----------------|-------------------------------------------|
| `id`          | String         | Eindeutiger Context-Pfad (`"project.create"`) |
| `title_key`   | String         | i18n-Key für Kurzanzeige                  |
| `content_key` | String         | i18n-Key für Langtext                     |
| `related`     | `Vec<String>`  | IDs verwandter Topics                     |
| `keywords`    | `Vec<String>`  | Suchwörter (immer lowercase)              |
| `kind`        | `HelpKindArc`  | Strategy: Internal oder External          |

---

## HelpKind (Strategy)

### InternalHelp (FreeSynergy-eigene Programme)

```rust
use fs_help::{internal, InternalHelp, HelpLink};

let kind = internal(InternalHelp::new()
    .with_links(vec![HelpLink::docs("https://freesynergy.net/docs")])
);
```

### ExternalHelp (Drittanbieter-Programme)

```rust
use fs_help::{external, ExternalHelp, HelpLink};

let kind = external(ExternalHelp::new()
    .with_links(vec![
        HelpLink::website("https://kanidm.com"),
        HelpLink::git("https://github.com/kanidm/kanidm"),
    ])
    .with_search("kanidm identity provider tutorial")
);
```

---

## HelpLink

```rust
HelpLink::website("https://example.com")
HelpLink::docs("https://docs.example.com")
HelpLink::git("https://github.com/example/repo")
    .with_label_key("help.link.git.kanidm")
```

| Kind      | Default i18n-Key    | Icon |
|-----------|---------------------|------|
| `Website` | `help.link.website` | 🌐   |
| `Docs`    | `help.link.docs`    | 📖   |
| `Git`     | `help.link.git`     | ⑂    |

---

## Cargo.toml

```toml
[dependencies]
fs-help = { path = "../fs-help" }
```
