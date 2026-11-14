# Übergabe: Strategie-Sitzung (Stand 2026-11-14, nach Kontingent 99 %)

Für eine neue Strategie-Sitzung (Opus). **Zuerst lesen:** diese Datei, dann das Memory `/home/kal/.claude/projects/-srv-FreeSynergy/memory/MEMORY.md` (alle verlinkten Dateien), dann die ADRs 0072–0085 in `conventions/decisions/`.

## Rollen
- **Strategie (Opus, `freesynergy-c5`):** spricht als Einzige mit dem Nutzer (Deutsch, einfache Sprache, Fragen am Ende), entscheidet, schreibt ADRs, prüft Bilder, gibt Aufträge an den Koordinator. Programmiert und installiert nicht selbst.
- **Koordinator (Sonnet, /loop, Zed):** heißt nach jedem Zed-Neustart anders (ListAgents; zuletzt `freesynergy-e2`). Startet Bau-Läufe (Sonnet), Reviews (Opus), Recherchen (Haiku). Pusht/tagt/veröffentlicht erst nach Opus-JA und grüner CI. Handelt nur auf Rot oder auf Freigabe-Gates (Stille bei Grün).
- **Kontingent:** Stand 2026-11-14 bei 99 %. Nichts Neues starten, nur Laufendes auslaufen lassen und sichern (siehe unten). Budgetplan: API bis So 15.11. 18:00, danach nur Abo (siehe Memory `project-budget-plan-week`).

## Regeln von heute (Nutzer, dauerhaft)
- **KEINE KI auf Servern:** kein Agent bekommt SSH/Root auf einen echten Server (auch nicht node1). Der Mensch führt Skripte aus; Agenten testen nur lokal (VM/Container) und lesen Protokolle. Jeder Workflow muss OHNE KI laufen (deterministisch, Trockenlauf, Protokoll). Ausgangspunkt eines Server-Aufbaus ist ein vorhandenes System mit SSH-Zugang (ADR 0079).
- **Stille bei Grün:** der Koordinator meldet nur Rot und Freigabe-Gates; Ereignis-Verkettung nach ADR 0081 (CI-Ereignisse = CloudEvents).
- **Wrapper statt Fork:** fremde Crates per Pin+Adapter; Anfragen an Upstreams (Blinc) per git-bug.
- **Lieber viele kleine Updates:** Blinc-Pin auf aktuelles main heben (Workflow `lift`, Gates aller Programme), dann regelmäßig (z. B. wöchentlich) nachziehen; gilt für alle Upstreams (Kanidm, Zentinel …).
- **Baustein-Analyse zuerst** (dossier/frontend-round, Prüfschritt `baustein-zuordnung`): Reihenfolge 1) jeden Bereich des Vorbilds einer Baustein-Familie zuordnen (Quellen: fs-components-Familie → Blinc-Widget per Adapter → neuer Baustein mit Begründung), 2) Aussehen (Stil/Tokens, ADR 0074), 3) Zusammensetzen. Beispiel: die Datei-Tabelle in fs-files ist derselbe Tabellen-Baustein wie später in fs-data (Formeln = Modul).
- **Stil-Vollständigkeit** (ADR 0074 Nachtrag, Entwurf in `plan-theme-bruecke.md` §10): jeder Stil gestaltet JEDEN Baustein mit allen Teilen/Zuständen des Theme-Vertrags (Skript `stil-vollstaendigkeit`, fehlender Eintrag = ROT); jedes nachgebaute Vorbild liefert einen gespeicherten Stil (`stil-sichern`, englischer Name); neuer Baustein/Teil/Zustand ⇒ neue Version des Theme-Vertrags + Schritt `alle-stile-erweitern`; Test `zwei-stile` (Craft + Admin/Fiori), Tokenprobe Stufe 2 vor Runde D; Vertrag 0.2 mit allen ~35 Namen; Toast bei Fehlern ohne Selbstablauf. Nichts im Blinc-Standardlook.
- **Echte Blinc-Bausteine statt gemalter** (Liste `bestand-gemalte-nachbildungen.md`, 32 Funde; Runden A Formularfelder, B Meldungen, C Reiter/Umschalter, D Überlagerungen, E Bäume/Button). Löschrückfragen als echte Dialoge mit Fokus auf „Behalten". Craft-Optik bleibt, aber nur über Tokens/Stil-Schicht.
- **Editor-Bausteine sind ANSICHT, nicht Frontend** (ADR 0084 Nachtrag): SourceEditor/BlockEditor/RichTextEditor/später Writer (ODF) je Dokument wählbar; Speicher bleibt unser Blockmodell; Umwandeln je Dokument/Block über Exporter; mehrere Ausgaben je Dokument.
- **Normalisierung an der Grenze** (ADR 0085, Entwurf): innen nur AS2 + Standards; Zeiten UTC + IANA-Zone (ganztägig = Datum, nie umgerechnet; schwebende Zeit wird mit `zone_assumed` aufgelöst); Personen = Verweis `PersonRef { id, art, abzug }`, eingefrorener Abzug bei „ausgestellt = eingefroren“ (Buchung, Rechnung, Vertrag …). Bestand: `.scratch/bestand-zeiten-personen.md`.
- **fs-server verbindet** (ADR 0082): Mediator zwischen Personen/Gruppen und Kanidm (fs-identity), Pilot 3 Anmeldung kanidm-unixd/PAM, Erkennung über fs-hub.
- **Abnahmebilder** müssen mit denselben Stilen wie das echte Programm gezeichnet werden (Harness richtigstellen, keine Toleranz). Bilder → Strategie-OK → erst dann tag/release.
- Weitere dauerhafte Regeln: R1 „Frontend“ nie „Gesicht“; R2 Dossier vor jedem Frontend (Menü-Inventar, Schritt `menue-vergleich`); ALLE Arbeit über Workflows; ADR-Greps vor technischen Entscheidungen; curl nur lesend auf amtlichen Domains; keine Credentials lesen.

