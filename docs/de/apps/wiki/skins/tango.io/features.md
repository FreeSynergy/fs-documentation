# Tango.io - Funktionen

## Übersicht

Tango.io nutzt einen modernen, visuellen Editor, der auf Web-Standards basiert. Der Editor ist stark an Notion angelehnt, aber mit Tango.io-spezifischen Funktionen.

## Verfügbare Editoren

### 1. Visueller Editor (WYSIWYG)

#### Funktionen:
- **Formatierung**: Überschriften (H1-H6), fett, kursiv, unterstreichen, durchstreichen
- **Listen**: Nummerierte Listen, Aufzählungslisten, Aufgabenlisten (checkboxes)
- **Tabellen**: Tabellen erstellen/bearbeiten (Spalten/Zeilen hinzufügen/löschen)
- **Medien**: Bilder einfügen, Links hinzufügen, Emojis
- **Ausrichtung**: Textausrichtung (links, zentriert, rechts)
- **Hinweise/Boxen**: Info-, Warn-, Erfolgshinweise
- **Code-Blöcke**: Syntax-Hervorhebung für mehrere Programmiersprachen
- **Embeds**: YouTube, Vimeo, Spotify, Figma, Notion, Confluence, etc.
- **Seiten-Verknüpfungen**: Verknüpfung zu anderen Tango.io-Seiten
- **Benutzer-Erwähnungen**: @Mention für Zusammenarbeit
- **Timestamps**: Automatische Datumsangaben

#### Was der Editor NICHT kann:
- Keine direkte HTML-Bearbeitung
- Keine Markdown-Syntax im Editor (wird automatisch konvertiert)
- Keine komplexen Tabellen-Formeln
- Keine vertikale Textausrichtung
- Keine Textumbrüche mit manuellem Zeilenumbruch zwischen allen Sätzen

---

## Editor-Features im Detail

### Block-basierte Bearbeitung

Tango.io verwendet einen **Block-Editor**, bei dem jede Textzeile oder Komponente ein eigener "Block" ist.

#### Typische Blöcke:
1. **Text-Block**: Normaler Text mit Formatierung
2. **Überschrift**: H1-H6 mit automatischer Gliederung
3. **To-Do-Liste**: `-[ ] Aufgabe` für Aufgaben
4. **Aufzählung**: `* Punkt` für Listen
5. **Nummerierte Liste**: `1. Punkt` für nummerierte Listen
6. **Zitat**: `>` für Zitate
7. **Code-Block**: ``` für Code mit Syntax-Highlighting
8. **Tabelle**: Tabellen-Block für Daten
9. **Bild**: Bild-Block mit Optionen
10. **Embed**: Embed-Block für externen Content
11. **Seiten-Link**: Verknüpfung zu anderen Seiten
12. **Datei**: Datei-Upload

#### Block-Navigation:
- `Enter`: Neue Zeile/Block erstellen
- `Tab`: Einrücken (Listen)
- `Shift+Tab`: Herausragen (Listen)
- `Escape`: Block verlassen
- `Cmd/Ctrl+Enter`: Block ausführen (z.B. Checkbox abhaken)

---

### Code-Block-Unterstützung

Tango.io unterstützt Syntax-Highlighting für viele Sprachen:

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

Unterstützte Sprachen:
- JavaScript, TypeScript
- Python, Java, C#, C++, Go, Rust
- HTML, CSS, SCSS
- SQL, JSON, YAML, XML
- Bash, PowerShell
- Ruby, PHP, Swift, Kotlin
- Markdown (für Code-Blöcke selbst)

---

### Table-Features

#### Funktionen:
- **Spalten/Zeilen**: Hinzufügen und Löschen
- **Formatierung**: Text, Nummern, Checkboxen
- **Filtern**: Spalten filtern (pro Workspace)
- **Sortieren**: Spalten sortieren
- **Resize**: Spaltenbreite anpassen

#### Beispiel:
| Name | Status | Priorität |
|------|--------|-----------|
| Task 1 | ✅ Erledigt | Hoch |
| Task 2 | ⏳ In Arbeit | Mittel |
| Task 3 | ❌ Offen | Niedrig |

---

### Embed-Unterstützung

Tango.io unterstützt Embeds von vielen Services:

- **Video**: YouTube, Vimeo
- **Audio**: Spotify, SoundCloud
- **Design**: Figma, Sketch, Adobe XD
- **Code**: GitHub Gist, CodePen, JSFiddle
- **Dokumente**: Google Docs, Notion, Slides
- **Maps**: Google Maps, OpenStreetMap
- **Social Media**: Twitter, LinkedIn, Instagram (Posts)

---

### Vorlagen-System

#### Funktionen:
- **Template-Selection**: Vorlagen beim Erstellen auswählen
- **Benutzerdefinierte Vorlagen**: Eigene Vorlagen erstellen
- **Template-Kategorie**: Organisation nach Typ
- **Template-Teilen**: Vorlagen mit dem Team teilen

#### Beispielen-Vorlagen:
- Meeting-Protokoll
- Projekt-Planung
- Produkt-Release-Notes
- Team-Onboarding
- Bug-Report
- Content-Kalender

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für eine vollständige Liste aller Tastatur-Shortcuts.

---

## Vergleich mit anderen Editoren

| Funktion | Tango.io | Notion | Confluence |
|----------|----------|--------|------------|
| Block-basiert | ✅ Ja | ✅ Ja | ❌ Nein |
| Code-Highlighting | ✅ Ja (20+ Sprachen) | ✅ Ja | ❌ Nein |
| Embeds | ✅ Ja (100+ Services) | ✅ Ja | ✅ Eingeschränkt |
| Tabellen | ✅ Mit Filter/Sort | ✅ Mit Filter/Sort | ✅ Basis |
| Vorlagen | ✅ Ja | ✅ Ja | ✅ Ja |
| Markdown | ❌ Nein | ✅ Ja | ❌ Nein |
| Visuelles Feedback | ✅ Ja | ✅ Ja | ✅ Ja |

---

## Empfehlung

- **Für Team-Zusammenarbeit**: Tango.io-Editor (hervorragende Embeds und Block-Struktur)
- **Für schnelles Schreiben**: Block-basierte Navigation
- **Für technische Dokumentation**: Code-Block mit Syntax-Highlighting
- **Für visuelle Organisation**: Embeds und Bilder
