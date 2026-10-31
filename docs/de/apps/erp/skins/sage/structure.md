# Sage - Struktur und UI/UX

## Oberflächen (je Produkt)

```
Business Cloud (Web):  Kachel-Start · Belege-Liste · Bank-Feed-Reconciliation
Sage 50/100 (Windows): MDI-Fenster, Funktionsbaum links,
                       Buchungsformulare mit Kontenspalten,
                       Reports als Listen/Druckdialoge
Sage X3 (Web):         Startpages (KPI-Kacheln) → Funktionsmenüs →
                       Tabellen-Grids mit „Bearbeitungsblöcken“
```

- Cloud: modern, geführt; 50/100: Windows-Territorium mit Tastatur-focus
- X3: funktionscode-lastig (Menüs mit Codes wie `SALINH`), Poweruser-orientiert

## UI/UX

- DE-Versionen mit Steuer-/Monatsabschluss-Assistenten
- Formulare tabelletypisch (Soll/Haben-Spalten), Massenbuchungen als Stapel

## Interaktionen

- Tastatursteuerung in Windows-Masken stark (Kontensuche über Aktenzeichen/Bezeichnung)
- X3: Grid-Editing, „Abläufe“ (Batches) planen

## Responsive Design

nur Cloud-Produkte responsiv; Windows-Clients desktopfixiert

## Accessibility

Windows-Basis (Screenreader je Version unterschiedlich); Cloud Standard-Web

## Performance

On-Prem skaliert über DB-Tuning; SaaS-Export-Limits beachten
