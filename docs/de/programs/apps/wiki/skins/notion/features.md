# Notion - Funktionen

## Übersicht

Notion verwendet einen **Block-basierten visuellen Editor**, der auf modernen Web-Standards basiert. Der Editor ist extrem benutzerfreundlich und ermöglicht eine hohe Flexibilität bei der Gestaltung von Inhalten.

## Verfügbare Editoren

### 1. Visueller Editor (WYSIWYG)

#### Funktionen:
- **Formatierung**: Überschriften (H1-H6), fett, kursiv, unterstreichen, durchstreichen
- **Listen**: Nummerierte Listen, Aufzählungslisten, Aufgabenlisten (checkboxes)
- **Tabellen**: Tabellen erstellen/bearbeiten (Spalten/Zeilen hinzufügen/löschen)
- **Medien**: Bilder, Dateien einfügen (Drag & Drop)
- **Links**: Externe und interne Links hinzufügen
- **Ausrichtung**: Textausrichtung (links, zentriert, rechts, blockbündig)
- **Hinweise/Boxen**: Info-, Warn-, Erfolgshinweise (callouts)
- **Code-Blöcke**: Syntax-Hervorhebung für viele Programmiersprachen
- **Mathe-Formeln**: LaTeX-Unterstützung (`$...$` oder `$$...$$`)
- **Diagramme**: Mermaid-Diagramme (mit Erweiterung)
- **Embeds**: YouTube, Twitter, GitHub, Google Maps, etc.
- **Datenbanken**: Datenbank-Blöcke mit Tabellen, Kanban-Boards, Kalender
- **Vorschau-Links**: URLs einfügen erstellt automatisch Karteikarte

#### Was der Editor NICHT kann:
- Keine direkte HTML-Bearbeitung
- Keine Markdown-Syntax im Editor (wird automatisch konvertiert)
- Keine komplexen Tabellen-Formeln
- Keine vertikale Textausrichtung
- Keine Textumbrüche mit manuellem Zeilenumbruch zwischen allen Sätzen

---

## Block-basierte Architektur

Notion verwendet einen **Block-Editor**, bei dem jede Textzeile, Liste, Tabelle, etc. ein eigener "Block" ist.

### Typische Blöcke:
1. **Text-Block**: Normaler Text mit Formatierung
2. **Überschrift**: H1-H6 mit automatischer Gliederung
3. **To-Do-Liste**: `-[ ] Aufgabe` für Aufgaben
4. **Aufzählung**: `* Punkt` für Listen
5. **Nummerierte Liste**: `1. Punkt` für nummerierte Listen
6. **Zitat**: `> Text` für Zitate
7. **Callout**: Hervorgehobener Hinweis (Info, Warnung, etc.)
8. **Code-Block**: ``` für Code mit Syntax-Highlighting
9. **Tabelle**: Tabellen-Block für Daten
10. **Bild**: Bild-Block mit Optionen (Größe, Ausrichtung)
11. **Embed**: Embed-Block für externen Content
12. **Database**: Datenbank-Block (Tabelle, Kanban, Kalender)
13. **Toggle**: Aufklappbarer Block
14. **Bookmark**: Link-Karteikarte
15. **PDF/Datei**: Datei-Embed

### Navigation im Block-Editor:
- `Enter`: Neue Zeile/Block erstellen
- `Tab`: Einrücken (Listen, Block-Ebene)
- `Shift+Tab`: Herausragen (Listen, Block-Ebene)
- `Escape`: Block fokussieren verlassen
- `Cmd/Ctrl+Enter`: Checkbox abhaken
- `Cmd/Ctrl+M`: Menü öffnen

---

## Code-Block-Unterstützung

Notion unterstützt Syntax-Highlighting für viele Sprachen:

```javascript
// JavaScript
function hello() {
  console.log("Hello World");
}
```

```python
// Python
def hello():
    print("Hello World")
```

```sql
// SQL
SELECT * FROM users WHERE active = true;
```

```go
// Go
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

Unterstützte Sprachen:
- JavaScript, TypeScript, JSX, TSX
- Python, Java, C#, C++, C, Go, Rust
- HTML, CSS, SCSS, LESS
- SQL, JSON, YAML, YAML, TOML
- Bash, PowerShell, PHP, Ruby, Swift
- Kotlin, Scala, Dart, Lua, R
- MATLAB, Fortran, COBOL, VHDL
- Markdown, ReStructuredText
- Assembly, Verilog, SystemVerilog

---

## Tabellen-Features

Notion-Tabellen sind besonders flexibel:

