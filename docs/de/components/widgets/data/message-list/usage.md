# Message List (Nachrichtenliste) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Zeigt eine Unterhaltung. Das aufnehmende Programm entscheidet, welche Aktionen und Gesten zu den Zeilen gehören.

## Beispiele

```jsx
<MessageList
  context={conversation.id}
  messages={messages}
  onLoadOlder={loadOlder}
  onVisible={markRead}
/>
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Messenger-Chat | `chat`, gesamter Bereich |
| Helpdesk-Ticket | `chat`, `small`, mit einem Antwortfeld darunter |
| Antwortstrang | `thread` in einer [drawer](../../overlays/drawer/) |

## Einbettung in andere Programme (ADR 0037)

Die Nachrichtenliste in einer Ticket- oder Kontaktansicht zeigt nur einen Ordner oder eine Gruppe. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Pfeiltasten hoch/runter bewegen zwischen Nachrichten, Pos1/Ende springt zur ersten/letzten, ein Kurzbefehl springt zur nächsten ungelesenen Nachricht.
- Screenreader kündigen neue eingehende Nachrichten höflich an; eigene Nachrichten werden nicht angesagt.
- Trenner werden als Überschriften gelesen (z. B. „Gestern“).
