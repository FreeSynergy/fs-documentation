# Kalendar - Struktur und UI/UX

## Fensterstruktur

Kalendar ist Ein-Fenster-Design mit linker Seitenleiste und schaltbarer Hauptansicht:

```
┌──────────────────────────────────────────────────────────────┐
│ ☰  Kalendar              [Agenden|Tag|Woche|Monat]  🔍  ⚙    │
├────────────────┬─────────────────────────────────────────────┤
│ Seitenleiste   │  Hauptansicht                               │
│                │  ┌───────────────────────────────────────┐  │
│ ⌚ Agenden     │  │ 08:00 ┤ ███████ Meeting                │  │
│ 📅 Tag         │  │ 09:00 ┤                                │  │
│ 📆 Woche       │  │ 10:00 ┤ ░░░░░░ Geburtstage             │  │
│ 🗓 Monat       │  │ ...                                    │  │
│                │  └───────────────────────────────────────┘  │
│ Kalender       │                                             │
│ ●● Privat      │  [+] Schnellerfassung (Natürlichsprache)    │
│ ○○○ Arbeit     │                                             │
│ ★ Geburtstage   │                                             │
│                │                                             │
│ + Kalender     │                                             │
└────────────────┴─────────────────────────────────────────────┘
```

## UI/UX-Design

- **Kirigami-Look**: adaptive Seitenleiste — auf schmalen Bildschirmen wird sie zum ausziehbaren Panel, die Kopfzeile komprimiert sich
- **Theming**: folgt dem Plasma-Farbschema (Hell/Dunkel, Breeze); Kalenderfarben frei wählbar
- **Kopfzeile**: Ansichtsumschalter als Segment-kontrolle, Suche, Einstellungen
- **Schnellerfassung** als dauerhafte Eingabezeile unter der Agenda (Agenden-Ansicht)

## Interaktionen

- **Drag & Drop**: Ereignisse in der Tages-/Wochenansicht verschieben und per Griff an der Kante in der Dauer ändern; zwischen Kalendern per Drop in die Seitenleiste (soweit serverseitig Schreibrecht)
- **Long-Press** auf Touch: öffnet das Ereigniskontextmenü
- **Wischen** zwischen Tagen/Wochen (mobil)
- **Animationen**: sanftes Ein-/Ausblenden der Panels, Listeneinträge gleiten beim Umschalten der Ansicht; bewusst dezent

## Responsive Design

| Bildschirmbreite | Verhalten |
|------------------|-----------|
| Desktop (> 1000 px) | feste Seitenleiste + Hauptansicht nebeneinander |
| Tablet | einklappbare Seitenleiste als Overlay |
| Telefon (Plasma Mobile) | nur eine Ansicht, Navigation über Hamburger-Panel |

## Accessibility

- Tastaturnavigation über QML-Fokusreihenfolge (Tab/Shift+Tab, Enter zum Öffnen)
- Bildschirmleser: Qt-Accessibility-Brücke; Beschriftungen an Buttons und Kalender-Einträgen vorhanden
- Kontrast folgt dem Plasma-Schema; reine Farbunterscheidung (Kalenderfarben) zusätzlich durch Text beschriftet
- Keine eigenen Shortcuts für Ansichtswechsel dokumentiert — die üblichen Browser-/Qt-Standards gelten (siehe [shortcuts.md](shortcuts.md))

## Performance

- Synchronisation läuft asynchron in Akonadi; UI bleibt bedienbar
- Bei sehr großen Kalendern (> 10.000 Events im Zeitraum) kann die Monatsansicht spürbar laden — Zeitraum eingrenzen
