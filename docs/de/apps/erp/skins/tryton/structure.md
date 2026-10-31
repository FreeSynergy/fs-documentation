# Tryton - Struktur und UI/UX

## Desktop-Client

```
┌──────────────────────────────────────────────────────────────────┐
│ Menü der Module ▾   „Sales“: Quotations ☐                         │
├──────────────┬───────────────────────────────────────────────────┤
│ Seitenbaum   │ Liste S/2026… | Party | Amount | State ▣           │
│ Account ▸    │ Form: State-Chips (draft/confirmed) · Felder      │
│ Sale ▸       │   Lines-Table · Related (Invoice/Move)             │
│ Stock ▸      │ Statusleiste: Speichern/Löschen/Persistieren      │
└──────────────┴───────────────────────────────────────────────────┘
```

- Baum links, Liste → Doppelklick → Form; Buttons oben; „Related“-Links zwischen Dokumenten

## UI/UX

- Desktop-Native-Konsistenz (GTK), Shortcuts-Menü in jeder Maske, Schnellstart (`Strg+S` Speichern)
- Formulare mit Tabs; Listen mit Spalten-Settings

## Interaktionen

- Auswahlen (Many2One) mit Popup-Suche + Anlegen; „Expand“-Knöpfe für Relateds
- Offline: Desktop schreibt Server-Queue bei Verbindung

## Responsive Design

entfällt (Desktop/Web-UI getrennt)

## Accessibility

- GTK-Basis Accessibility (Screenreader-Grundlagen); Konsistenz schlägt Eyecandy

## Performance

- Listen paginiert serverseitig; große Instanzen partitionieren (Perioden)
