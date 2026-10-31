# XWiki - Funktionen

## Übersicht

XWiki bietet mehrere Editoren an, je nach Konfiguration und Erweiterung. Der Standard-Editor ist der "WYSIWYG-Editor" (Web Content Editor), aber XWiki unterstützt auch Markdown und XWiki Syntax.

## Verfügbare Editoren

### 1. WYSIWYG-Editor (Web Content Editor)

#### Funktionen:
- **Visuelles Bearbeiten**: Wie Word oder Google Docs
- **Formatierung**: Überschriften (H1-H6), fett, kursiv, unterstreichen, durchstreichen
- **Listen**: Nummerierte Listen, Aufzählungslisten, Aufgabenlisten
- **Tabellen**: Tabellen erstellen/bearbeiten (Spalten/Zeilen hinzufügen/löschen)
- **Medien**: Bilder einfügen, Links hinzufügen
- **Ausrichtung**: Textausrichtung, Einzüge
- **Hinweise**: Boxen für Informationen, Warnungen, etc.
- **Code-Blöcke**: Syntax-Hervorhebung (optional)
- **Makros**: Visuelle Makro-Einbindung (z.B. Tabellen, Diagramme, Infoboxen)
- **Rich Content**: Videos, iframes, Diagramme

#### Was der Editor NICHT kann:
- Kein direktes HTML-Schreiben (nur über Makro)
- Kein Markdown-Syntax im WYSIWYG-Modus
- Keine komplexe Versionierung direkt im Editor
- Makros müssen über Menü eingefügt werden (nicht direkt in den Text)

---

### 2. XWiki Syntax Editor

#### Funktionen:
- **XWiki-Makro-Syntax**: Vollständige XWiki-Makro-Unterstützung
- **Direktes Schreiben**: Kein WYSIWYG, aber vollständige Kontrolle
- **Versionierung**: Komplette Historie
- **Makros**: `{{macro}}` Syntax für komplexe Elemente
- **Macros**:
  ```xwiki
  {{toc/}}
  {{message box="info"}}
  This is an info message
  {{/message}}
  {{velocity}}
  #set($x = 1)
  {{/velocity}}
  ```

#### Was der Editor NICHT kann:
- Kein visuelles Feedback (man sieht nur den Code)
- XWiki-Syntax muss gelernt werden
- Kein Drag & Drop für Bilder

---

### 3. Markdown Editor (optional)

#### Funktionen:
- **GitHub-Flavored Markdown**: Standard-Markdown
- **Live-Vorschau**: Echtzeit-Vorschau
- **Lists, Tables, Code**: Alles Markdown-Standard
- **Integration**: XWiki-Makros können integriert werden

#### Was der Editor NICHT kann:
- Keine XWiki-spezifischen Makros (außer über HTML-Inline)
- Weniger Funktionsumfang als WYSIWYG

---

## Vergleich der Editoren

| Funktion | WYSIWYG | XWiki Syntax | Markdown |
|----------|---------|--------------|----------|
| Visuelles Bearbeiten | ✅ Ja | ❌ Nein | ❌ Nein |
| XWiki-Makros | ✅ Via Menü | ✅ Direkt | ❌ Eingeschränkt |
| HTML | ❌ Nur via Makro | ✅ Ja | ✅ Inline HTML |
| Markdown | ❌ Nein | ✅ (XWiki-Extend) | ✅ Ja |
| Tabellen | ✅ Visuell | ✅ Syntax | ✅ Syntax |
| Live-Vorschau | ✅ Ja | ❌ Nein | ✅ Ja (optional) |
| Lernkurve | ✅ Niedrig | ❌ Hoch | ✅ Mittel |

---

## Empfehlung

- **Für Redakteure**: WYSIWYG-Editor ( intuitiv, visuell)
- ** Für Entwickler**: XWiki Syntax Editor (volle Kontrolle, Makros)
- **Für Frontender**: Markdown (wenn XWiki-Konfiguration erlaubt)

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für eine vollständige Liste aller Tastatur-Shortcuts.

---

## XWiki-Makros (Beispiele)

### Informations-Box
```xwiki
{{message box="info"}}
Dies ist eine Information
{{/message}}
```

### Tabelle
```xwiki
{{table}}
|| Kopfe 1 || Kopfe 2 ||
|| Zelle 1 | Zelle 2 ||
{{/table}}
```

### Velocity (Skripting)
```xwiki
{{velocity}}
#set($list = ["A", "B", "C"])
#foreach($item in $list)
$item
#end
{{/velocity}}
```

### Diagramm (mit Chart-Extension)
```xwiki
{{chart type="pie"}}
{"data": [1, 2, 3], "labels": ["A", "B", "C"]}
{{/chart}}
```
