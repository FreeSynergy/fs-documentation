# Zapier - Struktur und UI/UX

## Zap-Aufbau

```
┌──────────────────────────────────────────────────────────────────┐
│ Zap „Neue Tickets → CRM“        [Test] [Publish]  ⋮              │
├──────────────────────────────────────────────────────────────────┤
│ Step 1 Trigger   Zammad · New Ticket          [Test step]       │
│ Step 2 Action    Filter (nur Priority ≥ high) [Test step]       │
│ ├─ Path A: Bedingung „Kunde vorhanden“                          │
│ │   Step 3a Update Company                                      │
│ └─ Path B: sonst                                                │
│     Step 3b Create Company                                      │
│ Step 4 Action    Slack notify                                   │
├──────────────────────────────────────────────────────────────────┤
│ Run History (234 Runs) · Failed-Replay · Version v3             │
└──────────────────────────────────────────────────────────────────┘
```

- vertikale Step-Kette mit Paths; jeder Step hat Feld-Mapper links (Proben-Datensatz aus Trigger)

## UI/UX

- geführt, formfixiert — wenig Freiform (bewusst); Probedaten-Picker „Try again“ für Testdaten

## Interaktionen

- Klick-Ketten (Step → App → Event → Map), kein Canvas-Dragging (Paths als Blöcke)
- Replay fehlgeschlagener Runs; Versionsvergleich

## Responsive Design

- Web responsiv; Mobile-App für Zap-Verwaltung/Freigaben

## Accessibility

- Standard-Web-Formulare; kein Canvas

## Performance

- Trigger-Latenz = Polling-Intervall (5–15 min typisch, Instant-Triggers wo verfügbar); Tasks zählen pro Aktion
