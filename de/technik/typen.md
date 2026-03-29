# Typen-System (fs-types Primitives)

[← Zurück zum Index](../INDEX.md) | [Pakete](../konzepte/pakete.md) | [i18n](i18n.md)

---

## Grundregel: Typen statt Strings

Überall wo eine Information eine bestimmte Bedeutung hat, wird ein typsicherer Wert verwendet — kein roher `String`. Das verhindert falsche Werte, ermöglicht konsistente Validierung, und gibt der GUI automatisch Hilfetext.

```
String "1.0.0"        ← kann invalid sein, kein Vergleich möglich
SemVer { 1, 0, 0 }   ← immer strukturell valide, sortierbar
```

---

## FsValue Trait

Alle Primitive implementieren `FsValue` — das ist der **gemeinsame Kontrakt** für GUI und Validierung:

```rust
pub trait FsValue: Debug + Send + Sync {
    fn type_label_key(&self) -> &'static str;   // z.B. "type-url"
    fn placeholder_key(&self) -> &'static str;  // z.B. "placeholder-url"
    fn help_key(&self) -> &'static str;          // z.B. "help-url"
    fn validate(&self) -> Result<(), &'static str>;
    fn display(&self) -> String;
}
```

**Warum das wichtig ist:** Jedes Input-Feld in der GUI kann `placeholder_key()` und `help_key()` aufrufen — ohne individuellen Hilfetext ist immer ein Standard-Text da. Übersetzt in jeder Sprache.

Alle Schlüssel sind gültige FTL-Message-IDs (kebab-case):
| Methode | Schlüssel-Muster | Beispiel |
|---|---|---|
| `type_label_key` | `type-<name>` | `type-url` |
| `placeholder_key` | `placeholder-<name>` | `placeholder-url` |
| `help_key` | `help-<name>` | `help-url` |
| Fehler aus `validate` | `error-validation-<grund>` | `error-validation-url-scheme` |

Die zugehörigen Übersetzungen liegen in `fs-i18n/locales/{lang}/types.ftl`.

---

## Primitive Typen

Alle in `fs-types/src/primitives/` · alle implementieren `FsValue` · alle serialisieren als natürlicher String/Zahl.

### FsUrl

Ein URL mit Anzeige-Label. Für Links in Store, Dokumentation, Package-Quellen.

```rust
pub struct FsUrl {
    pub url: String,    // "https://freesynergy.net"
    pub label: String,  // "FreeSynergy" — leer: URL wird direkt angezeigt
}
```

TOML:
```toml
website = { url = "https://freesynergy.net", label = "FreeSynergy" }
```

Validation: URL muss nicht-leer und `http://` oder `https://` starten.

### LanguageCode

BCP-47 Sprachcode. **Nicht** verwechseln mit `fs_i18n::LanguageCode` (Laufzeit-Sprache) — dieser Typ ist für Package-Metadaten.

```rust
pub struct LanguageCode(String);  // "de", "ar", "zh-Hant", "yue"
```

TOML:
```toml
locales = ["en", "de", "ar"]
```

Validation: nicht-leer, nur ASCII-Buchstaben + Ziffern + Bindestrich.
Eingebaut: `is_rtl()` erkennt die vier RTL-Sprachen (ar, fa, ur, ps).

### SemVer

Semantische Versionsnummer — ersetzt `String` überall wo Versionen verglichen werden müssen.

```rust
pub struct SemVer {
    pub major: u16,
    pub minor: u16,
    pub patch: u16,
    pub pre: Option<String>,  // "alpha.1", "beta.2", "rc.1"
}
```

TOML (serialisiert als Plain-String):
```toml
version = "1.2.3"
version = "0.5.0-beta.1"
```

Ordering: `1.0.0-alpha < 1.0.0-rc.1 < 1.0.0` — Pre-Release ist immer kleiner als Release.

```rust
let v: SemVer = "1.2.3".parse().unwrap();
assert!(v > "1.2.3-rc.1".parse::<SemVer>().unwrap());
```

### FsPort

TCP/UDP-Portnummer (1–65535). Port `0` ist immer invalid.