### Funktionen:
- **Spalten/Zeilen**: Hinzufügen und Löschen
- **Formatierung**: Text, Nummern, Checkboxen, Datumsfelder, Selects, Multi-selects
- **Formeln**: `prop("Spalte")` für Berechnungen
- **Relationen**: Verknüpfung zu anderen Datenbanken
- **Rollup**: Aggregationen (SUM, COUNT, AVERAGE, etc.)
- **Filtern**: Spalten filtern (in der Datenbank)
- **Sortieren**: Spalten sortieren
- **Ansichten**: Ansichten bearbeiten (Tabelle, Kanban, Kalender, Liste)

### Datenbank-Typen:
- **Tabelle**:klassische Tabellenansicht
- **Kalender**: Daten in Kalender-Ansicht
- **Liste**: Listen-Ansicht mit Vorschaubildern
- **Kanban**: Karteikarten in Spalten
- **Galerie**: Bilder-Galerie

---

## Callout-Blöcke (Hinweise)

### Funktion:
Hervorgehobene Hinweise mit Icon und Text.

### Syntax:
`/callout` → Typ auswählen (Info, Warning, Success, Question, etc.)

### Beispiel:
> ℹ️ **Information**: Dies ist eine Info-Box

---

## Datenbanken

### Funktionen:
- **Spaltentypen**:
  - Text & Description
  - Number (Formeln möglich)
  - Select (einzelne Auswahl)
  - Multi-select (mehrere Auswahlen)
  - Date (Datum mit Uhrzeit)
  - Checkbox (Wahr/Falsch)
  - People (Mitglieder verknüpfen)
  - Files & Media (Dateien verknüpfen)
  - URL, Email, Phone
  - Relation (zu anderen Datenbanken)
  - Formula (Berechnungen)
  - Rollup (Aggregationen)

- **Ansichten**:
  - Tabellen-Ansicht
  - Kanban-Ansicht
  - Kalender-Ansicht
  - Liste-Ansicht
  - Galerie-Ansicht

---

## Formeln

### Syntax:
`prop("Spaltenname")` für Spaltenreferenz

### Beispiele:
```
prop("Preis") * prop("Menge")
dateBetween(prop("Ende"), prop("Start"), "days")
concat(prop("Vorname"), " ", prop("Nachname"))
```

### Funktionen:
- `concat()`: Text verknüpfen
- `dateBetween()`: Differenz zwischen Datums
- `format()`: Formatieren
- `if()`: Bedingung
- `dateAdd()`: Datum addieren
- `prop()`: Spaltenwert abrufen

---

## Embed-Unterstützung

Notion unterstützt Embeds von vielen Services:

- **Video**: YouTube, Vimeo, Loom, Streamable
- **Audio**: Spotify, SoundCloud
- **Code**: GitHub Gist, CodePen, JSFiddle, Replit
- **Design**: Figma, Sketch, Adobe XD
- **Social**: Twitter, LinkedIn, Instagram, TikTok
- **Dokumente**: Google Docs, Notion, Slides
- **Maps**: Google Maps, OpenStreetMap
- **Andere**: PDF, Webseiten (via Bookmark)

---

## Template-System

### Funktionen:
- **Template-Selection**: Vorlagen beim Erstellen auswählen
- **Benutzerdefinierte Vorlagen**: Eigene Vorlagen erstellen
- **Template-Kategorie**: Organisation nach Typ
- **Template-Teilen**: Vorlagen mit dem Team teilen

### Beispielen-Vorlagen:
- Meeting-Protokoll
- Projekt-Planung
- Produkt-Release-Notes
- Team-Onboarding
- Bug-Report
- Content-Kalender
- Personal-Datenbank
- Budget-Planung

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für eine vollständige Liste aller Tastatur-Shortcuts.

---

## Vergleich mit anderen Editoren

| Funktion | Notion | Tango.io | Confluence | XWiki |
|----------|--------|----------|------------|-------|
| Block-basiert | ✅ Ja | ✅ Ja | ❌ Nein | ❌ Nein |
| Code-Highlighting | ✅ Ja (40+ Sprachen) | ✅ Ja (20+ Sprachen) | ❌ Nein | ✅ Ja |
| Datenbanken | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Ja |
| Vorlagen | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Ja |
| Formeln | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Ja |
| Embeds | ✅ Ja (100+ Services) | ✅ Ja (100+ Services) | ✅ Ja | ✅ Ja |
| Markdown | ❌ Nein | ❌ Nein | ❌ Nein | ✅ Ja |
| Visuelles Feedback | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Ja |

---

## Empfehlung

- **Für Team-Zusammenarbeit**: Notion (hervorragende Datenbanken und Block-Struktur)
- **Für schnelles Schreiben**: Block-basierte Navigation
- **Für technische Dokumentation**: Code-Block mit Syntax-Highlighting
- **Für Daten-basierte Projekte**: Datenbanken mit Relationen und Formeln
- ** Für visuelle Organisation**: Embeds, Bilder, und flexible Layouts
