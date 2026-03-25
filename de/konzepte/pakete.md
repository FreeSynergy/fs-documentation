# Pakete

[← Zurück zum Index](../INDEX.md) | [Store](../programme/store/README.md) | [Rollen](rollen.md) | [Adapter-Pattern](adapter.md)

---

## Paket-Typen

Jedes Paket hat genau einen **Typ**. Rust-Enum: `ResourceType` in `fs-types`.

| Typ | Inhalt | Beispiele |
|---|---|---|
| `app` | Native Rust-Binary (ein oder mehrere Binaries) | Node, Desktop, Browser, Kanidm, Stalwart, Mistral, Bots |
| `container` | Container-App — läuft mit Podman oder Docker | Forgejo, Postgres, Outline, CryptPad |
| `widget` | Desktop-Widget | Uhr, System-Info |
| `language` | Shared Snippets (Mozilla Fluent) | Deutsch, Japanisch |
| `task` | Automatisierungs-Template | "Docs ins Wiki" |
| `bundle` | Meta-Paket, referenziert andere Pakete per ID — lebt in `bundles/` | Zentinel-Bundle |
| `theme` | Bundle-Unterart mit fester Design-Struktur — lebt in `themes/` | Midnight Blue |
| `bootstrap` | Sondertyp: Init-Binary zum Download (kein Install) | fs-init |
| `repo` | Store-Repository-Quelle — registriert neue Paketquelle | freesynergy-community |
| `icon_set` | SVG-Icon-Sammlung | freesynergy-default |
| `external` | Externes Produkt ohne direkten Install (nur Link/Doku) | Drittanbieter-Tools |

**`app` mit mehreren Binaries:** Ein `app`-Paket kann mehrere Binaries haben
(z.B. Bots: ein Binary pro Messenger-Typ). Alle kommen aus einem einzigen GitHub-Release.
Das Manifest verwendet `[[binaries]]` statt `binary`.

**`container` vs. `app`:**
- `app` = natives Binary (kein Container-Runtime nötig): Kanidm, Stalwart, Zentinel, Mistral
- `container` = läuft als Container-Image: Forgejo, Postgres, Outline

**`bundle` und `theme`** enthalten keine Binaries — sie referenzieren andere Pakete per ID.
Sie leben nicht unter `packages/`, sondern im Root-Verzeichnis:

```
Store/
  bundles/    ← generische Bundles (type = "bundle")
  themes/     ← Design-Bundles (type = "theme")
  packages/   ← alle anderen Pakete
```

---

## Pflicht-Metadaten

Jedes Paket MUSS haben:

| Feld | Pflicht | Inhalt |
|---|---|---|
| `id` | Ja | Eindeutiger Name, kein Typ-Prefix |
| `name` | Ja | Anzeigename |
| `version` | Ja | SemVer, aus Git-Tag |
| `type` | Ja | Einer der Paket-Typen (siehe oben) |
| `summary` | Ja | Max 255 Zeichen — Store-Karte, Suchergebnisse |
| `description` | Ja | Mittellang, inline im Katalog-TOML |
| `description_file` | Ja | Pfad zu `help/en/description.ftl` |
| `icon` | Ja | Pfad zu SVG-Datei |
| `tags` | Ja | Typsichere `FsTag`-Werte (keine freien Strings) |

Fehlt `description` oder `description_file` → `ValidationStatus::Broken` →
Paket kann nicht installiert werden.

### Drei Beschreibungsebenen (alle Pflicht)

| Feld | Max | Wo gezeigt | Übersetzbar |
|---|---|---|---|
| `summary` | 255 Zeichen | Store-Karte, Suchergebnisse | Ja, via i18n |
| `description` | frei | Store-Detailansicht | Ja, via i18n |
| `description_file` | — | Pfad zu `help/en/description.ftl` | Ja — `.ftl` pro Sprache |

---

## Binaries (`[[binaries]]`)

Pakete vom Typ `app` liefern ihre Binaries über GitHub Releases.
Das Manifest enthält einen oder mehrere `[[binaries]]`-Einträge:

```toml
# Einfach — ein Binary
[[binaries]]
name   = "fs-browser"
arch   = "x86_64-unknown-linux-musl"
url    = "https://github.com/FreeSynergy/fs-browser/releases/download/v1.0.0/fs-browser-linux-x86_64"
sha256 = "abc123..."

# Mehrere Binaries (z.B. Bots — ein Binary pro Messenger-Typ)
[[binaries]]
name   = "broadcast-bot"
arch   = "x86_64-unknown-linux-musl"
url    = "https://github.com/FreeSynergy/fs-bots/releases/download/v1.0.0/broadcast-bot-linux-x86_64"
sha256 = "def456..."

[[binaries]]
name   = "menu-bot"
arch   = "x86_64-unknown-linux-musl"
url    = "https://github.com/FreeSynergy/fs-bots/releases/download/v1.0.0/menu-bot-linux-x86_64"
sha256 = "789abc..."
```

