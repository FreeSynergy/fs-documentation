# Rich Text Editor (Rich-Text-Editor)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `textarea` |
| **Varianten** | `wysiwyg`, `wiki-syntax` |
| **Zustände** | `unspeichert`, `error` |
| **Gesten** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animationen** | `fade-in`, `highlight` |
| **Verwandt** | `textarea`, `code-editor`, `whiteboard`, `emoji-picker` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die frühere Komponente `wiki-editor` ist als Variante in `rich-text-editor` aufgegangen: `wysiwyg` und `wiki-syntax`.

## Beschreibung
Ein Rich Text Editor ist ein Editor für formatierten Text.

## Verwendungszweck

- Dokumente
- Artikel
- Nachrichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **wysiwyg** | Formatieren wie im Druckbild (Standard) |
| **wiki-syntax** | Editor mit Wiki-Syntax (Markdown) und Vorschau |

## Features

- Bold/Italic/Underline
- Headings
- Lists
- Links
- Images

## Abgrenzung

- **Nicht verwechseln mit** [textarea](../textarea/): das mehrzeilige Feld speichert reinen Text,
  dieser Editor speichert Formatierung als Struktur.
- **Nicht verwechseln mit** [code-editor](../../special/code-editor/): dort steht Quellcode mit
  Syntaxhervorhebung im Vordergrund, hier das Druckbild.
- **Nicht verwechseln mit** [whiteboard](../../special/whiteboard/): freie Zeichenfläche statt
  Textfluss.

## Best Practices

- Nur Werkzeuge anzeigen, die der Inhalt wirklich kennt (kein `Tabelle` in einem Kommentarfeld).
- Shortcuts parallel anbieten (`Strg+B`, `Strg+I`, `Strg+K` für Links).
- Fremden Text bereinigt einfügen (Formatierung aus anderen Anwendungen mitnehmen, nicht alles).
- Zwischenzustand automatisch sichern und den Speicherpunkt sichtbar machen (`unspeichert`).
- `wiki-syntax` immer mit Vorschau-Schalter, damit die Syntax lesbar bleibt.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Textarea](../textarea/) — reinen Text bearbeiten
- [Code Editor](../../special/code-editor/) — Quellcode
- [Basiskomponente](../../basics/base/)
