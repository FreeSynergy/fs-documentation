# Store — Das Wissen

[← Zurück zum Index](../../INDEX.md)

---

## Was der Store ist

Der Store ist NICHT nur eine Download-Plattform. Er ist ein **Wissensspeicher** der allen Programmen hilft.

## Drei Funktionen

1. **Bereitstellen:** Pakete zum Download (Plugins, Sprachen, Themes, Widgets, Bots, Tasks)
2. **Wissen:** Der Conductor fragt "Kennst du diesen Service?" → Store liefert Metadaten, Rollen, Variablen-Typen
3. **Versionierung:** Jedes Paket hat Version + Tag → Updates, Rollbacks, Changelogs

## Paket-Typen

| Typ | Inhalt |
|---|---|
| `container` | Service-Modul (Quadlet + Config) |
| `language` | Sprach-Snippets (.ftl) |
| `theme` | Visuelles Theme |
| `widget` | Desktop-Widget |
| `bot` | Bot-Definition |
| `bridge` | Service-Bridge |
| `task` | Automatisierungs-Template |

## Paket-Metadaten (jedes Paket hat diese)

```toml
[package]
id = "kanidm"                        # Eindeutiger Name (KEIN Typ-Prefix!)
name = "Kanidm"
version = "1.5.0"
type = "container"
description = "Modern identity management"
icon = "kanidm"                       # Icon-Name oder SVG-Pfad
tags = ["iam", "oidc", "scim", "mfa", "webauthn", "identity", "rust"]
author = "Kanidm Project"
license = "MPL-2.0"
homepage = "https://kanidm.com"
source = "https://github.com/FreeSynergy/Store"
```

**Tags sind entscheidend für die Suche.** Bei Modulen: Alle Service-Namen, Subservice-Namen, Rollen. Bei Themes: Farben, Stil. Bei Widgets: Funktionsbeschreibung. Ohne gute Tags findet man nichts.

Jedes Paket MUSS ein Icon haben. Wenn keins mitgeliefert wird, wird ein generisches Icon für den Paket-Typ verwendet.

## Verzeichnisstruktur

```
Store/
├── shared/          ← Für ALLE Programme
│   ├── i18n/
│   ├── themes/
│   ├── widgets/
│   ├── bots/
│   └── tasks/
├── node/            ← Für Node
│   ├── modules/
│   └── bridges/
├── desktop/         ← Für Desktop
└── catalog.toml
```

## Eigenständigkeit

Der Store ist ein Git-Repository. Man kann es klonen und komplett offline nutzen. Wenn Internet da ist, kann der Store auch von einer URL geladen werden.

## Repo

https://github.com/FreeSynergy/Store

---

Weiter: [Desktop](../desktop/README.md) | [Pakete](../../konzepte/pakete.md)
