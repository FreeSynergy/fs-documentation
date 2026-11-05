# 0016 – Lizenz: MIT OR Apache-2.0, für immer kostenlos

Status: akzeptiert (2026-11-05) · löst den Konflikt aus Protokoll §20 P5

## Kontext
Manifest-Text sagte MIT, Repo und Website sagten Apache-2.0.

## Entscheidung
- Alle FreeSynergy-Repos: **`MIT OR Apache-2.0`** (Doppellizenz, wie im Rust-Ökosystem üblich).
- Apache-2.0 ist dabei, **nur um zu schützen**: ausdrückliche Patenterteilung, damit niemand
  nachträglich ein Patent anmeldet und das Projekt verklagt. Sonst soll die Lizenz nichts
  einschränken.
- FreeSynergy bleibt **für immer kostenlos und für alle zugänglich**. Daten und Kommunikation
  dürfen nicht von Geld abhängen — **keine Armutsdiskriminierung**. Kein bezahlter Teil, keine
  Paywall, kein Open-Core.

## Folgen
- Jedes Repo trägt `LICENSE-MIT` und `LICENSE-APACHE`; `Cargo.toml`: `license = "MIT OR Apache-2.0"`.
- `fs-documentation`: `LICENSE` → `LICENSE-APACHE`, `LICENSE-MIT` neu, README-Badge angepasst.
