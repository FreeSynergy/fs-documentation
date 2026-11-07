# Notion — Funktionen (2026-11-07)

## Kann (geprüft)

| Bereich | Funktion | Quelle |
|---------|----------|--------|
| Blöcke | Typisierte Blöcke: Absatz, Überschrift 1–4, Aufzählungs- und nummerierter Listeneintrag, To-do, Umschalter, Zitat, Hinweisbox, Code, Tabelle, Tabellenzeile, Bild, Video, Audio, Datei, PDF, Einbettung, Lesezeichen, Gleichung, Trennlinie, Spaltenliste, Spalte, Inhaltsverzeichnis, synchronisierter Block, Unterseite, Unterdatenbank, Linkvorschau | [S9] (Aufzählung der Blocktypen; `code`, `tab`, `audio`, `meeting_notes` sind in der Referenz, fehlen aber in der Aufzählung) |
| Bearbeitung | Markdown-Präfixe erzeugen beim Tippen Blöcke (`# `, `- `, `[] `, `1. `, `> `, `" `, `---`) | [S11] |
| Bearbeitung | Mit Tab und Shift+Tab einrücken und ausrücken; Blöcke per Tastatur auswählen, verschieben, duplizieren und löschen | [S11] |
| Bearbeitung | Schrägstrich-Befehle, zum Beispiel `/h1`, `/todo`, `/toggle`, `/quote`, `/code`, `/embed`, `/image`, `/pdf`, `/video`, `/audio`, `/file`, `/equation`, `/toc`, `/template`, `/turn`, `/color` | [S11] |
| Text | Fett, kursiv, unterstrichen, durchgestrichen, Code im Text, Link, Textfarbe und Hervorhebung (`/color`) | [S11] |
| Erwähnungen | `@` erwähnt eine Person, verlinkt eine Seite im Text, fügt ein Datum ein, legt eine Erinnerung an | [S11] |
| Links | `[[` oder `+` verlinkt eine Seite oder erstellt eine Unterseite | [S11] |
| Tabellen | Zellen nach rechts oder unten füllen; Tabellenzeilen sind Blöcke | [S11, S9] |
| Seiten | Unterseiten, Favoriten, Seiten per Ziehen ordnen und verschachteln | [S12] |
| Seiten | Schrift (Standard, Serifen, Mono), kleiner Text, volle Breite, Inhaltsverzeichnis, Icon, Titelbild | [S15] |
| Seiten | Verschieben, duplizieren, in den Papierkorb legen, wiederherstellen | [S14, S21] |
| Seiten | Kommentare auf Seiten (erstellen mit cmd/ctrl+shift+M) | [S11, S16] |
| Datenbanken | Ansichten: Tabelle, Liste, Board, Kalender, Galerie, Diagramm | [S13] |
| Datenbanken | Ansichten können gesperrt werden; Sperren verhindert Änderungen an Eigenschaften und Ansichten | [S13] |
| Datenbanken | Eigenschaftstypen wie Status, Mehrfachauswahl, Relation, Rollup, Formel (Namen aus dem API-Changelog) | [S8] |
| Datenbanken | Formeln verwenden Verweise der Form `prop("Name")` | [S8] (Eintrag 12. Aug.) |
| Suche | Seiten und Datenquellen durchsuchen (API `POST /v1/search`) | [S10] |
| Suche | In der App öffnen cmd/ctrl+K oder cmd/ctrl+P die Suche oder springen zu einer zuletzt genutzten Seite | [S11, S12] |
| Export | Seiten können exportiert werden; die API liefert Markdown (Markdown-Endpunkte im Notion-Stil) | [S8] (Einträge 26. Feb., 2. März und 29. Juni). Exportmenü der App nicht geprüft |
| API | Seiten erstellen, lesen, aktualisieren und in den Papierkorb legen; Blöcke lesen und aktualisieren; Kinder anhängen (maximal 100 pro Anfrage) | [S19, S20, S21, S18] |
| API | Datenquellen mit Filtern und Sortierungen abfragen | [S17] |
| API | Webhook-Ereignisse für Seiten, Datenbanken, Datenquellen und Kommentare | [S5] |

## Kann nicht (geprüft) oder wird von der API nicht unterstützt

| Grenze | Quelle |
|--------|--------|
| Kleiner Text und volle Breite nur am Desktop und im Web | [S15] |
| Die API kann keine `block_id` als übergeordnetes Element einer neuen Seite setzen; übergeordnet sind `page_id`, `database_id`, `data_source_id` oder `workspace` | [S20] |
| Eine in den Papierkorb verschobene Seite kann bis zur Wiederherstellung nicht bearbeitet werden | [S14] |
| Eine Datenbank wiederherzustellen bringt Seiten und Eigenschaften zurück, nicht aber den Text darin | [S14] |
| Ansichten und Filter: Ein Benutzer mit "Can edit content" kann Filter oder Sortierungen nicht ändern | [S13] |
| Die API kann den vollständigen Seiteninhalt im Abruf der Seite nicht liefern; Kinder der Blöcke verwenden | [S19] |
| Webhook-Nutzlasten enthalten IDs und Metadaten, nicht den vollständigen Inhalt | [S5] |
| Die Suche umfasst nur Seiten und Datenquellen; `database` ist kein gültiger Filterwert mehr | [S10, S7] |

## Nicht geprüft (entfernt oder markiert)

- "Keine Markdown-Syntax im Editor" (frühere Seite). Falsch; Markdown-Eingabe gibt es [S11].
- Hinweisbox-Typen (info, warning, success); Hinweisboxen gibt es [S11], die Typliste ist ungeprüft.
- Liste der Programmiersprachen für Codeblöcke (40+ Namen). Die Sprachliste steht auf keiner gelesenen offiziellen Seite: ungeprüft.
- Mermaid-Diagramme. Ungeprüft.
- Anzahl der Einbettungsdienste (100+). Ungeprüft.
- Details des Vorlagensystems und Beispielvorlagen. Vorlagen gibt es [S12]; Details ungeprüft.
- Mobile Apps und ihre Funktionen. Ungeprüft.
- Automatisches Speichern. Ungeprüft (keine offizielle Aussage gelesen).
- SSO, Liste der Formelfunktionen (`concat`, `dateBetween`, `if` usw.). Ungeprüft.
