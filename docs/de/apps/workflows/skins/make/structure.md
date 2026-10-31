# Make - Struktur und UI/UX

## Szenario-Canvas

```
┌──────────────────────────────────────────────────────────────────┐
│ Szenario „Ticket→CRM“   [◀ Run once] [Start ▶]  History ⏱  💾    │
├────────┬─────────────────────────────────────────────────────────┤
│ Liste  │  (Webhooks) ──→ (Filter) ──┐                            │
│ Szenarien│                          ├──(Router)──┐               │
│ Ordner │                     (Zammad Search)   (Shopify…)        │
│        │                          │                │             │
│        │                     (Create Company)  (Add item)        │
│        │   Blasen zeigen Datensätze; Pfeile = Datenflüsse        │
└────────┴─────────────────────────────────────────────────────────┘
```

- Module horizontal von links nach rechts, Routen gabeln sich; Klick = Modalkonfiguration

## UI/UX

- farbcodierte App-Icons, „Instant preview“ zeigt echte Datensätze pro Modul
- Mapping-Designer für Felder (drag aus Quelle ins Zielformular)

## Interaktionen

- Drag: Module verbinden; Rechtsklick: Fehlerbehandlung/Sleep einfügen
- History-Dialog: Execution → jede Blase mit Ein-/Ausgabedaten (Fehlersuche)

## Responsive Design

- Desktop-lastig; mobile Ansicht lesen, aber Szenarien bauen → Desktop

## Accessibility

- Standard-Web-Komponenten; Canvas-Editing primär Maus

## Performance

- Scheduling-Intervalle ab Plan (Free 15 min, bezahlt bis 1 min); High-Volume → Batch-Optimierung (Iterator gruppieren)
