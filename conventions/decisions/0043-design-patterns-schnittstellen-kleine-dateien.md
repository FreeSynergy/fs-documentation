# 0043 – Entwurfsmuster, Schnittstellen zuerst, kleine Dateien, Refactoring und Doku

Status: akzeptiert (2026-11-06) · Regelwerk: `conventions/coding.md` · Prüfer: `scripts/check_rust_rules.py`

## Kontext (Nutzer)
Oberste Regel beim Programmieren ist die Wiederverwendbarkeit. Dafür gibt es Entwurfsmuster. Rust
kennt keine Objektorientierung, aber Entsprechungen. Nachtbefund 2026-11-06: Dateien bis 1.259 Zeilen.

## Entscheidung
1. **Alle Programme IMMER nach Entwurfsmustern** — benannt im Modul-Kopf (`Pattern: …`), Katalog in
   `conventions/coding.md` §2.
2. **Immer gegen Schnittstellen programmieren** (Traits; zwischen Programmen Cap'n Proto) — nie
   „einfach so“; Standards bestimmen die Schnittstelle.
3. **Kleine Dateien, dafür viele:** ein Konzept pro Datei; Richtwert ≤ 200, Grenze 300 Zeilen.
4. **Refactoring ist Pflicht**, getrennt committet, Tests bleiben grün.
5. **Dokumentation** für Menschen und für das nächste Modell: Modul-Doku, Doku jedes öffentlichen
   Elements, `DESIGN.md` mit Muster-Karte und aktuellem Stand.
6. Prüfung vor jedem Commit: fmt, clippy, Tests, `check_rust_rules.py`, Rust-Hygiene (ADR 0041).

## Folgen
- Bestehende Repos (fs-store, fs-people, fs-calendar, fs-maps, fs-hub, fs-wiki, fs-capnpc) werden
  nach diesen Regeln umgebaut.
