# GNOME Planner - Struktur und UI/UX

## Fensterstruktur

```
┌────────────────────────────────────────────────────────────────────┐
│ Datei Bearbeiten Ansicht Aufgaben Ressourcen Projekt Hilfe         │
│ [🆕][💾]  [Aufgaben | Ressourcen | Abhängigkeiten]                 │
├──────────────────────────────┬─────────────────────────────────────┤
│ Aufgabenbaum                 │ Gantt-Canvas                        │
│ # Name            Start Ende │  W27  W28  W29  W30                │
│ ├─ Konzept        01.06     │  ▐█░░░░░░░                         │
│ │ ├─ Recherche    01.06     │  ▐███░░░░░  ← kritischer Pfad rot  │
│ │ └─ Review       10.06     │      ▐█░░░░                        │
│ └─ Umsetzung      20.06     │        ◆   (Meilenstein)           │
│   [Dauer] [Completion %]    │                                     │
├──────────────────────────────┴─────────────────────────────────────┤
│ Status: 12 Aufgaben, kritischer Pfad: 3 Vorgänge                   │
└────────────────────────────────────────────────────────────────────┘
```

## Die drei Ansichten

1. **Aufgaben**: Baum links, Gantt-Balken rechts; Balken ziehen verschiebt Termine (bei fehlender Abhängigkeit)
2. **Ressourcen**: Ressourcenliste + Auslastungsbalken; Überlastung farbig
3. **Abhängigkeiten**: PERT-Netzwerk, Knoten per Maus verschiebbar, Kanten = Abhängigkeiten

## UI/UX

- Klassisches GTK-3-Desktop-Layout, keine adaptive Oberfläche
- Standardschrift/-thema des GTK-Desktops; keine eigenen Themes
- Detaildialoge als modale GTK-Dialoge (Aufgaben-Info mit Reiterblättern)

## Interaktionen

- **Drag & Drop**: Balken im Gantt verschieben; Reihenfolge im Baum per Ziehen (Hierarchie via Einrücken)
- **Rechtsklick**: Kontextmenü (siehe [menu.md](menu.md))
- **Doppelklick auf Balken/Zeile**: Aufgaben-Info
- **Zoom** des Canvas: Strg+Mausrad bzw. Skalenleiste

## Responsive Design / Accessibility

- Nicht responsive — klassisches Programmfenster; auf kleinen Bildschirmen horizontal scrollen
- Tastaturnavigation in Tabellen/Dialogen (GTK-Standard), Menüs mit Access-Keys (`Alt+F` etc.)
- Bildschirmleser: GTK-Accessibility für Listen/Dialoge; der Gantt-Canvas selbst ist **nicht** a11y-erschlossen (reine Zeichnung)

## Performance

- Auch mehrere hundert Vorgänge flüssig; PERT-Ansicht wird ab ~100 Knoten unübersichtlich und träge
