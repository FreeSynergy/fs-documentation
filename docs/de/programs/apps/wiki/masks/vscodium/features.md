# VSCodium - Funktionen

## Übersicht

VSCodium ist ein vollwertiger Quellcode-Editor mit umfangreichen Funktionen für Entwickler. Der Editor ist extrem anpassbar und erweiterbar über Erweiterungen.

## Verfügbare Editoren

### 1. Code-Editor (Standard)

#### Funktionen:
- **Syntax-Highlighting**: Unterstützt 100+ Programmiersprachen
- **Autovervollständigung**: IntelliSense (Vervollständigung, Parameter-Hints)
- **Code-Formatierung**: Auto-Formatierung (Prettier, ESLint, etc.)
- **Refactoring**: Umbenennen, Extract Method, etc.
- **Code-Navigation**: Definition springen, Referenzen anzeigen
- **Debugging**: Integrierter Debugger (Chrome, Node.js, Python, etc.)
- **Git-Integration**: Automatische Erkennung, Commit, Push, Pull
- **Multi-Cursor**: Mehrere Cursor gleichzeitig
- **Schnelles Bearbeiten**: Snippets, Tab-Completion
- **Vorschau**: Live-Vorschau bei Markdown, HTML, etc.

#### Was der Editor NICHT kann:
- Kein WYSIWYG für HTML/CSS (nur Syntax-Highlighting)
- Kein visueller Layout-Editor für Webseiten
- Keine direkte Datenbank-Verwaltung (nur über Erweiterungen)

---

## Syntax-Highlighting

VSCodium unterstützt Syntax-Highlighting für viele Sprachen:

### Unterstützte Sprachen (standardmäßig):
- JavaScript, TypeScript, JSX, TSX
- Python, Java, C#, C++, C, Go, Rust
- HTML, CSS, SCSS, LESS, SASS
- SQL, JSON, YAML, TOML, XML
- Bash, PowerShell, PHP, Ruby, Swift
- Kotlin, Scala, Dart, Lua, R
- Markdown, ReStructuredText
- Assembly, VHDL, Verilog
- Und viele mehr (100+ Sprachen)

### Beispiel:
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

---

## IntelliSense (Autovervollständigung)

### Funktionen:
- **Variablen-Vervollständigung**: Automatische Vervollständigung
- **Funktions-Vervollständigung**: Parameter-Hints anzeigen
- **Import-Vorschläge**: Automatische Import-Vorschläge
- **Type-Checking**: Typeninformationen anzeigen
- **Snippet-Vervollständigung**: Vorlagen-Vervollständigung

### Beispiel:
Typen Sie `fun` → Vorschlag für `function`

---

## Snippets (Code-Vorlagen)

### Funktionen:
- **Vordefinierte Snippets**: Für viele Sprachen
- **Benutzerdefinierte Snippets**: Eigene Vorlagen erstellen
- **Tab-Completion**: Mit Tab-Taste ausführen

### Beispiel-Snippets:
- `fori`: `for (let i = 0; i < array.length; i++) { ... }`
- `forEach`: `array.forEach(item => { ... })`
- `if`: `if (condition) { ... }`
- `console`: `console.log()`
- `imp`: `import ... from ...`

---

## Git-Integration

### Funktionen:
- **Automatische Erkennung**: Git-Repository automatisch erkennen
- **Status-Anzeige**: Datei-Änderungen markieren
- **Diff-Ansicht**: Änderungen im Kontext anzeigen
- **Commit**: Änderungen committen
- **Push/Pull**: Mit Remote-Repository synchronisieren
- **Branches**: Branches erstellen/wechseln
- **Konflikte**: Konflikte visuell beheben

### Git-Befehle:
- `Cmd/Ctrl+Shift+G`: Git-Panel öffnen
- `Cmd/Ctrl+Shift+J`: Suchfenster öffnen
- `Cmd/Ctrl+Shift+E`: Explorer öffnen

---

## Debugging

