# 0039 – Drei Text-Editoren

Status: akzeptiert (2026-11-05) · ersetzt in **0023** Punkt 4 (zwei Editoren)

## Entscheidung (Nutzer)
| Editor (Workbench) | Für | Format |
|--------------------|-----|--------|
| **Einfacher Texteditor** | Markdown und Code | Textdateien (`ropey`, `syntect`, `pulldown-cmark`) |
| **Erweiterter Editor (WYSIWYG)** | Dokumente, wie man sie aus Office kennt | z. B. ODF |
| **Block-Editor** | strukturierte Dokumente (wie Notion) | eigene Block-Spezifikation (ADR 0034) |

- Der **Composer** des Messengers nimmt den **einfachen** Editor.
