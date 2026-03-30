# fs-packages

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-packages` · `/home/kal/Server/fs-packages/`
**Typ:** Workspace (3 Crates: fs-pkg, fs-plugin-sdk, fs-plugin-runtime)
**Capabilities:** `packages.install`, `packages.manifest`, `packages.plugin-sdk`, `packages.plugin-runtime`

---

## Was ist das?

`fs-packages` ist die Package-Management-Engine für FreeSynergy.
Installiert, deinstalliert, validiert und aktualisiert Pakete aller Typen (bundle/program/adapter/artifact).
Verwaltet das Plugin-System: SDK für Plugin-Autoren + Runtime für WASM-Plugins.

---

## Workspace-Struktur

```
fs-packages/
├── fs-pkg/            — Package-Engine: Manifests, Installer, Setup-Flow, Signing
├── fs-plugin-sdk/     — Plugin SDK: Traits, Macros, Request/Response-Typen
└── fs-plugin-runtime/ — Plugin Runtime: WASM via wasmtime, Process-Runner
```

---

## fs-pkg — Package Engine

### Design

```
PackageInstaller (Trait)  — Strategy je Paket-Typ (Bundle, Program, Adapter, Artifact)
SetupStep (Trait)         — Chain of Responsibility: jeder Setup-Schritt ein Objekt
ManifestParser            — parse(bytes) → Manifest
InstallerRegistry         — welcher Installer für welchen Typ?
DependencyResolver        — topologische Sortierung, Zyklenerkennung
```

### Paket-Typen

| Typ        | Beschreibung                                          |
|------------|-------------------------------------------------------|
| `bundle`   | Gruppe von Paketen (z.B. "Workstation", "Server")     |
| `program`  | Laufender Container-Dienst                            |
| `adapter`  | Implementiert einen Trait, registriert Capability     |
| `artifact` | Reine Daten (Sprachen, Themes, Icon-Sets)             |

### Manifest-Format (package.toml)

```toml
[package]
name        = "fs-node"
version     = "0.3.0"
type        = "program"
description = "FreeSynergy Node server"

[capabilities]
provides = ["node.api", "node.storage"]
requires = ["db.engine", "auth.oauth"]

[install]
oci_image = "ghcr.io/freesynergy/fs-node:0.3.0"
```

---

## fs-plugin-sdk — Plugin SDK

Für Plugin-Autoren. Definiert Traits + Macros für WASM-Plugins.

```rust
use fs_plugin_sdk::prelude::*;

#[fs_plugin]
pub struct MyPlugin;

#[fs_plugin_impl]
impl PluginHandler for MyPlugin {
    fn handle(&self, req: PluginRequest) -> PluginResponse {
        PluginResponse::ok("result")
    }
}
```

### Command-Router

```rust
let router = PluginRouter::new()
    .route("greet", |req| PluginResponse::ok(format!("Hello, {}!", req.arg("name")?)));
```

---

## fs-plugin-runtime — Plugin Runtime

Lädt und führt WASM-Plugins via `wasmtime` aus.

```rust
use fs_plugin_runtime::PluginRuntime;

let runtime = PluginRuntime::new();
let handle  = runtime.load("my_plugin.wasm").await?;
let resp    = handle.call("greet", PluginRequest::new().arg("name", "Alice")).await?;
```

| Methode          | Beschreibung                            |
|------------------|-----------------------------------------|
| `load(path)`     | WASM-Modul laden + instanziieren        |
| `call(cmd, req)` | Command in der WASM-Sandbox aufrufen    |
| `unload()`       | Handle freigeben                        |

---

## Setup-Flow (Chain of Responsibility)

Jeder Installationsschritt ist ein `SetupStep`-Objekt mit `execute()` / `rollback()`:

```
ValidateManifestStep
  → ResolveDependenciesStep
    → DownloadArtifactsStep
      → VerifySignaturesStep
        → RunInstallersStep
          → RegisterCapabilitiesStep
```

Bei Fehler: automatisches Rollback in umgekehrter Reihenfolge.
