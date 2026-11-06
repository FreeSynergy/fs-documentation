# Mail View (Mailansicht) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Zeigt eine E-Mail in einem Lesebereich oder als kompakte Vorschau.

## Beispiele

```jsx
<MailView mail={email} onOpenAttachment={save} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Lesebereich für Mails | `full` |
| Suchergebnisse | `compact` |
| Ticketverlauf | `compact` in einer [list-view](../list-view/) |

## Einbettung in andere Programme (ADR 0037)

Eine kompakte Mailansicht erscheint im Verlauf eines Kontakts oder in einem Ticket. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Tab bewegt sich durch die Kopf-Aktionen, den Text und die Anhänge.
- Kopffelder werden als Beschreibungsliste bereitgestellt.
- Signatur- und Verschlüsselungsstatus gehören zum zugänglichen Namen.
