# Wiki.js - Funktionen

## Übersicht

Wiki.js bietet zwei Editor-Modi: Einen visuellen WYSIWYG-Editor und einen Markdown-Editor. Der Editor ist extrem benutzerfreundlich und modular erweiterbar.

## Verfügbare Editoren

### 1. Visueller Editor (WYSIWYG)

#### Funktionen:
- **Formatierung**: Überschriften, fett, kursiv, unterstreichen, durchstreichen
- **Listen**: Nummerierte Listen, Aufzählungslisten, Aufgabenlisten
- **Textauszeichnung**: Zitate, Code-Blöcke, hervorheben
- **Tabellen**: Tabellen erstellen und bearbeiten (Spalten/Zeilen hinzufügen/löschen)
- **Medien**: Bilder einfügen, Links hinzufügen, Emojis
- **Ausrichtung**: Textausrichtung (links, zentriert, rechts, blockbündig)
- **Hinweise/Boxen**: Info-, Warn-, Erfolgshinweise
- **Code-Blöcke**: Syntax-Hervorhebung für verschiedene Programmiersprachen
- **Mathe-Formeln**: LaTeX-Unterstützung (optional)
- **Diagramme**: Mermaid-Diagramme (optional)
- **Einbetten**: Videos (YouTube, Vimeo), iframes

#### Was der Editor NICHT kann:
- Keine direkte HTML-Bearbeitung im visuellen Modus
- Keine komplexen Makros (nur über Extensions)
- Keine vertikale Textausrichtung
- Keine Textumbrüche mit manuellem Zeilenumbruch zwischen allen Sätzen

---

### 2. Markdown-Editor

#### Funktionen:
- **Vollständige Markdown-Unterstützung**: Gängige Markdown-Syntax
- **GitHub-Flavoured Markdown**: Tabellen, Task-Lists, strikes
- **Front Matter**: Metadaten für Seiten (Titel, Beschreibung, etc.)
- **Live-Vorschau**: Echtzeit-Vorschau des Ergebnisses
- **Snippets**: Vorlagen für häufige Blöcke
- **Erweiterbare Syntax**: Über Plugins (z.B. Mermaid, LaTeX)

#### Markdown-Unterstützte Formatierungen:
```markdown
# Überschrift 1
## Überschrift 2
### Überschrift 3

**fett**, *kursiv*, `code`

- Aufzählung
- Item 2
- Item 3

1. Nummeriert
2. Listen

> Zitat

| Tabelle | Spalte 1 | Spalte 2 |
|---------|----------|----------|
| Zeile 1 | Daten A  | Daten B  |
```

#### Was der Editor NICHT kann:
- Kein WYSIWYG beim Bearbeiten (man muss Markdown-Syntax kennen)
- Keine visuelle Tabellenbearbeitung
- Keine direkte Formatierung von Textfarben (nur über HTML-Inline oder Erweiterungen)

---

## Editor-Vergleich

| Funktion | WYSIWYG | Markdown |
|----------|---------|----------|
| Visuelles Bearbeiten | ✅ Ja | ❌ Nein |
| Markdown-Syntax | ❌ Nein | ✅ Ja |
| Live-Vorschau | ✅ Ja | ✅ Ja |
| Tabellen | ✅ Visuell | ✅ Syntax |
| Code-Blöcke | ✅ Mit Syntax-Highlighting | ✅ Mit Syntax-Highlighting |
| Bilder | ✅ Drag & Drop | ✅ Markdown-Syntax |
| Links | ✅ Link-Button | ✅ Markdown-Syntax |
| Tabelleneditor | ✅ Visuell | ✅ Textbasiert |
| Keine Lernkurve | ✅ Ja | ❌ Markdown müssen lernen |
| Fortgeschrittene Formatierung | ❌ Eingeschränkt | ✅ Sehr flexibel |

---

## Erweiterbare Funktionen (über Plugins)

Wiki.js ist extrem erweiterbar. Via Plugins können folgende Funktionen hinzugefügt werden:

- **Mermaid**: Diagramme (Flowcharts, Sequenzdiagramme, etc.)
- **LaTeX**: Mathematische Formeln
- **Syntax Highlighting**: Unterstützung für 200+ Programmiersprachen
- **Embeds**: Youtube, Vimeo, Spotify, Twitter, etc.
- **Emoji**: Erweiterte Emoji-Unterstützung
- **Kroki**: Diagramme über Text (PlantUML, Mermaid, etc.)
- **MathJax**: Mathematische Formeln
- **VideoJS**: Erweiterte Video-Unterstützung

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für eine vollständige Liste aller Tastatur-Shortcuts.

---

## Empfehlung

- **Für Anfänger**: WYSIWYG-Editor ( intuitiv, keine Syntax nötig)
- **Für Fortgeschrittene**: Markdown-Editor (mehr Kontrolle, schnelleres Arbeiten)
- **Für Entwickler**: Markdown mit Code-Blöcken und Syntax-Highlighting
