# MediaWiki - Funktionen

## Übersicht

MediaWiki bietet zwei Haupt-Editoren an: Den klassischen **Quelltext-Editor** mit Wiki-Syntax und den **Visuellen Editor (VisualEditor)**. Die Verfügbarkeit hängt von der Server-Konfiguration ab.

## Verfügbare Editoren

### 1. Visueller Editor (VisualEditor)

#### Funktionen:
- **WYSIWYG**: So wie es aussieht, so wird es bearbeitet
- **Formatierung**: Überschriften (H1-H6), fett, kursiv, unterstreichen
- **Listen**: Nummerierte Listen, Aufzählungslisten
- **Tabellen**: Tabellen erstellen/bearbeiten (Spalten/Zeilen)
- **Medien**: Bilder, Dateien einfügen
- **Links**: Externe und interne Links hinzufügen
- **Vorlagen**: Vorlagen einfügen (visuell)
- **Quellen**: Zitationen und Referenzen
- **Code-Blöcke**: Syntax-Hervorhebung (optional)
- **Mathe-Formeln**: LaTeX-Unterstützung (optional)
- **Diagramme**: Mit Erweiterungen (z.B. Graphviz)

#### Was der Editor NICHT kann:
- Keine direkte Wiki-Syntax-Bearbeitung im visuellen Modus
- Keine komplexen Vorlagen-Parameter direkt sichtbar
- Kein direktes Bearbeiten von Wikitext-Strukturen
- Eingeschränkte Unterstützung für Fortgeschrittene Funktionen

---

### 2. Quelltext-Editor (WikiText)

#### Funktionen:
- **Vollständige Wiki-Syntax**: MediaWiki-Syntax (Wikitext)
- **Vollständige Kontrolle**: Jedes Zeichen kontrollieren
- **Vorlagen**: `{{Vorlage}}` Syntax
- **Links**: `[[Seitenname]]` interne Links
- **Bilder**: `[[Datei:Bild.jpg|Thumb|Beschreibung]]`
- **Kategorien**: `[[Kategorie:Name]]`
- **Formatierung**: `'fett'`, `''kursiv''`, `===Überschrift===`
- **Listen**: `* Aufzählung`, `# Nummeriert`
- **Tabellen**: `{| ... |}` Syntax
- **HTML**: Eingeschränkte HTML-Unterstützung

#### Wiki-Syntax-Beispiele:
```wikitext
== Überschrift ==
'''Fetter Text''' und ''kursiver Text''

* Aufzählung
* Item 2

1. Nummeriert
2. Listen

[[Interne Seite]]
[[Interne Seite|Angezeigter Text]]

[[Datei:Bild.jpg|mini|Rechts|Beschreibung]]

{{Vorlage|Parameter=Wert}}
```

#### Was der Editor NICHT kann:
- Kein visuelles Feedback (man sieht nur den Code)
- Wiki-Syntax muss gelernt werden
- Kein Drag & Drop für Bilder
- Kein Echtzeit-Vorschau (außer mit speziellen Erweiterungen)

---

### 3. Quelltext bearbeiten (Alternativer Modus)

#### Funktionen:
- **Code-Editor**: Für Entwickler
- **Syntax-Highlighting**: Farbige Kennzeichnung
- **Autovervollständigung**: Optional
- **Zeilennummern**: Optional

#### Was der Editor NICHT kann:
- Kein WYSIWYG
- Kein Live-Vorschau (ohne Erweiterung)

---

## Vergleich der Editoren

| Funktion | Visueller Editor | Quelltext-Editor |
|----------|------------------|------------------|
| Visuelles Bearbeiten | ✅ Ja | ❌ Nein |
| Wiki-Syntax | ❌ (unsichtbar) | ✅ Direkt sichtbar |
| Vorlagen | ✅ Visuell (eingeschränkt) | ✅ Vollständig |
| Tabellen | ✅ Visuell | ✅ Syntax (komplex) |
| Bilder einfügen | ✅ Drag & Drop | ✅ Syntax |
| Live-Vorschau | ✅ Ja | ❌ Nein (optional) |
| Lernkurve | ✅ Niedrig | ❌ Mittel-Hoch |
| Fortgeschrittene Funktionen | ❌ Eingeschränkt | ✅ Volle Kontrolle |

---

## Empfehlung

- **Für Anfänger**: Visueller Editor ( intuitiv, keine Syntax nötig)
- **Für Fortgeschrittene**: Quelltext-Editor (mehr Kontrolle, schnell)
- **Für Vorlagen-Nutzer**: Quelltext-Editor (komplette Vorlagen-Unterstützung)

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für eine vollständige Liste aller Tastatur-Shortcuts.

---

## MediaWiki-Variante "Source Editor" (Web UI)

Viele MediaWiki-Installationen bieten auch einen verbesserten Quelltext-Editor mit:

- **Syntax-Highlighting**: Farbige Syntax-Kennzeichnung
- **Zeilennummern**: Für bessere Orientierung
- **Autovervollständigung**: Für häufige Syntax
- **Diff-Ansicht**: Änderungen im Kontext

---

## Erweiterungen für den Editor

### VisualEditor Erweiterungen:
- **Citoid**: Automatische Zitation
- **Math**: LaTeX-Formeln
- **Graph**: Diagramme
- **Kartographer**: Karten
- **Score**: Musiknotation
- **Linter**: Fehlererkennung

### Quelltext Erweiterungen:
- **CodeEditor**: Verbesserter Quelltext-Editor
- **WikiEditor**: Erweiterte Werkzeugleiste
- **SyntaxHighlight**: Code-Highlighting
