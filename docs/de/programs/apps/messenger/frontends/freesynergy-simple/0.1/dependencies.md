# FreeSynergy Simple 0.1 — Abhängigkeiten (unsere Komponenten)

| Bereich / Funktion | Komponente | Ebene |
|--------------------|------------|-------|
| Vollbild-Nachricht | `mail-view` / `message-bubble` (NEU) | Widget |
| Verschlüsselungsstatus | `encryption-state` (NEU) | Primitive |
| Symbole in der oberen Leiste | `button` (Symbol) | Primitive |
| Listenansicht | `list-view` (braucht Änderungen bei Wischen/Auswahl) | Widget |
| Verfassen | `composer` mit dem einfachen Texteditor (ADR 0039) | Workbench |
| Empfängerauswahl | `search-field` + `list-view` | Primitive + Widget |
| Formular für neuen Kontakt | `field`, `text-input`, `form` (cn-Backlog bf7c901) | Primitive / Widget |
| Rückgängig nach Löschen/Abbrechen | `toast` | Primitive |
| Gesten | Wischen, Doppeltippen, langes Drücken (`interactions/gestures/`) | — |