## ADRs von heute (alle auf Doku-main)
0072–0076 Blöcke/Katalog/Facetten; 0077 Katalog-Arten (`kind` inkl. server/workflow/module); 0078 Paketquellen apt/dnf (fs-packages); 0079 fs-server (Weg A/C, SSH-Ausgangspunkt, btrfs-Standard, Mensch führt aus); 0080 Umzug fs-wiki → fs-text; 0081 CI-Ereignisse = CloudEvents; 0082 fs-server verbindet; 0083 reserviert (Web-Zugang der Programme, noch nicht geschrieben); 0084 Editor-Bausteine (+Nachträge Baustein≠Programm, Katalogart module, Editor-Wahl ist Ansicht); 0085 Normalisierung (Entwurf).

## Veröffentlicht (Stand 2026-11-14)
- fs-components **v0.0.18** (Umbau-Werkzeug, Bildtest mit Toleranzen charts/kanban/primitives + RASTER) und **v0.0.19** (Editor-Fixes N1/N2/C1–C3, W1–W4, E1–E5, Editor-Vertrag `TextEditor`, schmale Fenster).
- fs-wiki **v0.0.12** (Pre-release, im Katalog, sign grün) auf fs-components v0.0.19.
- fs-interfaces v0.0.20, fs-kanidm v1.12.1, fs-zentinel v26.11_2 (Pre-release), fs-catalog sign-check/verify-Job.