### Funktionen:
- **Haltepunkte**: Zeilen Haltepunkte setzen
- **Stack-Trace**: Aufrufstack anzeigen
- **Variablen**: Variablenwerte anzeigen
- **Ausdrucksüberwachung**: Ausdrücke überwachen
- **Schrittweise**: Step into, over, out
- **Konfiguration**: launch.json für Debugging-Konfiguration

### Debugging-Unterstützung:
- Node.js
- Python
- C#
- C++
- Go
- PHP
- Ruby
- Java
- Und viele mehr (via Erweiterungen)

---

## Terminal

### Funktionen:
- **Integriertes Terminal**: Bash, zsh, PowerShell, etc.
- **Mehrere Terminals**: Terminal teilen
- **Befehle**: Alle Befehle ausführen
- **Verlauf**: Befehlsverlauf
- **Filter**: Befehle filtern

### Terminal-Befehle:
- `Cmd/Ctrl+``: Terminal öffnen/schließen
- `Cmd/Ctrl+Shift+``: Neues Terminal

---

## Erweiterungen (Plugins)

### Funktionen:
- **Syntax-Highlighting**: Für weitere Sprachen
- **Linting**: Code-Qualität (ESLint, Pylint, etc.)
- **Debugging**: Für weitere Sprachen
- **Themes**: Farbschemata ändern
- **Snippets**: Für spezifische Frameworks
- **Git**: Erweiterte Git-Funktionen
- **Docker**: Docker-Integration
- **Database**: Datenbank-Verwaltung
- **API**: API-Test-Client (REST, GraphQL)

### Beliebte Erweiterungen:
- **Prettier**: Code-Formatierung
- **ESLint**: JavaScript-Linting
- **Python**: Python-Unterstützung
- **GitLens**: Erweiterte Git-Informationen
- **Markdown Preview**: Markdown-Vorschau
- **Docker**: Docker-Integration
- **PostgreSQL**: PostgreSQL-Verwaltung
- **REST Client**: API-Testen

---

## Anpassung

### Einstellungen:
- **Benutzer-Einstellungen**: Globale Einstellungen
- **Workspace-Einstellungen**: Projekt-spezifische Einstellungen
- **Einstellungs-Editor**: Visueller Einstellungs-Editor
- **settings.json**: JSON-basierte Einstellungen

### Beispiel-Settings:
```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "files.autoSave": "onFocusChange",
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für eine vollständige Liste aller Tastatur-Shortcuts.

---

## Vergleich mit anderen Editoren

| Funktion | VSCodium | Notion | Tango.io | Confluence |
|----------|----------|--------|----------|------------|
| Quellcode-Editor | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| Syntax-Highlighting | ✅ Ja (100+ Sprachen) | ✅ Ja (40+ Sprachen) | ✅ Ja (20+ Sprachen) | ✅ Ja (mit Erweiterung) |
| IntelliSense | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| Git-Integration | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| Debugging | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |
| Erweiterungen | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Ja |
| Snippets | ✅ Ja | ✅ Ja | ❌ Nein | ❌ Nein |
| Terminal | ✅ Ja | ❌ Nein | ❌ Nein | ❌ Nein |

---

## Empfehlung

- **Für Entwickler**: VSCodium (ausgereifte Entwicklungsumgebung)
- **Für schnelles Schreiben**: IntelliSense und Snippets
- **Für technische Dokumentation**: Code-Block mit Syntax-Highlighting
- ** Für Git-Nutzer**: Integrierte Git-Integration
- ** Für Debugging**: Integrierter Debugger mit mehreren Sprachen

---

## VSCodium vs. VS Code

VSCodium ist identisch mit VS Code, aber:
- **Open-Source**: Vollständig quelloffen
- **Kein Telemetry**: Kein Daten-Senden an Microsoft
- **Kein MS-EULA**: Andere Lizenz
- **Gleiche Erweiterungen**: VS Code-Erweiterungen sind kompatibel
