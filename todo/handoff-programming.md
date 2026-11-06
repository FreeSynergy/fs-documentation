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
| fs-calendar | JSCalendar 2.0 Event (+ noch Task → zieht nach fs-tasks), ICS, Einladungen | 45 | v0.1.0 |
| fs-maps | PMTiles bei Bedarf, Cache, Regionen, Orte | 30 | — |
| fs-hub | Programme verbinden, Objekt-Abgleich (Cap'n Proto RPC) | 9 | — |
| fs-wiki (crate fs-text) | Text + Ebenen, Markdown, Links, Vorlagen | 46 | — |
| fs-capnpc (crate capnp-compiler) | Cap'n-Proto-Compiler in reinem Rust, 14/14 Orakel | 30 | v0.1.0 |

## Offene Aufgaben (Reihenfolge)
1. `capnp-compiler` auf crates.io veröffentlichen — wartet auf bestätigte E-Mail des Nutzers; dann `cargo publish` in fs-capnpc.
2. **Ein Standard → ein Programm → eine Schnittstelle** (Nutzer): `Task` aus fs-calendar in **fs-tasks** (eigenes Repo,
   eigene Schnittstelle); fs-calendar bindet Aufgaben nur über diese Schnittstelle ein. Form/Ort der Schnittstellen
   (Repo `fs-interfaces`, ADR 0045) mit der Entscheidungs-Sitzung klären.
3. Themen-Schnittstellen für das Gebaute (people, events, tasks, places, texts, messages) als versionierte Ziele;
   bestehende Kerne werden Anbieter davon (ADR 0045).
4. Sichtbarer Teil: Wiki-Workbench auf Blinc (zeigt fs-documentation), dann Groupware-Suite.

## Regeln, die man leicht vergisst
- Abhängigkeiten zwischen Repos nur über Git-Tags (coding.md §8); Probe: frischer Klon nach /tmp baut.
- Vor jedem Commit: `cargo fmt --check` (ohne --all), clippy -D warnings (pedantic), Tests,
  `scripts/check_rust_rules.py <repo>` = 0 Fehler. Nach Rust-Arbeit `scripts/clean_rust.py --root <repo> --apply`
  (`--all` nur, wenn kein Build mehr läuft). RAM: mit llama aktiv nur ~6 GB frei → `-j 4`.
- Agenten früh und oft committen lassen (Abbrüche verlieren sonst alles).