## Offene Folgepunkte (Reihenfolge)
1. **fs-wiki 0.0.13:** geöffnete Seite muss im Seitenbaum markiert sein (Baum nach Speichern/Anlegen neu?); Wiki-Wörter vs. `for_locale` entdoppeln.
2. **fs-components 0.0.20:** `AppWidget::picture` mit UA-Stilen; Baum-Beschriftung `Handb…` + Tooltip; Classic im Schmal-Test (900/480); Tastenkürzel-Feld an Befehls-Id + `fs-menu-dump/1`; Bildtest `pixels.rs` unter Noto-only; Blinc-Pin-Lift; Theme-Brücke + Vertrag 0.2.
3. **fs-release 0.0.7/0.0.8-Bündel (lokal, NICHT gepusht):** wt/menue-vergleich (Kopf `e4b22a2`: baustein-zuordnung, programm-neu, zwei-stile/stil-sichern), upstream-update, server-einrichtung, anbieter-neuinstallation, ereignis-profil (Kleinpunkte: `_notify-red` jq --arg, @main→SHA, README), inhalt-aufbereiten + facette-anlegen (noch zu schreiben), Bilder-Gate. Opus-Review des Bündels vor Tag; alle Crates = Tag.
4. **Server-Kette (WIP-gesichert, unreviewed):** kanidm-deb (Fix lld/`kanidmd version`/Deps, Review), fs-server-run Wrapper + fs-server-bestand, APT-Repo fs-packages lokal + apt-sign-Action, Zentinel .deb; Montag (Nutzer führt aus): Server 2 Neuinstallation (Weg C), server-einrichtung, Zentinel + statische „im Umbau“-Seite für freesynergy.net/helfa.org/freeplanetearth.org.
5. **Umzug fs-wiki → fs-text (ADR 0080):** Platzhalter-Repo fs-text (Sicherung `archiv/fs-text-platzhalter.git`) → rename `fs-text-archive`, fs-wiki → fs-text; `replaces`-Katalogfeld vor Schritt 6; Pilot-Facette Wiki (`facette-anlegen`).
6. **Crate-Familien (Plan `plan-crate-familien.md`, 21 Familien):** erst `base`, `icons`, leeres `editor-api` nach 0.0.18; Editor-Crates `-editor-api` + `-editor-source/-block/-rich`; EIN Board-Baustein (plan+kanban → `board`), EIN Kalender-Raster; `tables` als Kernfamilie (list_view → table, Module für Formeln); Ordner `kern/` + `adapter/` + Prüfskript `check_kern_adapter.py`; Facades `widgets`/`workbenches` ≥ 2 Tags. Plan + Crate-Liste an Strategie VOR dem ersten Umzug.
7. **Welle-1-Bugfixes aus ADR 0085:** `fs-types::DateTime` UTC + Zone (Basis), Kalender-Einladungen/Kanban-assignee → PersonRef, Tasks ganztägige Fälligkeit (`plan-dossiers-welle1.md`, Abschnitt am Ende).
8. **Dossiers:** Welle 1 (files, wiki, store, tasks) auf Doku-main; Nachbesserungen Store/Discover (Plasma 6), Jira-Kürzel, Things/Windows; Welle B (Google/Outlook Kalender, OSM), Apple Kontakte; Welle 2 (Microsoft Store, M365 Groups, Apple Kalender).
9. **Weitere Pläne:** ADR 0083 (Web-Zugang der Programme) schreiben lassen; fs-identity `apply` umbauen (nur nach Bestätigung); Pilot Wiki online 1a (statischer HTML-Export); Rich-Editing-Spike (Blinc `rich_text_editor` per Adapter), node_editor-Spike niedrige Priorität nach Welle 1; Apps ohne gelesene Oberfläche eigene Runde nach Welle 1; Schema 2 Katalog (neutrales Server-Icon, 7 Icon-Fehler, `replaces`).
10. **Termine:** ~19.11. ArtCraft/VectorCraft-Text; ~24.11. Präsentation Anthropic (Bewerbung ~26.11.); SignPath (Nutzer-JA, wir bereiten vor); bis So 15.11. 18:00 `straenge-vollgas.md` final an Strategie (Entwurf 31 Stränge, mit F1–F8, fs-text-kein-Neubau, Dossiers, Ereignis-Verkettung aktualisieren).

## Offene Fragen an die Strategie/den Nutzer
- Blinc-Spike `rich_text_editor` ja (per Adapter); Fragen aus `blinc-bausteine.md` (cargo deny im Spike? git-bug an Blinc zu Bidi/LICENSE bei `blinc_game_kit`/`blinc_input`).
- ADR 0085 offen: Typ der `id` in PersonRef; eigener Typ „überall 8 Uhr“; woran „die Quelle“ erkannt wird; reines Datum vs. ADR 0020; DSGVO-Aussagen sind [nicht belegt].
- Theme-Brücke: Festwert-Anfragen an Darmie nach Spike S0 gebündelt per git-bug.

