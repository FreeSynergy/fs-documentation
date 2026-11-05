# 0023 – Darstellungs-Register; zwei Editor-Workbenches

Status: akzeptiert (2026-11-05) · Protokoll §11, §21.6 · ADR 0004, 0005

## Entscheidung
1. **Components speichern standardisiert** — primitives, widgets und workbenches lesen und
   schreiben Datenstandards (ADR 0014), nichts Eigenes.
2. **Darstellungs-Register:** Paare *Datentyp → Darstellung*, in beide Richtungen abfragbar.
   Jedes Element sagt, welche Daten es darstellen/bearbeiten kann; jeder Datentyp sagt, wie er
   dargestellt werden kann. Beispiele:
   - Kontakt (JSContact) → Karte, Listeneintrag, Text
   - Koordinate → Karte, Text (Dezimalgrad, Grad/Min/Sek, `geo:`-URI RFC 5870, …)
   - Liste/Aufzählung → Dropdown, Checkbox-Gruppe, Tags, Kanban
3. **Kanban ist Workbench** (Karten zeigen beliebige Objekte, erst zur Laufzeit bekannt). Es hat
   kein Menü; in einer App wird es größer und bekommt das Menü-Widget davor (ADR 0005).
4. **Zwei Text-Workbenches:**
   - **Code-Editor** — Textdateien (`.md`, `.js`, `.toml`, …), mit vorhandenen Formattern/Parsern;
     jeder Text kann so auch formatiert werden.
   - **Block-Editor** — strukturierte Dokumente als Blockbaum (wie Notion), jeder Block ein Datentyp.
   Die Frage ist nicht *wie* gespeichert wird, sondern **wann welche Workbench**: Datei mit
   Format → Code-Editor; strukturiertes Dokument → Block-Editor.
5. **Ziel:** Eine App entsteht aus *Datenstandard + Elementen + Aufbau*; ein Frontend klickt nur
   noch das Aussehen zusammen.

## Folgen
- Register-Format und Ort festlegen (`data/` oder `components/`); Abgleich mit Blinc.
- `components/workbenches/` bekommt `block-editor`; `code-editor` und `rich-text-editor` prüfen
  (rich-text = Block-Editor?).
