# Unsere Arbeitsweise als Workflows (Koordinator, 2026-11-12)

Handelnde: **M** Mensch (Nutzer), **S** Strategie-LLM, **K** Koordinator (Sonnet), **P** Programm-Agent (Sonnet), **O** Opus, **H** Haiku, **CI** GitHub-Actions, **Skript** mechanisch lauffähig.
Spalte „Token“: ● kostet heute Tokens und ein Programm könnte es mechanisch tun · ○ braucht echtes Urteil.

## W1 Auftrag → Release → Nutzertest („Release-Kette“)

| # | Schritt | Wer | Eingabe → Ergebnis | Prüfregel | Fehlerpfad | Token |
|---|---|---|---|---|---|---|
| 1 | Auftrag formulieren | S/M | Wunsch → Auftrag mit Akzeptanz | Ziel + Grenzen (was NICHT) | Rückfrage an M | ○ |
| 2 | Agent anlegen (Worktree, Branch) | K | Auftrag → Worktree `.wt-<thread>` | Name, Basis = origin/main | – | ● |
| 3 | Bauen/Ändern | P | Auftrag → Commits lokal | Design Patterns, Interfaces, Doku | Frage an K bei gemeinsamer Schicht (Stopp-Regel) | ○ |
| 4 | Lokale Gates | Skript (P ruft) | Baum → `gates.sh` ok/rot | fmt, clippy pedantic, Tests, Regeln, Blinc-Lock | P korrigiert, Wiederholung | ● (Lauf + Auswertung) |
| 5 | Sonderzeichen-/Tipptest (UI) | Skript | Binary → typing-test grün/rot | virtuelle KWin | P korrigiert | ● |
| 6 | Opus-Review | O | Diff + Gates → JA/NEIN + Befunde | Gegenprobe der Tests, RFC/Quelle, keine KI-Spuren (Blinc) | NEIN → zurück zu 3, Delta-Review | ○ |
| 7 | Push + GitHub-CI | CI (K stößt an) | Branch → check/typing-test grün | Rerun nur bei Runner-DNS/apt | rot → 3; Queue-Stau → Warten (Queue-Abfrage ●) | ● |
| 8 | Merge ff auf main | K | grün+JA → main | nur ff, Kopf = geprüfter Kopf | Rebase → neue CI | ● |
| 9 | Tag | K | main → Tag vX | „Grün vor Tag“, Opus-JA liegt vor | – | ● |
| 10 | release.yml (Draft) | CI | Tag → Draft-Release + Artefakte | – | Rerun | ● |
| 11 | Pre-release schalten | K | `gh release edit --draft=false --prerelease` | Opus ok | – | ● |
| 12 | Katalog-Bump | CI (K stößt an) | `bump.yml` in fs-catalog (ggf. packages.toml-Eintrag) | – | Eintrag ergänzen | ● |
| 13 | Signatur | CI | Katalog → signierte Datei | GPG/cosign | rot → Ursache | ● |
| 14 | `fs-store check` | Skript | Katalog → ok | Signatur, Hash, Fähigkeiten | rot → 12/13 | ● |
| 15 | Nutzertest | M | installieren, benutzen | Abnahmebild/Sitzung | Befund → 1 | ○ |
| 16 | Bericht gebündelt | K → S | Ergebnis ≤10 Zeilen | nur bei Release/Blocker/Frage | – | ○ |

**Mechanisierbar (●): Schritte 2, 4, 5, 7–14** – das ist eine Kette „`release <repo> <branch>`“, die nur bei O-Urteil (6), P-Arbeit (3) und M-Test (15) anhält. Heute gehen dafür pro Release ca. 8–12 Agentenrunden/Befehle drauf (Branch-Stand lesen, Lauf-Status abfragen, ff, Tag, Release, Bump, Sign, Check).

## W2 Blinc-Upstream-PR

