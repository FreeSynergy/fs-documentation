# Encryption State (Verschlüsselungsstatus) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Zeigt den Schutz einer Nachricht oder einer Unterhaltung und führt zum Leitfaden.

## Beispiele

```jsx
<EncryptionState kind={conversation.encryption} />
```

```jsx
<EncryptionState variant="warning" kind="none" onActivate={openGuide} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Unterhaltungskopf | `icon-text`, `medium` |
| Unverschlüsselte eingehende Nachricht | `warning`, direkt bei der Nachricht |
| Kompakte Listenzeile | nur `icon` |

## Einbettung in andere Programme (ADR 0037)

Dieselbe Markierung erscheint in jeder eingebetteten Nachrichtenansicht. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Fokussierbar; Enter und Leertaste aktivieren sie.
- Der zugängliche Name nennt die Art und die Aktion („Leitfaden öffnen“).
- Der unverschlüsselte Zustand wird angesagt, wenn eine Unterhaltung geöffnet wird, nicht bei jeder Nachricht.
