# Forks — Build-Strategie

[← Zurück zum Index](../INDEX.md) | [Build-Workflow](build-workflow.md)

---

## Übersicht

FreeSynergy nutzt mehrere Fork-Repos für Drittanbieter-Software. Diese werden nicht
neu entwickelt, sondern kompiliert, als OCI-Image verpackt und in den Store-Katalog
eingetragen. Eigene Code-Änderungen werden auf ein Minimum reduziert.

---

## Fork-Repos

| Fork | Original | Zweck |
|---|---|---|
| `FreeSynergy/kanidm` | `kanidm/kanidm` | Identity Provider (IAM) |
| `FreeSynergy/tuwunel` | `matrix-construct/tuwunel` | Matrix-Server |
| `FreeSynergy/stalwart` | `stalwartlabs/stalwart` | Mail-Server |
| `FreeSynergy/mistral.rs` | `EricLBuehler/mistral.rs` | LLM-Inference |
| `FreeSynergy/zentinel` | `zentinelproxy/zentinel` | Proxy |
| `FreeSynergy/zentinel-control-plane` | `zentinelproxy/zentinel-control-plane` | Proxy Control Plane |

---

## Grundregel: Nur OCI-Images

Für Forks gibt es **keine eigenen Binary-Releases**. Upstream liefert seine eigenen
Binaries — FreeSynergy verpackt sie als OCI-Image mit FreeSynergy-Konfiguration.

```
Kein:   ghcr.io/freesynergy/kanidm:v1.5.0 binary release
Ja:     ghcr.io/freesynergy/kanidm:v1.5.0 OCI-Image (mit FreeSynergy-Config)
```

---

## Eigene Änderungen

Minimale Patches — ausschließlich:
1. **Containerfile** — Packaging, FreeSynergy-Konfigurationsstruktur
2. **CI/CD-Konfiguration** — GitHub Actions
3. **FreeSynergy-Integration** — nur wenn zwingend nötig (z.B. `fs-registry` Anbindung)

**Keine Feature-Entwicklung im Fork.** Alle Features gehen als PR an Upstream.

---

## GitHub Actions — Automatischer Upstream-Sync

### Sync-Workflow (`sync-upstream.yml`)

```yaml
# Läuft wöchentlich + bei neuem Upstream-Tag
on:
  schedule:
    - cron: "0 3 * * 1"   # Montags 03:00 UTC
  workflow_dispatch:        # Manuell auslösbar

steps:
  - git fetch upstream
  - git rebase upstream/main
  # Bei Konflikten: Workflow schlägt fehl → GitHub-Notification → manuell lösen
```

Bei Rebase-Konflikten schlägt der Workflow fehl — keine automatische Auflösung.
Der Maintainer wird via GitHub-Notification informiert und löst manuell.

### Build-Workflow (`release.yml`)

```
Trigger: neuer Tag in diesem Repo (nach erfolgreichem Sync)
         oder manuell (workflow_dispatch)

Steps:
  1. cargo build --release (für target linux/amd64 + linux/arm64)
  2. Containerfile bauen → OCI-Image
  3. Image pushen zu ghcr.io/freesynergy/{name}:{upstream-tag}
  4. PR gegen Store/-Repo öffnen (catalog entry aktualisieren)
```

### Tag-Namensschema

```
ghcr.io/freesynergy/kanidm:1.5.0      ← Upstream-Version
ghcr.io/freesynergy/kanidm:latest     ← Zeigt auf neueste stabile Version
```

Kein eigenes Versioning — die Tag-Nummer entspricht immer der Upstream-Version.

---

## Store-Katalog-Eintrag

```toml
# Store/packages/programs/kanidm/1.5.0.toml
[package]
id      = "kanidm"
type    = "program"
source  = "fork"
upstream = "https://github.com/kanidm/kanidm"

[container]
image  = "ghcr.io/freesynergy/kanidm:1.5.0"
digest = "sha256:{digest}"
```

Das Feld `source = "fork"` zeigt im Store an, dass es sich um eine externe Software
handelt. Der Link zu Upstream ist verpflichtend (Lizenz-Compliance + Transparenz).

---

## Lizenz-Compliance

| Fork | Lizenz | Anforderung |
|---|---|---|
| kanidm | MPL-2.0 | Quellcode-Link im Katalog, Änderungen veröffentlichen |
| tuwunel | AGPL-3.0 | Quellcode öffentlich, alle Änderungen veröffentlichen |
| stalwart | AGPL-3.0 | Quellcode öffentlich, alle Änderungen veröffentlichen |
| mistral.rs | MIT | Keine Einschränkungen |
| zentinel | Apache-2.0 | NOTICE-Datei beibehalten |

Da alle Forks in öffentlichen GitHub-Repos sind, ist die Quellcode-Anforderung
automatisch erfüllt. Kein zusätzlicher Aufwand nötig.

---

## Warum keine eigenen Binaries?

1. **Upstream baut besser** — ihre CI kennt ihre Eigenheiten
2. **Weniger Maintenance** — kein eigenes Cross-Compilation-Setup nötig
3. **OCI reicht** — FreeSynergy-Nutzer installieren via Container

---

Weiter: [Build-Workflow](build-workflow.md) | [Adapter-Pattern](../konzepte/adapter.md) | [← Index](../INDEX.md)