```rust
pub struct FsPort(pub u16);
```

TOML:
```toml
port = 8080
```

---

## Tag-System

Tags sind das primäre Suchinstrument im Store. Sie müssen **typsicher** (aus einer bekannten Bibliothek) und **übersetzbar** (i18n-Schlüssel, kein Hardcode) sein.

### FsTag

```rust
pub struct FsTag(String);  // Schlüssel z.B. "package.database"
```

TOML (serialisiert transparent als String):
```toml
tags = ["package.database", "platform.linux", "api.rest"]
```

Jeder Tag-Schlüssel hat einen i18n-Schlüssel: `tag.<key>` → z.B. `tag.package.database` → übersetzt als `"Database"` (en), `"Datenbank"` (de).

`tag.is_known()` → prüft gegen alle drei Standard-Bibliotheken.
`tag.is_valid_key()` → prüft Naming Convention (lowercase, Punkte, Bindestriche).

### TagLibrary Trait

```rust
pub trait TagLibrary {
    fn all_keys() -> &'static [&'static str];
    fn contains(key: &str) -> bool;
    fn all() -> Vec<FsTag>;
}
```

Drei eingebaute Bibliotheken:

| Bibliothek | Prefix | Beispiele |
|---|---|---|
| `PackageTags` | `package.*` | `package.database`, `package.ai`, `package.chat` |
| `PlatformTags` | `platform.*` / `requires.*` | `platform.linux`, `requires.systemd` |
| `ApiTags` | `api.*` | `api.rest`, `api.oidc`, `api.matrix` |

Factory-Funktionen für typsichere Tags:
```rust
PackageTags::database()      // FsTag("package.database")
PlatformTags::linux()        // FsTag("platform.linux")
ApiTags::oidc()              // FsTag("api.oidc")
```

### Neue Tags hinzufügen

1. Schlüssel zu `ALL_KEYS` in der passenden Bibliothek hinzufügen
2. Factory-Funktion hinzufügen
3. i18n-Eintrag `tag.<key>` in alle Sprachpakete (`en`, `de`, …) eintragen
4. Der Test `tag_key_convention` prüft automatisch die Naming Convention

---

## Language Provider

Sprachen können von außen hinzugefügt werden — z.B. durch Plugins oder Community-Packs:

```rust
pub trait LanguageProvider: Send + Sync {
    fn name(&self) -> &str;
    fn languages(&self) -> Vec<LanguageMeta>;
}

// Registry aggregiert alle Provider, dedupliziert nach Code
let mut registry = LanguageRegistry::new();  // builtin vorregistriert
registry.register(Box::new(MyCommunityPack));

let de = registry.find("de");  // builtin gewinnt bei Duplikat-Code
```

Der eingebaute `BuiltinLanguageProvider` liefert 50 Sprachen aus `languages.toml`.

---

## ResourceMeta Felder mit den neuen Typen

| Feld | Typ vorher | Typ jetzt |
|---|---|---|
| `version` | `String` | `SemVer` |
| `tags` | `Vec<String>` | `Vec<FsTag>` |
| `AppResource::locales` | `Vec<String>` | `Vec<LanguageCode>` |

Backward-kompatibel über `serde` — TOML/JSON Format bleibt gleich (alle serialisieren als String/Array-of-Strings).

---

## ConfigFieldKind für die Manager-UI

Die Manager-GUI kennt typsichere Input-Arten:

```rust
pub enum ConfigFieldKind {
    // Basis
    Text, Password, Number, Bool, Select, Port, Path, Textarea,
    // Typisierte Felder (FsValue)
    Url,          // FsUrl-Input, built-in placeholder + help
    LanguageCode, // Language-Picker aus LanguageRegistry
    SemVer,       // Versionsnummer-Input (MAJOR.MINOR.PATCH[-PRE])
    Tag { library: TagLibraryKind },  // Tag-Picker aus einer Bibliothek
}
```

---

Weiter: [i18n](i18n.md) | [Pakete](../konzepte/pakete.md) | [Bibliotheken](bibliotheken.md)
