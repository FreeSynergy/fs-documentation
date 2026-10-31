# Confluence - Funktionen

## Übersicht

Confluence bietet zwei Haupt-Editoren an: Den **Visuellen Editor (Visual Editor)** und den **Quelltext-Editor (Wiki Markup)**. Seit Confluence Cloud ist der visuelle Editor der Standard.

## Verfügbare Editoren

### 1. Visueller Editor (Visual Editor)

#### Funktionen:
- **Formatierung**: Überschriften (H1-H6), fett, kursiv, unterstreichen, durchstreichen
- **Listen**: Nummerierte Listen, Aufzählungslisten, Aufgabenlisten
- **Tabellen**: Tabellen erstellen/bearbeiten (Spalten/Zeilen hinzufügen/löschen)
- **Medien**: Bilder, Dateien einfügen (Drag & Drop)
- **Links**: Externe und interne Links hinzufügen
- **Ausrichtung**: Textausrichtung (links, zentriert, rechts)
- **Hinweise/Boxen**: Info-, Warn-, Erfolgshinweise (callouts)
- **Code-Blöcke**: Syntax-Hervorhebung (mit Erweiterung)
- **Datenbanken**: Confluence Data Center (Tabellen, Kanban)
- **Embeds**: YouTube, Jira Issues, Confluence Pages, etc.
- **Makros**: Visuelle Makro-Einbindung
- **Vorlagen**: Vorlagen einfügen

#### Was der Editor NICHT kann:
- Keine direkte HTML-Bearbeitung im visuellen Modus
- Keine Markdown-Syntax im visuellen Editor
- Keine komplexen Wiki-Makro-Syntax im visuellen Modus
- Code-Highlighting ohne Erweiterung

---

### 2. Quelltext-Editor (Wiki Markup)

#### Funktionen:
- **Vollständige Wiki-Markup-Syntax**: Confluence-Syntax
- **Vollständige Kontrolle**: Jedes Zeichen kontrollieren
- **Makros**: `{macro}` Syntax für komplexe Elemente
- **HTML**: HTML-Unterstützung (mit Einschränkungen)
- **Links**: `[]` für interne Links
- **Bilder**: `!image.jpg!` für Bilder
- **Formatierung**: `*fett*`, `_kursiv_`, `h1. Überschrift`
- **Tabellen**: `{table}` Syntax
- **Makros-Beispiele**:
  ```confluence
  {toc}
  {note}
  This is a note
  {note}
  {code:javascript}
  console.log("Hello");
  {code}
  ```

#### Was der Editor NICHT kann:
- Kein visuelles Feedback (man sieht nur den Code)
- Confluence-Syntax muss gelernt werden
- Kein Drag & Drop für Bilder

---

## Vergleich der Editoren

| Funktion | Visueller Editor | Quelltext-Editor |
|----------|------------------|------------------|
| Visuelles Bearbeiten | ✅ Ja | ❌ Nein |
| Wiki-Makro-Syntax | ❌ (unsichtbar) | ✅ Direkt sichtbar |
| Makros | ✅ Visuell (eingeschränkt) | ✅ Vollständig |
| HTML | ❌ Nur via Makro | ✅ Ja (eingeschränkt) |
| Tabellen | ✅ Visuell | ✅ Syntax (komplex) |
| Bilder einfügen | ✅ Drag & Drop | ✅ Syntax |
| Live-Vorschau | ✅ Ja | ❌ Nein |
| Lernkurve | ✅ Niedrig | ❌ Mittel-Hoch |
| Fortgeschrittene Funktionen | ❌ Eingeschränkt | ✅ Volle Kontrolle |

---

## Confluence-Makros (Beispiele)

### Informations-Box
```confluence
{note:title=Information}
Dies ist eine Information
{note}
```

### Warnungs-Box
```confluence
{warning:title=Warnung}
Dies ist eine Warnung
{warning}
```

### Code-Block (mit Erweiterung)
```confluence
{code:javascript}
function hello() {
  console.log("Hello World");
}
{code}
```

### Tabelle
```confluence
{table}
| Kopf 1 | Kopf 2 |
| Zelle 1 | Zelle 2 |
{table}
```

### Inhalt einbetten
```confluence
{embed:http://example.com}
```

### Jira-Issue einbinden
```confluence
{jira:PROJECT-123}
```

---

## Code-Block-Unterstützung

Confluence unterstützt Syntax-Highlighting für viele Sprachen (mit Erweiterung oder neueren Versionen):

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

Unterstützte Sprachen (variiert je nach Konfiguration):
- JavaScript, TypeScript
- Python, Java, C#, C++, Go, Rust
- HTML, CSS, SCSS
- SQL, JSON, YAML, XML
- Bash, PowerShell
- Ruby, PHP, Swift, Kotlin
- Markdown, ReStructuredText
- Und viele mehr

---

## Confluence-Datenbank-Block (Confluence Data Center)

### Funktionen:
- **Tabellen-Ansicht**: Klassische Tabellen
- **Kanban-Ansicht**: Karteikarten in Spalten
- **Kalender-Ansicht**: Daten im Kalender
- **Filtern**: Spalten filtern
- **Sortieren**: Spalten sortieren

---

## Embed-Unterstützung

Confluence unterstützt Embeds von vielen Services:

- **Video**: YouTube, Vimeo
- **Dokumente**: Google Docs, Office 365
- **Code**: GitHub Gist, Bitbucket
- **Social**: Twitter
- **Daten**: Confluence Pages (interne Verknüpfung)
- **Maps**: Google Maps
- **Andere**: Jira Issues, Confluence Blogposts

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für eine vollständige Liste aller Tastatur-Shortcuts.

---

## Vergleich mit anderen Editoren

| Funktion | Confluence | Notion | Tango.io | XWiki |
|----------|------------|--------|----------|-------|
| Visueller Editor | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Ja |
| Wiki-Makro-Syntax | ✅ Ja | ❌ Nein | ❌ Nein | ✅ Ja |
| Code-Highlighting | ✅ Ja (mit Erweiterung) | ✅ Ja (40+ Sprachen) | ✅ Ja (20+ Sprachen) | ✅ Ja |
| Datenbanken | ✅ Ja (Data Center) | ✅ Ja | ❌ Nein | ✅ Ja |
| Vorlagen | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Ja |
| Embeds | ✅ Ja | ✅ Ja | ✅ Ja | ✅ Ja |
| Markdown | ❌ Nein | ✅ Ja | ❌ Nein | ✅ Ja |
| Live-Vorschau | ✅ Ja | ✅ Ja | ✅ Ja | ❌ Nein |

---

## Empfehlung

- **Für Enterprise-Umgebungen**: Confluence (Integration mit Jira, Sicherheit)
- **Für Team-Zusammenarbeit**: Confluence (hervorragende Integrationen)
- ** Für technische Dokumentation**: Code-Block mit Syntax-Highlighting
- ** Für Projekte mit Jira**: Confluence (native Integration)
- ** Für Anfänger**: Visueller Editor ( intuitiv)
