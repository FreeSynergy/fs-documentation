# Tasks — Automatisierungs-Pipelines

[← Zurück zum Index](../INDEX.md) | [Bus](bus.md) | [Rollen](rollen.md)

---

## Was Tasks sind

Tasks sind automatische Datenflüsse zwischen Services. "Wenn X passiert, mache Y."

## Unterschied zu Lenses

| Tasks | [Lenses](../programme/lenses/README.md) |
|---|---|
| Automatisierungen (laufen im Hintergrund) | Ansichten (Mensch schaut drauf) |
| Schreiben/Ausführen | Lesen/Filtern |
| Organisatorisch (für das System) | Persönlich (für den Menschen) |
| Event-/zeitgesteuert | Manuell ausgelöst |

## Data Offers & Data Accepts

Jeder Service deklariert was er anbieten und annehmen kann — mit **konkreten Feldern und Typen** (nicht "JSON"):

**Forgejo bietet an (Data Offers):**
```
repos.list → [{ name: String, description: String, url: Url, stars: Integer }]
commits.recent → [{ hash: String, message: String, author: String, date: DateTime }]
```

**Outline akzeptiert (Data Accepts):**
```
document.create ← { title: String, body: Markdown, collection: String }
```

## Feld-Mapping

Im Task Builder (Desktop) verbindet man Quell-Felder mit Ziel-Feldern:

```
Forgejo:repos.list.name ──────→ Outline:document.create.title
Forgejo:repos.list.readme ────→ Outline:document.create.body
"Repositories" (konstant) ────→ Outline:document.create.collection
```

Transformation über Tera-Templates möglich.

## Trigger

| Trigger | Wann |
|---|---|
| OnDemand | Manuell (Button klicken) |
| OnEvent | Wenn ein Bus-Event kommt |
| Scheduled | Cron-artig (täglich, stündlich, ...) |

---

Weiter: [Bots](bots.md) | [Bus](bus.md)
