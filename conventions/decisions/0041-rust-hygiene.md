# 0041 – Rust-Hygiene: Build-Ausgabe klein halten, nie in Git, regelmäßig aufräumen

Status: akzeptiert (2026-11-05)

## Kontext (Nutzer)
Rust erzeugt sehr viel Debug-Information und Cache. Das darf nicht ins Repo und muss immer wieder
aufgeräumt werden — das wird später noch wichtig (viele Repos, ADR 0017).

## Entscheidung
1. **`.gitignore`-Vorlage** für jedes Rust-Repo: `conventions/templates/rust/.gitignore`
   (`target/`, Debug-Symbole, Profiling-Reste, lokale Geheimnisse). `Cargo.lock` wird committet.
2. **Cache nie auf GitHub:** `target/` ist ignoriert; Zugangsdaten (crates.io-Token) liegen nur in
   `~/.cargo`, nie im Repo.
3. **Weniger Debug-Info von Anfang an:** `conventions/templates/rust/.cargo/config.toml` —
   `debug = "line-tables-only"` für eigenen Code, keine Debug-Info für Abhängigkeiten, Release ohne
   Symbole.
4. **Immer aufräumen:** `scripts/clean_rust.py` entfernt inkrementelle Caches und alte Debug-Builds
   in allen Repos unter `/srv/FreeSynergy` (Trockenlauf ohne `--apply`). **Nach jeder Arbeitssitzung
   mit Rust ausführen**; bei Bedarf Größengrenze `--max-gb`.
5. `--all` (alle `target/`-Ordner) **nur, wenn kein Build mehr läuft** — sonst reißt man laufenden Agenten den Build weg (passiert 2026-11-06). Im laufenden Betrieb `--root <repo>` verwenden.