## Lokale Arbeit (nichts davon gepusht außer `unreviewed/*`-Branches; Sicherung 2026-11-14)
Alle Worktrees unter `/srv/FreeSynergy/.scratch/api-runner/wt/<name>` wurden per WIP-Commit gesichert und als Branch `unreviewed/<name>` auf das jeweilige origin gepusht (kein main, kein Tag). Inventar: `.scratch/worktree-inventory.md`. Wichtige Köpfe: fs-release `wt/menue-vergleich` e4b22a2 (programm-neu, baustein-zuordnung, Theme-Workflows), `wt/server-einrichtung`, `wt/anbieter-neuinstallation`, `wt/upstream-update`, `wt/ereignis-profil`; `wt/kanidm-deb`, `wt/fs-server`, `wt/fs-server-bestand`, `wt/fs-release-apt`, `wt/fs-packages` (lokal, kein Remote).

### Pläne und Berichte in `/srv/FreeSynergy/.scratch` (ein Satz je Datei)
- `plan-crate-familien.md` — Aufteilung fs-components in 21 Familien-Crates, Tabelle als Kernfamilie, Reihenfolge, Fragen.
- `plan-theme-bruecke.md` — DTCG-Tokens → blinc_theme, Theme-Vertrag, Test zwei-stile, Entwurf Nachtrag ADR 0074.
- `plan-rich-editing.md` — Rich-Text-Plan mit Entscheidungen F1–F8 (Spike Blinc rich_text_editor).
- `plan-umzug-wiki-nach-text.md` — Schritte ADR 0080 (fs-wiki → fs-text).
- `plan-pilot-wiki-online.md`, `skizze-website-aus-fs-text.md`, `entscheidungen-website.md` — Wiki/Website online aus fs-text.
- `plan-dossiers-welle1.md` — Dossier-Aufträge Welle 1 + ADR-0085-Bugfix-Einträge.
- `plan-ereignis-verkettung.md` — CI-Ereignis-Verkettung (ADR 0081).
- `plan-server-pakete.md`, `plan-repos-signatur.md` — apt/dnf-Repos und Signatur.
- `papier-server-arten-und-wege.md`, `entscheidung-fs-server.md`, `entscheidung-kanidm-katalog.md`, `vergleich-dateisysteme.md`, `bestand-server-repos.md`, `befund-server-repos.md` — Server-Entscheidungen und Bestand.
- `zentinel-befund.md`, `zentinel-hetzner-dns.md`, `zentinel-static.md` — Zentinel-Test, Hetzner-DNS-Problem, statische Seiten.
- `blinc-bausteine.md` — Bestandsaufnahme aller Blinc-Bausteine/Repos, Lücken, Writer-Eignung.
- `bestand-gemalte-nachbildungen.md` — 32 gemalte Nachbildungen → echte Blinc-Widgets.
- `bestand-zeiten-personen.md` — freie Namen/lokale Zeiten im Bestand (ADR 0085).
- `entscheidungen-nutzerplan-montag.md` — P1–P5 Montag-Plan.
- `straenge-vollgas.md` — Strängeplan für die Abo-Woche (Entwurf, zu aktualisieren).
- `release-flow.md`, `release-profile-uebersicht.md` — Release-Kette und Profile.
- `review-*.md` — Opus-Reviews je Lauf (Beleg, nicht ändern); `q*-*.md`, `r*-*.md`, `sprint*.md` — ältere Läufe/Briefings.
- `api-kosten.md`, `abo-tokens.md`, `cleanup-protokoll.md`, `abgebrochene-laeufe.md` — Kosten-, Spar- und Aufräum-Protokolle.
- `api-runner/followups-wiki-0011.md` — Folgeaufträge Wiki/fs-components (0.0.13/0.0.20, Rich-Editing-Entscheidungen).
- `github-support-entwurf.md` — Entwurf, NIE senden.
