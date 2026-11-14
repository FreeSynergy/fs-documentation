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
   - `MarkdownEditor` (Classic, heutiger Stand): rohes Markdown.
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
- Der Notion- und der Confluence-Editor werden zu `BlockEditor` und `RichTextEditor`; `MarkdownEditor` ist der Rückfall und die Messlatte für Round-trip.

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
