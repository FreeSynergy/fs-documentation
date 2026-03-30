# fs-icons

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-icons` · `/home/kal/Server/fs-icons/`
**Typ:** Artifact (SVG-Daten) + Binary (`fs-icons-sync`)
**Capabilities:** `icons.homarrlabs`, `icons.we10x`

---

## Was ist das?

`fs-icons` enthält kuratierte SVG-Icon-Sets für den FreeSynergy-Desktop.
Es kombiniert zwei Upstream-Quellen und hält sie über das Binary `fs-icons-sync` aktuell —
ohne System-`git` vorauszusetzen (reines Rust, `gix`-basiert).

---

## Icon-Sets

| Set         | Upstream                                          | Pfad               | Inhalt                      |
|-------------|---------------------------------------------------|--------------------|-----------------------------|
| homarrlabs  | `homarr-labs/dashboard-icons`                     | `homarrlabs/`      | App- & Service-Icons (SVG)  |
| we10x       | `yeyushengfan258/We10X-icon-theme`                | `we10x/`           | System-Icons (SVG, rekursiv)|

---

## Binary: fs-icons-sync

```
sync/
└── src/main.rs   — Haupt-Binary
```

```bash
# Alle Sets synchronisieren
fs-icons-sync

# Nur ein bestimmtes Set
fs-icons-sync --set homarrlabs

# Anderes Icons-Root-Verzeichnis
fs-icons-sync --icons-dir /pfad/zu/icons
```

**Ablauf je Set:**

1. Shallow-Clone (depth=1) des Upstream-Repos via `gix` in ein temporäres Verzeichnis
2. Zielverzeichnis leeren und neu anlegen
3. SVGs kopieren (homarrlabs: flach aus `svg/`; we10x: rekursiv aus `src/`)
4. Temporäres Verzeichnis automatisch aufräumen

---

## Workspace-Struktur

```
fs-icons/
├── sync/              — Workspace-Member (Binary fs-icons-sync)
│   ├── Cargo.toml
│   └── src/main.rs
├── homarrlabs/        — App/Service-Icons (aus dashboard-icons)
├── we10x/             — System-Icons (aus We10X-icon-theme)
├── Cargo.toml         — Workspace-Root
└── package.toml       — FreeSynergy-Paketmetadaten
```

---

## Dependencies

| Crate      | Zweck                                              |
|------------|----------------------------------------------------|
| `gix`      | Shallow-Clone ohne System-git (pure Rust)          |
| `clap`     | CLI-Argument-Parsing (`--set`, `--icons-dir`)      |
| `tempfile` | Temporäre Klon-Verzeichnisse                       |
