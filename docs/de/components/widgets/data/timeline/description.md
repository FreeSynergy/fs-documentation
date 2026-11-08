# Timeline

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

- Darstellung eines Verlaufs
- Aktivitäten
- Historie
- Projektphasen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **senkrecht** | Einträge untereinander, Linie links (Standard) |
| **waagerecht** | Einträge nebeneinander, scrollt seitlich |
| **karten** | jeder Eintrag als Karte an der Linie |
| **ereignisse** | kompakt: Symbol, Zeitpunkt, ein Text |

## Funktionen

- Datum
- Titel
- Beschreibung
- Symbol
- Aktionen

## Abgrenzung

- **Nicht verwechseln mit** [calendar-view](../calendar-view/): der Kalender hat eine Zeitskala
  und zeigt Belegung, die Timeline zeigt die Reihenfolge ohne Skala.
- **Nicht verwechseln mit** [wizard](../../containers/wizard/): der Assistent führt durch Schritte, die
  noch offen sind, die Timeline blickt auf das Vergangene zurück.
- **Nicht verwechseln mit** [progress](../../../primitives/feedback/progress/): ein Balken zeigt einen Anteil,
  die Timeline zeigt die einzelnen Punkte.
- Eine [list-view](../list-view/) ist zeitlos und kann umsortiert werden; die Timeline bleibt chronologisch.

## Best Practices

- Bei Aktivitäten die neuesten Einträge zuerst; bei Plänen umgekehrt, und das deutlich kennzeichnen.
- Zeig die relative Zeit („vor 3 Tagen“) und halte den genauen Zeitpunkt als Tooltip bereit.
- Gruppiere nach Tag oder Woche, sonst verliert die Linie ihre Struktur.
- Symbol für die Art, Farbe für den Status — beides zu mischen ist nicht mehr lesbar.
- Lade rückwärts (ältere Einträge), damit der Anfang sofort sichtbar ist.

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
- [Calendar View](../calendar-view/) — Belegung auf einer Zeitskala
- [Wizard](../../containers/wizard/) — Führung durch offene Schritte
- [Basiskomponente](../../../primitives/basics/base.md)