| # | Schritt | Wer | Prüfregel | Fehlerpfad | Token |
|---|---|---|---|---|---|
| 1 | Fund (Repro/Test in virtueller KWin; reiner Quelltext = „Verdacht“) | P | echter Test vorher | Verdacht melden, kein PR | ○ |
| 2 | Frage an S: neuer PR erlaubt? | K→S | nur nach Freigabe | – | ○ |
| 3 | Kleiner Diff, Blinc-CLAUDE.md, **keine KI-Hinweise**, git-bug-Trailer | P | Diff klein, Test mit Gegenprobe | – | ○ |
| 4 | Opus-Review vor Push | O | Vollständigkeit, ehrliche Texte (Windows/macOS „nicht getestet“) | NEIN → 3 | ○ |
| 5 | Antworttext Englisch Punkt für Punkt | P | keine falschen Behauptungen | O prüft | ○ |
| 6 | Push (nach Push-Pause) | K | – | – | ● |
| 7 | Fork-Tag (fs-blinc-N), `approve-blinc add --expires`, fs-components heben | K/Skript | Lock-Gate nur freigegebene Quelle | rot → Ursache | ● |

Mechanisierbar: 6, 7 (Tag-Kette + Allow-Liste).

## W3 Doku-Commit

| # | Schritt | Wer | Prüfregel | Fehlerpfad | Token |
|---|---|---|---|---|---|
| 1 | Text schreiben (ADR/Befund) | P/Docs-Agent | amtliche Doku aktuell, Quellen belegt, [nicht belegt] markiert | – | ○ |
| 2 | `check-docs.sh` (strict + gen_decisions) | Skript | mkdocs strict grün | korrigieren | ● |
| 3 | Review durch S (ADR) | S | Strategie prüft | Rückgabe | ○ |
| 4 | Push main/Branch | K | nur fs-documentation-Worktree, nie Hauptbaum | – | ● |
| 5 | Pages-Deploy | CI | grün | Rerun | ● |

## W4 Recherche → Empfehlung → ADR

| # | Schritt | Wer | Prüfregel | Token |
|---|---|---|---|---|
| 1 | Fragenliste | S/K | Ziel, Grenzen, Quellenarten | ○ |
| 2 | Sammeln | H | Primärquellen (URL/Abschnitt), Unbelegtes markiert | ○ (billig) |
| 3 | Vergleichen + Stichproben prüfen | O | Widersprüche klären, Empfehlung + Varianten | ○ |
| 4 | Entscheidung/Fragen an Nutzer | S→M | Fragen gebündelt am Ende | ○ |
| 5 | ADR-Entwurf | Docs-Agent | Status Entwurf, strict grün | ○ |
| 6 | ADR akzeptiert + Merge | S/M | „akzeptiert (Strategie, Datum)“ | ● |

## W5 Queue-/Runner-Überwachung (heute oft von Hand)

Lauf-Status abfragen (ein Lauf, alle 30 min), Jobs zählen, Rate-Limit lesen, Cache-Größen – **vollständig mechanisch (●)**: Skript + Schwelle → nur bei Änderung wecken.

## Was heute Tokens kostet, ein Programm aber tun könnte (Kandidaten für die ersten Workflows)

1. **Release-Kette** (W1 7–14): ein Befehl, Haltepunkte nur bei Opus/M.
2. **Gate-Lauf + Auswertung** (W1 4–5): ein Befehl, Ausgabe = ok/rot + erste Fehlerzeile.
3. **Queue-/Rate-/Speicher-Wächter** (W5, Slot-Watch existiert als Skript).
4. **Worktree/Branch anlegen und Aufräumen** (W1 2).
5. **Blinc-Tag + Allow-Liste + Heben** (W2 7).
6. **Doku-Check + Push-Pfad** (W3 2, 4).
7. **Berichte**: Statusblatt aus Task-Daten statt Text (wenn Tasks live Kanban zeigt).
