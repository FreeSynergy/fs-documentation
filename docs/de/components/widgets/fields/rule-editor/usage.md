# Rule Editor (Regeleditor) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Bearbeitet die Regelmenge eines Kontos oder einer Unterhaltung.

## Beispiele

```jsx
<RuleEditor rules={rules} vocabulary="mail" onChange={update} onSave={store} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Mailfilter | `list`, Einstellungsseite |
| Wortfilter | `simple` |
| Aus dem Kontextmenü des Filters | vorausgefüllte neue Regel |

## Einbettung in andere Programme (ADR 0037)

Regeln gelten für Ordner und Gruppen; der Helpdesk kann einen reduzierten Editor für das Ticket-Routing einbetten. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Tab durch die Felder einer Zeile; Alt+Pfeiltaste hoch/runter verschiebt eine Regel.
- Jede Zeile hat einen zugänglichen Namen im Satzstil.
- Validierungsfehler sind mit ihren Feldern verknüpft.