`fs-store` (StoreReader) lädt alle Binaries, verifiziert den SHA256-Hash,
legt sie im Install-Verzeichnis ab und schreibt einen Eintrag in `fs-inventory`.

---

## Capabilities und Bus-Messages

Jedes Paket deklariert was es dem System anbietet und was es braucht.
Das ist die **API des Pakets** — nicht eine separate Datei, sondern Teil des Manifests.

```toml
[capabilities]
provides = ["browser.open", "browser.navigate", "browser.screenshot"]
requires = []

[[bus_messages]]
topic   = "browser.open"
type    = "command"
payload = { url = "FsUrl" }

[[bus_messages]]
topic   = "browser.navigate"
type    = "command"
payload = { url = "FsUrl", tab_id = "u32" }
```

Diese Deklaration wird beim Start in `fs-registry` eingetragen.
Programme die eine Capability brauchen fragen die Registry — nie direkt das Paket.

---

## Manageable-Trait — Pakete als selbstbeschreibende Objekte

Jedes installierte Paket implementiert den `Manageable`-Trait (in `fs-pkg`).
Das Paket ist selbst verantwortlich für seinen Zustand und seine Konfiguration.

| Methode | Was sie liefert |
|---|---|
| `meta()` | Name, Version, Beschreibung, Icon, Tags, Autor |
| `package_type()` | App / Container / Widget / Language / … |
| `is_installed()` | Ob das Paket installiert ist |
| `run_status()` | Running / Stopped / Starting / Stopping / Error / NotInstalled |
| `config_fields()` | Alle Konfigurationsfelder mit Typ, Wert, Hilfe-Text |
| `check_health()` | Health-Checks: Konfig vorhanden? Daten-Verzeichnis ok? |
| `apply_config()` | Konfiguration übernehmen (Key-Value-Map) |
| `instances()` | Sub-Instanzen (z.B. mehrere Container parallel) |
| `can_start()` / `can_stop()` | Welche Aktionen gerade möglich sind |

### Package-Objekt

Das `Package`-Struct (in `fs-pkg`) vereint:
- `ApiManifest` — Metadaten aus dem Store-Katalog
- `InstalledRecord` — Installations-Zustand (Version, Pfad, Status)
- `config_overrides` — aktive Konfiguration im RAM

Wer wissen will ob Kanidm läuft, fragt `package.run_status()` — nie die DB direkt.

### ConfigField — Felder beschreiben sich selbst

| Feld | Inhalt |
|---|---|
| `key` / `label` | Schlüssel und Anzeigename |
| `help` | Pflicht-Hilfetext (fehlt er → Manager markiert mit Warnung) |
| `kind` | Text / Password / Number / Bool / Select / Port / Path / Textarea |
| `value` | Aktueller Wert |
| `required` | Pflichtfeld? |
| `needs_restart` | Neustart nötig nach Änderung? |

Der Manager liest `config_fields()` und rendert daraus die fertige Oberfläche —
ohne paketspezifischen UI-Code. Jeder Manager sieht dasselbe Interface.

---

## Paket-Lifecycle

```
Store-Katalog lesen (StoreReader)
  → Paket auswählen
    → Download + SHA256-Verifikation
      → Signatur-Check (ed25519)
        → Abhängigkeiten auflösen
          → Installieren → Eintrag in fs-inventory
            → Konfigurieren (Manager)
              → Starten → Capabilities in fs-registry registrieren
                → Nutzen (Bus-Messages, API-Calls)
                  → Update (neue Version)
                    → Rollback (vorherige Version)
                      → Stoppen → Capabilities aus Registry entfernen
                        → Deinstallieren → Eintrag aus fs-inventory entfernen
```

---

## Installations-Pfad

Wird deterministisch abgeleitet — nie im Manifest hardcodiert:

```
{base_dir}/{type}/{id}/{id}-{version}/
```

| Paket | Typ | Pfad |
|---|---|---|
| kanidm 1.5.0 | app | `{base_dir}/app/kanidm/kanidm-1.5.0/` |
| midnight-blue 1.0.0 | theme | `{base_dir}/theme/midnight-blue/midnight-blue-1.0.0/` |

**`base_dir`** ist ein einziger konfigurierbarer Pfad (Standard: `/opt/freesynergy/` auf Linux).
Beim Ändern des Pfads verschiebt der Store alle installierten Pakete automatisch.

