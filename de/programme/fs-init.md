# fs-init

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-init` · `/home/kal/Server/fs-init/`
**Typ:** Binary (`fs-init`)
**Capabilities:** `init.bootstrap`

---

## Was ist das?

`fs-init` ist das Bootstrap-Binary für FreeSynergy.
Es klont den offiziellen Store-Katalog auf den lokalen Node — ohne `git` als System-Dependency.
Nach dem Klonen kann `fs-store` Pakete aus dem lokalen Katalog installieren.

---

## Ablauf

```
1. fs-init läuft (einmalig, beim ersten Boot oder Setup)
2. Klont https://github.com/FreeSynergy/Store.git → ~/.local/share/fsn/store/
3. fs-store liest den lokalen Katalog und installiert Pakete
```

---

## CLI

```bash
# Standard: klont Store nach ~/.local/share/fsn/store
fs-init

# Eigene Store-URL
fs-init --store-url https://github.com/MyOrg/MyStore.git

# Eigenes Zielverzeichnis
fs-init --target-dir /opt/freesynergy/store

# Bestimmter Branch
fs-init --branch staging
```

| Flag           | Default                                            | Beschreibung                  |
|----------------|----------------------------------------------------|-------------------------------|
| `--store-url`  | `https://github.com/FreeSynergy/Store.git`         | Store-Repo-URL                |
| `--target-dir` | `~/.local/share/fsn/store`                         | Zielverzeichnis               |
| `--branch`     | `main`                                             | Git-Branch                    |

---

## Implementierung

- Kein System-`git` nötig — nutzt `gix` (Pure-Rust Git-Implementierung)
- HTTP-Transport via `reqwest` + `rustls` (kein `libgit2`)
- Idempotent: wenn Zielverzeichnis bereits existiert, sofort beendet

---

## Erweiterungspläne (G1+)

| Phase | Inhalt                                                        |
|-------|---------------------------------------------------------------|
| G1    | Installer-Wizard (UI via fs-render/iced)                      |
| G1    | Varianten-Auswahl: Server / Workstation                       |
| G1    | bootc install to-disk Integration                             |
| G1    | Store laden + erste Pakete installieren nach dem Klonen       |
