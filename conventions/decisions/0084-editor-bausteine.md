# 0084 – Editor-Bausteine: ein Vertrag, mehrere Umsetzungen

Status: **akzeptiert** (Strategie, 2026-11-14; Nutzerentscheidung: mehrere Editor-Bausteine, Daten nur über unser Modell) · baut auf ADR 0031 und 0034 (Textmodell, Regal), 0057 (übersetzbare Texte), 0066 (Frontends ohne eigene Daten), 0072 (Blöcke), 0073 (Kollaboration, Loro), 0074 (Bausteine, feste Namen, Stil als Schicht), 0080 (`fs-text-model`)

## Kontext
- Heute hat jedes Frontend **seinen eigenen** Editor: das Notion-Frontend bearbeitet Blöcke, das Confluence-Frontend rohes Markdown. Die Bearbeitung steckt im jeweiligen Frontend, nicht in einem Baustein.
- Nutzertest (2026-11-14): Die Mängel liegen in der Bearbeitung, nicht im Modell. Je Frontend fehlt, was das Vorbild kann (Notion: Blocktypen per „/“; Confluence: Format-Symbolleiste statt rohem Markdown). Zugleich verhält sich Markdown beim Speichern nicht immer byte-gleich zur Eingabe (Tabellenausrichtung, Aufgabenlisten, Durchgestrichen, Kursiv).
- ADR 0074 verlangt Bausteine mit festem Namen und Stil als eigene Schicht; ADR 0066: Frontends haben keine eigenen Daten. Ein Editor ist also ein Baustein in `fs-components`, kein Teil eines Frontends.

## Entscheidung
1. **Ein Vertrag, Muster Strategy.** `fs-components` enthält mehrere Editor-Bausteine hinter dem Trait `TextEditor`. **Eingabe:** ein Dokument im Textmodell (`fs-text-model`, Blöcke nach 0072). **Ausgabe:** **nur Änderungs-Operationen** desselben Modells (z. B. Block einfügen, Text ersetzen, Marke setzen). Ein Editor ändert Daten **ausschließlich** über diese Operationen und formatiert nie eigenmächtig um.
2. **Umsetzungen** (feste Namen, 0074):
   - `BlockEditor` (Notion-Art): Enter = neuer Block, „/“-Menü mit den Blocktypen.
   - `RichTextEditor` (WYSIWYG, Confluence-Art): Format-Symbolleiste, Inline-Marken.
   - `SourceEditor` (Classic, heutiger Stand): reiner Text (Markdown, Code, Konfiguration); siehe Nachtrag.
3. **Frontends wählen** den Baustein; mehrere Frontends dürfen denselben nutzen, ein Frontend darf wechseln lassen. Die Wahl ändert keine Daten.
4. **Stil bleibt eigene Schicht** (0074): jeder Editor hat feste Baustein-Namen mit benannten Teilen und Zuständen (z. B. `block-editor` mit `block`, `slash-menu`; `rich-text-editor` mit `toolbar`, `mark-button`); Farben, Abstände, Bewegung kommen aus dem Stil, nicht aus dem Editor.
5. **Eine gemeinsame Konformitäts-Testsammlung** für alle Editoren. Jede Umsetzung muss sie bestehen:
   - **Round-trip byte-gleich** (laden, unverändert speichern = gleiche Bytes) mit der Nutzer-Fixture aus dem Test vom 14.11.
   - **GFM-Kern:** Tabellenausrichtung, Aufgabenlisten, Durchgestrichen, Kursiv.
   - **Erweiterungen über GFM hinaus** (z. B. Aufgaben-Kontrollkästchen in Tabellenzellen) sind **unsere Erweiterung**, werden im CHANGELOG als solche gekennzeichnet und liegen in einer **getrennten** Gruppe der Sammlung, damit der GFM-Kern rein bleibt.
6. **Kollaboration (0073).** Die Operationen sind die Schnittstelle zum Änderungsstrom (Loro, hinter `CollabDoc`). Dieser ADR legt sie dafür fest, **führt die Anbindung aber nicht aus**: **[offen]**.

