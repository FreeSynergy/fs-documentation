# Reaction Bar (Reaktionsleiste) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Zeigt und schaltet Reaktionen für eine Nachricht um.

## Beispiele

```jsx
<ReactionBar reactions={m.reactions} messageId={m.id} onToggle={toggleReaction} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Chat | `inline` in der Blase |
| Dichte Liste | `compact` |

## Einbettung in andere Programme (ADR 0037)

Reaktionen sind Teil jeder eingebetteten Nachrichtenansicht. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Die Chips sind Schaltflächen: Tab zum Wechseln, Leertaste oder Enter schaltet um.
- Jeder Chip wird als „Daumen hoch, 2 Reaktionen, eigene Reaktion“ gelesen.
- Der „+“-Chip öffnet die Auswahl, Esc schließt sie.
