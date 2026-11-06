# Call Controls (Anrufsteuerung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Leiste von Bedienelementen für einen laufenden Anruf, bereitgestellt vom Anruf-Programm.

## Beispiele

```jsx
<CallControls session={call} onToggleMic={mute} onHangUp={endCall} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Anruf-Programm | `bar` |
| Anderes Programm während eines Anrufs | `compact` als Mini-Leiste |

## Einbettung in andere Programme (ADR 0037)

Das Anruf-Programm zeigt im Messenger eine Mini-Leiste, während ein Anruf läuft. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Werkzeugleisten-Muster: Pfeiltasten bewegen den Fokus, Leertaste schaltet um.
- Zustandsworte („Mikrofon stummgeschaltet“) werden bei Änderung angesagt.
- Einen Kurzbefehl zum Stummschalten legt das Frontend fest, nicht die Komponente.
