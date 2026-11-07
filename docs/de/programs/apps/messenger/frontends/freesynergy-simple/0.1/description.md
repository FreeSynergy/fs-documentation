# FreeSynergy Simple 0.1 — Beschreibung

## Übersicht
Ein Messenger für Menschen, die einfach ihre Nachrichten lesen und beantworten wollen. Keine Ordner, keine Menübänder:
eine Nachricht füllt den ganzen Bildschirm, Gesten erledigen den Rest. Funktioniert zuerst auf Touch-Geräten; jede Geste hat
ein Gegenstück für Maus, Tastatur und Hilfstechnik (siehe [Interaktion](interaction.md)).

## Was es tut
- zeigt jede neue Nachricht im Vollbild, ungelesene zuerst
- wechselt per Geste zu ungelesenen Nachrichten, leitet weiter, löscht, antwortet
- schreibt Antworten und neue Nachrichten in einem einfachen Textfeld (einfacher Editor, ADR 0039)
- wählt Empfänger aus Kontakten oder legt spontan einen neuen Kontakt an
- zeigt immer, ob eine Nachricht verschlüsselt ist; unverschlüsselte sind mit einem Link zur Anleitung markiert (ADR 0018)

## Für wen es geeignet ist
Menschen, die von Mail-Programmen überfordert sind; schnelles Nachsehen am Telefon; eine Demo, dass ein Frontend klein sein kann.

## Abgrenzung
- gegenüber [FreeSynergy vollständig](../../index.md) (Referenz-Frontend Nr. 2, geplant): keine Ordner, Regeln, Suchfilter, Mehrfachauswahl
- gegenüber Outlook / Apple Mail: keine Liste als Startbildschirm; die Nachricht ist der Startbildschirm
