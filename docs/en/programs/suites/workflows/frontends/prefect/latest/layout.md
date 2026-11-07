# Prefect - Structure and UI/UX

## Object model

```
Flow code (@flow) ──build──► Deployment (schedule, parameters, work pool)
                                 │   Worker (process/Docker/K8s) fetches jobs
                                 ▼
                              Flow run ──► Task runs (logs, artifacts, states)
```

## UI layout

```
┌───────────────────────────────────────────────────────────────────┐
│ Prefect   Flows | Deployments | Work Pools | Automations | Events │
├───────────────────────────────────────────────────────────────────┤
│ Flow run "sync-crm"  ✔ success · 1m12s                            │
│ Timeline: ├extract ▮▮▮┤transform ▮▮┤load ▮  (subflows collapsible)│
│ Task tab: Logs / Artifacts / Results                              │
│ Deployment tab: Schedules ⏰ · Concurrency · Run button (params)  │
└───────────────────────────────────────────────────────────────────┘
```

## UI/UX

- Dark design with clear status colors (blue = running, green = ok, red = failed, yellow = late)
- Global search bar (`⌘K` palette: jump/actions) — palette present, check version

## Interactions

- Run start dialog (JSON form generated from the parameter schema)
- Log viewer with live stream; artifacts inline (tables/images)

## Responsive design

- Web responsive; read-only on mobile

## Accessibility

- Standard web; timeline graphic with table alternative (run list)

## Performance

- Event/run volume scales via server backends (Postgres tuning); Cloud abstracts this away
