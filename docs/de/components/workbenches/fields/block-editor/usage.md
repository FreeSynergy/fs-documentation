# Block Editor (Blockeditor) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Bearbeitet ein strukturiertes Dokument.

## Beispiele

```jsx
<BlockEditor value={doc} blockTypes={allowed} onChange={save} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Wiki-Seite | `edit` |
| Serienbrief | `template` |
| Eingebettete Notiz | `read` |

## Einbettung in andere Programme (ADR 0037)

Dokumente öffnen sich im Blockeditor, überall wo sie referenziert werden. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Der Schrägstrich öffnet das Blockmenü; Alt+Pfeiltaste hoch/runter verschiebt einen Block.
- Jeder Block wird mit seinem Typ angesagt.
- Verschieben und Umwandeln sind ohne Ziehen verfügbar.
