# Übergabe: Programmier-Sitzung (Stand 2026-11-06)

Für eine neue Sitzung, die programmiert. Zuerst lesen: `conventions/CONVENTIONS.md` (§0 Grundsätze),
`conventions/coding.md` (Muster, kleine Dateien, Abhängigkeiten), ADRs 0019–0049 (Index
`conventions/decisions/README.md`), dann die `DESIGN.md` des Repos, an dem gearbeitet wird.

## Rollen (Nutzer, 2026-11-06)
- **Programmier-Sitzung** (diese Rolle): Code, Tests, Repos, Umbauten, technische Doku (`DESIGN.md`).
- **Entscheidungs-Sitzung** (`freesynergy-9b`, falls noch aktiv): Entscheidungen, ADRs, öffentliche Roadmap,
  `docs/en/interfaces/`. Keine ADR-Nummern selbst vergeben — Entscheidungen dorthin übergeben.
- Öffentliche Doku immer aktuell halten (Transparenz).

## Repos (alle öffentlich, github.com/FreeSynergy, lokal /srv/FreeSynergy/<repo>)
| Repo | Inhalt | Tests | Tag |
|------|--------|-------|-----|
| fs-store | Objektspeicher (AS2-Hülle, Protokoll, Undo, Turso) | 37 | v0.2.0 |
| fs-people (früher fs-contacts) | JSContact, vCard, Gleiche-Person-Vorschläge | 21 | v0.1.0 |
| fs-calendar | JSCalendar 2.0 Event, ICS, Einladungen; Aufgaben nur über `TaskItems` | 47 | v0.2.0 |
| fs-tasks | Besitzer von JSCalendar `Task` (ADR 0050); Trait `TaskItems`, Vertrag `schema/tasks.capnp` (Entwurf) | 18 | v0.1.0 |
| fs-maps | PMTiles bei Bedarf, Cache, Regionen, Orte | 30 | — |
| fs-hub | Programme verbinden, Objekt-Abgleich (Cap'n Proto RPC) | 9 | — |
| fs-wiki (crate fs-text) | Text + Ebenen, Markdown, Links, Vorlagen | 46 | — |
| fs-capnpc (crate capnp-compiler) | Cap'n-Proto-Compiler in reinem Rust, 14/14 Orakel | 30 | v0.1.0 |

## Offene Aufgaben (Reihenfolge)
1. `capnp-compiler` auf crates.io veröffentlichen — wartet auf bestätigte E-Mail des Nutzers; dann `cargo publish` in fs-capnpc.
2. ✅ `Task` in fs-tasks umgezogen (2026-11-06), Kalender nutzt nur `TaskItems`, Hub auf Kalender v0.2.0.
   **Offen:** fs-tasks enthält Kopien von Zeit/Zonen, `Participant`, `RecurrenceRule`, ICS-Zerleger aus fs-calendar
   (Doppelung, ADR 0043 §4) → gemeinsame JSCalendar-Basis-Crate? Entscheidung liegt bei der Entscheidungs-Sitzung.
3. Themen-Schnittstellen für das Gebaute (people, events, tasks, places, texts, messages) als versionierte Ziele;
   bestehende Kerne werden Anbieter davon (ADR 0045).
4. Sichtbarer Teil: Wiki-Workbench auf Blinc (zeigt fs-documentation), dann Groupware-Suite.

## Neue Vorgaben (Nutzer über die Entscheidungs-Sitzung, 2026-11-06)
- **Repo `fs-interfaces`** enthält alle Verträge + erzeugten Code (mit unserem `capnp-compiler`); Programme beziehen
  Verträge nur von dort (Git-Tag).
- **Anbieter-Regel (ADR 0045, geändert):** wie eine Elternklasse — jeder Anbieter bietet **alle** Methoden und Attribute;
  erst einen Weg suchen, nur wenn wirklich unmöglich: ausdrücklich `Unsupported` (Trait-Standardmethode). Jeder
  Anbieter meldet, was er kann.
- **Alles Bestehende gegen den Schnittstellen-Katalog umbauen**, Reihenfolge: **people** → groups, files → Rest;
  immer erst den Schnittstellen-Entwurf, dann Code. `fs-people`: **noch keine Rollen** (wartet auf den Nutzer).
- **`fs-jscalendar`:** nur gemeinsame Typen (kein Programm, keine Daten); fs-calendar/fs-tasks entdoppeln; Aufgaben aus
  **jedem** Import-Format an fs-tasks weitergeben. Zweiter Nutzer für `TaskItems`: erstes Aufgaben-Frontend oder CLI
  (Kanban ist eine Ansicht von fs-tasks, ADR 0049).
- **Plugins** nach Vorbild Zentinel (`crates/agent-protocol`, Hot-Reload in FreeSynergy/zentinel): reine Konfiguration
  geprüft und atomar getauscht; sonst abgeschottete Agenten-Prozesse, bei uns mit Cap'n Proto.
- **Video:** nur offene Formate (AV1, Opus); keinen eigenen H.264-Encoder, kein eigenes OpenH264.
- Zurückgestellt: Zusammenführen, Details Speichern/Export, eigenständige Ansichten.

## Release-Werkzeuge (Nutzer, 2026-11-06)
- Repo **`fs-release`**: gemeinsame Workflows (CI + Release), getestet an capnp-compiler und fs-hub.
- **Nur Kostenloses:** Linux (deb, rpm, tar.gz, AppImage, Flatpak, Arch), Windows (msi, exe, zip, unsigniert),
  macOS universal `.dmg` **unsigniert** (Apple bekommt kein Geld; gespendetes Konto wäre ok), Android über **F-Droid**,
  iOS nur bauen. Releases nur als **Entwurf**, öffentlich erst, wenn es etwas bringt.
- Signatur: **GPG/OpenPGP** (offener Standard, native Paketsignatur); SBOM **SPDX**; Herkunft **SLSA**; SemVer.
- Erstes Blinc-Programm auf Android/iOS testet Blincs Mobil-Teil — Fehler per PR zurück an den Autor.
- **SignPath (Windows-Signatur, kostenlos für OSS): Nutzer am 2026-11-13 erneut fragen.**

## Regeln, die man leicht vergisst
- Abhängigkeiten zwischen Repos nur über Git-Tags (coding.md §8); Probe: frischer Klon nach /tmp baut.
- Vor jedem Commit: `cargo fmt --check` (ohne --all), clippy -D warnings (pedantic), Tests,
  `scripts/check_rust_rules.py <repo>` = 0 Fehler. Nach Rust-Arbeit `scripts/clean_rust.py --root <repo> --apply`
  (`--all` nur, wenn kein Build mehr läuft). RAM: mit llama aktiv nur ~6 GB frei → `-j 4`.
- Agenten früh und oft committen lassen (Abbrüche verlieren sonst alles).
