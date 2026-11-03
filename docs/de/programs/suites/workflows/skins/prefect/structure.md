# Prefect - Struktur und UI/UX

## Objektmodell

```
Flow-Code (@flow) ──build──► Deployment (Schedule, Parameter, Work Pool)
                                 │   Worker (Prozess/Docker/K8s) holt Aufträge
                                 ▼
                              Flow-Run ──► Task-Runs (Logs, Artifacts, Staaten)
```

## UI-Layout

```
┌───────────────────────────────────────────────────────────────────┐
│ Prefect   Flows | Deployments | Work Pools | Automations | Events │
├───────────────────────────────────────────────────────────────────┤
│ Flow-Run „sync-crm“  ✔ success · 1m12s                            │
│ Timeline: ├extract ▮▮▮┤transform ▮▮┤load ▮  (Subflows einklappbar)│
│ Task-Tab: Logs / Artifacts / Ergebnisse                                 │
│ Deployment-Tab: Schedules ⏰ · Concurrency · Run-Button (Parameter)│
└───────────────────────────────────────────────────────────────────┘
```

## UI/UX

- dunkles Design mit klaren Statusfarben (blau=läuft, grün=ok, rot=failed, gelb=late)
- Suchleiste global (`⌘K`-Palette: Springen/Aktionen) — Palette vorhanden, Version prüfen

## Interaktionen

- Run-Start-Dialog (JSON-Formular aus Parameter-Schema)
- Log-Viewer mit Live-Stream; Artifacts inline (Tabellen/Bilder)

## Responsive Design

- Web responsiv; Mobil lesend

## Accessibility

- Standard-Web; Timeline-Grafik mit Tabellenalternative (Run-Liste)

## Performance

- Event-/Run-Volumen skalieren über Server-Backends (Postgres-Tuning); Cloud hält es abstrahiert
