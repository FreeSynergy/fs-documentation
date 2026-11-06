# Key Verification (Schlüsselprüfung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Dialog zur Bestätigung eines Schlüssels oder Geräts.

## Beispiele

```jsx
<KeyVerification open={show} subject={contact} fingerprint={fp} onConfirm={trust} onReject={flag} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Aus dem encryption-state | für einen ungeprüften Schlüssel öffnen |
| Neues Gerät | `device-list` nach einem Anmeldehinweis |

## Einbettung in andere Programme (ADR 0037)

Jedes Programm, das eine Person anzeigt, kann die Prüfung öffnen. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Der Fokus wechselt in den Dialog; Esc schließt ihn, ohne zu bestätigen.
- Der Fingerabdruck kann Gruppe für Gruppe vorgelesen werden.
- Bestätigen und Ablehnen sind getrennte, klar benannte Schaltflächen.
