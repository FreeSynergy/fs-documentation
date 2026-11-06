# Message Status (Nachrichtenstatus) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Zeigt den Zustellstatus einer gesendeten Nachricht. Wird innerhalb von [message-bubble](../../../widgets/data/message-bubble/) und als Eintrag in Listenzeilen verwendet.

## Beispiele

```jsx
<MessageStatus status={message.state} at={message.stateAt} />
```

```jsx
<MessageStatus variant="icon-text" status="failed" reason="No encrypted path" />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Chat-Blase | `icon`, `small`, neben der Uhrzeit |
| Liste gesendeter Mails | `icon` in einer Spalte |
| Fehler | `failed` plus vom Host angebotene Wiederholungsaktion |

## Einbettung in andere Programme (ADR 0037)

Der Nachrichtenstatus wird überall angezeigt, wo eine Nachricht erscheint. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Nicht eigenständig fokussierbar; der Tooltiptext ist Teil des zugänglichen Namens des Elternelements.
- Screenreader lesen das Zustandswort („Gelesen“), nicht das Symbol.
- Zustandsänderungen werden nur für die neueste Nachricht einer Unterhaltung höflich angekündigt.
