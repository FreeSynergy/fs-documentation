# fs-error

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-error` ist das universelle Fehlerbehandlungs-Primitiv für FreeSynergy.
Es definiert den zentralen Fehlertyp `FsError`, den `FsErrorTrait`, sowie Hilfstypen
für Validierung und Reparatur von Konfigurationsdaten.

`fs-error` ist ein reines Library-Crate ohne Container, Daemon oder API —
es wird von allen anderen FreeSynergy-Crates als Abhängigkeit eingebunden.

---

## Architektur

```
FsErrorTrait      ← Trait: code / ftl_key / severity / cause
     ↑
FsError           ← Haupt-Enum (Config, Io, Parse, NotFound, Validation, …)
     |
ErrorSeverity     ← Info / Warn / Error / Fatal

ValidationIssue   ← Einzelner Validierungsbefund (field + message + IssueSeverity)
IssueSeverity     ← Info / Warning / Error (für Konfigurationsvalidierung)

Repairable        ← Trait: validate() + repair() auf Config-Structs
RepairOutcome     ← AutoRepaired / NeedsUserDecision / Unrecoverable / AlreadyValid
RepairAction      ← SetDefault / Remove / Rename / Trim / Insert
```

---

## Typen

### `FsError`

Haupt-Fehler-Enum für alle FreeSynergy Library-Crates.

| Variant | Beschreibung | Severity |
|---|---|---|
| `Config(String)` | Konfigurationsdatei ungültig oder fehlt | Error |
| `Io(std::io::Error)` | OS-I/O-Fehler | Error |
| `Parse(String)` | TOML/Format-Fehler | Error |
| `NotFound(String)` | Ressource nicht gefunden | Warn |
| `Validation { field, message }` | Feldvalidierung fehlgeschlagen | Warn |
| `Network(String)` | Netzwerkfehler | Error |
| `Plugin(String)` | Plugin-Fehler | Error |
| `Auth(String)` | Authentifizierungsfehler | Error |
| `Internal(String)` | Catch-all / interner Fehler | Fatal |

Convenience-Konstruktoren: `FsError::config(...)`, `FsError::parse(...)`, `FsError::not_found(...)`, etc.

### `FsErrorTrait`

```rust
pub trait FsErrorTrait: std::error::Error {
    fn code(&self) -> &'static str;       // "config", "io", "parse", …
    fn ftl_key(&self) -> &'static str;    // "errors.config_error", …
    fn severity(&self) -> ErrorSeverity;
    fn cause(&self) -> Option<&dyn std::error::Error>; // default: self.source()
}
```

Jede Fehler-Domäne implementiert `FsErrorTrait`. Generischer Code (Logging, Telemetrie,
UI) greift über den Trait zu — nie direkt auf `FsError`-Variants matchen.

### `ErrorSeverity`

```
Info < Warn < Error < Fatal
```

Steuert Entscheidungen wie "retry vs. abort" oder Log-Level.
Achtung: Unterschied zu `IssueSeverity` (die für Konfigurationsvalidierung ist, ohne `Fatal`).

### `Repairable`

Trait für Config-Structs die sich selbst validieren und reparieren können.

```rust
pub trait Repairable {
    fn validate(&self) -> Vec<ValidationIssue>;
    fn repair(&mut self) -> RepairOutcome;
    fn is_valid(&self) -> bool;   // convenience
    fn errors(&self) -> Vec<ValidationIssue>;   // nur Error-Severity
}
```

Wird von `fs-config::ConfigLoader` nach dem Deserialisieren aufgerufen.

---

## i18n

`FsErrorTrait::ftl_key()` gibt einen Snippet-Key zurück (z.B. `"errors.config_error"`).
Dieser Key wird über `fs_i18n` zur nutzerlesbaren Nachricht aufgelöst.

Die Keys entsprechen der `snippets/{lang}/errors.toml`-Struktur in `fs-i18n`:

| Variant | ftl_key |
|---|---|
| Config | `errors.config_error` |
| Io | `errors.io_error` |
| Parse | `errors.parse_error` |
| NotFound | `errors.not_found` |
| Validation | `errors.validation_required` |
| Network | `errors.network_error` |
| Plugin | `errors.plugin_error` |
| Auth | `errors.authentication_failed` |
| Internal | `errors.internal_error` |

**Regel:** Niemals `Display`-Output an Nutzer anzeigen — das ist nur für Logs.
Immer `i18n.t(error.ftl_key())` verwenden.

---

## From-Impls

| Quelltyp | Ziel-Variant |
|---|---|
| `std::io::Error` | `FsError::Io` |
| `std::num::ParseIntError` | `FsError::Parse` |
| `std::num::ParseFloatError` | `FsError::Parse` |
| `std::string::FromUtf8Error` | `FsError::Parse` |
| `std::str::Utf8Error` | `FsError::Parse` |

---

## Dependencies

| Crate | Zweck |
|---|---|
| `thiserror` | Einzige externe Dependency — Error-Derive-Makro |

---

## Verwendung

```rust
use fs_error::{FsError, FsErrorTrait, ErrorSeverity};

fn load(path: &str) -> Result<String, FsError> {
    let s = std::fs::read_to_string(path)?;  // io::Error → FsError::Io via From
    Ok(s)
}

fn log_error(e: &dyn FsErrorTrait) {
    eprintln!("[{}] {} — i18n key: {}", e.severity(), e.code(), e.ftl_key());
}
```

---

## Repo

- Lokal: `/home/kal/Server/fs-libs/fs-error/`
- GitHub: `git@github.com:FreeSynergy/fs-libs.git` (Workspace-Member)
