# 0040 – Cap'n-Proto-Schema-Compiler in reinem Rust; Anerkennung ohne Drama

Status: akzeptiert (2026-11-05) · Recherche `temp/research/capnp-codegen.md` · ADR 0013, 0015, 0021, 0025

## Kontext
Die Laufzeit `capnp` ist reines Rust, aber `capnpc` ruft zum Einlesen des Schemas den C++-Compiler
`capnp` auf. Ein Compiler in reinem Rust existiert nicht.

## Entscheidung
1. **Wir programmieren den Schema-Compiler in Rust nach** — Quelltext lesen (MIT), verstehen,
   in Rust neu schreiben: Parser, Namensauflösung, ID-Vergabe, Speicherlayout (bitgenau), Prüfung
   der Weiterentwicklung, Ausgabe als `CodeGeneratorRequest` für `capnpc::codegen`.
2. **Geprüft gegen das Original:** gleiche Schemas (inkl. der offiziellen Test-Schemas) mit unserem
   Compiler und mit `capnpc-embedded` übersetzen, Ergebnis Byte für Byte vergleichen.
3. **Veröffentlichung auf crates.io**, damit jeder ihn nutzen kann; Angebot an `capnproto-rust`.
4. **Bis dahin:** `capnpc-embedded` für Schema-Änderungen; der erzeugte Rust-Code liegt im Repo.

## Anerkennung (Nutzer, 2026-11-05)
Wer die Arbeit gemacht hat, bekommt den Lohn: das Original nennen wir in `NOTICE`/README fair
(„Layout-Algorithmus und Verhalten nach Cap'n Proto, MIT, Sandstorm/Cloudflare und Mitwirkende“),
unsere Arbeit ist unsere. Kein Drama daraus — es soll funktionieren.
Gilt allgemein für jedes Nachprogrammieren nach Lektüre offener Quellen.
