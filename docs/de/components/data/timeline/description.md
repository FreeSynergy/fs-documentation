# Timeline (Zeitlinie)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `senkrecht`, `waagerecht`, `karten`, `ereignisse` |
| **Zustände** | `aktiv`, `abgeschlossen` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in`, `stagger`, `tick-draw` |
| **Verwandt** | `calendar-view`, `list-view`, `wizard`, `progress` |
| **Status** | dokumentiert |

## Beschreibung
Eine Timeline ist eine chronologische Darstellung von Ereignissen.

## Verwendungszweck

- Verlauf anzeigen
- Aktivitäten
- Historie
- Projektphasen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **senkrecht** | Einträge untereinander, Linie links (Standard) |
| **waagerecht** | Einträge nebeneinander, scrollt seitlich |
| **karten** | jeder Eintrag als Karte an der Linie |
| **ereignisse** | kompakt: Icon, Zeitpunkt, ein Text |

## Features

- Date
- Title
- Description
- Icon
- Actions

## Abgrenzung

- **Nicht verwechseln mit** [calendar-view](../calendar-view/): der Kalender hat eine Zeitskala
  und zeigt Belegung, die Zeitlinie zeigt Reihenfolge ohne Skala.
- **Nicht verwechseln mit** [wizard](../../containers/wizard/): der Assistent führt durch noch offene Schritte,
  die Zeitlinie schaut auf Vergangenes zurück.
- **Nicht verwechseln mit** [progress](../../feedback/progress/): ein Balken zeigt einen Anteil,
  die Zeitlinie zeigt die einzelnen Punkte.
- Eine [list-view](../list-view/) ist zeitlos und umsortierbar; die Zeitlinie bleibt chronologisch.

## Best Practices

- Neueste Einträge zuerst, wenn es um Aktivität geht; bei Plänen umgekehrt und deutlich beschriften.
- Relative Zeit anzeigen ("vor 3 Tagen") und den exakten Zeitpunkt als Tooltip bereithalten.
- Nach Tag oder Woche gruppieren, sonst verliert die Linie ihre Struktur.
- Icon für den Typ, Farbe für den Status – beides gemischt ist nicht mehr lesbar.
- Rückwärts nachladen (ältere Einträge), damit der Anfang sofort sichtbar ist.

## Layout

```
┌─────────────────────────────────────────┐
│  📅 20. Januar 2024                     │
│  📝 Erster Schritt                      │
├─────────────────────────────────────────┤
│  📅 21. Januar 2024                     │
│  ✅ Schritt abgeschlossen               │
├─────────────────────────────────────────┤
│  📅 22. Januar 2024                     │
│  📝 Zweiter Schritt                     │
└─────────────────────────────────────────┘
```

## Siehe auch

- [data – Übersicht](../index.md)
- [Calendar View](../calendar-view/) — Belegung auf Zeitskala
- [Wizard](../../containers/wizard/) — offene Schritte führen
- [Basiskomponente](../../basics/base/)
