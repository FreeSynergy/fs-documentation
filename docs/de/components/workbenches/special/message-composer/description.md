# Message Composer (Nachrichtenverfasser)

| Feld | Wert |
|------|------|
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `chat`, `mail`, `reply` |
| **Zustände** | `empty`, `draft`, `sending`, `error` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `fade-in` |
| **Verwandt** | `code-editor`, `tags-input`, `mention-input`, `emoji-picker`, `file-upload`, `embed` |
| **Status** | Skizze |

## Beschreibung

Der Nachrichtenverfasser ist die Workbench zum Schreiben einer Nachricht: Empfänger, Betreff, ein einfacher Texteditor, Anhänge, Emojis und Erwähnungen.

## Verwendungszweck

- Chatnachrichten und Mails schreiben
- Antwortfeld in eingebetteten Ansichten (ADR 0037)
- Entwürfe, die Neustarts überstehen

## Varianten

| Variante | Beschreibung |
|---|---|
| **chat** | ein Feld mit Senden-Schaltfläche |
| **mail** | Empfänger, Betreff, Editor, Anhänge |
| **reply** | nur ein Antwortfeld (kompakt) |

## Features

- Empfänger über [tags-input](../../../primitives/fields/tags-input/) Variante `recipients` (Kontaktvorschläge, Schlüsselzustand pro Chip)
- Betreff (Mail)
- Einfacher Texteditor = [code-editor](../code-editor/) (Markdown), ADR 0039
- Anhänge über [file-upload](../../../widgets/fields/file-upload/)
- [emoji-picker](../../../widgets/fields/emoji-picker/) und [mention-input](../../../primitives/fields/mention-input/)
- Verschlüsselungshinweis vor dem Senden

## Datenbindung

Bindet einen Nachrichtenentwurf: ActivityStreams `Note` (Entwurf) plus Empfänger und das Schlüsselwort `$draft`. Ausgabe: `text/plain`, `text/markdown` und (bei Mail) `text/html`. Einordnung am 2026-11-05 entschieden: **Workbench**, weil sie den Editor enthält, der selbst eine Workbench ist; die Kindelemente werden zur Laufzeit gewählt.

## Abgrenzung

- **Nicht verwechseln mit** [code-editor](../code-editor/): Der Editor ist ein Teil des Verfassers.
- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): Der Verfasser nutzt den einfachen Editor (ADR 0039); der erweiterte kann ihn bei Mails ersetzen ⚠️.
- **Nicht verwechseln mit** einer App: Die App ergänzt Menü, Gesten und Einstellungen um den Verfasser (ADR 0037).

## Best Practices

- Entwürfe automatisch sichern.
- Den Verschlüsselungszustand vor dem Senden zeigen; erklären, wenn kein verschlüsselter Weg existiert.
- Anhänge nicht vor dem Screenreader verbergen.

## Hinweis zu Blinc

In unserer Schicht gebaut auf Blinc-Teilen (`textarea`, `button`, `rich_text_editor`, `selection_toolbar`). IME und Pre-Edit-Eingabe für CJK und mobile Geräte: Blinc-Backlog **e864f0c** (für einen Messenger verpflichtend). Combobox-Hover für Empfängervorschläge: **8115bf5**.

## Offene Punkte

- ⚠️ Zerlegung des Verfassers für den einfachen Chatfall (Textarea + Button) gegenüber dieser Workbench
- ⚠️ Platzierung von „Senden rückgängig“ und „Senden planen“

## Siehe auch

- [special – Übersicht](../index.md)
- [Code Editor](../code-editor/)
- [Rich Text Editor](../../fields/rich-text-editor/)
- [Embed](../embed/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
