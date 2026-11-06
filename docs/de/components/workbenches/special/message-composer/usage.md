# Message Composer (Nachrichtenverfasser) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Schreibfläche für Chat und Mail.

## Beispiele

```jsx
<MessageComposer variant="mail" draft={draft} onChange={save} onSend={send} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Messenger-Chat | `chat` |
| Mail | `mail` |
| Helpdesk-Antwort | `reply` unter dem Ticket |

## Einbettung in andere Programme (ADR 0037)

Als Antwortfeld in Tickets, Kontakten und Aufgaben. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Strg+Enter sendet (vom Frontend konfigurierbar); Enter fügt in der Mail-Variante eine Zeile ein.
- Tab-Reihenfolge: Empfänger, Betreff, Text, Anhänge, Senden.
- Autovervollständigungslisten werden mit ihrer Anzahl angesagt.
