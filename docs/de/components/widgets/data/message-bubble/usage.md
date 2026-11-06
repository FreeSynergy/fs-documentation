# Message Bubble (Nachrichtenblase) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Zeigt eine Chatnachricht; wird immer über eine Liste oder als zitiertes Element verwendet.

## Beispiele

```jsx
<MessageBubble message={m} variant={m.own ? "own" : "incoming"} onReply={reply} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Chat | innerhalb der [message-list](../message-list/) |
| Suchtreffer | `compact` |
| Weitergeleitete Nachricht | `compact` innerhalb einer anderen Blase |

## Einbettung in andere Programme (ADR 0037)

Eine einzelne Blase kann in einer Kontakt- oder Ticketansicht als „letzte Nachricht“ stehen. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Fokussierbar als Teil der Liste; Enter öffnet die vom Host bereitgestellten Aktionen.
- Lesereihenfolge: Absender, Uhrzeit, Inhalt, Anhänge, Reaktionen, Zustand.
- Reaktionen werden als „Daumen hoch, 2“ angesagt.
