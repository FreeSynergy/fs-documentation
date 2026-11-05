# 0031 – Jeder Text ist ein Wiki-Eintrag; die Bibliothek; Hilfe dort, wo man ist

Status: akzeptiert (2026-11-05) · Datenstandards dafür = offen (Phase 2, Domäne `documents`)

## Kontext
Texte stecken heute in jedem Programm getrennt: Hilfe, Anleitungen, Notizen, Doku. Interoperabilität
heißt: einmal geschrieben, überall nutzbar. Von Tango gelernt: ein Wiki ist nicht starr, es wird
dort genutzt, wo man gerade arbeitet.

## Entscheidung (Nutzer)
1. **Jeder Text ist ein Wiki-Eintrag.** Eine Sammlung von Texten ist ein Wiki.
2. **Aufbau:** Seiten → **Bücher** (wie BookStack) → **Bibliotheken**.
3. **Eine Bibliothek, die alle Programme nutzen:** Hilfetexte, Tool-Helfer, Anleitungen
   (z. B. „So verschlüsselst du deine Mails“, ADR 0018).
4. **Hilfe dort, wo man ist:** Jedes Werkzeug hat einen Punkt zum Nachfragen; er führt zum
   Wiki-Eintrag — angezeigt als Fenster/Workbench (Editor, ADR 0023), ohne die Wiki-App zu öffnen.
5. **Eigene Erklärungen:** Man kann eigene Erklärungen schreiben und Bildschirmkopien einfügen.
   Vorhandene Texte werden dabei **stumm geschaltet, nicht gelöscht**; die eigene Erklärung steht
   daneben — man kommt immer wieder an den ursprünglichen Text.
6. **Interoperabilität für alle Programme:** Wer etwas braucht, bedient sich. Einmal programmiert,
   immer wieder verwendbar.

## Warum (Nutzer, 2026-11-05)
Das Wiki ersetzt auch **mkdocs**: Unsere eigene Doku soll später in unserem Wiki laufen.
Präzisiert durch ADR 0033 (Markieren) und ADR 0034 (Absatz, Seite, Kollektion, Regal).

## Folgen / offen
- Neue Datendomäne **`documents`** (Seite, Buch, Bibliothek, Blockinhalt) — Standards recherchieren.
  Kandidaten: AS2 `Article`/`Page`, W3C **Web Annotation** für „eigene Erklärung daneben“ und
  Stummschalten, EPUB für Bücher-Export; Blockformat ist wahrscheinlich eine Lücke (eigene Spec).
- Versionskontrolle überall per **gitoxide** (Rust-Git) — Idee des Nutzers, später besprechen;
  Verhältnis zum Aktivitätsprotokoll (ADR 0020) klären.