## Folgen
- **Crate-Zuschnitt:** Vertrag und Operationstypen kommen in einen kleinen Crate (Vorschlag `fs-components-editor`), den `fs-components` und die Programme nutzen. So hängt der Vertrag nicht von `fs-text-model` ab und umgekehrt (0080: `fs-components` behält die Bausteine, sonst Zyklus). Die **Abbildung** der Operationen auf das Modell liegt im Programm (`fs-text`), nicht im Baustein.
- Die Editor-Logik wandert aus den Frontends in `fs-components`; die Frontends behalten nur die Wahl.
- Die Konformitätssammlung ist ein eigener Testbestand, den jede neue Umsetzung ohne Änderung einbindet.
- Der Notion- und der Confluence-Editor werden zu `BlockEditor` und `RichTextEditor`; `SourceEditor` ist der Rückfall und die Messlatte für Round-trip.

## Alternativen
| Option | Bewertung |
|---|---|
| Ein Editor für alle Frontends | Verworfen (Nutzer): kein Vorbild wird getroffen; Notion-Art und Confluence-Art verlangen verschiedene Bedienung. |
| Editor greift direkt aufs Dokument | Verworfen: Umformatieren beim Speichern, keine Anbindung an den Änderungsstrom (0073), nicht austauschbar. |

## Offen
- Format der Operationen **[nicht belegt]** (eigene Typen oder Anlehnung an das Loro-Modell).
- Gehören Cursor und Auswahl zum Vertrag? **[nicht belegt]**
- Wer macht Rückgängig (Editor, Modell oder Änderungsstrom)? **[nicht belegt]**
- Eingabemethoden (IME, Komposition) je Umsetzung **[nicht belegt]**.
- Anbindung der Operationen an den Änderungsstrom (Entscheidung 6) **[offen]**.
- Operationen tragen die Block-Ids aus ADR 0072, damit Übersetzung (sourceRev) und Kollaboration (0073) dieselben Ids sehen.

## Nachtrag 2026-11-14 (akzeptiert, Strategie, 2026-11-14; Nutzerentscheidung): Baustein ≠ Programm, drei Bausteine, Module
1. **Editor-Baustein ≠ Editor-Programm.** Der **Baustein** (`fs-components`) kann nur bearbeiten: Modell rein, Operationen raus. Das **Programm** (z. B. die Editor-Facette von `fs-text`) öffnet und speichert und wählt Frontend und Baustein.
2. **Drei grundverschiedene Bausteine:** `SourceEditor` (ersetzt den Namen `MarkdownEditor`: reiner Text, Markdown, Code, Konfiguration), `BlockEditor`, `RichTextEditor` (WYSIWYG). Der Name `MarkdownEditor` entfällt.
3. **Jeder Baustein ist durch Module erweiterbar**; die Erweiterungspunkte sind Traits je Baustein:
   - `SourceEditor`: Sprachmodule für Hervorhebung (Grammatik-Standard tree-sitter oder TextMate); Fehlersuche, Formatierung und Vervollständigung über LSP (Language Server Protocol). Markdown ist **ein** Sprachmodul, die Vorschau ein Modul.
   - `BlockEditor`: Blocktypen und Einträge des „/“-Menüs als Module, auch von anderen Programmen über den Hub (ADR 0019, 0068).
   - `RichTextEditor`: Marken und Knöpfe der Leiste als Module.
   - Module sind Hot-Plugins (ADR 0045): geprüft und atomar tauschbar. Katalogart `module`: siehe ADR 0077, Nachtrag 2026-11-14.
4. **Lizenzbelege** (per `gh api`, lesend, 2026-11-14):
   - tree-sitter (`tree-sitter/tree-sitter`): Lizenz **MIT** (GitHub-Lizenzerkennung der Datei `LICENSE`). Grammatiken sind eigene Repos mit **eigener Lizenz**: je Grammatik prüfen, nicht pauschal annehmen.
   - LSP (`microsoft/language-server-protocol`): Datei `License.txt` ist der Text „Attribution 4.0 International“ (**CC-BY-4.0**, GitHub-Erkennung `CC-BY-4.0`). Ob dieselbe Lizenz für alle Dateien des Repos gilt (z. B. Beispielcode), ist **[nicht belegt]**.
   - TextMate-Grammatiken: Format und Lizenzlage der Spezifikation **[nicht belegt]** (nicht gefunden; das Editor-Repo `textmate/textmate` steht unter GPL-3.0, das sagt nichts über das Grammatik-Format). Bis zum Beleg gilt tree-sitter als Vorzugsweg.