---

## Tags

Tags sind typsicher — Rust-Typ `FsTag` aus bekannten Bibliotheken.
Kein freier String. Jeder Tag-Schlüssel ist ein i18n-Schlüssel.

```toml
tags = ["package.database", "platform.linux", "api.oidc"]
```

| Bibliothek | Prefix | Beispiele |
|---|---|---|
| `PackageTags` | `package.*` | `package.database`, `package.ai`, `package.security` |
| `PlatformTags` | `platform.*` / `requires.*` | `platform.linux`, `requires.systemd`, `requires.podman` |
| `ApiTags` | `api.*` | `api.rest`, `api.oidc`, `api.matrix` |

Der Store kombiniert `PlatformTags` mit SysInfo und blendet Pakete aus,
deren Voraussetzungen auf dem aktuellen System nicht erfüllt sind.

**Neue Tags hinzufügen:**
1. Schlüssel zu `ALL_KEYS` in `fs-types/src/tags/<bibliothek>.rs`
2. Factory-Funktion: `pub fn database() -> FsTag`
3. i18n-Eintrag `tag.<key>` in alle Sprachpakete schreiben
4. Der Test `tag_key_convention` in `fs-types` prüft die Convention automatisch

---

## Sprachpakete

Sprachpakete (`type = "language"`) haben einen erweiterten `[language]`-Block:

```toml
[language]
locale       = "de-DE"
display_name = "Deutsch"
direction    = "ltr"
completeness = 100
programs     = ["node", "desktop", "store"]
family       = "Indo-European"
continent    = "Europe"
```

`family` und `continent` sind Pflichtfelder — damit sie beim Erstellen eines
neuen Pakets nicht vergessen werden können.

Jedes Sprachpaket enthält 12 TOML-Snippet-Dateien:
`actions`, `nouns`, `status`, `errors`, `validation`, `phrases`, `time`,
`help`, `labels`, `confirmations`, `notifications`, `meta`

---

## Versionierung

SemVer + Git-Tags. Release-Channels: `stable`, `testing`, `nightly`.
Parallele Versionen möglich — Standard: latest installieren, alte löschen.

## Signierung

ed25519 als Standard (austauschbar: ed448, RSA).
Signatur wird vor Installation geprüft. Fehlt sie → Installation abgebrochen.

## Scripts

| Script | Wann |
|---|---|
| `pre_install` | Vor Installation (Voraussetzungen prüfen) |
| `post_install` | Nach Installation (Setup, erste Konfiguration) |
| `pre_remove` | Vor Deinstallation (Warnung, Daten sichern) |
| `post_remove` | Nach Deinstallation (Cleanup) |

## Abhängigkeiten

```toml
[dependencies]
fs-node = ">= 0.5.0"

[optional-dependencies]
kanidm = ">= 1.4.0"
```

---

## Container-Manifest (Vollständiges Beispiel)

```toml
[package]
id      = "ollama"
name    = "Ollama + Open WebUI"
version = "0.1.0"
type    = "container"
summary = "Lokale LLMs mit Web-Interface"
icon    = "ollama.svg"
tags    = ["package.ai", "package.chat", "platform.linux"]
license = "MIT"

[capabilities]
provides = ["llm", "llm.chat", "llm.api"]
requires = []

[services.main]
name  = "open-webui"
image = "ghcr.io/open-webui/open-webui:main"
port  = 3000

[services.sub.ollama]
name     = "ollama"
image    = "docker.io/ollama/ollama:latest"
port     = 11434
internal = true

[variables]
WEBUI_SECRET_KEY    = { type = "secret",  required = true }
OLLAMA_BASE_URL     = { type = "url",     auto = "http://ollama:11434", internal = true }
OPENID_PROVIDER_URL = { type = "url",     capability = "iam", required = false }
OAUTH_CLIENT_ID     = { type = "string",  capability = "iam", required = false }
DATABASE_URL        = { type = "connection-string", capability = "database", required = false }

[healthcheck.ollama]
test     = "curl -f http://localhost:11434/api/tags"
interval = "30s"

[healthcheck.open-webui]
test     = "curl -f http://localhost:8080/health"
interval = "30s"

[network]
auto = "ollama-backend"

[volumes]
ollama_data    = { target = "/root/.ollama",     s3_path = "media/ollama" }
openwebui_data = { target = "/app/backend/data", s3_path = "media/open-webui" }
```

---

Weiter: [Store](../programme/store/README.md) | [Inventory](inventory.md) | [Adapter-Pattern](adapter.md) | [Rollen](rollen.md)
