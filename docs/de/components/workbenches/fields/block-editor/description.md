# Block Editor (Blockeditor)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `edit`, `read`, `template` |
| **Zustände** | `unsaved`, `readonly`, `error` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `reorder`, `fade-in` |
| **Verwandt** | `code-editor`, `rich-text-editor`, `dashboard`, `repeater` |
| **Status** | Skizze |

## Beschreibung

Der Blockeditor bearbeitet strukturierte Dokumente als Baum aus Blöcken (wie Notion). Jeder Block hat einen Datentyp. Er ist der dritte der drei Texteditoren (ADR 0039).

## Verwendungszweck

- Strukturierte Dokumente und Wiki-Seiten
- Dokumente aus Text plus Ebenen (ADR 0042)
- Vorlagen mit festen Teilen und Platzhaltern

## Varianten

| Variante | Beschreibung |
|---|---|
| **edit** | Blöcke bearbeiten |
| **read** | nur lesen |
| **template** | feste Teile mit Platzhaltern |

## Features

- Blockbaum mit Einfügen, Verschieben und Umwandeln
- Jeder Block bindet einen Datentyp aus dem Darstellungsregister (ADR 0023)
- Ebenen (Formatierung, Namen, Links, Variablen, eigene Erläuterungen) liegen als Markierungen über dem Text (ADR 0033) und werden nur in der Datenbank gespeichert
- Linktabelle: Verschieben schreibt Links um
- Dauerhaftes, begrenztes Rückgängig (ADR 0042)

## Datenbindung

Bindet ein Blockdokument (eigene Blockspezifikation, ADR 0034). Eine `.md`- oder Code-Datei ist ein Blockdokument mit **einem** Block, der auf den Text zeigt; Codemodus und Blockmodus sind zwei Ansichten desselben Modells (ADR 0042). `fs-store` ist die Wahrheit, Dateien sind Exporte.

## Abgrenzung

- **Nicht verwechseln mit** [code-editor](../../special/code-editor/): der einfache Editor für Markdown- und Codedateien.
- **Nicht verwechseln mit** [rich-text-editor](../rich-text-editor/): erweiterter WYSIWYG-Editor für Office-artige Dokumente (ODF).
- **Nicht verwechseln mit** [dashboard](../../special/dashboard/): Ein Dashboard ordnet Widgets an.

## Best Practices

- Den Blockmodus nutzen, wenn ein Dokument strukturiert ist; einfache Dateien bleiben im Code-Editor.
- Zeigen, wo Ebenen (Markierungen) existieren.
- Beim Speichern darauf hinweisen, dass der Rückgängig-Verlauf zurückgesetzt werden kann (ADR 0042).

## Hinweis zu Blinc

Nicht in Blinc vorhanden; in unserer Schicht auf Teilen von `rich_text_editor` gebaut ⚠️. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ Status der Blockspezifikation (ADR 0034)
- ⚠️ Verhältnis zum rich-text-editor (gleiches Modell oder getrennt)

## Siehe auch

- [fields – Übersicht](../index.md)
- [Code Editor](../../special/code-editor/)
- [Rich Text Editor](../rich-text-editor/)
- [Basiskomponente](../../../primitives/basics/base.md)
