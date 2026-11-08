# Rich Text Editor

| Feld | Wert |
|-------|-------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `textarea` |
| **Varianten** | `wysiwyg`, `wiki-syntax` |
| **Zustände** | `unspeichert`, `error` |
| **Gesten** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animationen** | `fade-in`, `highlight` |
| **Verwandt** | `textarea`, `code-editor`, `whiteboard`, `emoji-picker` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die bisherige Komponente `wiki-editor` ist eine Variante von `rich-text-editor` geworden:
    `wysiwyg` und `wiki-syntax`.

## Beschreibung
Ein Rich-Text-Editor ist ein Editor für formatierten Text.

## Zweck

- Dokumente
- Artikel
- Nachrichten

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **wysiwyg** | Formatierung wie im gedruckten Layout (Standard) |
| **wiki-syntax** | Editor mit Wiki-Syntax (Markdown) und Vorschau |

## Funktionen

- Fett/Kursiv/Unterstrichen
- Überschriften
- Listen
- Links
- Bilder

## Abgrenzung

- **Nicht verwechseln mit** [textarea](../../../primitives/fields/textarea/): Das mehrzeilige Feld
  speichert reinen Text, dieser Editor speichert Formatierung als Struktur.
- **Nicht verwechseln mit** [code-editor](../../special/code-editor/): Dort steht Quellcode mit
  Syntaxhervorhebung im Vordergrund, hier das gedruckte Layout.
- **Nicht verwechseln mit** [whiteboard](../../special/whiteboard/): eine freie Zeichenfläche statt
  eines Textflusses.

## Best Practices

- Nur Werkzeuge anbieten, die der Inhalt wirklich braucht (keine `Tabelle` in einem Kommentarfeld).
- Tastenkürzel parallel anbieten (`Strg+B`, `Strg+I`, `Strg+K` für Links).
- Eingefügten fremden Text bereinigen (Formatierung aus anderen Anwendungen übernehmen, aber nicht alles).
- Den Zwischenstand automatisch sichern und den Speicherstand sichtbar machen (`unspeichert`).
- `wiki-syntax` immer mit einem Vorschau-Schalter, damit die Syntax lesbar bleibt.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Textarea](../../../primitives/fields/textarea/) — reinen Text bearbeiten
- [Code Editor](../../special/code-editor/) — Quellcode
- [Base-Komponente](../../../primitives/basics/base.md)