5. **Nutzer-JA 2026-11-14** zur Katalogart `module` (ADR 0077). Darstellung der Module im Store: **offen** (später mit dem Nutzer).

## Nachtrag 2026-11-14 (akzeptiert, Strategie, 2026-11-14; Nutzerentscheidung): Editor-Wahl ist Ansicht, Umwandeln je Block
1. **Editor-Wahl ist eine Ansicht, kein Frontend.** `SourceEditor` (Markdown, Code, HTML), `BlockEditor`, `RichTextEditor` und später eine Writer-Seitenansicht (ODF) sind als **Ansicht** wählbar, im Ansicht-Menü wie Kacheln, Details und Liste (ADR 0061, 0076: eine Ansicht ist kein eigenes Programm). Sie sind **nicht** ein Frontend (Begriff „Frontend“ bleibt dem Programm-Gesicht nach ADR 0066 vorbehalten). Die Wahl gilt **je Dokument** und ist umschaltbar. Das ersetzt die Formulierung in Entscheidung 3 („Frontends wählen den Baustein“): das Frontend bietet das Ansicht-Menü an, die Ansicht bestimmt den Baustein.
2. **Der Speicher bleibt unser Modell** (Blöcke, ADR 0072; Textmodell ADR 0034). Keine Ansicht besitzt ein eigenes Dateiformat; Umschalten ändert keine Daten, nur die Darstellung und die Bedienung.
3. **Umwandeln je Dokument oder je Block.** Ein Dokument oder ein einzelner Block kann über die **Exporter** in HTML, Markdown, ODF u. a. gewandelt werden (z. B. Block → HTML, Block → Markdown). Markdown bleibt **nur Export/Import** (ADR 0034), nie Speicherformat. Ein Dokument kann **gleichzeitig mehrere Ausgaben** haben (z. B. ODF-Buch und HTML aus denselben Blöcken); alle sind Sichten auf dieselbe Quelle.
4. **Was beim Umschalten erhalten bleibt.**
   - Alles im Modell bleibt erhalten, unabhängig von der Ansicht. Eine Ansicht, die etwas nicht bearbeiten kann, zeigt es als „hier nicht bearbeitbar“ und **lässt es unverändert** (Regel aus `plan-rich-editing.md`, Abschnitt 4.2).
   - **Marken über Markdown hinaus** (Unterstrichen, Farbe, Hoch-/Tiefgestellt): beim Export nach Markdown gilt die **Inline-HTML-Regel** (z. B. `<u>…</u>`) aus dem Rich-Editing-Plan. Ob diese Regel gilt, ist dort Frage F4 und noch nicht entschieden: **[offen]** (Alternativen: weglassen oder Layer-Marken ohne Dateispur).
5. **Verlustwarnung.** Kann ein Ziel (Ansicht oder Exportformat) etwas **nicht darstellen oder nicht ausdrücken**, warnt die Oberfläche **vorher** und nennt, was betroffen ist (Block-Id, Art). Die Umwandlung läuft nie stillschweigend verlustbehaftet; die Quelle im Modell bleibt in jedem Fall unverändert.
6. **Zustand.** **Vorschlag:** Die Ansichtswahl ist **Nutzereinstellung** (je Nutzer und Dokument), **nicht Dokumentinhalt**: sie wird nicht mit dem Dokument versioniert und nicht über den Änderungsstrom (ADR 0073) geteilt. Ausgaben (Entscheidung 3) dagegen gehören zum Dokument. **[offen]**: Ablageort der Einstellung, Standardansicht je Dokumenttyp.

### Folgen
- Das Ansicht-Menü braucht je Baustein die gemeldeten **Fähigkeiten** (welche Blocktypen und Marken er bearbeiten kann), damit die Verlustwarnung ohne Ausprobieren auskommt.
- Die Konformitätssammlung (Entscheidung 5) erhält eine Gruppe „Umschalten“: Ansicht A → B → A ändert das Modell byte-gleich.
- Exporter sind je Zielformat austauschbare Bausteine; die Writer-Seitenansicht (ODF) kommt später und folgt demselben Vertrag.
